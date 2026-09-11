"""
monitor_oc.py

Consulta Ordenes de Compra emitidas a un organismo en Mercado Publico
(API v1 de ChileCompra). Genera alertas por umbral de monto.

COMPORTAMIENTO VERIFICADO:
  - El listado por fecha + organismo retorna solo: Codigo, CodigoEstado.
  - Para montos, proveedor e items: consultar por codigo individual.
  - Estructura OC: TotalNeto + Impuestos = Total (CLP)

Uso:
    python monitor_oc.py --organismo <CODIGO_ORGANISMO>
    python monitor_oc.py --organismo <CODIGO_ORGANISMO> --fecha 11052026
    python monitor_oc.py --codigo 2403-154-SE26
    python monitor_oc.py --organismo <CODIGO_ORGANISMO> --umbral 5000000
    python monitor_oc.py --organismo <CODIGO_ORGANISMO> --detalle --output oc.json

Requiere:
    TICKET_MP y (opcionalmente) CODIGO_ORGANISMO_MP en .env o variables de entorno
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
from datetime import datetime, date
from pathlib import Path

BASE_URL = "https://api.mercadopublico.cl/servicios/v1/publico"

ESTADOS_OC = {
    1: "Enviada a proveedor",
    2: "Aceptada",
    3: "Cancelada",
    4: "Enviada a proveedor",
    5: "Pendiente de recepcionar",
    6: "Recepcionada parcialmente",
    7: "Recepcion conforme",
    8: "Aceptada",
    12: "Enviada a proveedor",
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
        print(f"ERROR HTTP {e.code}: {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


def consultar_oc_detalle(ticket: str, codigo: str) -> dict:
    url = f"{BASE_URL}/ordenesdecompra.json?ticket={ticket}&codigo={codigo}"
    data = get_json(url)
    listado = data.get("Listado", [])
    return listado[0] if listado else {}


def main():
    parser = argparse.ArgumentParser(description="Monitor de Ordenes de Compra en Mercado Publico")
    parser.add_argument("--organismo", type=str, help="CodigoOrganismo a consultar (o CODIGO_ORGANISMO_MP en .env)")
    parser.add_argument("--fecha", type=str, help="Fecha DDMMYYYY (default: hoy)")
    parser.add_argument("--codigo", type=str, help="Codigo especifico de OC")
    parser.add_argument("--detalle", action="store_true", help="Descarga detalle completo de cada OC")
    parser.add_argument("--umbral", type=float, default=0, help="Monto total minimo para alerta (CLP)")
    parser.add_argument("--output", type=str, help="Archivo de salida JSON")
    args = parser.parse_args()

    ticket, organismo_default = cargar_config()
    organismo = args.organismo or organismo_default

    if args.codigo:
        print(f"Consultando OC {args.codigo}...")
        oc = consultar_oc_detalle(ticket, args.codigo)
        if not oc:
            print("No encontrada.")
            sys.exit(0)
        print(json.dumps(oc, ensure_ascii=False, indent=2))
        if args.output:
            Path(args.output).write_text(json.dumps(oc, ensure_ascii=False, indent=2), encoding="utf-8")
        return

    if not organismo:
        print("ERROR: especificar --organismo o CODIGO_ORGANISMO_MP en .env")
        sys.exit(1)

    fecha = args.fecha or date.today().strftime("%d%m%Y")

    url = f"{BASE_URL}/ordenesdecompra.json?ticket={ticket}&CodigoOrganismo={organismo}&fecha={fecha}"
    print(f"Consultando OC de organismo={organismo} fecha={fecha}...")
    data = get_json(url)
    listado = data.get("Listado", [])
    print(f"Resultados: {len(listado)} OC\n")

    if not listado:
        print("Sin resultados.")
        return

    print(f"{'Codigo':<20} {'Estado':<30} Nombre")
    print("-" * 90)
    for oc in listado:
        codigo = oc.get("Codigo") or oc.get("CodigoExterno", "?")
        estado_num = oc.get("CodigoEstado", 0)
        estado = ESTADOS_OC.get(estado_num, str(estado_num))
        nombre = (oc.get("Nombre") or "")[:45]
        print(f"{codigo:<20} {estado:<30} {nombre}")

    alertas = []
    resultado_completo = []

    if args.detalle or args.umbral > 0:
        print(f"\nDescargando detalle de {len(listado)} OC...")
        for i, oc in enumerate(listado):
            codigo = oc.get("Codigo") or oc.get("CodigoExterno", "")
            print(f"  [{i+1}/{len(listado)}] {codigo}...", end=" ", flush=True)
            detalle = consultar_oc_detalle(ticket, codigo)
            resultado_completo.append(detalle)

            total = detalle.get("Total") or 0
            if args.umbral > 0 and total >= args.umbral:
                proveedor = detalle.get("Proveedor", {})
                nombre_prov = proveedor.get("Nombre", "?") if isinstance(proveedor, dict) else str(proveedor)
                alertas.append({"codigo": codigo, "total": total, "proveedor": nombre_prov})
                print(f"OK [ALERTA ${total:,.0f}]")
            else:
                print("OK")
    else:
        resultado_completo = listado

    if alertas:
        print(f"\n=== ALERTAS (umbral: ${args.umbral:,.0f} CLP) ===")
        for a in alertas:
            print(f"  {a['codigo']}  ${a['total']:>14,.0f}  Proveedor: {a['proveedor']}")

    if args.output:
        out = {
            "Cantidad": len(resultado_completo),
            "FechaConsulta": datetime.now().isoformat(),
            "Fecha": fecha,
            "Organismo": organismo,
            "Alertas": alertas,
            "Listado": resultado_completo,
        }
        Path(args.output).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nGuardado en: {args.output}")


if __name__ == "__main__":
    main()
