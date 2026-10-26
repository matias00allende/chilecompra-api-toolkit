# Referencia API Mercado Público v1 (Licitaciones y Órdenes de Compra)

**Base URL:** `https://api.mercadopublico.cl/servicios/v1/publico/`
**Autenticación:** `?ticket=<GUID>` en cada request
**Formatos soportados:** JSON (default), JSONP, XML
**Límite:** 10.000 requests/día por ticket

> Para la API v2 (Compra Ágil): ver [`api-v2-compra-agil.md`](api-v2-compra-agil.md). Host
> diferente (`https://api2.mercadopublico.cl`), autenticación diferente (header HTTP).

---

## Autenticación

No hay OAuth ni API key estándar. La autenticación usa un ticket (GUID):

1. Ir a `https://api.mercadopublico.cl/modules/IniciarSesion.aspx`
2. Autenticarse con Clave Única del representante legal u oficial a cargo del organismo
3. El ticket se envía por correo al email registrado
4. Adjuntar en cada request como parámetro GET: `?ticket=<GUID>`

El ticket no tiene expiración por tiempo documentada; persiste hasta su revocación. Aparte,
rige un límite diario de 10.000 requests por ticket.

**Nunca hardcodear el valor del ticket en código ni en documentación.** Cargarlo siempre desde
variable de entorno (`TICKET_MP`) o un secret manager. Ver [`.env.example`](../.env.example).

---

## Cómo obtener tu CodigoOrganismo

Cada organismo público registrado en Mercado Público tiene un `CodigoOrganismo` (entero) que
se usa como parámetro de filtro en licitaciones y OC. Para encontrar el propio:

```bash
python scripts/buscar_comprador.py --buscar "nombre de tu organismo"
```

> El valor del campo `CodigoEmpresa` que retorna `BuscarComprador` es el mismo que se usa como
> parámetro `CodigoOrganismo` en los endpoints de licitaciones y OC.

---

## Comportamiento real de los endpoints (verificado)

### Endpoints de listado (licitaciones, OC con filtros de organismo/fecha/estado)

Retornan **campos mínimos**, no el objeto completo:

| Endpoint | Campos que retorna en listado |
|---|---|
| `licitaciones.json` con filtros | `CodigoExterno`, `Nombre`, `CodigoEstado`, `FechaCierre` |
| `ordenesdecompra.json` con filtros | `Codigo`, `CodigoEstado` |

Para obtener el detalle completo (montos, proveedor, items, fechas, adjudicación) es
**obligatorio consultar por código individual**.

### Consulta por código (detalle completo)

```
GET /licitaciones.json?ticket=<T>&codigo=<COD>
GET /ordenesdecompra.json?ticket=<T>&codigo=<COD>
```

Estas consultas retornan el objeto completo con todos los campos.

**Implicación de cuota:** obtener el detalle de N licitaciones/OC de un listado cuesta N+1
requests (1 listado + N detalles).

---

## `fecha` es obligatorio para búsquedas por estado + organismo

`licitaciones.json?CodigoOrganismo=<N>&estado=adjudicada` **sin** `fecha` retorna `Cantidad: 0`
(lo mismo con `CodigoProveedor` solo, sin organismo). El parámetro `fecha` filtra **un día
calendario específico a nivel nacional**, sin combinación de filtro por organismo/proveedor que
permita acotar sin iterar día por día.

**Iterar un rango multi-anual día por día es inviable en la práctica**: rate-limit real
observado de HTTP 429 tras ~2 requests seguidas, con esperas de 15-45s necesarias entre
reintentos. Para búsquedas históricas por proveedor a lo largo de años, usar el mecanismo de
**Trato Directo** (ver [`trato-directo.md`](trato-directo.md)) en vez de esta API.

---

## GET /licitaciones.json

**Parámetros:**

| Parámetro | Tipo | Descripción |
|---|---|---|
| `ticket` | GUID | Obligatorio |
| `estado` | string | `activas`, `publicadas`, `cerradas`, `desierta`, `adjudicada`, `revocada`, `suspendida` |
| `fecha` | string | Formato `DDMMYYYY` |
| `codigo` | string | Código de licitación - retorna objeto completo |
| `CodigoOrganismo` | int | Código numérico del organismo |
| `CodigoProveedor` | string | RUT del proveedor |

**Respuesta (listado):**
```json
{
  "Cantidad": 4,
  "FechaCreacion": "2026-05-11T18:30:31Z",
  "Version": "v1",
  "Listado": [
    {
      "CodigoExterno": "2403-36-LR26",
      "Nombre": "Ejemplo de titulo de licitacion",
      "CodigoEstado": 5,
      "FechaCierre": "2026-05-15T15:00:00"
    }
  ]
}
```

**Campos del detalle completo (consulta por código):**

| Campo | Descripción |
|---|---|
| `CodigoExterno` | Número de licitación |
| `Nombre` | Título |
| `Descripcion` | Descripción completa |
| `CodigoEstado` / `Estado` | Estado numérico y textual |
| `CodigoTipo` / `Tipo` | Código numérico / sigla textual (ver tabla de tipos abajo) |
| `Moneda` | CLP, CLF, USD... |
| `MontoEstimado` | Monto estimado (en la moneda indicada) |
| `VisibilidadMonto` | 1=visible, 0=reservado |
| `Comprador.CodigoOrganismo` | Código del organismo |
| `Comprador.NombreOrganismo` | Nombre organismo |
| `Comprador.RutUnidad` | RUT de la unidad |
| `Comprador.ComunaUnidad` | Comuna |
| `Comprador.RegionUnidad` | Región |
| `Comprador.NombreUsuario` | Nombre del funcionario responsable |
| `Comprador.RutUsuario` | RUT del funcionario responsable |
| `Comprador.CodigoUsuario` | Código de usuario |
| `Comprador.CargoUsuario` | Cargo del funcionario responsable |
| `Fechas.FechaCreacion` | Fecha publicación |
| `Fechas.FechaCierre` | Fecha cierre de ofertas |
| `Fechas.FechaAdjudicacion` | Fecha adjudicación real |
| `Fechas.FechaEstimadaFirma` | Fecha estimada de firma contrato |
| `Adjudicacion.Tipo` | Tipo de adjudicación |
| `Adjudicacion.Fecha` | Fecha de adjudicación |
| `Adjudicacion.NumeroOferentes` | Cantidad de oferentes recibidos |
| `Adjudicacion.UrlActa` | URL del acta pública |
| `Items.Listado` | Array de items con código UNSPSC, descripción, cantidad, precio |
| `Items.Listado[].CodigoProducto` | Código UNSPSC de 8 dígitos |
| `Items.Listado[].CodigoCategoria` | Categoría UNSPSC |
| `Items.Listado[].NombreProducto` | Descripción del item |
| `Items.Listado[].Cantidad` | Cantidad |
| `Items.Listado[].Adjudicacion` | Resultado de adjudicación del item |
| `DiasCierreLicitacion` | Días restantes para el cierre |
| `Informada` | 1=Sí, 0=No |
| `TomaRazon` | Si requiere toma de razón de la Contraloría |
| `Modalidad` / `TipoPago` | Modalidad y tipo de pago |
| `TiempoDuracionContrato` | Duración del contrato |
| `EsRenovable` | 1=renovable, 0=no |
| `SubContratacion` | Permite subcontratación |
| `CantidadReclamos` | Reclamos recibidos |

**Tipos de licitación (`CodigoTipo` + sigla `Tipo`):**

| CodigoTipo | Sigla | Descripción | Rango |
|-----------|-------|-------------|-------|
| 1 | LR | Pública | >= 5.000 UTM |
| 2 | LP | Pública | 1.000 - 2.000 UTM |
| 3 | LQ | Pública | 2.000 - 5.000 UTM |
| 4 | LE | Pública | 100 - 1.000 UTM |
| 5 | L1 | Pública | < 100 UTM |
| 6 | LS | Pública, servicios personales especializados | - |
| 1 (privada) | E2 | Privada | < 100 UTM |
| - | CO | Privada | 100 - 1.000 UTM |
| - | B2 | Privada | 1.000 - 2.000 UTM |
| - | H2 | Privada | 2.000 - 5.000 UTM |
| - | I2 | Privada | > 5.000 UTM |

**Monedas soportadas:** CLP, CLF, USD, UTM, EUR

**Estimación del monto (`Estimacion`):**

| Valor | Descripción |
|-------|-------------|
| 1 | Presupuesto Disponible |
| 2 | Precio Referencial |
| 3 | No estimable |

### Estados (`CodigoEstado`) - documentado vs. verificado en vivo

| Código | Estado según documentación | Estado real observado |
|---|---|---|
| 1 | Publicada | - |
| 2 | Cerrada | - |
| 3 | Desierta | - |
| 4 | Adjudicada | - |
| 5 | Publicada (activa) | - |
| 6 | Revocada | **Cerrada** (confirmado en producción) |
| 7 | Suspendida | **Desierta (o art. 3 o 9 Ley 19.886)** (confirmado vía filtro `estado=desierta` + detalle) |
| 8 | (no documentado) | **Adjudicada** (confirmado vía filtro `estado=adjudicada` + detalle) |
| 15 | (no documentado) | **Revocada** (confirmado vía filtro `estado=revocada` + detalle) |

**`CodigoEstado` NO es confiable - no mapear estados por código.** El campo `Estado` (texto) es
la única fuente de verdad. Si construyes lógica de "estado terminal" (para dejar de monitorear
un proceso), hacer match por **prefijo** de texto, no igualdad exacta: el texto real de
"Desierta" suele traer un sufijo legal, ej. `"Desierta (o art. 3 ó 9 Ley 19.886)"`.

---

## GET /ordenesdecompra.json

Mismos parámetros que licitaciones. El listado retorna solo `Codigo` y `CodigoEstado`.

**Campos del detalle completo:**

| Campo | Descripción |
|---|---|
| `Codigo` | Número de OC |
| `Nombre` | Descripción de la OC |
| `CodigoEstado` / `Estado` | Estado |
| `CodigoLicitacion` | Licitación de origen |
| `CodigoTipo` / `Tipo` | Tipo (SE, OC, etc.) |
| `TipoMoneda` | CLP, CLF, USD... |
| `TotalNeto` | Total sin IVA |
| `PorcentajeIva` | IVA (19% típicamente) |
| `Impuestos` | Monto IVA |
| `Total` | Total con IVA (`TotalNeto + Impuestos = Total`) |
| `Financiamiento` | Código presupuestario |
| `Comprador.CodigoOrganismo` | Código del organismo |
| `Comprador.NombreOrganismo` | Nombre organismo |
| `Comprador.RutUnidad` | RUT |
| `Comprador.Actividad` / `Comprador.Pais` | Actividad y país del organismo comprador |
| `Comprador.NombreContacto` / `CargoContacto` / `FonoContacto` / `MailContacto` | Datos de contacto del organismo |
| `Proveedor.Nombre` | Nombre del proveedor |
| `Proveedor.RutSucursal` | RUT proveedor |
| `Proveedor.Direccion` | Dirección proveedor |
| `Proveedor.Codigo` / `CodigoSucursal` / `NombreSucursal` | Identificadores internos del proveedor |
| `Proveedor.NombreContacto` / `CargoContacto` / `FonoContacto` / `MailContacto` | Datos de contacto del proveedor |
| `Fechas.FechaCreacion` | Fecha creación OC |
| `Fechas.FechaEnvio` | Fecha envío al proveedor |
| `Items.Listado[].CodigoProducto` | Código UNSPSC |
| `Items.Listado[].EspecificacionComprador` / `EspecificacionProveedor` | Especificación de cada parte |
| `Items.Listado[].PrecioNeto` / `Total` / `TotalCargos` / `TotalDescuentos` / `TotalImpuestos` | Desglose de montos del item |
| `Descuentos` / `Cargos` | Totales a nivel de OC |

**Estados OC (`CodigoEstado` observados):**

| Código | Estado |
|---|---|
| 1, 4, 12 | Enviada a proveedor |
| 2, 8 | Aceptada |
| 3 | Cancelada |
| 5 | Pendiente de recepcionar |
| 6 | Recepcionada parcialmente |
| 7 | Recepción conforme |

**Tipos de despacho (`TipoDespacho`):**

| Valor | Descripción |
|-------|-------------|
| 7 | Despachar a Dirección de envío |
| 9 | Despachar según programa adjuntado |
| 12 | Otra Forma de Despacho |
| 14 | Retiramos de su bodega |
| 20 | Despacho por courier o encomienda aérea |
| 21 | Despacho por courier o encomienda terrestre |
| 22 | A convenir |

**Formas de pago (`FormaPago`):**

| Valor | Descripción |
|-------|-------------|
| 1 | 15 días contra la recepción de la factura |
| 2 | 30 días contra la recepción de la factura |
| 39 | Otra forma de pago |
| 46 | 50 días contra la recepción de la factura |
| 47 | 60 días contra la recepción de la factura |

---

## GET /Empresas/BuscarComprador

Lista todos los organismos compradores registrados.

**Respuesta real:**
```json
{
  "Cantidad": 899,
  "listaEmpresas": [
    {
      "CodigoEmpresa": "12345",
      "NombreEmpresa": "NOMBRE DEL ORGANISMO"
    }
  ]
}
```

> **Atención:** los campos son `CodigoEmpresa` y `NombreEmpresa`, no `CodigoOrganismo` y
> `Nombre`. El valor de `CodigoEmpresa` es el que se usa como parámetro `CodigoOrganismo` en los
> demás endpoints.

## GET /Empresas/BuscarProveedor

```
GET /Empresas/BuscarProveedor?rutempresaproveedor=<RUT>&ticket=<T>
```

Busca un proveedor por RUT. Retorna datos de la empresa proveedora - útil para verificar que un
RUT o ID interno de proveedor corresponde realmente a la razón social esperada antes de confiar
en un resultado de autocomplete (ver [`trato-directo.md`](trato-directo.md)).

---

## Códigos UNSPSC

Los ítems de licitaciones y OC usan UNSPSC v7 (United Nations Standard Products and Services Code).

- `CodigoProducto` - 8 dígitos (ej: `43231602` = Software ERP; `80101601` = Estudios de factibilidad)
- `CodigoCategoria` - 8 dígitos de la categoría padre
- Primeros 2 dígitos = segmento (ej: `43` = TI; `80` = Servicios profesionales)

---

## Notas de integración

1. **Encoding:** los nombres con caracteres especiales (ñ, acentos) pueden llegar con encoding
   latin-1 envuelto en UTF-8. Normalizar antes de comparar (ver el patrón en
   `scripts/buscar_comprador.py`).
2. **Campos nulos:** el listado retorna objetos mínimos; siempre consultar por código para
   obtener montos y proveedor.
3. **Sin paginación:** el listado retorna todos los registros del filtro. Combinar con
   `CodigoOrganismo` cuando la consulta lo permita; las búsquedas por `fecha` son nacionales y
   no se acotan por organismo (ver la sección sobre `fecha`).
4. **Cuota:** cada consulta de detalle consume 1 request.
5. **HTTPS obligatorio:** la API acepta HTTP pero usar siempre HTTPS en producción.

---

## Manejo de errores

| Código HTTP | Causa típica |
|---|---|
| 200 | Éxito - revisar `Cantidad`; puede ser 0 sin error |
| 400 | Parámetro inválido o faltante |
| 401 | Ticket inválido o revocado |
| 429 | Límite diario alcanzado (10.000 req) |
| 500 | Error interno - `CodigoOrganismo` no numérico o fuera del catálogo |
