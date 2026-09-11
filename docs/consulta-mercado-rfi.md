# Referencia - Consulta al Mercado (RFI)

**Estado:** no documentado por ChileCompra en su API pública (v1/v2). Backend propio
identificado por inspección de tráfico de red del buscador público oficial.

---

## Qué es

La Consulta al Mercado (RFI - Request for Information) es un mecanismo de compras públicas
chilenas distinto de Licitación, Orden de Compra, Compra Ágil y Trato Directo. Permite a un
organismo público sondear el mercado - información técnica, comercial, de plazos y costos - 
antes de un proceso de compra formal. Es informativo y no vinculante para los proveedores que
responden. Regulado en el Reglamento de la Ley 19.886. Código con sufijo `-RFI<AA>` (ej.
`5001-9-RFI26`, donde `5001` es el `CodigoUnidad` del organismo y `26` el año).

Se publica en `www.mercadopublico.cl` bajo la sección "Consultas al Mercado", con buscador
propio en `https://consulta-mercado.mercadopublico.cl/buscador-publico`.

---

## Por qué no está en la referencia de la API v1/v2

Esas dos APIs cubren exhaustivamente la API pública documentada de ChileCompra, verificada
contra la documentación oficial. Consulta al Mercado usa un **backend HTTP completamente
distinto** (`servicios-consultas-prd.mercadopublico.cl`), sin mención en esos documentos ni en
`chilecompra.cl/api/`. El backend real se identificó navegando el buscador público oficial y
capturando las llamadas de red que hace la SPA al cargar resultados (ver metodología al final de
este documento).

---

## Autenticación

```
GET https://servicios-prd.mercadopublico.cl/v1/auth/publico
```

Sin headers ni parámetros. Retorna un JWT anónimo:

```json
{"success":"OK","trace":"...","payload":{"access_token":"eyJhbGci..."}}
```

El token trae `preferred_username: "anonimouser"` y roles
`["offline_access","uma_authorization","publico"]` - no contiene datos personales ni
institucionales, es una sesión anónima de solo lectura emitida por el Keycloak de ChileCompra
(`heimdall.mercadopublico.cl`). Vida útil observada: `exp - iat` = 28.800s (8h). **No es el
`TICKET_MP`** usado en las APIs v1/v2 - son sistemas de autenticación independientes.

Se solicita un token nuevo por ejecución del script; no se persiste (no hay necesidad, es
gratuito y sin límite de emisión observado).

---

## Endpoint de listado

```
GET https://servicios-consultas-prd.mercadopublico.cl/v1/consulta-mercado
Authorization: Bearer <access_token>
```

### Parámetros

| Parámetro | Formato | Descripción |
|-----------|---------|-------------|
| `desde` | `YYYY-MM-DD HH:MM:SS` (URL-encoded) | Fecha de publicación inicio del rango |
| `hasta` | `YYYY-MM-DD HH:MM:SS` (URL-encoded) | Fecha de publicación fin del rango |
| `estado` | `100` o `200` | `100`=Publicadas (activas), `200`=Cerradas. **Omitir el parámetro devuelve ambos estados combinados** (verificado: total sin `estado` = total con `estado=100` + total con `estado=200`) |
| `ordenarPor` | `100` | Único valor observado en el formulario ("Publicadas más recientes") |
| `pagina` | entero, 1-indexed | Página a consultar |
| `palabraClave` | texto libre | Filtra por coincidencia en `nombre`/`descripcion`. **No filtra por organismo comprador** |

**No existe parámetro de filtro por organismo, RUT ni código de institución.** Probado
exhaustivamente: `codigoInstitucion`, `institucion`, `organismo`, `rutOrganismo` - ninguno
filtra (todos devuelven el universo completo sin cambios). La única forma de acotar por
comprador es paginar todo y filtrar en cliente por el campo `codigoInstitucion` o
`rutOrganismo` de cada resultado.

**`pageSize` no es configurable.** Fijo en 15 resultados por página. Probado sin efecto:
`pageSize`, `tamanoPagina`, `tamanioPagina`, `cantidadPorPagina`, `size`.

### Respuesta

```json
{
  "success": "OK",
  "trace": null,
  "payload": {
    "resultCount": 7737,
    "pageCount": 516,
    "page": 1,
    "pageSize": 15,
    "resultados": [
      {
        "id": "8da1af3f-bab3-4867-8a06-f10d561e3e27",
        "codigoConsulta": "5001-9-RFI26",
        "nombre": "Ejemplo de titulo de consulta al mercado",
        "codigoUnidadCompra": "5001",
        "fechaPublicacion": "2026-07-14T16:10:50.378",
        "fechaCierre": "2026-07-17T16:00:46",
        "estado": 200,
        "codigoInstitucion": "12345",
        "codigoUsuario": "9999999",
        "descripcion": "...",
        "motivo": "Obtener informacion tecnica de un producto o servicio",
        "nombreUsuario": "NOMBRE DEL FUNCIONARIO RESPONSABLE",
        "nombreInstitucion": "NOMBRE DEL ORGANISMO",
        "nombreUnidadCompra": "NOMBRE DE LA UNIDAD DE COMPRA",
        "rutUsuario": "0.000.000-0",
        "rutOrganismo": "12.345.678-9",
        "tipoOrganismo": 2
      }
    ],
    "errores": null
  }
}
```

> Los campos `nombreUsuario` y `rutUsuario` de este endpoint son datos personales reales del
> funcionario que crea cada Consulta al Mercado (la API los expone públicamente sin
> anonimizar). Si vas a procesar o almacenar resultados masivamente, trátalos como PII: no los
> repitas en logs, reportes o ejemplos públicos.

**Campo clave para filtrar por un organismo específico:** `codigoInstitucion == "<CODIGO>"`
(coincide exactamente con el `CodigoOrganismo` de la API v1) o `rutOrganismo == "<RUT>"`. Ambos
campos son consistentes entre sí en todos los casos observados.

### Códigos de estado observados

Solo dos, confirmados por aritmética exacta (`total sin filtro == total(100) + total(200)`):

| Código | Significado |
|--------|-------------|
| 100 | Publicadas (activas, aún abiertas a respuesta de proveedores) |
| 200 | Cerradas (plazo de respuesta vencido) |

No se observaron otros códigos (probados 0, 1, 2, 3, 300, 400 - todos vacíos o 401).

---

## Limitaciones técnicas

| Limitación | Impacto | Mitigación |
|------------|---------|------------|
| Sin filtro de organismo en la API | Hay que paginar el universo nacional completo | Filtrar en cliente por `codigoInstitucion`/`rutOrganismo`; ver `scripts/monitor_consulta_mercado.py` |
| `pageSize` fijo en 15 | Barrido de "Cerradas" nacional = cientos de páginas (miles de registros) | Script con reintento en 401 (token expira a mitad de barrido) y `sleep(0.3s)` entre páginas |
| `palabraClave` busca texto libre, no organismo | Falsos positivos: una RFI de otro organismo que menciona tu organismo en su descripción también matchea | No usar como filtro de comprador; solo para búsqueda temática |
| Sin documentación oficial de ChileCompra | Contrato no garantizado, puede cambiar sin aviso | Revalidar campos si el script empieza a fallar; no hay Swagger/OpenAPI que avise breaking changes |
| Sin `codigo_organismo` como la API v1 | Requiere doble verificación (campo `codigoInstitucion` Y `rutOrganismo`) | Ya implementado en `filtrar_organismo()` del script |

---

## Script

`scripts/monitor_consulta_mercado.py` - no requiere `TICKET_MP` ni `.env` (token anónimo
obtenido en cada ejecución).

---

## Método de descubrimiento (para replicar si el backend cambia)

1. Buscar en el HTML servidor de
   `https://www.mercadopublico.cl/Procurement/Modules/RFB/StepsProcessSearch/BuscarProceso.aspx`
   el enlace de navegación a "Consultas al mercado" (SPA en subdominio propio).
2. Navegar la SPA con un navegador real e inspeccionar las llamadas de red (panel Network del
   navegador, o herramientas de automatización con captura de requests) mientras la página
   carga resultados por defecto - revela el endpoint XHR real y sus parámetros en la URL.
3. Inspeccionar `document.cookie` / `localStorage` / `sessionStorage` de la SPA para encontrar
   el token de autenticación (`access_token` en cookie, en este caso) y su mecanismo de emisión
   (llamada previa a `/v1/auth/publico` visible en el mismo panel de red).
4. Confirmar que el endpoint y el token funcionan fuera del navegador (`requests` directo en
   Python) antes de formalizar el script - evita depender de un navegador automatizado en
   producción.
