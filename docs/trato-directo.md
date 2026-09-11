# Referencia - Trato Directo (búsqueda histórica por proveedor)

**Estado:** no documentado por ChileCompra en su API pública (v1/v2). Backend propio
identificado por inspección de tráfico del buscador público oficial, mismo patrón de
autenticación anónima que [Consulta al Mercado](consulta-mercado-rfi.md).

---

## Por qué existe este mecanismo alternativo

La API v1 documentada (ver [`api-v1-licitaciones-oc.md`](api-v1-licitaciones-oc.md)) exige el
parámetro `fecha` - un **día calendario específico, a nivel nacional** - para cualquier consulta
por `estado` combinada con `CodigoOrganismo` o `CodigoProveedor`. Sin `fecha`, la respuesta es
`Cantidad: 0`. Esto hace inviable en la práctica una búsqueda histórica multi-anual por
proveedor: habría que iterar día por día durante años, contra un rate-limit real (HTTP 429 tras
~2 requests seguidas, esperas de 15-45s necesarias entre reintentos).

El backend de **Trato Directo** sí permite filtrar por proveedor + rango de fechas en una sola
búsqueda paginada, sin ese problema - es el único mecanismo de este kit que resuelve una
búsqueda histórica multi-anual por proveedor de forma práctica.

---

## Autenticación

Igual patrón que Consulta al Mercado:

```
GET https://servicios-prd.mercadopublico.cl/v1/auth/publico
```

Retorna un JWT anónimo, válido ~8h, sin necesitar `TICKET_MP` ni login. Se solicita uno nuevo
por ejecución.

---

## Endpoint de búsqueda

```
GET https://serv-trato-directo.mercadopublico.cl/v1/trato-directo-busqueda/buscar
Authorization: Bearer <access_token>
```

### Parámetros

| Parámetro | Formato | Descripción |
|-----------|---------|-------------|
| `provider` | RUT, formato `NN.NNN.NNN-N` | RUT del proveedor a buscar |
| `dateFrom` / `dateTo` | `DD/MM/YYYY` | Rango de fechas |
| `orderBy` | `1` | Único valor observado |
| `page` | entero, 0-indexed | Página a consultar |
| `size` | entero | Tamaño de página (probado hasta 50 sin error) |

**Sin filtro de organismo en la API** - cada item de la respuesta ya trae `nombreOrganismo`, así
que el filtro por organismo (si se necesita) se hace en cliente sobre ese campo. El script
`scripts/buscar_tratos_directos_proveedor.py` acepta `--organismo` (repetible, substring
case/accent-insensitive) para esto; sin ese filtro, guarda todos los resultados nacionales del
proveedor.

### Campos relevantes de cada item

`idFicha` (código de proceso), `nombreProveedor`, `nombre`, `nombreOrganismo`, `estado`,
`causal`, `fechaPublicacion`, `fechaCreacion`, `montoTotal`, `moneda`, `nombreMoneda`,
`montoReferencial`.

---

## Detalle de una ficha (para descargar adjuntos)

```
GET https://serv-trato-directo.mercadopublico.cl/v1/trato-directo-busqueda/detalle?idFicha=<CODIGO>
```

Retorna, entre otros campos, referencias a adjuntos (`cotizaciones[].idAdjunto`,
`adjuntoResolucionDecreto.idAdjunto`, `adjuntoCausal.idAdjunto`, `adjuntoOpcional.idAdjunto`).
Cada `idAdjunto` se resuelve a una URL de descarga presignada vía:

```
GET https://adjuntos-api.adjuntos.mercadopublico.cl/adjuntos-api/3000/1/<idAdjunto>
Authorization: Bearer <access_token>
```

La respuesta trae `filename`, `size` y una `URL` presignada que se descarga sin autenticación
adicional. Implementado en `scripts/descargar_adjuntos_trato_directo.py`.

---

## Licitaciones Públicas por proveedor (mecanismo distinto, mismo problema)

El buscador `www.mercadopublico.cl/BuscarLicitacion/Home/Buscar` permite filtrar licitaciones
adjudicadas (`idEstado=8`) por un array de `proveedores: ["<id>"]`, donde `<id>` es un **ID
interno**, no el RUT - se obtiene vía el autocomplete propio del buscador
(`Home/BuscarProveedor?q=<texto>`).

**Advertencia importante:** el índice de autocomplete de este buscador es distinto del índice
usado por Trato Directo, y puede:
- usar variantes de la razón social con/sin puntuación distinta a la oficial, o
- (más grave) devolver una empresa homónima **distinta, con RUT diferente**.

**Nunca asumir que un match de texto = el proveedor correcto.** Verificar siempre el RUT real
del ID devuelto antes de confiar en los resultados, contra el registro oficial:

```
GET https://api.mercadopublico.cl/servicios/v1/publico/Empresas/BuscarProveedor?rutempresaproveedor=<RUT_CON_PUNTOS>&ticket=<T>
```

Implementado en `scripts/buscar_licitaciones_proveedor.py`. Este endpoint responde HTML (no
JSON) - el script parsea con expresiones regulares sobre bloques `lic-bloq-wrap`; es
best-effort y puede requerir ajuste si el sitio cambia su plantilla. La paginación del buscador
es fija en 10 resultados por página (ignora `registrosPorPagina`), y el contador `n-result` del
HTML puede estar subestimado - no usarlo como condición de parada, usar "página con menos de 10
resultados = última página".

---

## Lectura de ficha de Licitación Pública sin CAPTCHA (monto real + todos los oferentes)

Hallazgo adicional, útil para completar el desglose de una Licitación Pública que Trato Directo
no cubre: la ficha pública de una licitación
(`https://www.mercadopublico.cl/Procurement/Modules/RFB/DetailsAcquisition.aspx?idlicitacion=<codigo>`)
expone, sin CAPTCHA:

- El **acta de adjudicación renderizada en pantalla** (ícono `#imgAdjudicacion`, abre un frame
  `PreviewAwardAct.aspx`), con el monto neto real de adjudicación en texto plano - útil para
  licitaciones tipo LR con rango de monto reservado en la API. El CAPTCHA solo protege la
  **descarga del PDF** del acta/informe, no la lectura del HTML renderizado.
- El **Cuadro de Ofertas** (ícono `#imgCuadroOferta`, abre un frame `SupplySummary.aspx`) con
  **todos los oferentes** (no solo el ganador) y sus anexos Administrativo/Técnico/Económico. La
  descarga individual de cada archivo (botón "Ver" por fila) tampoco exige CAPTCHA; solo la
  descarga masiva en ZIP lo exige (no usada en este kit).

Implementado en `scripts/leer_ficha_licitacion.py` con Playwright (requiere navegador headless,
no HTTP directo - la información se genera dinámicamente en el cliente).

---

## Resumen de mecanismos de búsqueda histórica por proveedor

| Mecanismo | Cubre | Filtro por organismo | Requiere navegador |
|---|---|---|---|
| Trato Directo (`buscar_tratos_directos_proveedor.py`) | Procesos de Trato Directo | Sí, en cliente (por nombre) | No |
| Licitaciones Públicas (`buscar_licitaciones_proveedor.py`) | Licitaciones Públicas adjudicadas/desiertas/etc. | Sí, en cliente (por nombre) | No |
| Lectura de ficha (`leer_ficha_licitacion.py`) | Monto real + Cuadro de Ofertas de una LP puntual | N/A (una ficha a la vez) | Sí (Playwright) |
