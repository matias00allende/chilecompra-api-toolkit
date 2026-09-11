"""
buscar_licitaciones_proveedor.py

Busca licitaciones publicas adjudicadas a un proveedor especifico, usando el
buscador nuevo de Mercado Publico (www.mercadopublico.cl/BuscarLicitacion),
filtrado por el ID INTERNO de proveedor (no el RUT) que retorna su propio
autocomplete. Permite acotar opcionalmente a uno o mas organismos por nombre.

IMPORTANTE: el indice de autocomplete de este buscador (Home/BuscarProveedor?q=)
es DISTINTO del indice usado por Trato Directo y puede no tener el nombre
exacto de razon social, usar variantes con/sin guion, o (mas grave) devolver
una empresa homonima distinta con RUT diferente. NO asumir que un match de
texto = el proveedor correcto: verificar el RUT real antes de confiar en el ID
(ej. via `Empresas/BuscarProveedor?rutempresaproveedor=<RUT>` de la API v1).

Uso:
    python buscar_licitaciones_proveedor.py --id-proveedor 34685 --alias mi-proveedor --idestado 8

    # Acotado a organismos cuyo nombre contenga alguno de estos textos (repetible)
    python buscar_licitaciones_proveedor.py --id-proveedor 34685 --alias mi-proveedor \
        --idestado 8 --organismo "MUNICIPALIDAD DE"
"""

import html as html_module
import json
import re
import sys
import time
import argparse
import unicodedata
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

BUSCAR_URL = "https://www.mercadopublico.cl/BuscarLicitacion/Home/Buscar"
AUTOCOMPLETE_URL = "https://www.mercadopublico.cl/BuscarLicitacion/Home/BuscarProveedor"
REFERER = "https://www.mercadopublico.cl/BuscarLicitacion?IsFirstTableDesign=True"

DEFAULT_OUT_DIR = Path(__file__).parent.parent / "data"


def normalizar(texto):
    texto = (texto or "").upper()
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn").strip()


def coincide_organismo(nombre_organismo, filtros_normalizados):
    if not filtros_normalizados:
        return True
    nombre_norm = normalizar(nombre_organismo)
    return any(f in nombre_norm for f in filtros_normalizados)


def buscar_proveedor_autocomplete(q):
    url = f"{AUTOCOMPLETE_URL}?q={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))


def post_buscar(id_proveedor, id_estado, fecha_inicio_iso, fecha_fin_iso, pagina, size=50, intentos=6):
    body = {
        "textoBusqueda": "", "idEstado": str(id_estado), "codigoRegion": "-1", "idTipoLicitacion": "-1",
        "fechaInicio": fecha_inicio_iso, "fechaFin": fecha_fin_iso,
        "registrosPorPagina": str(size), "idTipoFecha": [], "idOrden": "1", "compradores": [],
        "garantias": None, "rubros": [], "proveedores": [str(id_proveedor)],
        "montoEstimadoTipo": [0], "esPublicoMontoEstimado": None, "pagina": pagina,
    }
    data = json.dumps(body).encode("utf-8")
    for i in range(intentos):
        req = urllib.request.Request(BUSCAR_URL, data=data, method="POST", headers={
            "Content-Type": "application/json; charset=UTF-8", "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0", "Accept": "*/*", "Referer": REFERER,
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(8 * (i + 1))
                continue
            raise
    raise RuntimeError("Agotados los reintentos en post_buscar")


RE_CODIGO = re.compile(r'ID Licitaci\w+:</strong><span class="clearfix">\s*([\w\-]+)\s*</span>')
RE_NOMBRE = re.compile(r'<h2 class="text-weight-light">([^<]*)</h2>')
RE_MONTO_CLP = re.compile(r'<span class="highlight-text text-weight-light">\$</span>\s*<span class="highlight-text text-weight-light campo-numerico-punto-coma">([\d\.,]+)</span>')
RE_MONTO_UF = re.compile(r'<p><strong>Monto estimado</strong></p><span class="highlight-text text-weight-light">([\d\.,]+)</span>\s*<span>(\w+)</span>')
RE_MONTO_DISPONIBLE_UF = re.compile(r'<p><strong>Monto disponible\s*</strong></p><span class="highlight-text text-weight-light">([\d\.,]+)</span>\s*<span>(\w+)</span>')
RE_MONTO_RANGO = re.compile(r'<p><strong>Monto\s*</strong></p><span class="text-weight-light monto-no-publico">([^<]+)</span>')
RE_FECHA_PUB = re.compile(r'Fecha de publicaci\w+</strong></p><span class="highlight-text text-weight-light">([\d/]+)</span>')
RE_FECHA_CIERRE = re.compile(r'Fecha de cierre</strong></p><span class="highlight-text text-weight-light">([\d/]+)</span>')
RE_ORGANISMO = re.compile(r'<div class="col-md-4"><strong>([^<]{2,150})</strong>')
RE_ESTADO_TEXTO = re.compile(r'estado-texto">([^<]+)<')

ESTADOS_DISPONIBLES = {
    "5": "Publicada", "6": "Cerrada (en evaluacion, sin adjudicar)",
    "7": "Desierta", "8": "Adjudicada", "15": "Revocada", "-1": "Todos",
}


def parsear_resultados(html):
    """Extrae bloques de licitacion del HTML de respuesta. Best-effort - el HTML no es JSON."""
    items = []
    bloques = html.split('lic-bloq-wrap')[1:]
    for b in bloques:
        m_cod = RE_CODIGO.search(b)
        if not m_cod:
            continue
        m_nom = RE_NOMBRE.search(b)
        m_monto_clp = RE_MONTO_CLP.search(b)
        m_monto_uf = RE_MONTO_UF.search(b) or RE_MONTO_DISPONIBLE_UF.search(b)
        m_monto_rango = RE_MONTO_RANGO.search(b)
        m_fecha = RE_FECHA_PUB.search(b)
        m_fecha_cierre = RE_FECHA_CIERRE.search(b)
        m_org = RE_ORGANISMO.search(b)
        m_estado = RE_ESTADO_TEXTO.search(b)
        items.append({
            "codigo": m_cod.group(1),
            "nombre": html_module.unescape(m_nom.group(1).strip()) if m_nom else "",
            "estado_texto": html_module.unescape(m_estado.group(1).strip()) if m_estado else "",
            "monto_clp": m_monto_clp.group(1) if m_monto_clp else "",
            "monto_uf": m_monto_uf.group(1) if m_monto_uf else "",
            "monto_rango_no_publico": html_module.unescape(m_monto_rango.group(1).strip()) if m_monto_rango else "",
            "unidad_monto": m_monto_uf.group(2) if m_monto_uf else ("CLP" if m_monto_clp else ""),
            "fecha_publicacion": m_fecha.group(1) if m_fecha else "",
            "fecha_cierre": m_fecha_cierre.group(1) if m_fecha_cierre else "",
            "organismo_raw": html_module.unescape(m_org.group(1).strip()) if m_org else "",
        })
    return items


def total_resultados(html):
    m = re.search(r"<span class='n-result'>([\d\.]+)</span>", html)
    if m:
        return int(m.group(1).replace(".", ""))
    return 0


def procesar_proveedor(id_proveedor, alias, id_estado, fecha_inicio_iso, fecha_fin_iso, filtros_organismo, out_dir: Path, sufijo=""):
    out_path = out_dir / f"licitaciones_{alias}{sufijo}.jsonl"
    out_dir.mkdir(parents=True, exist_ok=True)
    filtros_normalizados = [normalizar(f) for f in filtros_organismo]

    pagina = 0
    total = None
    guardados = 0
    vistos = 0
    with open(out_path, "w", encoding="utf-8") as f:
        while True:
            html = post_buscar(id_proveedor, id_estado, fecha_inicio_iso, fecha_fin_iso, pagina)
            if total is None:
                total = total_resultados(html)
                print(f"[{alias}] total nacional reportado: {total}")
            items = parsear_resultados(html)
            if not items:
                print(f"[{alias}] pagina {pagina}: 0 bloques parseados (fin o parser desalineado)")
                break
            vistos += len(items)
            for it in items:
                if not coincide_organismo(it["organismo_raw"], filtros_normalizados):
                    continue
                it["rut_proveedor_id_autocomplete"] = id_proveedor
                it["alias_proveedor"] = alias
                it["tipo_proceso"] = "LP"
                it["idestado_consultado"] = str(id_estado)
                f.write(json.dumps(it, ensure_ascii=False) + "\n")
                guardados += 1
            print(f"[{alias}] pagina {pagina}: {len(items)} parseados, {vistos} vistos acumulados, {guardados} guardados")
            pagina += 1
            if len(items) < 10:
                break  # pagina incompleta = ultima pagina (el sitio pagina fijo en 10, ignora registrosPorPagina)
            time.sleep(1.5)

    alcance = f"organismos que coinciden con {filtros_organismo}" if filtros_organismo else "sin filtro de organismo"
    print(f"[{alias}] COMPLETO: {vistos}/{total} vistos, {guardados} guardados ({alcance})")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id-proveedor", required=True)
    parser.add_argument("--alias", required=True)
    parser.add_argument("--idestado", default="8",
                         help="Uno o mas separados por coma. 5=Publicada 6=Cerrada(sin adjudicar) 7=Desierta 8=Adjudicada 15=Revocada -1=Todos")
    parser.add_argument("--fecha-inicio", default="2022-08-27T00:00:00.000Z")
    parser.add_argument("--fecha-fin", default="2026-08-27T23:59:59.000Z")
    parser.add_argument("--organismo", action="append", default=[], help="Texto que debe contener el nombre del organismo (repetible, sin filtro = todos)")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUT_DIR), help="Directorio de salida")
    args = parser.parse_args()
    estados = [e.strip() for e in args.idestado.split(",") if e.strip()]
    for idestado in estados:
        nombre_estado = ESTADOS_DISPONIBLES.get(idestado, idestado)
        sufijo = f"_estado{idestado}" if len(estados) > 1 or idestado != "8" else ""
        print(f"=== {args.alias} - idEstado={idestado} ({nombre_estado}) ===")
        procesar_proveedor(args.id_proveedor, args.alias, idestado, args.fecha_inicio, args.fecha_fin, args.organismo, Path(args.output_dir), sufijo=sufijo)


if __name__ == "__main__":
    main()
