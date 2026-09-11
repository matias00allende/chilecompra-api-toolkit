#!/usr/bin/env python3
"""
Monitor de Compra Agil para un organismo publico chileno.

Consulta la API v2 de ChileCompra (api2.mercadopublico.cl) para listar,
filtrar y sincronizar Compras Agiles de un organismo, identificado por su RUT.

COMPORTAMIENTO REAL VERIFICADO:
- tamano_pagina minimo: 10 (no 1 o 5 - retorna 400)
- tamano_pagina maximo: 50
- Sin filtro, la cuota se agota rapido (200 paginas x region x estado)
- Usar siempre --horas o --estado para acotar; nunca paginar sin filtro de tiempo
- La cuota de la API v2 es INDEPENDIENTE de la cuota v1
- No existe filtro `codigo_organismo` en la API v2: hay que filtrar localmente
  por RUT dentro de una region (ver docs/api-v2-compra-agil.md)

Uso:
    # Compras Agiles activas del organismo (ultimas 24h, recomendado)
    python monitor_compra_agil.py --rut 12.345.678-9 --region 13 --horas 24

    # Por estado
    python monitor_compra_agil.py --rut 12.345.678-9 --region 13 --estado publicada
    python monitor_compra_agil.py --rut 12.345.678-9 --region 13 --estado proveedor_seleccionado

    # Detalle de una CA especifica
    python monitor_compra_agil.py --codigo 1057539-228-COT26

    # Busqueda por palabras clave (toda la region indicada, sin filtro de RUT)
    python monitor_compra_agil.py --buscar "materiales electricos" --region 13

    # Exportar a JSON
    python monitor_compra_agil.py --rut 12.345.678-9 --region 13 --horas 24 --output compras-agiles.json
"""

import os
import sys
import json
import argparse
import requests
from dotenv import load_dotenv

load_dotenv()

TICKET = os.getenv("TICKET_MP", "")
BASE_V2 = "https://api2.mercadopublico.cl"


def get_headers():
    if not TICKET:
        print("[ERROR] Variable TICKET_MP no configurada en .env")
        sys.exit(1)
    return {"ticket": TICKET}


def paginar(params_base):
    """Itera todas las paginas de resultados y retorna lista consolidada."""
    todos = []
    pagina = 1
    while True:
        # tamano_pagina minimo validado por la API es 10; maximo 50
        params = {**params_base, "tamano_pagina": 50, "numero_pagina": pagina}
        resp = requests.get(f"{BASE_V2}/v2/compra-agil", headers=get_headers(), params=params)
        if resp.status_code == 429:
            print("[ERROR] Cuota diaria agotada. Intentar manana.")
            sys.exit(1)
        resp.raise_for_status()
        data = resp.json()
        if data.get("success") != "OK":
            print(f'[ERROR] API retorno error: {data.get("errors")}')
            sys.exit(1)
        payload = data["payload"]
        pag = payload["paginacion"]
        todos.extend(payload["items"])
        print(f'  pagina {pag["numero_pagina"]}/{pag["total_paginas"]} - {len(payload["items"])} items', flush=True)
        if pagina >= pag["total_paginas"]:
            break
        pagina += 1
    return todos


def listar_organismo(rut, region, estado=None, horas=None):
    """Lista Compras Agiles de un organismo filtrando localmente por RUT.

    NOTA: Requiere ttl_cambio_ms o estado para no paginar todo el universo de
    la region. Sin filtro de tiempo, la cuota se agota en decenas de requests.
    """
    params = {"region": region, "ordenar_por": "FechaUltimaModificacion"}
    if estado:
        params["estado"] = estado
    if horas:
        params["ttl_cambio_ms"] = horas * 3600 * 1000
    elif not estado:
        # Defecto conservador: ultimas 48h para no agotar cuota
        params["ttl_cambio_ms"] = 48 * 3600 * 1000
        print("[INFO] Sin filtro de tiempo ni estado. Usando ultimas 48h por defecto.")
    desc = f"region={region}{', estado=' + estado if estado else ''}"
    desc += f", ultimas {horas}h" if horas else (", ultimas 48h (defecto)" if not estado else "")
    print(f"Consultando API v2 ({desc})...")
    items = paginar(params)
    return [i for i in items if i["institucion"]["rut"].lower() == rut.lower()]


def detalle_ca(codigo):
    """Obtiene el detalle completo de una Compra Agil."""
    resp = requests.get(f"{BASE_V2}/v2/compra-agil/{codigo}", headers=get_headers())
    if resp.status_code == 404:
        print(f"[ERROR] Codigo {codigo} no encontrado en la API")
        sys.exit(1)
    if resp.status_code == 429:
        print("[ERROR] Cuota diaria agotada.")
        sys.exit(1)
    resp.raise_for_status()
    data = resp.json()
    if data.get("success") != "OK":
        print(f'[ERROR] {data.get("errors")}')
        sys.exit(1)
    return data["payload"]


def buscar_keywords(q, region, estado=None):
    """Busca Compras Agiles por palabras clave en una region (sin filtro de organismo)."""
    params = {"q": q, "region": region, "ordenar_por": "FechaUltimaModificacion"}
    if estado:
        params["estado"] = estado
    print(f'Buscando "{q}" en region {region}...')
    return paginar(params)


def imprimir_listado(items):
    """Imprime el listado de Compras Agiles."""
    if not items:
        print("Sin resultados.")
        return
    print(f'\n{"CODIGO":<25} {"ESTADO":<25} {"MONTO CLP":>14}  NOMBRE')
    print("-" * 100)
    for i in items:
        codigo = i["codigo"]
        estado_glosa = i["estado"]["glosa"]
        monto = i["montos"].get("monto_disponible_clp") or 0
        nombre = i["nombre"][:55]
        print(f"{codigo:<25} {estado_glosa:<25} {monto:>14,.0f}  {nombre}")
    print(f"\nTotal: {len(items)} Compras Agiles")


def imprimir_detalle(ca):
    """Imprime el detalle de una Compra Agil."""
    print(f'\n=== {ca["codigo"]} ===')
    print(f'Nombre    : {ca["nombre"]}')
    print(f'Estado    : {ca["estado"]["glosa"]}')
    print(f'Organismo : {ca["institucion"]["organismo_comprador"]} ({ca["institucion"]["rut"]})')
    print(f'Unidad    : {ca["institucion"]["unidad_compra"]}')
    print(f'Presupuesto: ${ca["presupuesto"].get("monto_disponible_clp") or 0:,.0f} {ca["presupuesto"]["moneda"]}')
    print(f'Cierre    : {ca["fechas"]["fecha_cierre"]}')
    print(f'Convocatoria: {ca["convocatoria"]["descripcion"]}')
    print()
    print(f'Productos ({len(ca["productos_solicitados"])})::')
    for p in ca["productos_solicitados"]:
        print(f'  [{p["codigo_producto"]}] {p["nombre"]} x{p["cantidad"]} {p.get("unidad_medida", "")}')
    print()
    provs = ca.get("proveedores_cotizando", [])
    print(f"Proveedores cotizando ({len(provs)}):")
    for p in provs:
        selec = " [SELECCIONADO]" if p.get("seleccion", {}).get("proveedor_seleccionado") else ""
        emt = " (EMT)" if p.get("es_emt") else ""
        total = p.get("monto_total") or 0
        print(f'  {p["rut_proveedor"]} - {p["razon_social"]}{emt}{selec} - ${total:,.0f}')
    oc = ca.get("orden_compra", {})
    if oc.get("id_orden_compra"):
        print(f'\nOC emitida: id={oc["id_orden_compra"]} | codigo={oc.get("codigo_orden_compra") or "(consultar API v1)"}')
    flags = ca.get("flags", {})
    if flags.get("considera_requisitos_medioambientales"):
        print("[FLAG] Considera requisitos medioambientales")
    if flags.get("considera_requisitos_impacto_social_economico"):
        print("[FLAG] Considera requisitos de impacto social/economico")


def main():
    parser = argparse.ArgumentParser(description="Monitor Compra Agil de un organismo (API v2)")
    parser.add_argument("--rut", help="RUT del organismo comprador, formato 12.345.678-9 (obligatorio salvo --codigo/--buscar)")
    parser.add_argument("--region", type=int, default=13, help="Codigo de region 1-16 (default: 13, Metropolitana)")
    parser.add_argument("--codigo", help="Codigo exacto de Compra Agil (ej: 1057539-228-COT26)")
    parser.add_argument("--estado", help="Estado: publicada, cerrada, desierta, cancelada, proveedor_seleccionado")
    parser.add_argument("--horas", type=int, help="Cambios en las ultimas N horas")
    parser.add_argument("--buscar", help="Palabras clave para buscar (toda la region, sin filtro de RUT)")
    parser.add_argument("--output", help="Exportar resultados a archivo JSON")
    args = parser.parse_args()

    resultado = None

    if args.codigo:
        ca = detalle_ca(args.codigo)
        imprimir_detalle(ca)
        resultado = ca
    elif args.buscar:
        items = buscar_keywords(args.buscar, args.region, estado=args.estado)
        imprimir_listado(items)
        resultado = items
    else:
        if not args.rut:
            print("ERROR: especifica --rut (o usa --codigo / --buscar)")
            sys.exit(1)
        items = listar_organismo(args.rut, args.region, estado=args.estado, horas=args.horas)
        imprimir_listado(items)
        resultado = items

    if args.output and resultado is not None:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(resultado, f, ensure_ascii=False, indent=2)
        print(f"\nExportado a {args.output}")


if __name__ == "__main__":
    main()
