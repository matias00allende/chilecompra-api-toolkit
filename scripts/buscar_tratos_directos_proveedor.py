"""
buscar_tratos_directos_proveedor.py

Busca tratos directos adjudicados a un proveedor especifico en Mercado Publico,
usando el backend publico de Trato Directo (no requiere TICKET_MP - usa token
anonimo). Permite acotar opcionalmente a uno o mas organismos por nombre.

Backend descubierto por inspeccion de trafico del buscador publico oficial
(https://trato-directo.mercadopublico.cl/buscador-publico), mismo patron de
autenticacion anonima documentado en docs/trato-directo.md.

Por que este script existe: la API v1 documentada de ChileCompra exige el
parametro `fecha` (un dia calendario especifico, a nivel nacional) para el
endpoint de licitaciones/OC, lo que hace inviable una busqueda historica
multi-anual por proveedor (habria que iterar dia por dia, con rate-limit real).
Este backend de Trato Directo si permite filtrar por proveedor + rango de
fechas en una sola busqueda paginada.

Uso:
    # Todos los tratos directos del proveedor en los ultimos 4 anos (sin filtro de organismo)
    python buscar_tratos_directos_proveedor.py --rut 76.123.456-7 --alias mi-proveedor

    # Acotado a organismos cuyo nombre contenga alguno de estos textos (repetible)
    python buscar_tratos_directos_proveedor.py --rut 76.123.456-7 --alias mi-proveedor \
        --organismo "MUNICIPALIDAD DE" --organismo "GOBIERNO REGIONAL"

    # Rango de fechas explicito
    python buscar_tratos_directos_proveedor.py --rut 76.123.456-7 --alias mi-proveedor \
        --desde 27/08/2022 --hasta 27/08/2026

Requiere: sin credenciales previas (token anonimo obtenido en runtime, valido ~8h)
"""

import json
import sys
import time
import argparse
import unicodedata
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime
from pathlib import Path

AUTH_URL = "https://servicios-prd.mercadopublico.cl/v1/auth/publico"
BUSCAR_URL = "https://serv-trato-directo.mercadopublico.cl/v1/trato-directo-busqueda/buscar"

DEFAULT_OUT_DIR = Path(__file__).parent.parent / "data"


def normalizar(texto: str) -> str:
    texto = (texto or "").upper()
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn").strip()


def coincide_organismo(nombre_organismo: str, filtros_normalizados: list) -> bool:
    if not filtros_normalizados:
        return True
    nombre_norm = normalizar(nombre_organismo)
    return any(f in nombre_norm for f in filtros_normalizados)


def get_json(url, headers=None, intentos=6):
    headers = dict(headers or {})
    headers.setdefault("User-Agent", "Mozilla/5.0")
    headers.setdefault("Accept", "application/json")
    for i in range(intentos):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                espera = 10 * (i + 1)
                print(f"  429, esperando {espera}s (intento {i+1}/{intentos})...", file=sys.stderr)
                time.sleep(espera)
                continue
            raise
    raise RuntimeError(f"Agotados los reintentos para {url}")


def obtener_token() -> str:
    data = get_json(AUTH_URL)
    return data["payload"]["access_token"]


def buscar_pagina(token, rut_proveedor, date_from, date_to, page, size=50):
    params = {
        "dateFrom": date_from,
        "dateTo": date_to,
        "orderBy": "1",
        "page": str(page),
        "size": str(size),
        "provider": rut_proveedor,
    }
    url = BUSCAR_URL + "?" + urllib.parse.urlencode(params)
    return get_json(url, headers={"Authorization": f"Bearer {token}"})


def procesar_proveedor(rut_proveedor, alias, date_from, date_to, filtros_organismo, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"tratos_directos_{alias}.jsonl"
    progreso_path = out_dir / f"progreso_td_{alias}.json"
    filtros_normalizados = [normalizar(f) for f in filtros_organismo]

    progreso = {}
    if progreso_path.exists():
        progreso = json.loads(progreso_path.read_text(encoding="utf-8"))

    estado_prov = progreso.get(alias, {"pagina_completada": -1, "total_paginas": None, "total_elementos": None})

    token = obtener_token()
    print(f"[{alias}] token obtenido")

    pagina = estado_prov["pagina_completada"] + 1
    total_paginas = estado_prov["total_paginas"]
    total_elementos = estado_prov["total_elementos"]
    guardados = 0

    modo = "a" if (out_path.exists() and pagina > 0) else "w"
    with open(out_path, modo, encoding="utf-8") as f:
        while total_paginas is None or pagina < total_paginas:
            data = buscar_pagina(token, rut_proveedor, date_from, date_to, pagina)
            payload = data["payload"]
            total_paginas = payload["totalPages"]
            total_elementos = payload["totalElements"]
            for item in payload["content"]:
                nombre_organismo = item.get("nombreOrganismo", "")
                if not coincide_organismo(nombre_organismo, filtros_normalizados):
                    continue
                registro = {
                    "rut_proveedor": rut_proveedor,
                    "alias_proveedor": alias,
                    "proveedor": item.get("nombreProveedor"),
                    "codigo_proceso": item.get("idFicha"),
                    "tipo_proceso": "TD",
                    "nombre": item.get("nombre"),
                    "nombre_organismo": nombre_organismo,
                    "estado": item.get("estado"),
                    "causal": item.get("causal"),
                    "fecha_publicacion": item.get("fechaPublicacion"),
                    "fecha_creacion": item.get("fechaCreacion"),
                    "monto_total": item.get("montoTotal"),
                    "moneda": item.get("moneda"),
                    "nombre_moneda": item.get("nombreMoneda"),
                    "monto_referencial_clp": item.get("montoReferencial"),
                }
                f.write(json.dumps(registro, ensure_ascii=False) + "\n")
                guardados += 1
            f.flush()
            print(f"[{alias}] pagina {pagina + 1}/{total_paginas} procesada, {guardados} coincidencias hasta ahora")
            progreso[alias] = {"pagina_completada": pagina, "total_paginas": total_paginas, "total_elementos": total_elementos}
            progreso_path.write_text(json.dumps(progreso, ensure_ascii=False, indent=2), encoding="utf-8")
            pagina += 1
            time.sleep(1.5)

    alcance = f"organismos que coinciden con {filtros_organismo}" if filtros_organismo else "sin filtro de organismo"
    print(f"[{alias}] COMPLETO: {total_elementos} tratos directos nacionales revisados, {guardados} guardados ({alcance})")
    return total_elementos, guardados


def main():
    parser = argparse.ArgumentParser(description="Busca tratos directos adjudicados a un proveedor, opcionalmente acotado a organismos")
    parser.add_argument("--rut", required=True, help="RUT del proveedor, formato 76.123.456-7")
    parser.add_argument("--alias", required=True, help="Alias corto para el archivo de salida (ej: mi-proveedor)")
    parser.add_argument("--organismo", action="append", default=[], help="Texto que debe contener el nombre del organismo (repetible, sin filtro = todos)")
    parser.add_argument("--desde", default=None, help="Fecha desde, DD/MM/YYYY (default: hace 4 anos)")
    parser.add_argument("--hasta", default=None, help="Fecha hasta, DD/MM/YYYY (default: hoy)")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUT_DIR), help="Directorio de salida")
    args = parser.parse_args()

    hoy = datetime.now()
    hasta = args.hasta or hoy.strftime("%d/%m/%Y")
    desde = args.desde or hoy.replace(year=hoy.year - 4).strftime("%d/%m/%Y")

    procesar_proveedor(args.rut, args.alias, desde, hasta, args.organismo, Path(args.output_dir))


if __name__ == "__main__":
    main()
