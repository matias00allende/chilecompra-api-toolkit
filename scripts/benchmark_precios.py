"""
benchmark_precios.py

Compara precios de adjudicacion para un codigo UNSPSC dado, filtrando
licitaciones adjudicadas a nivel nacional en los ultimos N meses.
Util para estimar precio de mercado antes de publicar una nueva licitacion.

Uso:
    python benchmark_precios.py --unspsc 43211501
    python benchmark_precios.py --unspsc 43211501 --meses 6
    python benchmark_precios.py --unspsc 43211501 --output reporte.json

Requiere:
    TICKET_MP en variable de entorno o en .env
"""

import os
import sys
import json
import argparse
import statistics
import urllib.request
import urllib.error
from datetime import datetime, timedelta
from pathlib import Path

BASE_URL = "https://api.mercadopublico.cl/servicios/v1/publico"


def cargar_ticket():
    ticket = os.environ.get("TICKET_MP")
    if ticket:
        return ticket
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        for linea in env_path.read_text().splitlines():
            if linea.startswith("TICKET_MP="):
                return linea.split("=", 1)[1].strip()
    print("ERROR: TICKET_MP no configurado.")
    sys.exit(1)


def consultar_licitaciones_fecha(ticket: str, fecha: str) -> list:
    url = f"{BASE_URL}/licitaciones.json?ticket={ticket}&estado=adjudicada&fecha={fecha}"
    try:
        with urllib.request.urlopen(url, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("Listado", [])
    except Exception:
        return []


def main():
    parser = argparse.ArgumentParser(description="Benchmark de precios por codigo UNSPSC")
    parser.add_argument("--unspsc", type=str, required=True, help="Codigo UNSPSC de 8 digitos (ej: 43211501)")
    parser.add_argument("--meses", type=int, default=3, help="Cantidad de meses hacia atras (default: 3)")
    parser.add_argument("--output", type=str, help="Archivo de salida JSON con detalle")
    args = parser.parse_args()

    ticket = cargar_ticket()

    # Generar fechas a consultar (una por semana para conservar cuota)
    hoy = datetime.now()
    fechas = []
    for semana in range(0, args.meses * 4):
        fecha = hoy - timedelta(weeks=semana)
        fechas.append(fecha.strftime("%d%m%Y"))

    print(f"Buscando licitaciones adjudicadas con UNSPSC '{args.unspsc}' en los ultimos {args.meses} meses...")
    print(f"Consultando {len(fechas)} fechas (una por semana para conservar cuota)...\n")

    items_encontrados = []
    licitaciones_revisadas = 0

    for fecha in fechas:
        licitaciones = consultar_licitaciones_fecha(ticket, fecha)
        licitaciones_revisadas += len(licitaciones)

        for lic in licitaciones:
            items = lic.get("Items", {}).get("Listado", []) if isinstance(lic.get("Items"), dict) else []
            for item in items:
                codigo_prod = str(item.get("CodigoProducto", ""))
                if args.unspsc in codigo_prod or codigo_prod.startswith(args.unspsc[:6]):
                    precio = item.get("MontoUnitario", 0) or 0
                    if precio > 0:
                        items_encontrados.append({
                            "licitacion": lic.get("CodigoExterno"),
                            "organismo": lic.get("Comprador", {}).get("NombreOrganismo", ""),
                            "fecha_adjudicacion": lic.get("Adjudicacion", {}).get("Fecha", ""),
                            "producto": item.get("NombreProducto", ""),
                            "codigo_unspsc": codigo_prod,
                            "cantidad": item.get("Cantidad", 0),
                            "precio_unitario": precio,
                            "moneda": lic.get("Moneda", "CLP"),
                        })

    print(f"Licitaciones revisadas: {licitaciones_revisadas}")
    print(f"Items con UNSPSC '{args.unspsc}' encontrados: {len(items_encontrados)}\n")

    if items_encontrados:
        precios = [i["precio_unitario"] for i in items_encontrados]
        print("=== Resumen estadistico de precios (precio unitario) ===")
        print(f"  Minimo:  {min(precios):>12,.0f}")
        print(f"  Maximo:  {max(precios):>12,.0f}")
        print(f"  Promedio:{statistics.mean(precios):>12,.0f}")
        print(f"  Mediana: {statistics.median(precios):>12,.0f}")
        if len(precios) > 1:
            print(f"  Desv.Est:{statistics.stdev(precios):>12,.0f}")
        print(f"  Muestra: {len(precios)} items en {len(set(i['licitacion'] for i in items_encontrados))} licitaciones")

        if args.output:
            reporte = {
                "unspsc": args.unspsc,
                "periodo_meses": args.meses,
                "fecha_consulta": datetime.now().isoformat(),
                "estadisticas": {
                    "minimo": min(precios),
                    "maximo": max(precios),
                    "promedio": statistics.mean(precios),
                    "mediana": statistics.median(precios),
                    "muestra": len(precios),
                },
                "items": items_encontrados,
            }
            Path(args.output).write_text(json.dumps(reporte, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"\nDetalle guardado en: {args.output}")
    else:
        print("Sin datos suficientes para el benchmark. Ampliar el periodo con --meses o verificar el codigo UNSPSC.")


if __name__ == "__main__":
    main()
