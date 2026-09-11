# API Compra Ágil v2 - Referencia técnica

**Host base:** `https://api2.mercadopublico.cl`
**Documentación oficial:** [chilecompra.cl/api](https://www.chilecompra.cl/api/)

---

## Contexto

Compra Ágil es el mecanismo de contratación simplificada de Mercado Público para adquisición
rápida de bienes y servicios. Los procesos tienen código único con formato `1057539-228-COT26`.

La API v2 es **completamente separada** de la API v1 de licitaciones y OC:
- Host diferente: `api2.mercadopublico.cl` (no `api.mercadopublico.cl`)
- Autenticación diferente: header HTTP (no parámetro GET)
- Formato de respuesta diferente: envelope estándar
- Sin equivalente de filtro por `CodigoOrganismo`

El mismo ticket usado en la API v1 es válido para la API v2.

---

## Autenticación

**Método:** header HTTP (no parámetro GET como en v1).

```http
GET https://api2.mercadopublico.cl/v2/compra-agil
ticket: TU_TICKET_AQUI
```

```python
import os
import requests

TICKET = os.environ["TICKET_MP"]
BASE = "https://api2.mercadopublico.cl"

headers = {"ticket": TICKET}
response = requests.get(f"{BASE}/v2/compra-agil", headers=headers,
                        params={"ttl_cambio_ms": 300000})
```

---

## Control de cuota

- Límite diario por ticket (valor de `-1` = ilimitado)
- Reset al cambio de día calendario (no ventana de 24h)
- HTTP 429 cuando se agota; header `Retry-After` indica tiempo de espera

```python
if resp.status_code == 429:
    # La cuota se restablece al inicio del proximo dia calendario
    raise Exception("Cuota diaria agotada. Intentar manana.")
```

---

## Endpoints

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `GET /v2/compra-agil` | GET | Listado paginado con filtros |
| `GET /v2/compra-agil/{codigo}` | GET | Detalle completo de una CA |

---

## GET /v2/compra-agil - Parámetros

### Grupo 1: ventana de cambios (usar A o B, no ambos)

| Parámetro | Tipo | Ejemplo | Descripción |
|-----------|------|---------|-------------|
| `ttl_cambio_ms` | int (ms) | `3600000` | Cambios en los últimos X ms |
| `cambio_desde` | datetime ISO-8601 | `2026-01-19T00:00:00Z` | Inicio del rango de cambios |
| `cambio_hasta` | datetime ISO-8601 | `2026-01-20T00:00:00Z` | Fin del rango de cambios |

### Grupo 2: fecha de publicación

| Parámetro | Tipo | Ejemplo |
|-----------|------|---------|
| `publicado_desde` | datetime ISO-8601 | `2026-01-01T00:00:00Z` |
| `publicado_hasta` | datetime ISO-8601 | `2026-01-31T23:59:59Z` |

### Grupo 3: estado (múltiples separados por coma)

| Valor | Descripción |
|-------|-------------|
| `publicada` | Abierta, recibiendo cotizaciones |
| `cerrada` | Plazo de cotización finalizó |
| `desierta` | Sin ofertas válidas |
| `cancelada` | Cancelada por el organismo |
| `proveedor_seleccionado` | Ganador elegido; incluye OC ya emitidas en la práctica |
| `oc_emitida` | Definido en el modelo pero NO funciona en producción - usar `proveedor_seleccionado` |

Ejemplo: `estado=publicada,proveedor_seleccionado`

### Grupo 4: región (entero 1-16, repetible)

| Código | Región | Código | Región |
|--------|--------|--------|--------|
| 1 | Tarapacá | 9 | Araucanía |
| 2 | Antofagasta | 10 | Los Lagos |
| 3 | Atacama | 11 | Aysén |
| 4 | Coquimbo | 12 | Magallanes y Antártica |
| 5 | Valparaíso | 13 | Metropolitana |
| 6 | O'Higgins | 14 | Los Ríos |
| 7 | Maule | 15 | Arica y Parinacota |
| 8 | Biobío | 16 | Ñuble |

**LIMITACIÓN CRÍTICA:** no existe parámetro `codigo_organismo` en la API v2. Para filtrar por un
organismo específico: usar `region=<N>` y luego filtrar localmente por `institucion.rut` o
`institucion.organismo_comprador` (ver `scripts/monitor_compra_agil.py`).

**COBERTURA HISTÓRICA:** la API v2 solo contiene datos desde diciembre 2024 en adelante
(verificado - el registro más antiguo disponible es 2024-12-17).

### Grupo 5: búsqueda por código o palabras clave (mutuamente excluyentes)

| Parámetro | Tipo | Ejemplo | Descripción |
|-----------|------|---------|-------------|
| `id` | string | `507428-142-COT25` | Código exacto de la CA |
| `q` | string (URL-encoded) | `materiales%20electricos` | Palabras clave en nombre/descripción |

### Grupo 6: paginación

| Parámetro | Default | Máximo | Descripción |
|-----------|---------|--------|-------------|
| `tamano_pagina` | 15 | 50 | Resultados por página |
| `numero_pagina` | 1 | - | Página a consultar |

### Grupo 7: orden

| Valor | Descripción |
|-------|-------------|
| `FechaUltimaModificacion` (default) | Descendente por último cambio |
| `FechaPublicacion` | Descendente por publicación |

Uso: `&ordenar_por=FechaPublicacion`

---

## Estructura de respuesta

Todas las respuestas siguen este envelope:

```json
{
  "success": "OK",
  "trace": null,
  "payload": {},
  "errors": null
}
```

En error: `success: "NOK"`, `payload: null`, `errors: [{codigo, mensaje, detalle}]`.

---

## Campos del listado (`payload.items[]`)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `codigo` | string | Código único. Ej: `1057539-228-COT26` |
| `nombre` | string | Título del proceso |
| `estado.id_estado` | int | ID numérico del estado |
| `estado.codigo` | string (enum) | Código normalizado del estado |
| `estado.glosa` | string | Descripción legible. Ej: `OC Emitida` |
| `convocatoria.estado_convocatoria` | int | 1=primer llamado, 2=segundo llamado |
| `convocatoria.descripcion` | string | Glosa del llamado |
| `documentos[].id` | string (UUID) | ID del documento adjunto |
| `documentos[].nombre` | string | Nombre del archivo adjunto |
| `fechas.fecha_publicacion` | datetime ISO-8601 | Fecha de publicación |
| `fechas.fecha_cierre` | datetime ISO-8601 | Fecha de cierre del llamado vigente |
| `fechas.fecha_ultimo_cambio` | datetime ISO-8601 | Timestamp del último cambio (usar para sincronización) |
| `fechas.fecha_cancelacion` | datetime o null | Fecha de cancelación si aplica |
| `montos.moneda` | string | Moneda. Ej: `CLP` |
| `montos.monto_disponible` | number | Monto disponible |
| `montos.monto_disponible_clp` | number | Monto normalizado a CLP |
| `institucion.organismo_comprador` | string | Nombre del organismo |
| `institucion.rut` | string | RUT del organismo |
| `institucion.unidad_compra` | string | Unidad/división de compra |
| `institucion.region` | int o null | Código de región (1-16) |
| `institucion.nombre_region` | string o null | Nombre de la región |
| `resumen.total_ofertas_recibidas` | int | Cotizaciones en el llamado actual |
| `motivos.motivo_cancelacion` | string o null | Si aplica |
| `motivos.motivo_desierta` | string o null | Si aplica |
| `motivos.motivo_seleccion` | string o null | Si aplica |
| `links.detalle` | string | URL relativa al detalle. Ej: `/v2/compra-agil/1057539-228-COT26` |

### Paginación (`payload.paginacion`)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `total_paginas` | int | Total de páginas |
| `numero_pagina` | int | Página actual |
| `tamano_pagina` | int | Resultados por página |
| `total_resultados` | int | Total de registros que coinciden |

---

## Campos del detalle (`payload` en `/v2/compra-agil/{codigo}`)

### Identificación y estado

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `codigo` | string | Código externo de la CA |
| `nombre` | string | Título del proceso |
| `descripcion` | string | Descripción detallada de la necesidad |
| `estado.id_estado` / `codigo` / `glosa` | - | Estado numérico, normalizado y legible |
| `convocatoria.estado_convocatoria` | int | 1=primer llamado, 2=segundo llamado |
| `convocatoria.fecha_cierre_primer_llamado` / `_segundo_llamado` | datetime o null | Cierre de cada llamado |

### Fechas

`fechas.fecha_publicacion`, `fecha_cierre`, `fecha_ultimo_cambio`, `fecha_cancelacion`.

### Entrega y presupuesto

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `entrega.direccion_entrega` | string | Dirección de entrega |
| `entrega.plazo_entrega_dias` | int o null | Plazo en días |
| `presupuesto.tipo_presupuesto` | string | `Disponible` o `Estimado` |
| `presupuesto.moneda` | string | Ej: `CLP` |
| `presupuesto.presupuesto_estimado` | number o null | Presupuesto estimado |
| `presupuesto.monto_disponible` / `_clp` | number o null | Monto disponible informado / normalizado |
| `presupuesto.valor_cambio_moneda` / `fecha_cambio_moneda` | - | Tipo de cambio si moneda != CLP |

### Orden de Compra (campos críticos)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `orden_compra.id_orden_compra` | int o null | **INDICADOR CONFIABLE** de OC emitida. Distinto de null = OC existe |
| `orden_compra.id_oc` | int o null | ID interno adicional. Usar para cruzar con API v1 OC |
| `orden_compra.codigo_orden_compra` | string o null | Código externo. **ADVERTENCIA: retorna null en producción** aunque la OC exista |
| `orden_compra.estado_orden_compra` | string o null | Estado textual. **Retorna null en `proveedor_seleccionado`** aunque la OC exista |

**Cómo relacionar CA con su OC:**
1. Verificar `orden_compra.id_orden_compra != null` en el detalle.
2. Usar `id_orden_compra` o `id_oc` para consultar el detalle en la API v1:
   `GET https://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?codigo=<COD>&ticket=<T>`

### Institución

`institucion.organismo_comprador`, `rut`, `unidad_compra`, `region`, `nombre_region`.

---

## Campos de productos solicitados (`payload.productos_solicitados[]`)

`codigo_producto`, `nombre`, `descripcion`, `cantidad`, `unidad_medida` (ej. `EA`, `KG`).

---

## Campos de proveedores cotizando (`payload.proveedores_cotizando[]`)

| Campo | Descripción |
|-------|-------------|
| `rut_proveedor` / `razon_social` | Identidad del proveedor |
| `es_emt` | Es Empresa de Menor Tamaño |
| `id_cotizacion` / `codigo_empresa` / `codigo_sucursal_empresa` | Identificadores internos |
| `activo` / `fecha_creacion` / `fecha_vigencia` | Vigencia de la cotización |
| `valor_neto` / `total_impuesto` / `monto_despacho` / `monto_total` | Desglose de montos |
| `nombre_impuesto` / `porcentaje_impuesto` | Ej: `IVA`, `19` |
| `descripcion_cotizacion` / `descripcion` | Texto libre de la oferta |
| `justificacion_inadmisibilidad` | Si fue declarada inadmisible |
| `seleccion.proveedor_seleccionado` / `motivo_seleccion` / `criterio_seleccion` | Resultado de selección |
| `productos_cotizados[].codigo_producto` / `nombre_producto` / `descripcion` / `cantidad` / `precio_unitario` / `monto_total_producto` | Detalle de la cotización |

---

## Campos de resumen y flags (`payload`)

`resumen.multa_sancion`, `resumen.total_ofertas_recibidas`, `resumen.total_demandas`,
`flags.considera_requisitos_medioambientales`, `flags.considera_requisitos_impacto_social_economico`.

---

## Códigos de error

| HTTP | Nombre | Causa | Acción |
|------|--------|-------|--------|
| 400 | Bad Request | Parámetros inválidos o combinaciones no permitidas | Revisar parámetros |
| 401 | Unauthorized | Falta header `ticket` | Agregar `ticket: TU_TICKET` |
| 403 | Forbidden | Ticket inválido, inactivo o bloqueado | Verificar ticket |
| 404 | Not Found | Código de CA no existe o no es público | Verificar código |
| 429 | Too Many Requests | Cuota diaria agotada | Esperar al día siguiente; ver header `Retry-After` |
| 500 | Internal Server Error | Error inesperado | Reintentar en minutos |
| 503 | Service Unavailable | Mantenimiento | Esperar |

---

## Ejemplos de uso

### Compras Ágiles activas de un organismo (filtrar localmente por RUT)

```python
import os
import requests

TICKET = os.environ["TICKET_MP"]
BASE = "https://api2.mercadopublico.cl"
RUT_ORGANISMO = "12.345.678-9"  # reemplazar por el RUT del organismo a monitorear

resp = requests.get(
    f"{BASE}/v2/compra-agil",
    headers={"ticket": TICKET},
    params={"estado": "publicada", "region": 13, "tamano_pagina": 50}
)
items = resp.json()["payload"]["items"]
organismo = [i for i in items if i["institucion"]["rut"] == RUT_ORGANISMO]
for ca in organismo:
    print(ca["codigo"], ca["nombre"], ca["montos"]["monto_disponible_clp"])
```

### Sincronización incremental (últimas 24 horas)

```python
import os
import requests
from datetime import datetime, timezone, timedelta

TICKET = os.environ["TICKET_MP"]
BASE = "https://api2.mercadopublico.cl"
RUT_ORGANISMO = "12.345.678-9"

ahora = datetime.now(timezone.utc)
hace_24h = ahora - timedelta(hours=24)

pagina = 1
todos = []
while True:
    resp = requests.get(
        f"{BASE}/v2/compra-agil",
        headers={"ticket": TICKET},
        params={
            "cambio_desde": hace_24h.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "cambio_hasta": ahora.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "region": 13,
            "tamano_pagina": 50,
            "numero_pagina": pagina,
            "ordenar_por": "FechaUltimaModificacion"
        }
    )
    payload = resp.json()["payload"]
    pag = payload["paginacion"]
    todos.extend(payload["items"])
    if pagina >= pag["total_paginas"]:
        break
    pagina += 1

organismo = [i for i in todos if i["institucion"]["rut"] == RUT_ORGANISMO]
print(f"{len(organismo)} cambios del organismo en ultimas 24h")
```

### Detectar OC emitidas en Compras Ágiles de un organismo

```python
import os
import requests

TICKET = os.environ["TICKET_MP"]
BASE = "https://api2.mercadopublico.cl"
RUT_ORGANISMO = "12.345.678-9"

resp = requests.get(
    f"{BASE}/v2/compra-agil",
    headers={"ticket": TICKET},
    params={"estado": "proveedor_seleccionado", "region": 13, "tamano_pagina": 50}
)
cas = [i for i in resp.json()["payload"]["items"] if i["institucion"]["rut"] == RUT_ORGANISMO]

for ca in cas:
    det = requests.get(f"{BASE}/v2/compra-agil/{ca['codigo']}", headers={"ticket": TICKET}).json()["payload"]
    id_oc = det.get("orden_compra", {}).get("id_orden_compra")
    if id_oc is not None:
        print(f"{ca['codigo']} tiene OC emitida (id_orden_compra={id_oc})")
    else:
        print(f"{ca['codigo']} seleccionado, OC pendiente")
```

---

## Reglas del modelo (estados y convocatoria)

- `publicada` + `estado_convocatoria=1` - primer llamado abierto
- `publicada` + `estado_convocatoria=2` - segundo llamado abierto
- `cerrada` + `estado_convocatoria=1` - primer llamado cerrado
- `cerrada` + `estado_convocatoria=2` - segundo llamado cerrado

El detalle completo de cotizaciones se muestra desde estado `cerrada` en segundo llamado en
adelante. Si no hay ofertas, `proveedores_cotizando` es `[]` (no se omite el campo).

---

## Diferencias críticas con API v1

| Dimensión | API v1 (Licitaciones/OC) | API v2 (Compra Ágil) |
|-----------|--------------------------|----------------------|
| Host | `api.mercadopublico.cl` | `api2.mercadopublico.cl` |
| Autenticación | Parámetro GET `?ticket=...` | Header HTTP `ticket: ...` |
| Fechas | `ddmmaaaa` | ISO-8601 |
| Paginación | Sin paginación documentada | Nativa, configurable |
| Filtro por organismo | `?CodigoOrganismo=<N>` | No existe - filtrar localmente |
| Sincronización incremental | Por fecha exacta | `ttl_cambio_ms` o rango ISO |
| Envelope respuesta | Sin envelope | `{success, trace, payload, errors}` |
| Proveedores cotizando | No | Sí (detalle por CA) |
| Flags medioambientales/social | No | Sí |
