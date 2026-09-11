# ChileCompra API Toolkit

Kit de apoyo a la gestión pública chilena en compras públicas: scripts de integración con la
API de Mercado Público (ChileCompra) - incluyendo dos mecanismos **no documentados** por
ChileCompra, descubiertos por ingeniería inversa del tráfico de sus propios buscadores
públicos - y un corpus de jurisprudencia de la Contraloría General de la República sobre
compras públicas.

Sin dependencias de ningún organismo, RUT ni dato institucional específico: todos los ejemplos
usan valores ficticios y los scripts reciben el organismo/RUT como parámetro.

## Qué incluye

### 1. Scripts de integración con Mercado Público (`scripts/`)

| Script | Mecanismo | Qué hace |
|---|---|---|
| [`buscar_comprador.py`](scripts/buscar_comprador.py) | API v1 | Busca el `CodigoOrganismo` de un organismo por nombre |
| [`monitor_licitaciones.py`](scripts/monitor_licitaciones.py) | API v1 | Lista y consulta el detalle de licitaciones de un organismo |
| [`monitor_oc.py`](scripts/monitor_oc.py) | API v1 | Lista Órdenes de Compra de un organismo, con alerta por umbral de monto |
| [`benchmark_precios.py`](scripts/benchmark_precios.py) | API v1 | Compara precios de adjudicación nacionales por código UNSPSC |
| [`monitor_compra_agil.py`](scripts/monitor_compra_agil.py) | API v2 | Lista y consulta Compras Ágiles de un organismo (por RUT + región) |
| [`monitor_consulta_mercado.py`](scripts/monitor_consulta_mercado.py) | No documentado | Busca Consultas al Mercado (RFI) de un organismo - token anónimo, sin `TICKET_MP` |
| [`buscar_tratos_directos_proveedor.py`](scripts/buscar_tratos_directos_proveedor.py) | No documentado | Búsqueda histórica multi-anual de Tratos Directos por proveedor |
| [`buscar_licitaciones_proveedor.py`](scripts/buscar_licitaciones_proveedor.py) | No documentado | Búsqueda histórica de Licitaciones Públicas por proveedor |
| [`descargar_adjuntos_trato_directo.py`](scripts/descargar_adjuntos_trato_directo.py) | No documentado | Descarga cotizaciones/decretos adjuntos de una ficha de Trato Directo |
| [`leer_ficha_licitacion.py`](scripts/leer_ficha_licitacion.py) | No documentado (Playwright) | Lee el monto real de adjudicación y el Cuadro de Ofertas completo, sin CAPTCHA |

Documentación técnica completa de cada mecanismo, con hallazgos verificados y limitaciones
reales: [`docs/`](docs/).

### 2. Jurisprudencia de compras públicas (`jurisprudencia-compras-publicas/`)

309 dictámenes de la Contraloría General de la República + normas marco (Ley 19.886, Decreto
661/2024), con índice maestro y una base de criterios operativos ya destilados por escenario de
decisión. Ver [`jurisprudencia-compras-publicas/README.md`](jurisprudencia-compras-publicas/README.md).

## Por qué existen los mecanismos "no documentados"

ChileCompra documenta oficialmente la API v1 (Licitaciones/OC) y v2 (Compra Ágil). Pero esa API
v1 exige el parámetro `fecha` - un día calendario específico, a nivel nacional - para cualquier
consulta combinada con organismo o proveedor. Esto hace **inviable en la práctica** una búsqueda
histórica multi-anual (habría que iterar día por día, contra un rate-limit real de ~2
requests/intento antes de un HTTP 429).

Los buscadores públicos oficiales de Mercado Público (Consulta al Mercado, Trato Directo,
ficha de licitación) sí resuelven estas búsquedas sin esa limitación, porque tienen sus propios
backends internos - no expuestos como API pública, pero **accesibles con las mismas solicitudes
HTTP que hace el navegador de cualquier visitante anónimo del sitio público**, sin necesitar
ninguna credencial, sesión autenticada ni bypass de control de acceso. Cada uno se documentó
leyendo el tráfico de red que genera el propio sitio público al usarlo normalmente (ver método
de descubrimiento en [`docs/consulta-mercado-rfi.md`](docs/consulta-mercado-rfi.md)).

## Instalación

```bash
git clone https://github.com/matias00allende/chilecompra-api-toolkit.git
cd chilecompra-api-toolkit
pip install -r requirements.txt
playwright install chromium  # solo si vas a usar leer_ficha_licitacion.py

cp .env.example .env
# Editar .env con tu TICKET_MP (ver docs/api-v1-licitaciones-oc.md, seccion Autenticacion)
```

Los scripts de mecanismos "no documentados" (`monitor_consulta_mercado.py`,
`buscar_tratos_directos_proveedor.py`, `buscar_licitaciones_proveedor.py`,
`descargar_adjuntos_trato_directo.py`, `leer_ficha_licitacion.py`) **no requieren `TICKET_MP`**:
obtienen un token anónimo en cada ejecución, igual que cualquier visitante del buscador público.

## Uso rápido

```bash
# Encontrar tu CodigoOrganismo
python scripts/buscar_comprador.py --buscar "nombre de tu organismo"

# Licitaciones activas de tu organismo
python scripts/monitor_licitaciones.py --organismo 12345

# Ordenes de compra del dia, con alerta sobre 5 millones CLP
python scripts/monitor_oc.py --organismo 12345 --umbral 5000000

# Benchmark de precios antes de licitar (codigo UNSPSC)
python scripts/benchmark_precios.py --unspsc 43231602 --meses 6

# Historial de Tratos Directos de un proveedor, sin filtro de organismo
python scripts/buscar_tratos_directos_proveedor.py --rut 76.123.456-7 --alias mi-proveedor
```

## Alcance ético y legal

Todo lo que consultan estos scripts es información pública, accesible sin autenticación por
cualquier visitante del sitio de Mercado Público, replicando exactamente las solicitudes HTTP
que hace el navegador de un usuario anónimo. Ningún script hace bypass de autenticación, evade
controles de acceso, ni automatiza acciones que modifiquen datos (todos son de solo lectura).
Respetar siempre los límites de tasa documentados en cada backend (ver `docs/`) - varios de
estos backends no tienen límites publicados explícitamente y se infirieron empíricamente
observando respuestas HTTP 429/403.

## Requisitos

- Python 3.10+
- `requests`, `python-dotenv` (ver [`requirements.txt`](requirements.txt))
- `playwright` + navegador Chromium, solo para `leer_ficha_licitacion.py`

## Autor

Matías Allende
[LinkedIn](https://www.linkedin.com/in/matiasallende/) · matias.allende.contreras@gmail.com

## Licencia

MIT. Ver [LICENSE](LICENSE). El corpus de jurisprudencia tiene su propia nota de licencia en
[`jurisprudencia-compras-publicas/README.md`](jurisprudencia-compras-publicas/README.md)
(dictámenes y normas son información pública sin restricción de uso).
