"""
monitor_consulta_mercado.py

Consulta las "Consultas al Mercado" (RFI - Request for Information) de un
organismo publico chileno en Mercado Publico, filtrando por CodigoOrganismo
o RUT.

Mecanismo distinto de Licitacion, Orden de Compra, Compra Agil o Trato Directo:
es un sondeo previo, informativo y no vinculante, regulado en el Reglamento de
la Ley 19.886, usado para levantar informacion tecnica/comercial del mercado
antes de un proceso de compra formal. Codigo con sufijo "-RFIAA" (ej. 5001-9-RFI26).

Backend no documentado en la API v1/v2 publica de ChileCompra - ver
docs/consulta-mercado-rfi.md para el detalle completo del descubrimiento y la
API. Resumen:
  - Backend propio, distinto de api.mercadopublico.cl y api2.mercadopublico.cl.
  - Front-end SPA: https://consulta-mercado.mercadopublico.cl/buscador-publico
  - Auth: GET https://servicios-prd.mercadopublico.cl/v1/auth/publico
    Retorna un JWT anonimo, vida corta (~8h). Se pide uno nuevo por ejecucion,
    no requiere ticket ni login. NO es el TICKET_MP de las APIs v1/v2.
  - Listado: GET https://servicios-consultas-prd.mercadopublico.cl/v1/consulta-mercado
    Sin parametro de filtro por organismo/RUT: hay que paginar todo el
    universo nacional y filtrar localmente por codigoInstitucion o rutOrganismo.
    pageSize fijo en 15, no configurable.

Uso:
    python monitor_consulta_mercado.py --codigo-organismo 12345              # anio actual completo
    python monitor_consulta_mercado.py --rut-organismo 12.345.678-9 --desde 2026-01-01 --hasta 2026-08-20
    python monitor_consulta_mercado.py --codigo-organismo 12345 --estado 100  # solo publicadas/activas
    python monitor_consulta_mercado.py --codigo-organismo 12345 --output rfi-2026.json

No requiere TICKET_MP ni .env: el token se obtiene de forma anonima en cada
ejecucion.
"""

import sys
import json
import argparse
import time
from datetime import date
from pathlib import Path

import requests

AUTH_URL = "https://servicios-prd.mercadopublico.cl/v1/auth/publico"
BASE_URL = "https://servicios-consultas-prd.mercadopublico.cl/v1/consulta-mercado"


def obtener_token() -> str:
    resp = requests.get(AUTH_URL, timeout=20)
    resp.raise_for_status()
    return resp.json()["payload"]["access_token"]


def paginar(token: str, desde: str, hasta: str, estado=None) -> list:
    todos = []
    pagina = 1
    pageCount = 1
    headers = {"Authorization": f"Bearer {token}"}
    while pagina <= pageCount:
        params = {"desde": desde, "hasta": hasta, "ordenarPor": 100, "pagina": pagina}
        if estado is not None:
            params["estado"] = estado
        for intento in range(3):
            resp = requests.get(BASE_URL, params=params, headers=headers, timeout=30)
            if resp.status_code == 401:
                # token expirado a mitad de barrido: renovar y reintentar la misma pagina
                token = obtener_token()
                headers = {"Authorization": f"Bearer {token}"}
                continue
            resp.raise_for_status()
            data = resp.json()
            break
        else:
            print(f"  ERROR: fallo definitivo en pagina {pagina}, abortando.")
            break
        payload = data["payload"]
        pageCount = payload["pageCount"]
        todos.extend(payload["resultados"])
        if pagina == 1 or pagina % 25 == 0 or pagina == pageCount:
            print(f"  pagina {pagina}/{pageCount} - {payload['resultCount']} resultados totales")
        pagina += 1
        time.sleep(0.3)
    return todos


def filtrar_organismo(items: list, codigo_organismo=None, rut_organismo=None) -> list:
    return [
        i for i in items
        if (codigo_organismo and str(i.get("codigoInstitucion")) == str(codigo_organismo))
        or (rut_organismo and (i.get("rutOrganismo") or "").lower() == rut_organismo.lower())
    ]


def main():
    parser = argparse.ArgumentParser(description="Monitor Consultas al Mercado (RFI) de un organismo")
    parser.add_argument("--codigo-organismo", type=str, help="CodigoOrganismo (mismo valor que CodigoOrganismo en la API v1)")
    parser.add_argument("--rut-organismo", type=str, help="RUT del organismo, formato 12.345.678-9")
    parser.add_argument("--desde", type=str, help="Fecha inicio YYYY-MM-DD (default: 1-ene del anio actual)")
    parser.add_argument("--hasta", type=str, help="Fecha fin YYYY-MM-DD (default: hoy)")
    parser.add_argument("--estado", type=int, choices=[100, 200], help="100=Publicadas, 200=Cerradas (default: ambos)")
    parser.add_argument("--output", type=str, help="Archivo de salida JSON")
    args = parser.parse_args()

    if not args.codigo_organismo and not args.rut_organismo:
        print("ERROR: especifica --codigo-organismo o --rut-organismo")
        sys.exit(1)

    hoy = date.today()
    desde = f"{args.desde or f'{hoy.year}-01-01'} 00:00:00"
    hasta = f"{args.hasta or hoy.isoformat()} 23:59:59"

    print("Obteniendo token anonimo...")
    token = obtener_token()

    encontrados = []
    estados = [args.estado] if args.estado else [100, 200]
    for estado in estados:
        etiqueta = {100: "Publicadas", 200: "Cerradas"}[estado]
        print(f"Barriendo estado={estado} ({etiqueta}) entre {desde} y {hasta}...")
        items = paginar(token, desde, hasta, estado)
        filtrados = filtrar_organismo(items, args.codigo_organismo, args.rut_organismo)
        print(f"  -> {len(items)} a nivel nacional, {len(filtrados)} del organismo consultado")
        encontrados.extend(filtrados)

    encontrados.sort(key=lambda x: x.get("fechaPublicacion", ""))

    print(f"\n{'Codigo':<18} {'Estado':<12} {'FechaPublicacion':<20} Nombre")
    print("-" * 100)
    for r in encontrados:
        estado_txt = {100: "Publicada", 200: "Cerrada"}.get(r.get("estado"), str(r.get("estado")))
        fecha = (r.get("fechaPublicacion") or "")[:16]
        print(f"{r.get('codigoConsulta', '?'):<18} {estado_txt:<12} {fecha:<20} {(r.get('nombre') or '')[:55]}")
    print(f"\nTotal Consultas al Mercado del organismo en el rango: {len(encontrados)}")

    if args.output:
        Path(args.output).write_text(
            json.dumps({"Cantidad": len(encontrados), "Desde": desde, "Hasta": hasta, "Listado": encontrados},
                       ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"Guardado en: {args.output}")


if __name__ == "__main__":
    main()
