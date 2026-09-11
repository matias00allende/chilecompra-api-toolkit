"""
leer_ficha_licitacion.py

Lee datos de la ficha publica de una Licitacion Publica (Mercado Publico) que
la API v1/v2 y el buscador HTML no exponen: monto real de adjudicacion (para
licitaciones con rango reservado) y ofertas economicas de TODOS los
oferentes, no solo el ganador (util para desglose comparativo por proveedor).

Hallazgo clave:
- La ficha se resuelve directo con
  https://www.mercadopublico.cl/Procurement/Modules/RFB/DetailsAcquisition.aspx?idlicitacion=<codigo>
  (parametro en texto plano, sin necesitar el "qs=" cifrado que usa la navegacion normal del sitio).
- El icono #imgAdjudicacion (deshabilitado si aun no hay adjudicacion) abre un FRAME
  (PreviewAwardAct.aspx) que muestra el acta de adjudicacion RENDERIZADA EN PANTALLA,
  con "Monto Neto Adjudicado" y "Monto Neto Estimado del Contrato" en texto plano,
  SIN CAPTCHA. El CAPTCHA solo protege la DESCARGA del PDF adjunto (Informe de
  Evaluacion, Decreto), no la lectura del acta en si.
- El icono #imgCuadroOferta abre un frame (SupplySummary.aspx) con TODOS los
  oferentes (no solo el ganador) y sus anexos Administrativo/Tecnico/Economico.
- La descarga individual de cada archivo (boton "Ver" por fila, patron
  input[id*='DWNL_grdId'][id$='_search']) NO exige captcha; solo la descarga masiva
  en ZIP lo exige (no se usa en este script).

Uso:
    python leer_ficha_licitacion.py monto <codigo>
    python leer_ficha_licitacion.py listar-oferentes <codigo>
    python leer_ficha_licitacion.py descargar-economicos <codigo> [--out carpeta]

Ejecutar siempre con PYTHONIOENCODING=utf-8 (nombres de archivo con tildes).

Requisitos: playwright (pip install playwright && playwright install chromium)
"""
import argparse
import json
import re
import sys
import time
import unicodedata
from pathlib import Path

from playwright.sync_api import sync_playwright

FICHA_URL_TPL = "https://www.mercadopublico.cl/Procurement/Modules/RFB/DetailsAcquisition.aspx?idlicitacion={cod}"
DEFAULT_OUT = Path(__file__).parent.parent / "data" / "anexos_economicos"

TIPOS_ANEXO = {
    "AdministrativeAttachment": "Anexos Administrativos",
    "TechnicalAttachment": "Anexos Tecnicos",
    "EconomicAttachment": "Anexos Economicos",
}

RE_MONTO_ADJUDICADO = re.compile(r"Monto Neto Adjudicado\s+([^\n\r]+)")
RE_MONTO_TOTAL_ADJUDICADO = re.compile(r"Monto Total Adjudicado\s*\n?\s*([^\n\r]+)")
RE_MONTO_ESTIMADO_ACTA = re.compile(r"Monto Neto Estimado del Contrato\s+([^\n\r]+)")
RE_MONEDA = re.compile(r"^Moneda\s+([^\n\r]+)", re.MULTILINE)
RE_FECHA_ADJ_PORTAL = re.compile(r"Adjudicaci\w+ Informada en portal el\s*\n?\s*([^\n\r]+)")
RE_DECRETO = re.compile(r"Nro de Decreto\s*\n?\s*([^\n\r]+)")


def sanear_nombre_carpeta(nombre):
    return re.sub(r'[<>:"/\\|?*]', "_", nombre or "").strip()


def _abrir_pagina(context, codigo):
    page = context.new_page()
    url = FICHA_URL_TPL.format(cod=codigo)
    page.goto(url, wait_until="networkidle", timeout=45000)
    return page


def leer_monto_adjudicado(codigo, browser=None):
    """Retorna dict con el resultado de la adjudicacion leido directo del acta (sin CAPTCHA,
    sin descargar ningun archivo). Si la licitacion aun no esta adjudicada, retorna
    estado='no_adjudicada'."""
    cerrar_browser = browser is None
    pw = None
    if browser is None:
        pw = sync_playwright().start()
        browser = pw.chromium.launch(headless=True)
    try:
        context = browser.new_context()
        page = _abrir_pagina(context, codigo)

        icono = page.locator("#imgAdjudicacion")
        if icono.count() == 0:
            return {"codigo": codigo, "estado": "sin_icono_adjudicacion"}
        disabled = icono.get_attribute("disabled")
        if disabled is not None:
            return {"codigo": codigo, "estado": "no_adjudicada"}

        icono.click(timeout=8000)
        page.wait_for_timeout(1500)
        frame = None
        for intento in range(3):
            frame = next((fr for fr in page.frames if "PreviewAwardAct" in fr.url or "Award" in fr.url), None)
            if frame is not None:
                break
            page.wait_for_timeout(1500)
        if frame is None:
            return {"codigo": codigo, "estado": "frame_acta_no_encontrado"}
        frame.wait_for_load_state("networkidle", timeout=20000)
        texto = frame.locator("body").inner_text()

        m_adj = RE_MONTO_ADJUDICADO.search(texto)
        m_total = RE_MONTO_TOTAL_ADJUDICADO.search(texto)
        m_est = RE_MONTO_ESTIMADO_ACTA.search(texto)
        m_mon = RE_MONEDA.search(texto)
        m_fecha = RE_FECHA_ADJ_PORTAL.search(texto)
        m_decreto = RE_DECRETO.search(texto)

        monto_adj_raw = m_adj.group(1).strip() if m_adj else ""
        monto_total_raw = m_total.group(1).strip() if m_total else ""
        # "Monto Neto Adjudicado" no siempre existe (licitaciones con multiples items/servicios) -
        # "Monto Total Adjudicado" (al pie de la tabla "Resultado de la Adjudicacion") es el fallback.
        monto_final = monto_adj_raw or monto_total_raw

        context.close()
        return {
            "codigo": codigo,
            "estado": "adjudicada",
            "monto_neto_adjudicado_raw": monto_final,
            "monto_neto_adjudicado_fuente": "Monto Neto Adjudicado" if monto_adj_raw else ("Monto Total Adjudicado" if monto_total_raw else ""),
            "monto_neto_estimado_raw": m_est.group(1).strip() if m_est else "",
            "moneda_raw": m_mon.group(1).strip() if m_mon else "",
            "fecha_adjudicacion_portal": m_fecha.group(1).strip() if m_fecha else "",
            "nro_decreto": m_decreto.group(1).strip() if m_decreto else "",
            "texto_completo_acta": texto,
        }
    finally:
        if cerrar_browser and pw:
            browser.close()
            pw.stop()


def abrir_cuadro_ofertas(page):
    icono = page.locator("#imgCuadroOferta")
    if icono.count() == 0:
        raise RuntimeError("No existe #imgCuadroOferta en esta ficha")
    icono.click(timeout=10000)
    frame = None
    for _ in range(6):
        page.wait_for_timeout(2000)
        frame = next((fr for fr in page.frames if "SupplySummary" in fr.url), None)
        if frame is not None:
            break
    if frame is None:
        raise RuntimeError("No se pudo abrir el frame SupplySummary (Cuadro de Ofertas)")
    frame.wait_for_load_state("networkidle", timeout=15000)
    return frame


def listar_oferentes(codigo, browser=None):
    cerrar_browser = browser is None
    pw = None
    if browser is None:
        pw = sync_playwright().start()
        browser = pw.chromium.launch(headless=True)
    try:
        context = browser.new_context()
        page = _abrir_pagina(context, codigo)
        frame = abrir_cuadro_ofertas(page)

        filas = frame.eval_on_selector_all(
            "[id*='_GvLblProvider']",
            "els => els.map(e => ({id: e.id, text: e.textContent.trim()}))",
        )
        proveedores = {}
        for f in filas:
            m = re.search(r"grdSupplies_(ctl\d+)__GvLblProvider", f["id"])
            if m:
                proveedores[m.group(1)] = f["text"]

        resultado = {}
        for ctl, nombre in proveedores.items():
            disponibles = [t for t in TIPOS_ANEXO if frame.locator(f"[id*='{ctl}__GvImgb{t}']").count() > 0]
            resultado[ctl] = {"nombre": nombre, "anexos": disponibles}
        context.close()
        return resultado
    finally:
        if cerrar_browser and pw:
            browser.close()
            pw.stop()


def descargar_archivos_de_anexo(context, frame, icono_id, carpeta_destino):
    with context.expect_page(timeout=8000) as popup_info:
        frame.click(f"#{icono_id}", timeout=5000)
    popup = popup_info.value
    popup.wait_for_load_state("networkidle", timeout=10000)

    carpeta_destino.mkdir(parents=True, exist_ok=True)
    descargados = []
    pagina_actual = 1
    while True:
        botones_ver = popup.locator("input[id*='DWNL_grdId'][id$='_search']")
        total_filas = botones_ver.count()
        for i in range(total_filas):
            boton = botones_ver.nth(i)
            fila_id = boton.get_attribute("id")
            m = re.match(r"(DWNL_grdId_ctl\d+)_search", fila_id or "")
            if not m:
                continue
            nombre_span = popup.locator(f"#{m.group(1)}_File")
            nombre_archivo = nombre_span.text_content().strip() if nombre_span.count() > 0 else f"archivo_{i}"
            try:
                with popup.expect_download(timeout=15000) as descarga_info:
                    boton.click()
                descarga = descarga_info.value
                ruta_final = carpeta_destino / (descarga.suggested_filename or nombre_archivo)
                descarga.save_as(str(ruta_final))
                descargados.append(ruta_final.name)
                print(f"    Descargado: {ruta_final.name}")
            except Exception as e:
                print(f"    No se pudo descargar '{nombre_archivo}': {e}")

        siguiente = popup.locator(f"a:has-text('{pagina_actual + 1}')")
        if siguiente.count() > 0:
            siguiente.first.click()
            popup.wait_for_timeout(1500)
            pagina_actual += 1
        else:
            break
    popup.close()
    return descargados


def descargar_economicos(codigo, carpeta_raiz, browser=None):
    """Descarga el Anexo Economico de TODOS los oferentes (no solo el ganador)."""
    cerrar_browser = browser is None
    pw = None
    if browser is None:
        pw = sync_playwright().start()
        browser = pw.chromium.launch(headless=True)
    try:
        context = browser.new_context(accept_downloads=True)
        page = _abrir_pagina(context, codigo)
        frame = abrir_cuadro_ofertas(page)

        filas = frame.eval_on_selector_all(
            "[id*='_GvLblProvider']",
            "els => els.map(e => ({id: e.id, text: e.textContent.trim()}))",
        )
        resumen = {}
        for f in filas:
            m = re.search(r"grdSupplies_(ctl\d+)__GvLblProvider", f["id"])
            if not m:
                continue
            ctl, nombre = m.group(1), f["text"]
            icono_id = f"grdSupplies_{ctl}__GvImgbEconomicAttachment"
            if frame.locator(f"#{icono_id}").count() == 0:
                resumen[nombre] = "sin_anexo_economico"
                continue
            carpeta = carpeta_raiz / codigo / sanear_nombre_carpeta(nombre)
            try:
                archivos = descargar_archivos_de_anexo(context, frame, icono_id, carpeta)
                resumen[nombre] = archivos
            except Exception as e:
                resumen[nombre] = f"error: {e}"
        context.close()
        return resumen
    finally:
        if cerrar_browser and pw:
            browser.close()
            pw.stop()


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="accion", required=True)

    p_monto = sub.add_parser("monto")
    p_monto.add_argument("codigo")

    p_listar = sub.add_parser("listar-oferentes")
    p_listar.add_argument("codigo")

    p_descargar = sub.add_parser("descargar-economicos")
    p_descargar.add_argument("codigo")
    p_descargar.add_argument("--out", default=str(DEFAULT_OUT))

    args = parser.parse_args()

    if args.accion == "monto":
        print(json.dumps(leer_monto_adjudicado(args.codigo), ensure_ascii=False, indent=2))
    elif args.accion == "listar-oferentes":
        print(json.dumps(listar_oferentes(args.codigo), ensure_ascii=False, indent=2))
    elif args.accion == "descargar-economicos":
        resumen = descargar_economicos(args.codigo, Path(args.out))
        print(json.dumps(resumen, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
