"""
monitor_licitaciones.py

Consulta licitaciones de un organismo en Mercado Publico (API v1 de ChileCompra).
Pensado para ejecucion periodica (cron/scheduler) o consulta puntual.

COMPORTAMIENTO VERIFICADO:
  - El endpoint de listado retorna solo 4 campos: CodigoExterno, Nombre,
    CodigoEstado, FechaCierre.
  - Para obtener el detalle completo (monto, proveedor, items, etc.)
    es necesario consultar cada licitacion por codigo individual.
  - CodigoEstado NO es confiable como fuente de estado (ver docs/api-v1-licitaciones-oc.md);
    usar siempre el campo de texto 'Estado' del detalle.

Uso:
    python monitor_licitaciones.py --organismo <CODIGO_ORGANISMO>
    python monitor_licitaciones.py --organismo <CODIGO_ORGANISMO> --estado adjudicada
    python monitor_licitaciones.py --codigo 2403-36-LR26
    python monitor_licitaciones.py --organismo <CODIGO_ORGANISMO> --detalle --output output.json

Requiere:
    TICKET_MP y (opcionalmente) CODIGO_ORGANISMO_MP en .env o variables de entorno
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

BASE_URL = "https://api.mercadopublico.cl/servicios/v1/publico"

ESTADOS_CODIGO = {
    1: "Publicada",
    2: "Cerrada",
    3: "Desierta",
    4: "Adjudicada",
    5: "Publicada (activa)",
    6: "Revocada",
    7: "Suspendida",
}


def cargar_config():
    env = {}
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        for linea in env_path.read_text().splitlines():
            if "=" in linea and not linea.startswith("#"):
                k, v = linea.split("=", 1)
                env[k.strip()] = v.strip()

    ticket = os.environ.get("TICKET_MP") or env.get("TICKET_MP")
    organismo = os.environ.get("CODIGO_ORGANISMO_MP") or env.get("CODIGO_ORGANISMO_MP")

    if not ticket:
        print("ERROR: TICKET_MP no configurado.")
        sys.exit(1)

    return ticket, organismo


def get_json(url: str) -> dict:
    try:
        with urllib.request.urlopen(url, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"ERROR HTTP {e.code}: {e.reason} - {url}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


def consultar_listado(ticket: str, params: dict) -> list:
    query = "&".join(f"{k}={v}" for k, v in params.items() if v is not None)
    url = f"{BASE_URL}/licitaciones.json?ticket={ticket}&{query}"
    data = get_json(url)
    return data.get("Listado", [])


def consultar_detalle(ticket: str, codigo: str) -> dict:
    url = f"{BASE_URL}/licitaciones.json?ticket={ticket}&codigo={codigo}"
    data = get_json(url)
    listado = data.get("Listado", [])
    return listado[0] if listado else {}


def main():
    parser = argparse.ArgumentParser(description="Monitor de licitaciones en Mercado Publico")
    parser.add_argument("--organismo", type=str, help="CodigoOrganismo a consultar (o CODIGO_ORGANISMO_MP en .env)")
    parser.add_argument("--estado", type=str, default="activas", help="Estado: activas, adjudicada, etc.")
    parser.add_argument("--fecha", type=str, help="Fecha DDMMYYYY")
    parser.add_argument("--codigo", type=str, help="Codigo especifico de licitacion")
    parser.add_argument("--detalle", action="store_true", help="Descarga detalle completo de cada licitacion")
    parser.add_argument("--output", type=str, help="Archivo de salida JSON")
    args = parser.parse_args()

    ticket, organismo_default = cargar_config()
    organismo = args.organismo or organismo_default

    if args.codigo:
        print(f"Consultando licitacion {args.codigo}...")
        lic = consultar_detalle(ticket, args.codigo)
        if not lic:
            print("No encontrada.")
            sys.exit(0)
        print(json.dumps(lic, ensure_ascii=False, indent=2))
        if args.output:
            Path(args.output).write_text(json.dumps(lic, ensure_ascii=False, indent=2), encoding="utf-8")
        return

    if not organismo:
        print("ERROR: especificar --organismo o CODIGO_ORGANISMO_MP en .env")
        sys.exit(1)

    params = {"estado": args.estado, "CodigoOrganismo": organismo}
    if args.fecha:
        params["fecha"] = args.fecha

    print(f"Consultando licitaciones [{args.estado}] organismo={organismo}...")
    listado = consultar_listado(ticket, params)
    print(f"Resultados: {len(listado)} licitaciones\n")

    if not listado:
        print("Sin resultados.")
        return

    print(f"{'Codigo':<20} {'Estado':<25} {'FechaCierre':<22} Nombre")
    print("-" * 100)
    for lic in listado:
        codigo = lic.get("CodigoExterno", "?")
        estado_num = lic.get("CodigoEstado", 0)
        estado = ESTADOS_CODIGO.get(estado_num, str(estado_num))
        fecha_cierre = lic.get("FechaCierre", "")[:16] if lic.get("FechaCierre") else "-"
        nombre = (lic.get("Nombre") or "")[:55]
        print(f"{codigo:<20} {estado:<25} {fecha_cierre:<22} {nombre}")

    resultado_completo = []
    if args.detalle:
        print(f"\nDescargando detalle completo de {len(listado)} licitaciones...")
        for i, lic in enumerate(listado):
            codigo = lic.get("CodigoExterno", "")
            print(f"  [{i+1}/{len(listado)}] {codigo}...", end=" ", flush=True)
            detalle = consultar_detalle(ticket, codigo)
            resultado_completo.append(detalle)
            print("OK")
    else:
        resultado_completo = listado

    if args.output:
        out = {"Cantidad": len(resultado_completo), "FechaConsulta": datetime.now().isoformat(), "Listado": resultado_completo}
        Path(args.output).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nGuardado en: {args.output}")


if __name__ == "__main__":
    main()
