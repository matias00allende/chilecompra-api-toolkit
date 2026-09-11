"""
descargar_adjuntos_trato_directo.py

Descarga todos los adjuntos (decreto, informe tecnico, cotizaciones) de una o mas
fichas de Trato Directo de Mercado Publico, usando el mismo token anonimo del
backend de Trato Directo (ver docs/trato-directo.md para el patron de auth).

Flujo por ficha:
  1. GET .../trato-directo-busqueda/detalle?idFicha=<X>  -> ids de adjuntos
  2. GET .../adjuntos-api/3000/1/<idAdjunto>              -> URL S3 presignada
  3. Descarga del binario con esa URL (sin auth adicional)

Uso:
    python descargar_adjuntos_trato_directo.py --codigo 2403-28-FTD25
    python descargar_adjuntos_trato_directo.py --codigos-file codigos.txt --output-dir data/anexos
"""

import json
import sys
import time
import argparse
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

AUTH_URL = "https://servicios-prd.mercadopublico.cl/v1/auth/publico"
DETALLE_URL = "https://serv-trato-directo.mercadopublico.cl/v1/trato-directo-busqueda/detalle"
ADJUNTO_URL = "https://adjuntos-api.adjuntos.mercadopublico.cl/adjuntos-api/3000/1"

DEFAULT_OUT = Path(__file__).parent.parent / "data" / "anexos"


def get_json(url, headers=None, intentos=6):
    headers = dict(headers or {})
    headers.setdefault("User-Agent", "Mozilla/5.0")
    headers.setdefault("Accept", "application/json")
    headers.setdefault("Referer", "https://trato-directo.mercadopublico.cl/")
    headers.setdefault("Origin", "https://trato-directo.mercadopublico.cl")
    for i in range(intentos):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 403):
                espera = 8 * (i + 1)
                print(f"  {e.code}, esperando {espera}s...", file=sys.stderr)
                time.sleep(espera)
                continue
            raise
    raise RuntimeError(f"Agotados los reintentos para {url}")


def obtener_token():
    return get_json(AUTH_URL)["payload"]["access_token"]


def detalle_ficha(codigo, token):
    url = f"{DETALLE_URL}?{urllib.parse.urlencode({'idFicha': codigo})}"
    return get_json(url, {"Authorization": f"Bearer {token}"})["payload"]


def resolver_adjunto(id_adjunto, token):
    url = f"{ADJUNTO_URL}/{id_adjunto}"
    data = get_json(url, {"Authorization": f"Bearer {token}"})
    adjuntos = data.get("adjuntos") or []
    return adjuntos[0] if adjuntos else None


def descargar(url, destino: Path):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        destino.write_bytes(r.read())


def extraer_ids_adjuntos(detalle):
    """Devuelve lista de (rol, idAdjunto) para todos los adjuntos referenciados en el detalle."""
    ids = []
    for cot in detalle.get("cotizaciones", []) or []:
        if cot.get("idAdjunto"):
            ids.append(("cotizacion", cot["idAdjunto"]))
    for campo, rol in [
        ("adjuntoResolucionDecreto", "decreto"),
        ("adjuntoCausal", "causal"),
        ("adjuntoOpcional", "opcional"),
    ]:
        info = detalle.get(campo)
        if info and info.get("idAdjunto"):
            ids.append((rol, info["idAdjunto"]))
    return ids


def procesar_ficha(codigo, token, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"[{codigo}] consultando detalle...")
    detalle = detalle_ficha(codigo, token)
    ids = extraer_ids_adjuntos(detalle)
    print(f"[{codigo}] {len(ids)} adjunto(s) referenciados")

    resultado = {
        "codigo_proceso": codigo,
        "nombre": detalle.get("nombre"),
        "causal": detalle.get("causalTratoDirecto"),
        "monto_total": detalle.get("montoTotal"),
        "moneda": detalle.get("moneda"),
        "rut_proveedor": detalle.get("rutProveedor"),
        "proveedor": detalle.get("proveedor"),
        "nombre_comprador": detalle.get("nombreComprador") or detalle.get("nombreLegalComprador"),
        "fecha_publicacion": detalle.get("fechaPublicacion"),
        "adjuntos_descargados": [],
    }

    for rol, id_adjunto in ids:
        info = resolver_adjunto(id_adjunto, token)
        if not info:
            print(f"[{codigo}]   adjunto {id_adjunto} ({rol}): sin metadata (vacio)")
            continue
        filename = info["filename"]
        safe_name = f"{codigo}_{rol}_{filename}".replace("/", "-")
        destino = out_dir / safe_name
        try:
            descargar(info["URL"], destino)
            tamano_ok = destino.stat().st_size == int(info["size"])
            print(f"[{codigo}]   {rol}: {filename} -> {destino.name} ({destino.stat().st_size}B, esperado {info['size']}B, {'OK' if tamano_ok else 'MISMATCH'})")
            resultado["adjuntos_descargados"].append({
                "rol": rol, "filename": filename, "archivo_local": str(destino),
                "size_esperado": int(info["size"]), "size_real": destino.stat().st_size,
                "tamano_ok": tamano_ok,
            })
        except Exception as e:
            print(f"[{codigo}]   {rol}: {filename} -> ERROR: {e}")
        time.sleep(2)

    return resultado


def main():
    parser = argparse.ArgumentParser(description="Descarga adjuntos de fichas de Trato Directo")
    parser.add_argument("--codigo", action="append", default=[], help="Codigo de ficha (repetible)")
    parser.add_argument("--codigos-file", help="Archivo con un codigo de ficha por linea")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUT), help="Directorio de salida")
    parser.add_argument("--output-json", help="Guardar resumen JSON de la corrida")
    args = parser.parse_args()

    codigos = list(args.codigo)
    if args.codigos_file:
        codigos += [l.strip() for l in Path(args.codigos_file).read_text(encoding="utf-8").splitlines() if l.strip()]

    if not codigos:
        print("ERROR: especificar --codigo o --codigos-file")
        sys.exit(1)

    token = obtener_token()
    print(f"Token obtenido. Procesando {len(codigos)} ficha(s)...\n")

    out_dir = Path(args.output_dir)
    resultados = []
    for codigo in codigos:
        resultados.append(procesar_ficha(codigo, token, out_dir))
        time.sleep(1)

    if args.output_json:
        Path(args.output_json).write_text(json.dumps(resultados, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nResumen guardado en {args.output_json}")


if __name__ == "__main__":
    main()
