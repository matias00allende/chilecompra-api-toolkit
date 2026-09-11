"""
buscar_comprador.py

Busca el CodigoOrganismo de un organismo comprador en el catalogo publico de
Mercado Publico (API v1 de ChileCompra), por nombre.

Uso:
    python buscar_comprador.py --buscar "nombre del organismo"
    python buscar_comprador.py --listar-municipios

Requiere:
    TICKET_MP en variable de entorno o en archivo .env del proyecto

NOTA sobre la API:
    BuscarComprador retorna los campos 'CodigoEmpresa' y 'NombreEmpresa'.
    El valor de 'CodigoEmpresa' se usa como parametro 'CodigoOrganismo'
    en los endpoints de licitaciones y ordenes de compra.
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
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
    print("ERROR: TICKET_MP no encontrado. Crear .env con TICKET_MP=<GUID>")
    sys.exit(1)


def buscar_compradores(ticket: str) -> list:
    url = f"{BASE_URL}/Empresas/BuscarComprador?ticket={ticket}"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            # La API retorna 'CodigoEmpresa' y 'NombreEmpresa' (no CodigoOrganismo/Nombre)
            return data.get("listaEmpresas", [])
    except urllib.error.HTTPError as e:
        print(f"ERROR HTTP {e.code}: {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Busca organismos compradores en Mercado Publico")
    parser.add_argument("--buscar", type=str, help="Texto a buscar en nombre del organismo (case insensitive)")
    parser.add_argument("--listar-municipios", action="store_true", help="Lista solo municipalidades")
    args = parser.parse_args()

    ticket = cargar_ticket()
    print(f"Consultando catalogo de organismos... (ticket: {ticket[:8]}...)")

    empresas = buscar_compradores(ticket)
    print(f"Total organismos registrados: {len(empresas)}\n")

    def nombre_normalizado(e):
        nombre = e.get("NombreEmpresa", "")
        try:
            return nombre.encode("latin-1").decode("utf-8")
        except Exception:
            return nombre

    if args.buscar:
        termino = args.buscar.lower()
        resultados = [
            e for e in empresas
            if termino in e.get("NombreEmpresa", "").lower() or termino in nombre_normalizado(e).lower()
        ]
        print(f"Resultados para '{args.buscar}':")
        for e in resultados:
            print(f"  CodigoOrganismo: {e.get('CodigoEmpresa')}  |  Nombre: {e.get('NombreEmpresa')}")
        if not resultados:
            print("  Sin resultados.")

    elif args.listar_municipios:
        municipios = [
            e for e in empresas
            if "unicipalidad" in e.get("NombreEmpresa", "").lower() or "unicipalidad" in nombre_normalizado(e).lower()
        ]
        print(f"Municipalidades encontradas: {len(municipios)}")
        for m in sorted(municipios, key=lambda x: x.get("NombreEmpresa", "")):
            print(f"  {m.get('CodigoEmpresa'):>10}  {m.get('NombreEmpresa')}")

    else:
        print("Especifica --buscar <termino> o --listar-municipios.")


if __name__ == "__main__":
    main()
