# Índice maestro - Jurisprudencia y normas de Compras Públicas

Corpus de dictámenes de la Contraloría General de la República y normas marco
(Ley 19.886, sus reglamentos y decretos asociados) organizados por materia de
compras públicas. Generado para consulta directa por sistemas de IA que evalúen,
preparen o revisen procesos de compras públicas, sin necesidad de inferir contenido
no verificado.

## Cómo usar este índice

1. **Búsqueda por materia**: usa la sección de la categoría correspondiente (coincide
   con las carpetas del corpus: Bases, Adjudicacion, Garantias, Grandes Compras, etc.,
   nombres tal como existen en el sistema de archivos, sin tilde).
2. **Búsqueda por número de dictamen/norma**: usa el 'Índice alfanumérico por número'
   al final de este documento.
3. **Búsqueda por artículo de ley/reglamento**: usa el 'Índice por artículo citado'.
4. **Regla de no inferencia**: cada fila enlaza al `.md` con el texto completo del
   documento. Si un campo aparece como `-` (no disponible), NO debe completarse por
   deducción ni conocimiento general: abre el `.md` fuente y verifica directamente.
5. **Vigencia y jerarquía**: los dictámenes de Contraloría son jurisprudencia
   administrativa (precedente interpretativo), no normas. Ante dictámenes que traten
   la misma materia con criterios distintos, prevalece el más reciente, salvo que uno
   de ellos indique expresamente que reconsidera, complementa o deja sin efecto al otro
   (columna 'Fecha' de este índice, u observar si el propio dictamen dice 'aplica',
   'reconsidera' o 'complementa' a otro número).
6. **Calidad de extracción**: la columna 'Ext.' indica el método. `OPTIMA/BUENA/PARCIAL`
   = extraído con markitdown desde el PDF nativo. `VISION` = transcrito por lectura
   visual del PDF (el original no tenía capa de texto o estaba dañado). `IRRECUPERABLE`
   = el PDF está corrupto y no se pudo recuperar contenido (ver el `.md` para el detalle
   técnico del intento de recuperación).
7. **Marca ⚠ junto al número de dictamen**: el documento cita el Decreto 250/2004,
   reglamento derogado por el Decreto 661/2024 (ver alerta siguiente). El propio `.md`
   tiene la misma advertencia agregada al final de su texto.
8. **Reglas operativas ya sintetizadas**: para no leer los `.md` completos, usa
   `CRITERIOS-OPERATIVOS.md` (en la raíz de este proyecto). Agrupa la jurisprudencia por
   escenario de decisión (bases, garantías, trato directo, compra ágil, grandes
   compras, etc.) con reglas ya destiladas y su cita de respaldo. Este índice sirve
   para *ubicar* el documento fuente exacto; ese archivo sirve para *aplicar* el
   criterio sin leer todo el corpus.

## ALERTA DE VIGENCIA NORMATIVA (leer antes de citar artículos del reglamento)

- El **Decreto N° 661, de 2024, del Ministerio de Hacienda** (publicado 12-12-2024)
  aprueba el reglamento vigente de la Ley 19.886 y **deja sin efecto expresamente**
  el **Decreto Supremo N° 250, de 2004**, del mismo ministerio.
- La gran mayoría de los dictámenes de este corpus son anteriores a esa derogación y
  citan artículos del **DTO 250/2004** (ver sección 'Decreto 250/2004' en el índice por
  artículo citado, con 329 citas: la norma reglamentaria más citada del corpus).
- **Antes de aplicar el criterio de un dictamen que cite el DTO 250/2004 a un caso
  actual, verificar la disposición correlativa en el Decreto 661/2024** (la numeración
  de artículos cambió). El criterio interpretativo de fondo puede seguir siendo válido
  si la norma correlativa no cambió en su contenido, pero la cita formal del artículo
  del reglamento antiguo ya no corresponde a la norma vigente.
- La **Ley 19.886** fue modernizada por la **Ley N° 21.634** (publicada 11-12-2023,
  'Moderniza la ley N 19.886... para mejorar la calidad del gasto público, aumentar
  los estándares de probidad y transparencia e introducir principios de economía
  circular'). Dictámenes anteriores a esa fecha pueden referirse a una versión previa
  del articulado.
- Las normas **Ley 21.663** (Ley Marco de Ciberseguridad) y **Ley 21.719** (Protección
  de Datos Personales) incluidas en 'Normas marco' NO son normativa específica de
  compras públicas: son normativa transversal de contexto institucional.
- **Fuente oficial vigente (BCN LeyChile)** para verificar el texto actualizado del
  Decreto 661/2024, incluyendo modificaciones posteriores a su publicación:
  https://www.bcn.cl/leychile/navegar?idNorma=1209290&idParte=10527757

## Alcance del corpus

- Total de documentos indexados: **309**
- Documentos transcritos por lectura visual (sin capa de texto en el PDF original): 4
- Documentos irrecuperables (PDF corrupto, sin contenido disponible): 1
- Fuente: carpeta de trabajo del usuario, dictámenes descargados de la Base de
  Dictámenes de la Contraloría General de la República (contraloria.cl) y normativa
  de compras públicas.
- Cada `.md` tiene front-matter YAML con las claves (sin tilde, son identificadores):
  `fuente_pdf`, `categoria`, `numero_documento`, `anio`, `calidad_extraccion`, `metodo`.

## Normas marco

### Decreto-661_12-DIC-2024
- Número/año: 661 / 2024
- Organismo: Ministerio de Hacienda
- Objeto (según el propio texto): Aprueba el Reglamento de la Ley N 19.886, de Bases sobre Contratos Administrativos de Suministro y Prestacion de Servicios, y DEJA SIN EFECTO el Decreto Supremo N 250, de 2004, del Ministerio de Hacienda.
- Rol en el sistema de compras públicas: ALERTA DE VIGENCIA: este decreto es el reglamento actualmente vigente de la Ley 19.886 y deroga expresamente el D.S. 250/2004. La gran mayoria de los dictamenes de este corpus citan 'DTO 250/2004' porque son anteriores a esta derogacion (vigente desde su publicacion, 12-12-2024) - al aplicar esos criterios hoy, verificar la correlativa disposicion en el Decreto 661/2024 antes de citar el articulo antiguo como vigente.
- Archivo: `Decreto-661_12-DIC-2024.md`

### LEY-19886_30-JUL-2003
- Número/año: 19.886 / 2003
- Organismo: Ministerio de Hacienda
- Objeto (según el propio texto): Ley de Bases sobre Contratos Administrativos de Suministro y Prestacion de Servicios. Articulo 1: los contratos que celebren los organismos del Estado, a titulo oneroso, para el suministro de bienes muebles y de los servicios que se requieran para el desarrollo de sus funciones, se ajustaran a las normas y principios de esta ley y su reglamentacion.
- Rol en el sistema de compras públicas: Es la ley base del sistema de compras publicas chileno. Ultima modificacion registrada en el texto: Ley 21.634 (11-DIC-2023) y Ley 21.806 (version vigente al 05-FEB-2026 segun ficha BCN incluida en el documento).
- Archivo: `LEY-19886_30-JUL-2003.md`

### Ley-21663_08-ABR-2024
- Número/año: 21.663 / 2024
- Organismo: Ministerio del Interior y Seguridad Publica
- Objeto (según el propio texto): Ley Marco de Ciberseguridad. Articulo 1 (Objeto): establece la institucionalidad, principios y normativa general para estructurar, regular y coordinar las acciones de ciberseguridad de los organismos del Estado y crea la Agencia Nacional de Ciberseguridad (ANCI).
- Rol en el sistema de compras públicas: NO es una norma especifica de compras publicas. Es normativa transversal de ciberseguridad aplicable a organismos del Estado; se incluye en este corpus como referencia de contexto institucional, no como fuente directa de jurisprudencia de compras.
- Archivo: `Ley-21663_08-ABR-2024.md`

### Ley-21719_13-DIC-2024
- Número/año: 21.719 / 2024
- Organismo: Ministerio Secretaria General de la Presidencia
- Objeto (según el propio texto): Regula la proteccion y el tratamiento de los datos personales y crea la Agencia de Proteccion de Datos Personales. Sustituye y moderniza la Ley 19.628 sobre proteccion de la vida privada.
- Rol en el sistema de compras públicas: NO es una norma especifica de compras publicas. Es normativa transversal de proteccion de datos personales, aplicable por ejemplo al tratamiento de datos de oferentes/proveedores en procesos de compra; se incluye como referencia de contexto, no como fuente directa de jurisprudencia de compras.
- Archivo: `Ley-21719_13-DIC-2024.md`

### Decreto-661_12-DIC-2024 (1)
- Número/año: 661 / 2024
- Organismo: Ministerio de Hacienda
- Objeto (según el propio texto): aprueba reglamento de la ley 19886 que reconoce modificaciones introducidas por ley 21634 para mejorar probidad, transparencia, eficiencia e incorporar economía circular
- Rol en el sistema de compras públicas: reglamento establece procedimientos de contratación con énfasis en probidad, transparencia, eficiencia, sustentabilidad y participación de empresas de menor tamaño
- Archivo: `Normas macro/Decreto-661_12-DIC-2024 (1).md`

### ICG-N-6
- Número/año: - / 2024
- Organismo: Tribunal de Defensa de la Libre Competencia
- Objeto (según el propio texto): establece instrucciones generales para criterios de adjudicación en bases de licitación municipal de obra pública a fin de prevenir conductas contrarias a libre competencia
- Rol en el sistema de compras públicas: el precio debe ser el principal factor de adjudicación; factores estáticos no pueden impedir participación de oferentes idóneos mediante barreras artificiales
- Archivo: `Normas macro/ICG-N-6.md`

### LEY-19886_30-JUL-2003 (2)
- Número/año: 19886 / 2003
- Organismo: Ministerio de Hacienda
- Objeto (según el propio texto): ley de bases sobre contratos administrativos de suministro y prestación de servicios que establece normas y principios para contratación pública
- Rol en el sistema de compras públicas: contratación pública se rige por principios de licitación pública, probidad, transparencia, igualdad, competencia y valor por dinero
- Archivo: `Normas macro/LEY-19886_30-JUL-2003 (2).md`

### Ley-21634_11-DIC-2023 (3)
- Número/año: 21634 / 2023
- Organismo: Ministerio de Hacienda
- Objeto (según el propio texto): moderniza ley 19886 para mejorar calidad del gasto público, aumentar estándares probidad y transparencia, e introducir economía circular en compras del estado
- Rol en el sistema de compras públicas: contratación pública persigue satisfacer necesidades públicas con énfasis en libre acceso, competencia, probidad, transparencia y valor por dinero
- Archivo: `Normas macro/Ley-21634_11-DIC-2023 (3).md`

## Dictámenes por categoría

### Acta Apertura de Ofertas  (2 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 29.549 | 2000 | 07-VIII-2000 | OPTIMA | la Municipalidad no se encuentra obligada, en esta etapa, a poner en conocimiento del solicitante las ofertas presentadas por los demás participantes en el proceso de licitación. | El acto de apertura de ofertas es público en cuanto a permitir presencia de oferentes, pero los antecedentes de otras ofertas no deben ser entregados hasta adjudicación. | acta apertura, publicidad, conocimiento ofertas | `Acta Apertura de Ofertas/29.549-2000.md` |
| 005380N00 | 2000 | 14-II-2000 | OPTIMA | esta Contraloría General no se encuentra obligada a dar copia de la consulta formulada por la Superintendencia de Servicios Sanitarios. | Una consulta a órgano fiscalizador no constituye acto administrativo hasta su resolución definitiva; durante control previo rige reserva de fiscalización. | acto administrativo, publicidad, control previo | `Acta Apertura de Ofertas/5380-2000.md` |

### Adjudicacion  (10 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 15.331 | 2018 | 20-VI-2018 | OPTIMA | no se observan irregularidades respecto del contenido de las aludidas bases administrativas, por cuanto sus factores de evaluación, en especial el relativo a la experiencia de los oferentes, fueron establecidos por el servicio recurrido con apego a las atribuciones de que dispone. | Las bases pueden incluir criterios de evaluación como experiencia con escalas de puntaje que respeten principios de eficacia y eficiencia pública. | experiencia oferentes, revocación licitación, criterios evaluación | `Adjudicacion/15.331-2018 - Supletoria 19.880, experiencia (Bases no definen nada, igual CGR esta bien).md` |
| 20.061 | 2017 | 01-VI-2017 | OPTIMA | deberá adoptar las medidas conducentes a que sus actos administrativos de esta naturaleza, en lo sucesivo, den cuenta de manera expresa en su texto de las circunstancias de hecho y de derecho que los motiven. | El desestimamiento de ofertas debe estar expresamente motivado en el acto administrativo, no solo remitiendo a otras actuaciones. | motivación, rechazo propuestas, acto administrativo | `Adjudicacion/20.061-2017_ Necesidad de motivacion hecho derecho en acto.md` |
| ⚠ 37.260 | 2014 | 28-V-2014 | OPTIMA | la omisión de un oferente, en orden a no indicar el monto total o neto de su propuesta, si es que se ha consignado al menos uno de esos datos, reviste un carácter formal y no constituye un error esencial. | La omisión del valor neto o total es error formal si se puede obtener mediante operación aritmética simple sin modificar el precio ofertado. | operación aritmética, valor neto, valor total | `Adjudicacion/37.260-2014_ Operacion aritmetica.md` |
| 37.613 | 2017 | 24-X-2017 | OPTIMA | dado que no existe discordancia entre el precio neto ofertado por la empresa seleccionada y el precio bruto adjudicado, es dable colegir que la oferta seleccionada sí contempló el IVA relativo a las utilidades. | Si existe concordancia entre precio neto y bruto con IVA desglosado, la oferta que incluye IVA en distintos componentes (costo directo, utilidades, impuestos) cumple requisitos de presentación. | IVA, utilidades, precio oferta | `Adjudicacion/37.613-2017_ Ofertas e IVA.md` |
| 73.638 | 2015 | 15-IX-2015 | OPTIMA | esta Sede de Control no advierte reproche que formular en torno a lo obrado por la Municipalidad de San José de Maipo sobre la materia. | El presupuesto establecido en bases es monto referencial estimativo, no límite absoluto; ofertas que superan hasta 10% pueden adjudicarse con autorización de fondos complementarios. | presupuesto disponible, suplemento presupuestario, adjudicación | `Adjudicacion/73.638-2015_ Adjudicación sobre presupuesto disponible.md` |
| ⚠ 007948N18 | 2018 | 22-III-2018 | OPTIMA | el hecho que la singularizada empresa ofertara su precio con IVA incluido reviste un carácter formal y no constituye un error esencial que afecte la validez de la oferta. | Incluir IVA en el precio cuando bases exigen valor neto es error formal no esencial si mediante operación aritmética se obtiene el valor neto sin modificar el precio. | IVA, precio neto, error formal | `Adjudicacion/007948N18 - Tribunales inclinense!.md` |
| ⚠ 011782N18 | 2018 | 09-V-2018 | OPTIMA | se determinó que las evaluaciones técnicas no fueron suscritas por la totalidad de los funcionarios que habían sido designados en cada una de las Actas de Comisión Evaluadora, conforme con lo previsto en las respectivas bases administrativas. | Las evaluaciones técnicas de ofertas deben ser suscritas por la totalidad de funcionarios designados en las Actas de Comisión Evaluadora conforme a bases. | evaluación técnica, comisión evaluadora, adjudicación | `Adjudicacion/011782N18 - Evaluaciones suscritas por todos los nombrados.md` |
| ⚠ 061067N16 | 2016 | 18-VIII-2016 | OPTIMA | en mérito de lo expuesto se desestima el aspecto de la denuncia relativa a evaluación de experiencia por fórmula comparativa entre oferentes. | Una fórmula comparativa de experiencia basada en relación entre ofertas máximas y evaluadas no vulnera libre concurrencia si no es requisito de admisibilidad sino factor de ponderación. | evaluación experiencia, fórmula comparativa, libre concurrencia | `Adjudicacion/MERITO! Eval. Experiencia.md` |
| ⚠ 067134N16 | 2016 | 12-IX-2016 | OPTIMA | ese servicio se encontraba en el imperativo de comunicar a través del Sistema de Información las razones que justificaban el incumplimiento de dicho término. | Cuando adjudicación se realiza fuera del plazo de bases, la entidad debe publicar en Sistema de Información las razones del incumplimiento y nuevo plazo estimado. | plazo adjudicación, sistema información, transparencia | `Adjudicacion/Publicar razones de demora adj.md` |
| ⚠ 084937N16 | 2016 | 23-XI-2016 | OPTIMA | Comisiones evaluadoras deben fundamentar las medidas que impliquen no considerar antecedentes presentados por los participantes en un proceso concursal. | Los actos evaluadores que rechacen antecedentes de experiencia deben justificar los fundamentos en el acta respectiva conforme a artículo 40 bis del DTO 250. | experiencia, comisión evaluadora, fundamentación | `Adjudicacion/Debe indicar mot rech experiencia.md` |

### Bases  (15 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 14.200 | 2018 | 07-06-2018 | OPTIMA | Esta Contraloría General entiende que aquellos oferentes que no posean la experiencia en los términos exigidos en el mencionado acápite, se evaluarán con 0 punto, no resultando procedente exigir una determinada experiencia como requisito de admisibilidad de los participantes, pero esta sí se puede evaluar conforme lo dispone el artículo 38 del decreto N° 250, de 2004. | La experiencia no puede exigirse como requisito de admisibilidad conforme al principio de libre concurrencia, pero sí puede evaluarse como criterio de calificación de ofertas. | experiencia, libre concurrencia, evaluación, criterios, requisitos | `Bases/14.200-2018, Experiencia no exigible, evaluable.md` |
| 14.202 | 2018 | 07-06-2018 | OPTIMA | Las disposiciones contenidas en las letras E. y M. del anexo N° 2 no pueden restringir las facultades propias de la Administración del Estado ni traducirse en renuncias a derechos y acciones que no estén permitidos en el ordenamiento jurídico, dejando a salvo el ejercicio de las acciones correspondientes por parte de la Tesorería General de la República. | La Administración no puede renunciar a facultades o derechos mediante cláusulas contractuales, particularmente cuando estas limitarían su capacidad de ejercer acciones por perjuicios imputables al contratista. | renuncias de derechos, facultades administrativas, trato directo, cláusulas contractuales | `Bases/14.202-2018, No weiwer derechos Administracion.md` |
| ⚠ 14.828 | 2018 | 14-06-2018 | OPTIMA | No resulta procedente la obligación que se establece al proveedor en el N° 22.3 del pliego de condiciones relativa a hacer entrega de la cuarta copia cedible de la factura al momento del pago, puesto que transgrede lo preceptuado en el inciso final del artículo 4° de la ley N° 19.983, reemplazado por la ley N° 20.323, en cuanto se prohíbe cualquier condición que limite la libre circulación de un crédito que conste en una factura. | Las bases no pueden exigir la entrega de la cuarta copia cedible de factura, ya que esto limita la libre circulación del crédito, prohibida por ley. | cuarta copia factura, libre circulación, crédito mercantil, licitación pública | `Bases/14.828-2018, Cuarta copia factura.md` |
| 21.503 | 2003 | 26-05-2003 | OPTIMA | La Contraloría General ha debido abstenerse de dar curso al decreto de 2002 que aprueba convenio complementario de concesión de la obra pública, en atención a que la cláusula séptima del contrato que establece renuncia a efectuar cualquier reclamación que pudiera haber correspondido por materias tratadas y no tratadas en él resulta jurídicamente improcedente, pues la amplitud de su contenido impide la determinación del objeto de la declaración de voluntad. | Una renuncia de derechos debe tener un objeto claro y determinado; no es válida una renuncia amplia e indeterminada que incluya materias tratadas y no tratadas. | renuncia de derechos, concesión de obra pública, claridad del objeto, concesión Oriente-Poniente | `Bases/21.503-2003_ Renuncia debe tener objeto claro.md` |
| 21.674 | 2018 | 30-08-2018 | OPTIMA | Si bien en el contexto de la evaluación del factor responsabilidad social el pliego indica que se otorgará puntaje a las empresas que certifiquen tener empleados con discapacidad, ello solo podrá ocurrir en la medida que dichas contrataciones superen el mínimo legal establecido en el artículo 157 bis del Código del Trabajo. | El puntaje por responsabilidad social respecto a empleados con discapacidad solo procede si la empresa supera el mínimo legal de contratación de personas con discapacidad. | responsabilidad social, discapacidad, puntaje evaluación, Carabineros | `Bases/21.674-2018_ Min discapacidad, evaluacion.md` |
| 33.246 | 2017 | 12-09-2017 | OPTIMA | No resulta procedente la obligación que se establece al proveedor en el párrafo final de la cláusula quinta del acuerdo de voluntades, relativa a hacer entrega de la cuarta copia de la factura al momento del pago, puesto que transgrede lo preceptuado en el inciso final del artículo 4° de la ley N° 19.983, reemplazado por la ley N° 20.323, en cuanto se prohíbe cualquier condición que limite la libre circulación de un crédito que conste en una factura. | La cuarta copia cedible de factura no puede ser exigida como condición de pago, pues esto vulnera la libre circulación de créditos mercantiles. | cuarta copia factura, libre circulación de crédito, PDI, contrato de servicio | `Bases/33.246-2017, Cuarta copia factura, sin condiciones a credito.md` |
| 37.465 | 2013 | 12-06-2013 | OPTIMA | Para órganos públicos de la Administración del Estado, el ejercicio del derecho de información, retención y pago por subrogación constituye un imperativo legal, no facultativo. Estos derechos disminuyen su grado de responsabilidad de solidaria a subsidiaria en materias de subcontratación. | Los órganos públicos deben ejercer los derechos de información, retención y pago por subrogación sobre subcontratistas, ya que estos derechos son imperativos para limitar su responsabilidad solidaria. | subcontratación, información, retención, subrogación, responsabilidad solidaria | `Bases/37.465-2013_ Informacion, retencion y subrogacion.md` |
| 42.462 | 2011 | 06-07-2011 | OPTIMA | En la licitación no se está en presencia de una exigencia meramente formal, sino de un requisito que tanto el reglamento como las bases elevaron expresamente al carácter de esencial, al disponer que su omisión trae aparejada la exclusión de la licitación. La Administración no puede evaluar si los antecedentes presentados son equivalentes a los exigidos, pues ello infringiría el principio de igualdad y estricta sujeción a las bases. | Cuando las bases elevan un requisito al carácter de esencial, su omisión es causal de exclusión; la Administración no puede valorar equivalencias o interpretar finalidades en forma más flexible. | requisitos esenciales, estricta sujeción a bases, igualdad de oferentes, obra pública, capacidad económica | `Bases/42.462-2011_ Reqs formales elevados a esenciales, bases.md` |
| ⚠ 47.664 | 2012 | 06-08-2012 | OPTIMA | Contraviene el principio de libre concurrencia de los oferentes exigir que los licitantes se encuentren inscritos en uno de los registros especiales y que presenten certificado de inscripción, pues ello no se concilia con el principio consagrado en los artículos 4° y 6° de la ley N° 19.886. | No se puede exigir inscripción en registros especiales como requisito para participar, ya que esto vulnera la libre concurrencia de oferentes. | libre concurrencia, inscripción registro, construcción, establecimientos de salud | `Bases/47.664-2012_ no puedo exigir inscripcion en reg especial.md` |
| ⚠ 48.929 | 2012 | 09-08-2012 | OPTIMA | El servicio debe entregar a los licitantes antecedentes que guarden la debida correspondencia entre sí, de modo que los interesados puedan conocer con exactitud el objeto de la convocatoria. La omisión de especificaciones técnicas del proyecto con sus anexos, planimetría y estudios constituye un obstáculo para la toma de razón de las bases administrativas. | Las bases deben contener toda la información necesaria y coherente para que los oferentes comprendan claramente el alcance de la licitación; no se puede omitir documentación técnica esencial. | información completa, especificaciones técnicas, planimetría, suma alzada, Hospital Laja | `Bases/48.929-2012_ Ob de entregar toda la info.md` |
| ⚠ 55.867 | 2016 | 28-07-2016 | OPTIMA | Si la persona contratada en el marco de la ley N° 19.886 no tiene a su cargo trabajadores regidos por el Código del Trabajo, no es posible aplicar a su respecto las disposiciones sobre obligaciones laborales y previsionales, por lo que basta la sola declaración de la persona contratada de que no cuenta con trabajadores a su cargo. | No se puede exigir certificado de cumplimiento de obligaciones laborales a un proveedor que no tiene trabajadores; basta su declaración jurada. | trabajadores, obligaciones laborales, OTEC, certificado, SENCE | `Bases/Art. 22, N° 9, Sin gente a cargo.md` |
| 61.067 | 2016 | 18-08-2016 | OPTIMA | La disposición que rechaza ofertas cuando la económica sea inferior al 95% disponible contraviene los principios de eficiencia y de ahorro que debe observar la Administración en sus contrataciones, al restringir la competencia respecto del factor económico. | No se puede establecer un piso de presupuesto mínimo (como 95% de lo presupuestado) porque limita la competencia y vulnera los principios de eficiencia y ahorro. | piso presupuestario, eficiencia, ahorro, libre concurrencia, Independencia | `Bases/Criticas a Bases, competencia TCP.md` |
| 63.391 | 2014 | 18-08-2014 | OPTIMA | No resulta procedente la obligación que se establece al contratista en las bases relativa a hacer entrega de su copia cedible de la factura para ser inutilizada, puesto que transgrede lo preceptuado en el inciso final del artículo 4° de la ley N° 19.983, reemplazado por la ley N° 20.323, en cuanto se prohíbe cualquier condición que limite la libre circulación de un crédito que conste en una factura. | No se puede exigir la inutilización de la copia cedible de factura, pues esto restringe la libre circulación del crédito mercantil. | cuarta copia factura, inutilización, libre circulación, Universidad de Santiago | `Bases/63.391-2014, Cuarta copia factura, sin condiciones a credito.md` |
| ⚠ 65.731 | 2013 | 11-10-2013 | OPTIMA | Las bases técnicas contemplaron las dimensiones que deben cumplir los vehículos licitados, sin que la Dirección Nacional de Logística de Carabineros haya explicado la manera en que esas características influyen en la seguridad, frenado, estabilidad, ergonomía, comportamiento en ruta; por tanto, la sola invocación técnica no es suficiente para quitar el reproche de arbitrariedad. | Las exigencias técnicas deben estar fundamentadas y explicadas para demostrar que responden a necesidades reales de la institución, no a preferencia por marcas específicas. | especificaciones técnicas, libre concurrencia, fundamentación, motos de tránsito, Carabineros | `Bases/65.731-2013_ Explicar razones de EETT.md` |
| ⚠ - | 2016 | 03-10-2016 | OPTIMA | La determinación adoptada por el municipio en orden a exigir determinados requisitos de fabricación de los bienes se funda en una razón apreciada por esa entidad edilicia en el marco de sus atribuciones, relacionada con el servicio de post venta, por lo que no aparece que se haya incurrido en una decisión arbitraria. | Una exigencia de fabricación nacional puede ser válida si está justificada por razones operacionales reales, como facilitar post-venta, sin vulnerar los principios de libre concurrencia. | fabricación nacional, butacas, requisitos de fabricación, teatro Oriente | `Bases/Art. 22, N° 2.md` |

### Comisiones de Evaluacion  (1 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 84.990 | 2016 | 23-11-2016 | OPTIMA | Las autoridades correspondientes pueden designar a los integrantes de las comisiones evaluadoras de procedimientos concursales regulados por la ley N° 19.886 a través de un acto administrativo previo, sin que sea necesario designarlas en cada licitación. | La designación de comisiones evaluadoras puede hacerse mediante un acto administrativo previo general, referenciado luego en las bases de cada licitación. | comisiones evaluadoras, designación, acto previo, licitación pública, La Granja | `Comisiones de Evaluacion/Se puede por acto previo.md` |

### Compras agiles  (17 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| D87N26 | 2026 | 25-02-2026 | OPTIMA | No resulta procedente que municipalidades entreguen en concesión el servicio de recolección de residuos sólidos domiciliarios a través del procedimiento de compra ágil. | Compra ágil no puede utilizarse para otorgar concesiones de servicios municipales como recolección de residuos, ya que estas requieren procedimientos específicos (licitación pública o propuesta privada) con toma de razón previa. | compra agil, concesion, residuos domiciliarios, municipalidad coyhaique | `Compras agiles/contraloria (14).md` |
| OF59317 | 2026 | 27-03-2026 | OPTIMA | compra ágil se ajusta a regulación para contratación de monto igual o inferior a 100 UTM con cotizaciones requeridas | compra ágil requiere cumplimiento de exigencias de monto, solicitud de cotizaciones y que elegida corresponda a lo solicitado | compra ágil, 100 UTM, cotizaciones, procedimiento especial | `Compras agiles/contraloria (9).md` |
| 002659N21 | 2021 | 11-11-2021 | OPTIMA | Los aludidos funcionarios no pueden intervenir directamente en el marco de las manifestaciones sociales, ya que dicha situación importaría exceder las labores de apoyo y colaboración para las que están habilitados. | Municipalidades pueden desarrollar funciones de seguridad comunal como apoyo coordinado a organismos competentes, pero no pueden asumir funciones de orden público reservadas a Carabineros e Investigaciones. | municipalidad, orden publico, seguridad ciudadana, briop | `Compras agiles/contraloria (23).md` |
| ⚠ E11631N25 | 2025 | 23-01-2025 | OPTIMA | No se advierte reproche que formular en torno a la contratación de la especie, efectuada bajo la modalidad de contratación denominada compra ágil. | La compra ágil requiere constancia de los motivos considerados por la entidad compradora para elegir al proveedor, ajustándose a lo previsto en la solicitud de cotizaciones. | compra agil, subsecretaria salud, grabado patentes | `Compras agiles/contraloria (18).md` |
| ⚠ E68062N25 | 2025 | 24-04-2025 | OPTIMA | No resultó procedente que el Instituto Nacional de Estadísticas exigiera una marca específica en los procesos de compras ágiles que se indican. | No es procedente exigir que las ofertas en procesos de compra correspondan a productos de marca determinada, pues ese requisito vulnera el principio de libre concurrencia de proveedores. | compra agil, ine, marca especifica, impresoras credenciales | `Compras agiles/contraloria (17).md` |
| E72886N25 | 2025 | 05-05-2025 | OPTIMA | El uso de la modalidad de compra ágil impone el deber de velar que tanto el objeto de la contratación como la selección de las cotizaciones se ajusten a la normativa que regula la materia. | Es responsabilidad de los órganos de administración que utilicen el sistema de información velar que el objeto de sus contrataciones y la selección de cotizaciones en compra ágil se ajusten al ordenamiento jurídico. | compra agil, objeto contratacion, seleccion cotizaciones, dccp | `Compras agiles/contraloria (16).md` |
| ⚠ OF87469N26 | 2026 | 07-05-2026 | OPTIMA | No procedió que la Universidad de Chile exigiera experiencia para presentar cotizaciones en el marco de un proceso de compra ágil. | No resulta procedente exigir determinada pericia como requisito de admisibilidad en procesos licitatorios, atendido el principio de libre concurrencia de oferentes, aunque pueda considerarse como criterio de evaluación. | compra agil, uchile, libre concurrencia, requisitos admisibilidad | `Compras agiles/contraloria (13).md` |
| OF93103N26 | 2026 | 14-05-2026 | OPTIMA | Compete a la Dirección de Compras y Contratación Pública comprobar que las empresas que declaran ser de menor tamaño tengan esa calidad. | En compra ágil, la Dirección de Compras debe verificar la declaración jurada de empresas para constatar si son realmente de menor tamaño o si pertenecen a un grupo empresarial donde la controladora no es de menor tamaño. | compra agil, empresa menor tamaño, directiva compras | `Compras agiles/contraloria (12).md` |
| ⚠ E108767N21 | 2021 | 27-05-2021 | ESCANEADO_VISION | Si se utiliza la modalidad de compra ágil, las cotizaciones deben requerirse a través del sistema de información de compras y contrataciones de la Administración. | Compra ágil requiere obligatoriamente solicitud de cotizaciones a través del sistema de información, no siendo aplicables otros mecanismos previstos en artículo 7 bis decreto 250. | compra agil, carabineros, cotizaciones, sistema informacion | `Compras agiles/contraloria (25).md` |
| OF120447N26 | 2026 | 23-06-2026 | ESCANEADO_VISION | No se advierten irregularidades en torno a la evaluación de las ofertas presentadas en la compra ágil que se indica. | La compra ágil es una modalidad especial de trato directo que requiere constancia de los motivos considerados por la entidad compradora para seleccionar al proveedor, ajustándose a lo previsto en la solicitud de cotizaciones. | compra agil, subsecretaria niñez, evaluacion tecnica | `Compras agiles/contraloria (11).md` |
| E141710N25 | 2025 | 22-08-2025 | OPTIMA | La contratación de la especie, efectuada bajo la modalidad de compra ágil, no se ajustó a las normas que la rigieron, por lo que la entidad contratante deberá iniciar un procedimiento de invalidación. | Cuando se verifica error en la aplicación de criterios de admisibilidad y puntaje en compra ágil, la entidad debe iniciar procedimiento de invalidación conforme a ley 19880 art. 53. | compra agil, seremi agricultura, error admisibilidad, sillones ejecutivos | `Compras agiles/contraloria (15).md` |
| ⚠ E152886N21 | 2021 | 04-11-2021 | OPTIMA | Municipalidad no requiere la emisión de un decreto alcaldicio que autorice la modalidad de compra ágil prevista en el artículo 10 bis del Decreto N° 250, de 2004. | Compra ágil no requiere dictación de acto administrativo, bastando cumplimiento de requisitos del artículo 10 bis del decreto 250; las municipalidades se rigen por esta normativa. | compra agil, municipalidad, decreto alcaldicio, san pedro atacama | `Compras agiles/contraloria (24).md` |
| ⚠ E189914N22 | 2022 | 02-03-2022 | OPTIMA | La orden de compra es el instrumento mediante el cual se autorizan los tratos directos celebrados a través de la modalidad de contratación denominada compra ágil. | Compra ágil no requiere dictación de resolución fundada, bastando con emisión y aceptación de orden de compra como documento formal y público que acredita la causal. | compra agil, orden compra, carabineros, resolucion fundada | `Compras agiles/contraloria (22).md` |
| ⚠ E240653N22 | 2022 | 29-07-2022 | OPTIMA | Contratación se efectuó de acuerdo a lo establecido en la normativa que regula la modalidad de contratación denominada compra ágil. | Compra ágil es modalidad de trato directo para contrataciones inferiores a 30 UTM con mínimo 3 cotizaciones; la entidad determina el proveedor sin obligación de menor precio. | compra agil, uchile, trato directo, monto | `Compras agiles/contraloria (21).md` |
| ⚠ E287821N22 | 2022 | 15-12-2022 | OPTIMA | Contratación se efectuó de acuerdo a lo establecido en la normativa que regula la modalidad de contratación denominada compra ágil. | Compra ágil es modalidad especial de trato directo donde deben existir constancia de motivos para elegir proveedor, ajustándose a lo previsto en solicitud de cotizaciones. | compra agil, snpc, eleccion proveedor, fundamento | `Compras agiles/contraloria (20).md` |
| E464046N24 | 2024 | 18-03-2024 | OPTIMA | Aspectos relacionados con las principales modificaciones a la ley Nº 19.886, introducidas por la ley Nº 21.634. | Ley 21634 incorpora regulaciones sobre probidad administrativa, transparencia, prohibición de comunicación entre participantes, prohibiciones de contratos y deber de abstención en procedimientos de contratación pública. | ley 21634, probidad, transparencia, modificaciones contratacion | `Compras agiles/contraloria (19).md` |
| - | - | - | IRRECUPERABLE | - | - | compra agil, irrecuperable | `Compras agiles/contraloria (10).md` |

### Contratacion  (2 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 89.921 | 2016 | 15-12-2016 | OPTIMA | No se aprecia que la empresa adjudicataria haya acompañado el certificado de inscripción vigente en el registro de contratistas del Ministerio de Obras Públicas exigido en las bases, por lo que no se observa reproche a la decisión municipal de dejar sin efecto la adjudicación. | Si el oferente no presenta la inscripción requerida en el registro específico indicado por las bases al momento de contratar, la Administración puede dejar sin efecto la adjudicación. | inscripción, registro de contratistas, obra pública, Isla de Maipo | `Contratacion/Deja sin efecto contratacion por papel faltante.md` |
| 89.921 | 2016 | 15-12-2016 | OPTIMA | No se aprecia que la empresa adjudicataria haya acompañado el certificado de inscripción vigente en el registro de contratistas del Ministerio de Obras Públicas exigido en las bases, por lo que no se observa reproche a la decisión municipal de dejar sin efecto la adjudicación. | Si el oferente no presenta la inscripción requerida en el registro específico indicado por las bases al momento de contratar, la Administración puede dejar sin efecto la adjudicación. | inscripción, registro de contratistas, obra pública, Isla de Maipo | `Contratacion/www.contraloria.cl_LegisJuri_DictamenesGeneralesMunicipales.md` |

### Convenio Marco  (1 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 89.567 | 2016 | 14-12-2016 | OPTIMA | Se representa el instrumento del epígrafe, a fin de que esa superioridad ordene la reapertura del proceso en examen y adopte las acciones encaminadas a determinar la responsabilidad administrativa de los empleados involucrados. | En grandes compras dentro de convenio marco, entidad solo puede fijar condiciones complementarias; no es procedente modificar sustancialmente criterios de evaluación del convenio, como separar ponderaciones o cambiar definiciones de factores. | convenio marco, grandes compras, criterios evaluacion | `Convenio Marco/Grandes Compras - No MOD CRITERIOS!.md` |

### Criterios de evaluacion  (5 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 14.813 | 2019 | 31-05-2019 | OPTIMA | La comisión evaluadora se encuentra en el imperativo de verificar que los antecedentes presentados sean idóneos para la asignación de puntajes. | Las pautas de evaluacion elaboradas por comisión deben precisar forma de calificar factores definidos en bases pero no pueden introducir subfactores no previstos. | criterios evaluacion, pautas comision, puntajes, antecedentes | `Criterios de evaluacion/14.813-2019_ Pautas para evaluar criterios que haga comision valen.md` |
| 20.203 | 1999 | 04-06-1999 | BUENA | La decisión de municipalidad de no adjudicar la propuesta al oferente que presentó oferta de menor valor se encuentra ajustada a derecho. | Corresponde a municipalidad ponderar ofertas conforme criterios técnicos propios; Contraloria no puede evaluar aspectos de mérito y conveniencia en evaluacion. | criterios evaluacion, oferta menor valor, merito administrativo, municipio | `Criterios de evaluacion/20.203-1999_ CGR no se puede meter con evaluación.md` |
| 32.261 | 1989 | 01-12-1989 | OPTIMA | La Contraloría no está facultada para ponderar las ofertas presentadas a una propuesta pública ni las razones de mérito que sirvan de fundamento para rechazarlas. | Contraloria incompetente para ponderar criterios evaluacion licitaciones; esa atribucion corresponde exclusivamente a administracion activa. | incompetencia Contraloria, criterios evaluacion, merito, ofertas | `Criterios de evaluacion/32.261-1989_ CGR no se puede meter con evaluación.md` |
| ⚠ 61.067 | 2016 | 18-08-2016 | OPTIMA | La disposición en comento contraviene los principios de eficiencia y de ahorro que debe observar la Administración en sus contrataciones. | Criterio que rechaza ofertas economicas inferiores a porcentaje minimo del presupuesto contraviene principios eficiencia y ahorro pues restringe competencia. | precio minimo, ofertas economicas, eficiencia, ahorro, licitacion | `Criterios de evaluacion/61.067-2016_ Criterio que limita precio minimo NO!.md` |
| 65449 | 2015 | 17-08-2015 | OPTIMA | fórmula de asignación de puntaje por experiencia del oferente que usa regla de tres genera diferencia arbitraria en desmedro de restantes oferentes | criterios evaluación deben evitar que puntajes queden determinados por elemento ajeno a experiencia propia del oferente; debe propender a eficiencia, eficacia y ahorro | experiencia oferente, criterios evaluación, regla de tres, igualdad oferentes | `Criterios de evaluacion/65.449-2015_ Regla de tres, experiencia.md` |

### Derechos Consolidados  (13 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 5.448 | 2015 | 20-01-2015 | OPTIMA | No se aprecia que la medida impugnada haya significado transgredir los límites precedentemente reseñados, toda vez que, en la especie, el contrato a que pudo dar lugar la licitación no se verificó. | La revocación de licitación es procedente cuando no se ha completado la tramitación del contrato ni se han adquirido derechos consolidados. | revocación licitación, contrato no verificado, total tramitación, cambio proyecto | `Derechos Consolidados/Dictamen 5448 - Derechos consolidados contrato tramitado.md` |
| ⚠ 14238 | 2018 | 07-06-2018 | OPTIMA | evaluación de ofertas se hizo con infracción a bases, vulnerándose principio estricta sujeción a bases por falta de acreditación de experiencia del gásfiter residente | incumplimiento de requisito de experiencia acreditada posterior a inscripción infringe estricta sujeción a bases e igualdad de oferentes | licitación pública, experiencia, criterios formales, invalidación contrato | `Derechos Consolidados/14.238-2018, ESB e IOf, invalidación ctto ejec. No hay Ds C.md` |
| ⚠ 20.061 | 2015 | 13-03-2015 | OPTIMA | Procede invalidar licitación cuyas bases contravienen la normativa de compras y contratación pública. | Las bases administrativas deben cumplir requisitos mínimos y establecer criterios de evaluación conforme a la ley 19.886. | invalidación licitación, vicios bases administrativas, adjudicación improcedente | `Derechos Consolidados/20.061-2015.md` |
| ⚠ 22.161 | 2017 | 16-06-2017 | OPTIMA | La Municipalidad de Puerto Octay deberá arbitrar las medidas que resulten pertinentes para invalidar el acto de adjudicación de la especie. | Las aclaraciones a la oferta no pueden traducirse en modificación de la propuesta presentada pues constituiría contraoferta que afecta la igualdad de oferentes. | aclaraciones oferta, modificación propuesta, igualdad oferentes, invalidación adjudicación | `Derechos Consolidados/22161-2017_ Invalidacion mala adjudicacion.md` |
| 24.337 | 2002 | 01-07-2002 | OPTIMA | Es jurídicamente improcedente el ejercicio de la potestad invalidatoria si el acto administrativo ilegal ha producido efectos y estos han ingresado al patrimonio de sus beneficiarios de buena fe. | La invalidación tiene como límite aquellas situaciones jurídicas consolidadas sobre la base de la confianza de los particulares en la administración. | derechos consolidados, buena fe, invalidación límites, situación jurídica consolidada | `Derechos Consolidados/24337-2002_ Limite a invalidacion (Ramiro!).md` |
| 28.251 | 2016 | 15-04-2016 | OPTIMA | El Servicio de Salud Metropolitano Occidente no ajustó su actuación a las bases administrativas al dejar sin efecto la adjudicación de la propuesta pública que indica. | La administración debe cumplir el procedimiento establecido en bases: elaborar contrato y citar adjudicatario dentro de los 15 días posteriores a adjudicación. | garantía de fiel cumplimiento, plazo presentación garantía, contrato administrativo, invalidación improcedente | `Derechos Consolidados/28251-2016_ Inv. por malas bases.md` |
| 35.087 | 2014 | 20-05-2014 | OPTIMA | No se aprecia que lo resuelto mediante el oficio que se impugna -en el sentido de que el proceso licitatorio deba retrotraerse- afecte derechos adquiridos de la empresa recurrente. | Los derechos adquiridos se consolidan cuando el contrato es totalmente tramitado; si no se completó la tramitación, la retrotracción es procedente conforme a las bases. | total tramitación, derechos adquiridos, retrotracción proceso, contrato administrativo | `Derechos Consolidados/Dictamen 35.087-2014 - Derechos consolidados contrato tramitado.md` |
| ⚠ 36.593 | 2016 | 17-05-2016 | OPTIMA | Se desestima la solicitud de reconsideración y se confirma y complementa el citado oficio N° 20.393, de 2015, de la Sede Regional del Bío-Bío. | La revocación de un acto administrativo no procede cuando se trata de actos declarativos o creadores de derechos adquiridos legítimamente. | revocación licitación, derechos adquiridos, bases de licitación, evaluación ofertas | `Derechos Consolidados/36.593-2016.md` |
| 37.221 | 1994 | 31-10-1994 | OPTIMA | Cursa por esta vez el DTO 59/94 de la Subsecretaría de Telecomunicaciones que adjudica propuesta pública para la adquisición de instrumentos. | En derecho público la voluntad de la administración se manifiesta al dictar el acto de autoridad que aprueba el convenio, solo produciendo efectos válidos tras tramitación total del decreto o resolución. | compraventa muebles, derecho público, tramitación acto administrativo, perfeccionamiento contrato | `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md` |
| 45.487 | 2016 | 20-06-2016 | OPTIMA | No procede analizar actuación de comisión que señala, por haber sido revocada la licitación que indica; municipio debe arbitrar medidas para evitar la revocación de procesos concursales. | La revocación de bases de licitación procede cuando no se han consumado efectos ni afectado situaciones jurídicas consolidadas respecto de terceros. | revocación bases, derechos adquiridos, comisión evaluadora, licitación pública | `Derechos Consolidados/45.487-2016.md` |
| 76.032 | 2015 | 24-09-2015 | OPTIMA | No se ajustó a derecho que el Centro de Referencia de Salud de Peñalolén Cordillera Oriente dejara sin efecto las resoluciones de adjudicación y de aprobación de contrato, sin audiencia previa de la interesada. | La invalidación de actos administrativos requiere procedimiento previo con audiencia del interesado, no puede revocarse acto que genera derechos adquiridos de buena fe. | audiencia previa, invalidación procedimiento, derechos adquiridos, buena fe, revocación improcedente | `Derechos Consolidados/76.032-2015.md` |
| 76.032 | 2015 | 24-09-2015 | OPTIMA | No se ajustó a derecho la resolución exenta N° 1.755, de 2014, del CRSCO, que dejó sin efecto sus actos exentos N°s. 1.516 y 1.631, ambos de 2014. | Una situación jurídica consolidada resultado de adjudicación y suscripción de contrato de buena fe no puede ser afectada por revocación sin procedimiento de invalidación. | derechos consolidados, caducidad plazo, situación consolidada, invalidación improcedente | `Derechos Consolidados/76.032-2015_ Ds Consolidados por caducidad de plazo invalidacion.md` |
| 96.610 | 2015 | 04-12-2015 | OPTIMA | Rectificación de oficio de la evaluación de las ofertas y de la adjudicación no se ajustó a derecho, ya que advertido el error en la evaluación correspondía su invalidación previa audiencia del interesado. | El error de cálculo en evaluación de ofertas vicia el proceso de selección, requiriendo invalidación con audiencia previa, no aclaración de oficio si ha generado derechos consolidados. | error de cálculo, evaluación ofertas, aclaración vs invalidación, derechos consolidados | `Derechos Consolidados/96.610-2015.md` |

### Directivas  (12 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 6 | 2025 | 2025-12-24 | OPTIMA | - | - | plan anual de compras, PAC, planificación | `Directivas/568-B_Res_Directiva6_2025_PAC.md` |
| 10 | 2025 | 2025-12-23 | OPTIMA | - | - | trato directo, contratación excepcional, publicidad | `Directivas/565-B-Res.-Aprueba-Directiva-de-Contratacion-Publica-N°-10-2025-sobre-Trato-Directo.md` |
| 14 | 2026 | 2026-01-28 | OPTIMA | - | - | comisiones evaluadoras, funcionamiento, recomendaciones | `Directivas/054-B-Res.-Aprueba-Directiva-de-Contratacion-N°-14-2026-Comisiones-Evaluadoras.md` |
| 28 | 2025 | 2025-12-18 | OPTIMA | - | - | código de ética, probidad, compras públicas | `Directivas/557BRes-Directiva28-2025-CodigodeEtica.md` |
| 31 | 2026 | 2026-01-21 | OPTIMA | - | - | ética, proveedores, código de ética, probidad | `Directivas/037-B-Res.-Aprueba-Directiva-de-Contratacion-N-31-2026-Codigo-etica-proveedores.md` |
| - | - | 2025-12-22 | OPTIMA | - | - | eficiencia, contratación pública, recomendaciones | `Directivas/561BRes-Directiva26-eficiencia.md` |
| - | - | 2025-12-22 | OPTIMA | - | - | compra ágil, modalidad de contratación, recomendaciones | `Directivas/563BRes-Directiva35CompraAgil.md` |
| - | - | 2026-02-05 | OPTIMA | - | - | pago oportuno, proveedores, contratación pública | `Directivas/72-B-directiva-pago-oportuno.md` |
| - | - | 2025-07-31 | OPTIMA | - | - | género, empresas mujer, igualdad, equidad, autonomía económica | `Directivas/Actualizacion-Directiva20.md` |
| - | - | 2026-03-12 | OPTIMA | - | - | inteligencia artificial, ciencia de datos, ética, sesgos, transparencia, ciberseguridad, privacidad | `Directivas/Directiva-44-Ciencia-de-Datos-IA.md` |
| - | - | 2026-02-18 | OPTIMA | - | - | compras coordinadas, agregación de demanda, eficiencia, ahorro, colaboración estatal | `Directivas/directiva-compras-coordinadas.md` |
| - | - | 2025-02-06 | OPTIMA | - | - | datos personales, protección de privacidad, seguridad, compras públicas, transparencia, confidencialidad | `Directivas/Directiva45.md` |

### Errores no esenciales  (8 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 42.421 | 2001 | 14-11-2001 | OPTIMA | Excluir a la sociedad por aplicación de las bases constituye una decisión que se apartaría de la finalidad última del procedimiento de licitación, cual es la selección del mejor proponente entre el mayor número de ofertas. | Enmiendas en formulario de oferta que no influyen en el monto y no afectan validez son intrascendentes y no justifican descalificacion. | enmiendas oferta, formulario, suma alzada, error dactilografico | `Errores no esenciales/Modificacion Formulario.md` |
| 68.010 | 2012 | 30-10-2012 | OPTIMA | La omisión de los valores unitarios con IVA reviste un carácter formal y no constituye un error esencial que afecte la validez de la misma. | Omisiones formales que mediante operacion aritmetica simple pueden completarse y que no afectan transparencia ni principios de igualdad no justifican inadmisibilidad. | valores unitarios, IVA, omision formal, operacion aritmetica | `Errores no esenciales/Omisión de los valores unitarios con IVA.md` |
| 70.019 | 2011 | 08-11-2011 | OPTIMA | La omisión incurrida por la oferente, es de aquéllas susceptibles de ser subsanadas, pues no recae en aspectos esenciales de la licitación pública. | El principio de libre concurrencia busca considerar ofertas de todos los proponentes evitando que errores sin trascendencia y no esenciales queden fuera de concurso. | omisión formal, licitacion publica, error no esencial, subsanacion | `Errores no esenciales/Doc. No esenciales.md` |
| ⚠ 72.362 | 2014 | 17-09-2014 | OPTIMA | De este modo, considerando la normativa y principios citados precedentemente y reconocidos de manera expresa por las bases administrativas de la propuesta pública correspondiente, la empresa recurrente no debió ser marginada de ese proceso. | Omisiones formales no esenciales que no afecten aspectos de evaluación ni rompan el principio de igualdad no justifican la exclusion de ofertas en licitaciones publicas. | errores no esenciales, licitacion publica, principio libre concurrencia, exclusion oferentes | `Errores no esenciales/72.362-2014_ PNF - Formatos diferentes.md` |
| ⚠ 72.362 | 2014 | 17-09-2014 | OPTIMA | La omisión esgrimida reviste un carácter formal y no constituye un error esencial que afecte la validez de la oferta, pues no guarda relación con aspectos objeto de evaluación. | Omisiones formales no esenciales que no sean vinculadas a aspectos de evaluacion no justifican marginacion de oferentes de procesos licitatorios. | error no esencial, omision formal, validez oferta, licitacion publica | `Errores no esenciales/Errores no esenciales.md` |
| - | 2002 | 20-10-2002 | OPTIMA | La inobservancia de las formalidades producirá la ineficacia de la propuesta de un oferente, sólo en la medida que se constate que realmente la omisión tipificada cause desmedro a los derechos del Estado. | Errores intrascendentes o no esenciales no constituyen causal suficiente para rechazar postulaciones en procesos concursales si no afectan aspectos de evaluación o principios de igualdad. | error no esencial, analisis precio unitario, desmedro estado, principio igualdad | `Errores no esenciales/Error no esencial.md` |
| - | 2019 | 26-03-2019 | OPTIMA | La toma de razón es un control obligatorio de juridicidad que se efectúa sobre los actos que deben ser tramitados ante la Contraloría General por tratar materias consideradas esenciales. | Exencion de toma de razon aplicable a actos sobre materias no esenciales conforme facultades del Contralor General para dictar disposiciones fundadas. | toma de razon, materias esenciales, exencion, control juridicidad | `Errores no esenciales/Res. 7 CGR (Nva 1600).md` |
| - | 2019 | 27-03-2019 | OPTIMA | Los siguientes actos quedarán sujetos a toma de razón en los casos que se indica, determinando montos en unidades tributarias mensuales. | Montos minimos en UTM establecen umbrales a partir de los cuales actos administrativos se someten a control de toma de razon segun materias. | montos UTM, toma de razon, transferencias recursos, contratacion | `Errores no esenciales/Res. 8 CGR (Fija montos para Nva 1600).md` |

### Estricta Sujecion a las Bases  (3 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 32.073 | 2013 | 24-05-2013 | OPTIMA | Cabe concluir que la decisión adoptada se ajustó a derecho, debiendo desestimarse el reclamo del interesado. | Las bases constituyen la principal fuente de derechos y obligaciones en procesos concursales; su incumplimiento configura inadmisibilidad. | certificado, previsionales, bases, inadmisibilidad | `Estricta Sujecion a las Bases/PESB - Certificado de Ob. Previsionales.md` |
| 54.426 | 2007 | 30-11-2007 | OPTIMA | No se advierte ilegalidad en la circunstancia de que las ofertas hayan excedido el monto del presupuesto oficial. | Las incongruencias en las bases pueden solucionarse mediante interpretación armónica de las mismas bases. | incongruencias, presupuesto referencial, interpretación armónica, oferta mayor | `Estricta Sujecion a las Bases/54.426-2007_ Incongruencias bases se salvan con mismas bases.md` |
| - | - | - | PARCIAL | - | - | cronograma, modificación, acto distinto | `Estricta Sujecion a las Bases/Mod de cronograma por acto distinto al que las aprobo.md` |

### Evaluacion  (45 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 298 | 2008 | 04-01-2008 | OPTIMA | Esta Contraloría General ha debido abstenerse de dar curso a resolución N° 322, de 2007, que aprueba el contrato celebrado entre la Dirección General de Aeronáutica Civil y la empresa EMFLO | La omisión de requisitos mínimos de admisibilidad en la apertura debe resultar en declaración de inadmisibilidad, no en subsanación posterior vía información anterior. | requisitos admisibilidad, apertura ofertas, igualdad oferentes, bases administrativas | `Evaluacion/www.contraloria.cl_LegisJuri_DictamenesGeneralesMunicipales.md` |
| ⚠ 1395 | 2021 | 25-06-2021 | OPTIMA | la adjudicación cuestionada no se ajustó a derecho | La entidad licitante debe aceptar la propuesta más ventajosa según los criterios establecidos en las bases; desviarse de ello vulnera el principio de estricta sujeción a las bases | adjudicación arbitraria, criterios de evaluación, estricta sujeción a bases | `Evaluacion/1.395-2021_ No se apega a criterios de las bases.md` |
| ⚠ 3117 | 2015 | 13-01-2015 | OPTIMA | la Municipalidad de Melipilla debe ajustar en lo sucesivo su actuar a la jurisprudencia administrativa vigente | Cuando las bases establecen un presupuesto disponible, las ofertas que lo superen deben ser declaradas inadmisibles. | presupuesto, licitaciones, inadmisibilidad, bases | `Evaluacion/Mas del ppto DISPONIBLE NO.md` |
| 4797 | 2017 | 09-02-2017 | OPTIMA | la decisión de FONASA de declarar inadmisible la oferta del recurrente y aceptar la del proponente adjudicado se ajusta a lo previsto en la ley N° 19.886 | Las ofertas que no cumplen los requisitos específicos de forma establecidos en las bases pueden ser declaradas inadmisibles | plazo de ejecución, formato especificado, estricta sujeción | `Evaluacion/ESB.md` |
| ⚠ 6810 | 2018 | 09-03-2018 | OPTIMA | se representa la resolución del rubro | La etapa de aclaraciones debe otorgarse en igualdad de condiciones a todos los oferentes; no puede beneficiarse a un oferente en particular sin dar oportunidad a los demás | aclaraciones, igualdad de oferentes, principio de estricta sujeción | `Evaluacion/6.810-2018 - Aclaraciones a todos.md` |
| ⚠ 7948 | 2018 | 22-03-2018 | OPTIMA | la empresa recurrente no debió ser marginada de ese proceso, por lo que se rechaza la solicitud de reconsideración presentada por el recurrente | Incluir IVA en el precio cuando las bases exigen valor neto es un error formal sin trascendencia que puede determinarse por simple operación matemática. | precios, IVA, errores formales, ofertas | `Evaluacion/79.48-2018 - Precios neto y bruto.md` |
| ⚠ 11358 | 2017 | 04-04-2017 | OPTIMA | se representa el instrumento señalado | Las bases tipo deben incorporar las modificaciones efectuadas por decreto vigentes antes de la convocatoria del proceso concursal. | licitaciones, toma de razón, bases administrativas, requisitos formales | `Evaluacion/011358N17 - Acta Fundada2.md` |
| ⚠ 17585 | 2018 | 12-07-2018 | OPTIMA | no procedió que se invalidara la adjudicación dispuesta a través de la aludida resolución exenta N° 3.070, como se hizo, pues ésta última ya había producido todos sus efectos | Cuando la contratación se perfecciona con la emisión y aceptación de orden de compra, la invalidación posterior no procede pues nacen derechos y obligaciones consolidados. | contratos, adjudicación, invalidación, perfeccionamiento | `Evaluacion/17.585-2018 - Excepcion en dejar vacio item oferta.md` |
| 20678 | 2014 | 21-03-2014 | OPTIMA | resulta improcedente que se haya declarado inadmisible la oferta por haber superado el presupuesto oficial, toda vez que dicho presupuesto no fue fijado como límite máximo | Si las bases no establecen el presupuesto oficial como límite máximo vinculante, las ofertas que lo exceden no pueden ser rechazadas por esa causa | presupuesto oficial, información referencial, admisibilidad oferta | `Evaluacion/Mas del ppto estimado OK.md` |
| 24469 | 2012 | 26-04-2012 | OPTIMA | este Órgano de Control no advierte reproche que formular acerca de lo resuelto por la Administración en el proceso concursal de que se trata | La evaluación de ofertas conforme a los criterios de evaluación establecidos en las bases constituye aspectos cuyo mérito y conveniencia competen a la Administración, sin perjuicio del control jurídico de la Contraloría | experiencia, requisitos mínimos, descalificación, evaluación técnica | `Evaluacion/024469N12 - Acta fundada.md` |
| ⚠ 29281 | 2013 | 13-05-2013 | OPTIMA | no se ajustó a derecho que el Gobierno Regional de Magallanes haya autorizado la adjudicación | Las ofertas que exceden el monto disponible especificado en las bases deben ser declaradas inadmisibles; debe convocarse a nuevo proceso si se modifica el presupuesto | presupuesto máximo, monto disponible, nueva licitación | `Evaluacion/Mas del ppto estimado NO.md` |
| ⚠ 31433 | 2018 | 18-12-2018 | OPTIMA | la Dirección Nacional de Logística de Carabineros de Chile se ajustó al tenor de las bases que rigieron la respectiva licitación al declarar inadmisible la propuesta técnica | Las ofertas que no cumplen con los requisitos técnicos mínimos establecidos en las bases deben ser declaradas inadmisibles | admisibilidad, requisitos técnicos mínimos, propuesta técnica | `Evaluacion/31.433-2018_ Inad si no cumple req tec min.md` |
| 31725 | 2013 | 23-05-2013 | OPTIMA | la declaración de inadmisibilidad de la oferta de la empresa Fenty Gourmet Ltda., se ajustó a derecho, por cuanto dicha empresa señaló en su propuesta un valor neto distinto al ingresado al portal www.mercadopúblico.cl | Cuando las bases establecen que debe prevalecer el valor del portal en caso de discrepancia, la oferta que consigne valores distintos en el formulario y el portal es inadmisible. | ofertas económicas, discrepancia valores, portal mercado público, inadmisibilidad | `Evaluacion/31.725-2013, valor portal distinto anexo oferta, inadmisible.md` |
| 37397 | 2017 | 04-12-2014 | OPTIMA | se reconsidera el dictamen N° 2.785, de 2014, en los términos expuestos y se envían los antecedentes a la División de Auditoría Administrativa de este Organismo de Fiscalización para que pondere la procedencia de investigar si se encuentra comprometida la responsabilidad administrativa de los funcionarios en la demora | El retraso injustificado de la Administración en la tramitación del acto administrativo que perfecciona el contrato genera desequilibrio económico que debe restituir la Administración. | equilibrio económico, retraso, tramitación, reajustabilidad | `Evaluacion/37.397-2017_ Retraso en evaluacion rompe equilibrio economico. Perjuicios a trib.md` |
| 37397 | 2017 | 20-10-2017 | OPTIMA | procede que esa repartición ajuste su actuación al criterio antes señalado, para lo cual deberá considerar el período posterior al vencimiento del plazo contemplado en el citado artículo 86 | Si la demora en la tramitación de la adjudicación excede los 60 días permitidos por responsabilidad de la Administración, ésta debe restablecer el equilibrio económico de las prestaciones | demora en evaluación, equilibrio económico, reajuste de oferta | `Evaluacion/37.397-2017_ Retraso en evaluacion rompe equilibrio economico (6 meses).md` |
| 37405 | 2017 | 20-10-2017 | OPTIMA | no resulta procedente reajustar el precio de la oferta de que se trata | Si el contratista expresa voluntaria y expresamente su intención de mantener el valor de la propuesta a pesar de la demora, no procede exigir el reajuste de oferta | equilibrio económico, consentimiento, mantención de oferta | `Evaluacion/37.405-2017_ Retraso Eval. rompe EE, pero no se reajusta of si consiente ex mantenerla.md` |
| 37409 | 2017 | 20-10-2017 | OPTIMA | procede que esa dirección, en coordinación con la entidad mandante, y teniendo presente el criterio antes reseñado, arbitre las medidas tendientes a efectuar la actualización de la oferta adjudicada | Cuando la adjudicación se dilata más allá de 60 días por causas atribuibles a la Administración, corresponde actualizar el precio de la oferta para mantener el equilibrio económico. | obras públicas, actualización de precio, demora adjudicación, equilibrio | `Evaluacion/37.409-2017_ Retraso en evaluacion rompe equilibrio economico (9 meses).md` |
| 37412 | 2017 | 20-10-2017 | OPTIMA | esa repartición deberá efectuar la actualización de la oferta adjudicada, considerando para tales efectos el período posterior al del vencimiento del plazo establecido en el referido artículo 86 | La demora en evaluación que supera los 60 días por responsabilidad administrativa genera obligación de actualizar el precio de la oferta | demora en evaluación, actualización de precio, equilibrio económico | `Evaluacion/37.412-2017_ Retraso en evaluacion rompe equilibrio economico (9 meses).md` |
| 37515 | 2017 | 23-10-2017 | OPTIMA | procede que esa dirección, en coordinación con la entidad mandante, y teniendo presente el criterio antes reseñado, arbitre las medidas tendientes a efectuar la actualización de la oferta adjudicada | El retraso administrativo más allá de 60 días genera desequilibrio económico que debe ser compensado mediante actualización del precio ofertado. | licitaciones, equilibrio económico, demora, actualización | `Evaluacion/37.515-2017_ Retraso en evaluacion rompe equilibrio economico (7 meses).md` |
| ⚠ 39705 | 2013 | 25-06-2013 | OPTIMA | los vicios de forma no tienen la aptitud de afectar la validez del procedimiento, pues no modifican el resultado del proceso licitatorio | Los errores no esenciales en la evaluación que no alteran el resultado final no vician el procedimiento licitatorio | errores no esenciales, defectos de forma, validez procedimiento | `Evaluacion/39.705-2013_ Si hay error pero no cambia el tenor de la evaluación, vale igual.md` |
| ⚠ 41236 | 2017 | 24-11-2017 | OPTIMA | de los antecedentes tenidos a la vista, no se aprecia en la especie la irregularidad denunciada por el peticionario, puesto que la comisión evaluadora se ajustó al pliego de condiciones respecto de los aspectos impugnados | Cuando las bases especifican que en caso de diferencias prevalece el precio indicado en el portal, la comisión debe considerar ese criterio en la evaluación. | evaluación ofertas, precio portal, bases administrativas, criterios | `Evaluacion/41.236-2017, valor portal distinto anexo oferta, lo que digan las bases.md` |
| 42421 | 2001 | 14-11-2001 | OPTIMA | excluir a la sociedad Con Pax S.A., por aplicación del punto 5.5 de las bases administrativas especiales particulares resulta contrario a las reglas del concurso | Las enmiendas formales intrascendentes en formularios de oferta no son causa de exclusión si no afectan el monto u esencia de la propuesta. | enmiendas, formularios, suma alzada, ofertas | `Evaluacion/Modificacion Formulario.md` |
| ⚠ 45041 | 2017 | 28-12-2017 | OPTIMA | procede que la referida Dirección adopte las medidas tendientes a retrotraer el proceso al momento de la evaluación de la oferta del recurrente | La presentación de anexos en formato distinto al especificado (Word en lugar de Excel) constituye un defecto formal no esencial cuando la información está disponible | defectos formales, formato documento, información disponible | `Evaluacion/45.041-2017 Se pidio pdf, subio word, no vicia.md` |
| 49409 | 2012 | 13-08-2012 | OPTIMA | procede que el Servicio de Vivienda y Urbanización de la Región de Valparaíso actualice la oferta de Equipos y Construcciones S.A., considerando para ello el periodo comprendido entre la fecha de presentación de la misma y aquélla en que se le adjudicó el contrato | La demora en la adjudicación por causas atribuibles a la Administración genera derecho a actualizar el precio de la oferta según el período de retraso. | equilibrio económico, actualización oferta, contratación, principios rectores | `Evaluacion/49.409-2012_ Retraso en evaluacion rompe equilibrio economico (primero).md` |
| ⚠ 51404 | 2016 | 12-07-2016 | OPTIMA | no se advierten inconvenientes para la sustitución del instrumento que garantiza el fiel y oportuno cumplimiento de los contratos | La sustitución de instrumentos de garantía es procedente si cumplen con los requisitos del artículo 68 del DTO 250, aplicando criterio finalista sobre la rigidez formal | garantías, cauciones, sustitución, criterio finalista | `Evaluacion/ESB - Criterio Finalista.md` |
| ⚠ 52709 | 2011 | 22-08-2011 | OPTIMA | el asignar puntaje en materia de contratación de discapacitados únicamente a empresas domiciliadas en Chile, como se prescribe, sin que conste la existencia de un elemento relevante que permita tal diferenciación respecto de los proveedores domiciliados en el extranjero atenta contra el principio de trato igualitario de los oferentes | Los criterios de evaluación deben ser de aplicación general y no establecer diferenciaciones arbitrarias entre oferentes. | igualdad, oferentes, criterios, principios | `Evaluacion/Igualdad Oferentes - Definicion.md` |
| ⚠ 61067 | 2016 | 18-08-2016 | OPTIMA | el municipio deberá adoptar las medidas necesarias a fin de evitar la reiteración de situaciones como la acontecida | Un criterio que limita la competencia económica rechazando ofertas por ser inferiores a un porcentaje mínimo del presupuesto contraviene principios de eficiencia y ahorro. | competencia económica, principios, evaluación, experiencia | `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md` |
| ⚠ 61067 | 2016 | 18-08-2016 | OPTIMA | al restringir la competencia respecto del factor económico, impide alcanzar la combinación más ventajosa entre todos los beneficios del servicio y sus costos asociados | Criterios que establecen límites mínimos a las ofertas económicas contravienen principios de eficiencia y ahorro en contratación pública. | criterios evaluación, presupuesto, principios, eficiencia | `Evaluacion/Criterio que limita precio minimo NO!.md` |
| ⚠ 61067 | 2016 | 18-08-2016 | OPTIMA | se desestima este aspecto de la denuncia | La evaluación de experiencia de oferentes mediante fórmulas comparativas entre participantes es procedente como criterio técnico | experiencia, criterios técnicos, fórmula comparativa | `Evaluacion/MERITO! Eval. Experiencia.md` |
| 63418 | 2014 | 18-08-2014 | OPTIMA | no cabe sino concluir que en la especie no resulta procedente que la Municipalidad de La Florida otorgue una concesión para la prestación del servicio de recolección de residuos sólidos domiciliarios a través del contrato de transacción | Las concesiones municipales deben otorgarse mediante licitación pública según lo establece la ley, no a través de transacción. | concesiones, transacción, municipalidades, licitación | `Evaluacion/Mas del ppto estimado.md` |
| 65942 | 2013 | 14-10-2013 | OPTIMA | CENABAST deberá arbitrar las medidas para subsanar tales defectos, dictando la respectiva resolución que declare la inadmisibilidad de la oferta y fundiéndola en términos tales que permita determinar por sí sola de qué manera la propuesta no dio cumplimiento a los requerimientos establecidos | La declaración de inadmisibilidad debe realizarse a través de un acto administrativo fundado que especifique qué requerimientos no cumplió la oferta. | inadmisibilidad, ofertas, evaluación, fundamentación | `Evaluacion/065942N13 - Acta Fundada3.md` |
| 66064 | 2016 | 06-09-2016 | OPTIMA | CONICYT deberá arbitrar las medidas para establecer criterios objetivos a fin de evitar que los puntajes de los postulantes se alteren | La reevaluación por cambio de evaluadores debe mantener coherencia en los criterios de puntuación para resguardar la equidad entre participantes | reevaluación, evaluadores, consistencia puntaje | `Evaluacion/66.064-2016_ Orden de los factores no altera, reclamo.md` |
| 68010 | 2012 | 30-10-2012 | OPTIMA | la omisión de los valores unitarios con IVA en la oferta del proveedor, reviste un carácter formal y no constituye un error esencial | La omisión de valores unitarios con IVA es un defecto formal no esencial si se pueden calcular mediante operación aritmética simple con datos disponibles | defecto formal, valores unitarios, IVA | `Evaluacion/Omisión de los valores unitarios con IVA.md` |
| 70019 | 2011 | 08-11-2011 | OPTIMA | la omisión incurrida por la oferente, es de aquéllas susceptibles de ser subsanadas, pues no recae en aspectos esenciales de la licitación pública | Las omisiones formales que no afecten aspectos objeto de evaluación pueden ser subsanadas si las bases administrativas lo contemplan expresamente. | errores formales, requisitos, libre concurrencia, no formalización | `Evaluacion/Doc. No esenciales.md` |
| ⚠ 71923 | 2013 | 06-11-2013 | OPTIMA | ninguna de las ofertas hechas por las personas individualizadas en el párrafo precedente debió ser evaluada -ni menos, adjudicada-, toda vez que las bases de licitación que regularon el procedimiento concursal de que se trata no previeron la posibilidad de solicitar la presentación de certificaciones o antecedentes omitidos | Si las bases no prevén expresamente la facultad de requerir antecedentes omitidos, las ofertas que no adjunten documentos requeridos deben ser declaradas inadmisibles sin posibilidad de subsanación posterior. | inadmisibilidad, documentos, requisitos, admisibilidad | `Evaluacion/71.923-2013_ Debio subir F30, no lo hizo, inadmisible.md` |
| ⚠ 72362 | 2014 | 17-09-2014 | OPTIMA | la empresa recurrente no debió ser marginada de ese proceso | Los defectos formales no esenciales que no incidan en aspectos de fondo no justifican la exclusión de una propuesta del proceso licitatorio | defectos formales, exclusión, principio libre concurrencia | `Evaluacion/Errores no esenciales.md` |
| ⚠ 73183 | 2013 | 12-11-2013 | OPTIMA | el referido error no es esencial por estimar que el error en la glosa no impiden identificar el proceso licitatorio ni la oferta a la que corresponde la caución | errores no esenciales en bases de licitación no justifican rechazo de propuestas cuando no impiden identificar el proceso ni la oferta | licitación, error formal, glosa garantía, seriedad oferta | `Evaluacion/ESB - Error en glosa no esencial.md` |
| 73638 | 2015 | 15-09-2015 | OPTIMA | esta Sede de Control no advierte reproche que formular en torno a lo obrado por la Municipalidad de San José de Maipo sobre la materia | Si las bases establecen el presupuesto como monto referencial y permiten suplementar hasta 10%, una oferta que supere ese tope pero se autorice por mandante es admisible. | presupuesto estimativo, suplemento, autorización, adjudicación | `Evaluacion/Mas del ppto estimado OK si no esta en base limite.md` |
| ⚠ 74523 | 2015 | 17-09-2015 | OPTIMA | esta Contraloría General no advierte irregularidades en la evaluación de las ofertas antes descrita | La aclaración de ofertas no puede permitir la modificación de propuestas; una respuesta que implique contraoferta es improcedente | aclaraciones, modificación de oferta, contraoferta | `Evaluacion/74.523-2015_ Mod. Oferta no se puede.md` |
| ⚠ 77815 | 2016 | 21-10-2016 | OPTIMA | corresponde a la entidad licitante asignar los puntajes a las ofertas conforme lo prevean las bases administrativas | La evaluación de criterios técnicos y la asignación de puntajes corresponde a la Administración conforme a las bases; estos aspectos de mérito no son revisables por la Contraloría | criterios técnicos, puntajes, mérito administrativo | `Evaluacion/Merito.md` |
| ⚠ 84937 | 2016 | 23-11-2016 | OPTIMA | se mantiene la observación que sobre la materia mencionada se efectuó en el dictamen N° 26.069, de 2016 | La comisión evaluadora debe fundamentar expresamente los motivos por los cuales rechaza antecedentes presentados para acreditar experiencia | experiencia, fundamentación evaluación, acta evaluación | `Evaluacion/Debe indicar mot rech experiencia.md` |
| 89409 | 2016 | 13-12-2016 | OPTIMA | esta sede de control no tiene reproches que formular al respecto | La elección de criterios de evaluación, su ponderación y asignación de puntajes es facultad de los órganos de la Administración activa. | criterios evaluación, méritos, títulos profesionales, experiencia | `Evaluacion/Merito2.md` |
| 90883 | 2015 | 16-11-2015 | OPTIMA | esta Contraloría General en el estudio de legalidad que realiza de los actos que adjudican contratos, no puede dejar de examinar si la Administración ha dado cumplimiento a dicha jurisprudencia | Los defectos formales menores que no afectan el análisis de fondo de las propuestas no deben causar exclusión del proceso | defectos formales menores, criterios uniformes evaluación | `Evaluacion/Calculo.md` |
| - | 2009 | - | OPTIMA | la sugerencia formulada por la Comisión de Evaluación en orden a declarar fuera de bases a todas las empresas oferentes, no se ajusta a derecho | Los errores intrascendentes o no esenciales no constituyen causal suficiente para rechazar postulaciones en procesos concursales. | ofertas, evaluación, errores, razonabilidad | `Evaluacion/Error no esencial.md` |
| - | - | - | PARCIAL | - | - |  | `Evaluacion/Mod de cronograma por acto distinto al que las aprobo.md` |

### Experiencia  (6 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 10.957 | 2017 | 30-03-2017 | OPTIMA | La remisión que se hace debe entenderse efectuada al número correcto y no como aquí se indica, con los alcances que anteceden. | Requisitos de experiencia no deben restringir participacion estableciendo inhabilidades no reconocidas en ordenamiento juridico vulnerando principio libre concurrencia. | experiencia, licitacion publica, libre concurrencia, inhabilidades | `Experiencia/10957-2017.md` |
| 11.409 | 2018 | 04-05-2018 | OPTIMA | No se encuentra debidamente fundada la nota que la comisión de evaluación asignó en el factor 'Experiencia del Oferente'. | Evaluacion de experiencia de oferentes debe estar fundada en antecedentes verificables y no puede considerar periodos menores o certificados de terceros sin explicacion. | experiencia oferente, evaluacion fundada, mezcla asfaltica, licitacion publica | `Experiencia/11.409-2018, Exp. Fundada.md` |
| ⚠ 14.200 | 2018 | 07-06-2018 | OPTIMA | Aquellos oferentes que no posean la experiencia en los términos exigidos se evaluarán con 0 punto. | La experiencia puede evaluarse conforme criterios objetivos pero no puede ser requisito de admisibilidad respetando principio libre concurrencia. | experiencia, criterio evaluacion, libre concurrencia, telecomunicaciones | `Experiencia/14.200-2018.md` |
| ⚠ 44.460 | 2010 | 05-08-2010 | OPTIMA | Las entidades licitantes podrán considerar como experiencia del oferente la de su equipo gestor, personal profesional o sociedades que la integran si las bases lo permiten. | Experiencia de sociedad filial no se transfiere automaticamente de sociedad matriz pues son personas juridicas distintas; transferencia posible solo si bases lo permiten expresamente. | experiencia, sociedades filiales, traspaso experiencia, licitacion publica | `Experiencia/44.460-10_ Experiencia sociedades filiales.md` |
| 49.345 | 2016 | 04-07-2016 | OPTIMA | No se ajustó a derecho lo obrado por la referida comisión evaluadora al determinar la exclusión de oferentes en razón de que no habrían acreditado adecuadamente la experiencia. | La experiencia es factor de evaluacion no requisito de admisibilidad; certificados de mandantes constituyen acreditacion valida si contienen información solicitada. | experiencia empresa, certificados mandantes, recepciones municipales, evaluacion | `Experiencia/49.345-2016.md` |
| ⚠ 61.067 | 2016 | 18-08-2016 | OPTIMA | La experiencia del proponente era considerada por las bases como un factor para calificar las ofertas y no como un requisito mínimo para postular. | Formula de evaluacion experiencia basada en comparacion entre oferentes es valida si experiencia es factor evaluacion y no requisito admisibilidad. | experiencia, criterio evaluacion, licitacion publica, principios eficiencia | `Experiencia/61067-2016.md` |

### Foro Inverso  (18 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 6.810 | 2018 | 09-03-2018 | OPTIMA | Se representa la resolución del rubro. | No es procedente solicitar vía foro inverso información relativa a requisito mínimo pues confiere ventaja al oferente seleccionado y vulnera igualdad; rechazada oferta de otro por no presentar igual información, se produce trato discriminatorio. | foro inverso, igualdad oferentes, requisitos mínimos | `Foro Inverso/6.810-2018_ Igualdad de los oferentes, exclusion.md` |
| ⚠ 11.274 | 2018 | 03-05-2018 | OPTIMA | En consecuencia, no observándose irregularidades respecto de lo obrado por la mencionada entidad licitante, procede desestimar el reclamo de la peticionaria. | La modificación de bases mediante foro inverso es facultad legítima de la DCCP cuando se realiza antes del plazo de presentación de ofertas y se informa por el portal Mercado Público; los oferentes tienen obligación de consultar el foro inverso para tomar conocimiento de aclaraciones. | foro inverso, modificación de bases, convenio marco | `Foro Inverso/11.274-2018_ Ob. consultar foro inverso del proveedor.md` |
| 11.400 | 2017 | 04-04-2017 | OPTIMA | En consecuencia, corresponde a la Administración activa, en este caso al Ministerio de Defensa Nacional, decidir acerca de suspender o no los efectos de un acto administrativo en el marco de un procedimiento de impugnación. | Los recursos administrativos no suspenden efectos de actos administrativos a menos que la autoridad competente disponga expresamente su suspensión conforme a los supuestos del artículo 57 inc. 2 Ley 19.880. | suspensión de actos, recurso administrativo, concesión marítima | `Foro Inverso/11.400-2017_ Suspensión del acto.md` |
| ⚠ 14.238 | 2018 | 07-06-2018 | OPTIMA | La Corporación de Fomento de la Producción deberá iniciar un procedimiento de invalidación conforme con lo previsto en el inciso primero del artículo 53 de la ley N° 19.880. | Las aclaraciones vía foro inverso no pueden traducirse en modificación de la propuesta ya presentada, pues constituye contraoferta que afecta igualdad de oferentes; debe rechazarse solicitud de aclaraciones que requiera información evaluable que no haya sido presentada. | igualdad de oferentes, foro inverso, invalidación | `Foro Inverso/14.238-2018_ Igualdad de los oferentes, que no hacer.md` |
| ⚠ 18.889 | 2018 | 26-07-2018 | OPTIMA | En consecuencia, en mérito de lo expuesto, se desestima el reclamo del rubro. | La asignación de puntajes se ajusta a bases cuando la comisión evaluadora aplica criterios uniformemente a todos los oferentes; si una práctica de no solicitar documentos es uniforme, no afecta el igual tratamiento ni vulnera principios de estricta sujeción. | evaluación técnica, puntajes, foro inverso | `Foro Inverso/18.889-2018_ Igualdad, foro inverso.md` |
| ⚠ 19.265 | 2013 | 01-04-2013 | OPTIMA | De este modo, si en la misma resolución de adjudicación no se indican las ofertas inadmisibles, la respectiva declaración de inadmisibilidad debe contenerse en otro acto administrativo fundado que así lo exprese. | Las aclaraciones vía foro inverso deben respetar trato igual de todos los oferentes; no es procedente otorgar plazos distintos para presentar certificados omitidos según oferente, ni hacer efectivo un certificado omitido de plazo vencido. | aclaraciones foro inverso, igualdad oferentes, convenio marco | `Foro Inverso/19.265-2013_ FI, ley pareja.md` |
| 22.161 | 2017 | 16-06-2017 | OPTIMA | La Municipalidad de Puerto Octay deberá arbitrar las medidas que resulten pertinentes para invalidar el referido acto de adjudicación. | Las aclaraciones a través de foro inverso no pueden traducirse en modificación de propuesta ya presentada; cuando la aclaración resulta en cambio de monto ofertado, constituye contraoferta que vulnera igualdad de oferentes. | foro inverso, contraoferta, concesión | `Foro Inverso/22.161-2017_ FI no es posibilidad de contraoferta.md` |
| ⚠ 25.674 | 2017 | 12-07-2017 | OPTIMA | La omisión respectiva no constituye un aspecto meramente formal que pueda ser subsanado por esa vía y sólo suponga la rebaja en el criterio de cumplimiento de requisitos formales. | Los requisitos evaluables no pueden ser solicitados como aclaraciones vía foro inverso si su presentación tardía conferiría privilegio a un oferente; debe rechazarse el documento no cumplidor de exigencias formales sin oportunidad de corrección. | foro inverso, requisitos evaluables, buenas prácticas manufactura | `Foro Inverso/25.674-2017_ Foro Inverso, antecedente que no cumple.md` |
| ⚠ 29.349 | 2017 | 09-08-2017 | OPTIMA | Corresponde que el SSVQ disponga las medidas de control pertinentes a fin de evitar que situaciones como la previamente señalada se repitan en lo sucesivo. | Pueden admitirse aclaraciones vía foro inverso de antecedentes referidos a situaciones no mutables entre cierre de ofertas y evaluación; estados financieros y autorizaciones notariales legalizado después no alteran su contenido sustancial. | foro inverso, situaciones no mutables, libre concurrencia | `Foro Inverso/29.349-2017_ Foro inverso, no mutables.md` |
| ⚠ 36.248 | 2016 | 17-05-2016 | OPTIMA | Por lo tanto, la oferta de Auter S.A. se ajustó, en los aspectos señalados precedentemente, a los requisitos establecidos en el pliego de condiciones. | Es procedente solicitar vía foro inverso un documento requerido en bases que no sea objeto de evaluación; complementar un antecedente no evaluable no confiere ventaja si la información evaluable ya estaba en la oferta original. | foro inverso, antecedentes no evaluables, carta gantt | `Foro Inverso/36.248-2016_ FI, complemenatción de antecedentes no evaluables.md` |
| ⚠ 41.236 | 2017 | 24-11-2017 | OPTIMA | En consecuencia, de los antecedentes tenidos a la vista, no se aprecia en la especie la irregularidad denunciada por el peticionario. | Es procedente solicitar complementación formal vía foro inverso de omisiones que no afecten criterios de evaluación; si la información evaluable estuvo presente en la oferta original, no se vulnera igualdad. | vicio formal, ascensores, foro inverso | `Foro Inverso/41.236-2017_ Def. Vicio Formal.md` |
| 42.462 | 2011 | 06-07-2011 | OPTIMA | No cabe, por consiguiente, respecto del punto que se estudia, que la Administración entre a evaluar si los antecedentes que presentan los proponentes son equivalentes o no a los exigidos por las bases. | Cuando el reglamento y bases elevan expresamente al carácter de esencial la omisión de un antecedente, no procede ponderarlo como infracción meramente formal ni evaluar si otros documentos acompañados serían equivalentes. | requisitos esenciales, omisión de antecedentes, obras públicas | `Foro Inverso/42.462-2011_ Reqs formales elevados a esenciales, bases.md` |
| ⚠ 53.300 | 2016 | 18-07-2016 | OPTIMA | Esta Contraloría General ha dado curso a las resoluciones del epígrafe, que aprueban las bases administrativas, técnicas y anexos para adquisición de los bienes que en cada caso se indican, por cuanto se ajustan a derecho. | La posibilidad de rectificar antecedentes vía foro inverso no dice relación con aquellos que son evaluables; no deben solicitarse aclaraciones de documentos evaluables cuya presentación tardía conferiría ventaja. | foro inverso, antecedentes evaluables, bases administrativas | `Foro Inverso/53.300-2016_ FI no pa pedir evaluables.md` |
| 66.909 | 2015 | 21-08-2015 | OPTIMA | Se representa el decreto N° 1.692, de 2015, de la Universidad de Santiago de Chile. | No procede solicitar vía foro inverso documento esencial que no fue acompañado en oferta original, pues confiere oportunidad de subsanación solo a algunos oferentes; requisitos esenciales deben estar presentes en oferta inicial. | foro inverso, requisitos esenciales, obras públicas | `Foro Inverso/66.909-2015_ Se pide esencial por foro inverso.md` |
| 67.555 | 2015 | 24-08-2015 | OPTIMA | Se representa la resolución N° 922, de 2015, de la Junta Nacional de Jardines Infantiles. | Cuando se solicita aclaración vía foro inverso de documentos evaluables que fueron omitidos inicialmente, debe descuentosobre puntaje formal; no procede asignar puntaje máximo si hubo incumplimiento de requisito. | foro inverso, puntaje formal, obras públicas | `Foro Inverso/67.555-2015_ FI, necesidad de descontar ptje.md` |
| 67.557 | 2015 | 24-08-2015 | OPTIMA | Se representa la resolución N° 919, de 2015, de la Junta Nacional de Jardines Infantiles. | Cuando se solicita vía foro inverso rectificación de itemizados tras evaluación inicial, procede descuentar puntaje en criterio formal; no debe asignarse puntaje máximo si hubo incumplimiento que requirió aclaración. | foro inverso, puntaje formal, obras públicas | `Foro Inverso/67.557-2015_ FI, necesidad de descontar ptje.md` |
| ⚠ 74.223 | 2016 | 07-10-2016 | OPTIMA | En mérito de lo expuesto, y teniendo presente, además, que el uso del mencionado foro inverso constituye un mecanismo de consulta que, atendidas las circunstancias descritas, en la especie no procedía utilizar, no corresponde acoger la reclamación del rubro. | Cuando oferta contiene información contradictoria que afecta el puntaje en factor de evaluación, confiere privilegio respecto de competidores y hace inadmisible la oferta; no procede foro inverso para aclaración de incoherencia esencial. | inadmisibilidad, foro inverso, plazo ejecución | `Foro Inverso/74.223-2016_ FI no es posibilidad de contraoferta.md` |
| 83.993 | 2016 | 21-11-2016 | OPTIMA | Se representa la resolución N° 109, de 2016, del Servicio de Salud Metropolitano Sur. | No procede solicitar vía foro inverso cuando bases expresamente prohíben requerimiento de información omitida; si bases establecen que omisión resulta en declaración de inadmisibilidad, no hay facultad de aclaración. | foro inverso, normalización, omisión informacion | `Foro Inverso/83.993-2016_ FI, omision de solicitar documentos (Asumo societarios).md` |

### Fragmentacion  (1 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 14.236 | 2018 | 07-06-2018 | OPTIMA | El INDAP deberá iniciar un sumario administrativo destinado a investigar las causas que motivaron la ocurrencia de la irregularidad antes mencionada. | No procede fragmentar compras en múltiples órdenes por montos inferiores a UTM límite con fin de evadir procedimiento de grandes compras; razones de urgencia o financiamiento tardío no justifican vulneración de prohibición de fragmentación. | fragmentacion, grandes compras, convenio marco | `Fragmentacion/14.236-2018, Frag. GC. Ordena sumario.md` |

### Garantias  (23 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 6.365 | 2012 | 01-02-2012 | OPTIMA | Esta Contraloría General estima que la declaración de inadmisibilidad de la oferta de la solicitante, se ajustó a derecho, en tanto ese proponente no mantuvo vigente su boleta de seriedad de la oferta en los términos indicados en las bases. | La garantía de seriedad de la oferta debe renovarse antes de su vencimiento durante todo el proceso de licitación y hasta el décimo día hábil siguiente a la toma de razón del contrato. | inadmisibilidad, renovación garantía, seriedad oferta, prórroga | `Garantias/006365N12 - Inadmisible oferta no entrega GSO.md` |
| 6.365 | 2012 | 01-02-2012 | OPTIMA | Esta Contraloría General estima que la declaración de inadmisibilidad de la oferta de la solicitante, se ajustó a derecho, en tanto ese proponente no mantuvo vigente su boleta de seriedad de la oferta. | No mantener vigente la garantía de seriedad en los términos indicados en las bases constituye causal de inadmisibilidad. | inadmisibilidad, renovación, vigencia, no renovada | `Garantias/6.365-2012_ Inadmisible por no renovación GSO.md` |
| 14.005 | 2011 | 08-03-2011 | OPTIMA | La misma no vicia la propuesta de la recurrente. | El objeto fundamental de la garantía de seriedad es respaldar la actuación de un licitante hasta el momento en que firma el contrato adjudicado. | objetivo garantía, firma contrato, criterio finalista, rigidez formal | `Garantias/14.005-2011_ Objetivo GSO resguardar la firma del contrato.md` |
| 20.341 | 2013 | 04-04-2013 | OPTIMA | Esta Contraloría General considera del caso desestimar las alegaciones de la peticionaria por estimar que los errores invocados no son esenciales. | Los errores no esenciales en la glosa de la garantía de seriedad no afectan aspectos esenciales ni vicien la propuesta si permite identificar el proceso licitatorio. | error glosa, no esencial, identificación proceso, rigidez formal | `Garantias/20.341-2013_ Error en la glosa no esencial GSO.md` |
| 21.246 | 2016 | 18-03-2016 | OPTIMA | Se representa el instrumento de la suma. | Los 180 días corridos de vigencia exigidos se cumplen en el día exacto 180, no posterior. | cálculo plazo, 180 días, vigencia, apertura ofertas | `Garantias/Como calcula plazo - GSO.md` |
| 27.386 | 2018 | 06-11-2018 | OPTIMA | La situación descrita por ese servicio no se enmarca en la causal que habilita para el cobro de la garantía de seriedad en comento. | La falsedad de documentos solo habilita el cobro de la garantía de seriedad si está expresamente prevista como causal en las bases administrativas. | falsedad documentos, cobro garantía, bases, causal | `Garantias/027386N18 - Falsedad de documentos habilita para cobrar GSO cuando esta en bases.md` |
| ⚠ 31.421 | 2018 | 18-12-2018 | OPTIMA | El Centro se ajustó a previsto en el pliego de condiciones al cobrar la garantía de seriedad de la oferta presentada por el recurrente. | Las causales para cobrar la garantía de seriedad deben estar expresamente establecidas en las bases administrativas. | cobro garantía, bases administrativas, causales, estricta sujeción | `Garantias/031421N18- Causales para cobrar GSO deben estar en bases.md` |
| ⚠ 31.798 | 2013 | 23-05-2013 | OPTIMA | No resulta procedente hacer efectivas las boletas de garantía correspondientes a ofertas que han sido declaradas inadmisibles. | Los errores en garantías de seriedad que no son esenciales no vician la propuesta si se respeta el principio de igualdad de oferentes. | error no esencial, garantía seriedad, derechos consolidados, inadmisibles | `Garantias/031798N13 - Error GSO y derechos consolidados.md` |
| ⚠ 37.573 | 2011 | 14-06-2011 | OPTIMA | Este Organismo Fiscalizador no advierte reparos que formular, sin perjuicio de hacer presente que, en todo caso, en la presentación que se atiende no se precisa de qué manera se infringiría el ordenamiento aplicable. | Las bases deben establecer el monto, plazo de vigencia y moneda en que debe expresarse la garantía de seriedad. | monto obligatorio, plazo vigencia, bases, menciones | `Garantias/37.573-2011_ Menciones obligatorias GSO.md` |
| ⚠ 57.470 | 2012 | 14-09-2012 | OPTIMA | Deben estar contenidos en las bases y no sólo en el calendario del llamado publicado en el Sistema de Información de la Dirección de Compras. | Las bases deben establecer expresamente el monto y plazo de vigencia de la garantía de seriedad. | monto, plazo, bases obligatorias, contenido esencial | `Garantias/57.470-2012_ Debe consignarse monto y plazo GSO.md` |
| ⚠ 58.646 | 2013 | 10-09-2013 | OPTIMA | Tal circunstancia no constituye un error de una magnitud tal que afecte la validez de la licitación pública en comento. | El objeto fundamental de la garantía de seriedad es respaldar la actuación del oferente hasta el momento que firma el contrato, permitiendo un criterio finalista que trascienda rigidez formal. | vigencia garantía, criterio finalista, plazo menor, contrato firmado | `Garantias/058646N13 - GSO, doctrina.md` |
| ⚠ 58.646 | 2013 | 10-09-2013 | OPTIMA | Tal circunstancia no constituye un error de una magnitud tal que afecte la validez de la licitación pública en comento. | Un plazo de vigencia menor al exigido en bases es vicio formal si el contrato se firma mientras la garantía está vigente. | plazo menor, vicio formal, contrato firmado, vigencia | `Garantias/58.646-2013_ Plazo menor GSO vicio formal mientras firmen contrato en plazo.md` |
| 68.755 | 2013 | 23-10-2013 | OPTIMA | Debe concluirse que tal circunstancia no constituye un error de una magnitud tal que afecte la validez de la licitación pública en comento. | Los errores no esenciales en la vigencia de la garantía no afectan la validez si el oferente mantuvo su oferta vigente. | error no esencial, vigencia, validez, licitación | `Garantias/68.755-2013_ Error en la glosa no esencial GSO.md` |
| 73.183 | 2013 | 12-11-2013 | OPTIMA | Razón por la cual no debió ser desestimada la oferta del afectado. | No procede rechazar una propuesta por errores no esenciales en la glosa de la garantía si permite identificar el proceso licitatorio. | error glosa, rechazo improcedente, no esencial, identificación | `Garantias/73.183-2013_ Error glosa No esencial, No inadmisible!.md` |
| 84.775 | 2013 | 11-10-2013 | REPARADO_PARCIAL | No corresponde que el Servicio de Salud Metropolitano Central haya hecho efectiva la caución en comento, puesto que el referido cobro no se condice con la naturaleza y el fin de la garantía de seriedad de la oferta. | No procede hacer efectivas boletas de garantía de seriedad cuando las ofertas han sido declaradas inadmisibles. | inadmisibles, cobro prohibido, naturaleza garantía, fin específico | `Garantias/065771N13 - No se puede cobrar GSO a inadmisibles.md` |
| 100.441 | 2015 | 21-12-2015 | OPTIMA | Se ha tomado razón del acto administrativo del epígrafe. | La garantía de seriedad de la oferta puede otorgarse física o electrónicamente y puede ser tomada por el proponente o por un tercero a su nombre. | garantía tercero, nombre oferente, física electrónica, formas | `Garantias/100.441-2015_ Garantia por tercero.md` |
| - | 2017 | 15-05-2017 | BUENA | Con el alcance que antecede se ha tomado razón del acto administrativo del rubro. | La garantía de seriedad puede ser tomada por el oferente o por un tercero a su nombre. | tercero, nombre oferente, tomada a su nombre | `Garantias/17407-2017_ Garantia por tercero.md` |
| - | 2016 | 09-03-2016 | OPTIMA | Saluda atentamente a Ud. | Las garantías de seriedad y de fiel cumplimiento pueden ser tomadas por el proponente o un tercero a su nombre. | tercero, garantía cumplimiento, proponente o tercero | `Garantias/18872-2016_ Garantia por tercero.md` |
| - | 2013 | 17-07-2013 | OPTIMA | El comité de evaluación se ajustó a lo dispuesto en las bases administrativas que se examinan. | La boleta de garantía tomada por tercero debe consignar, además del objeto de la garantía, la individualización del sujeto por quien se rinde. | tercero nombre, individualización, sujeto, requisito formal | `Garantias/45257-2013_ Tercero si, pero debe ser a nombre de el.md` |
| - | 2021 | 15-09-2021 | OPTIMA | No corresponde acoger la reclamación del recurrente. | Los errores en la glosa de la garantía que no impiden identificar el proceso licitatorio no son esenciales. | glosa, error no esencial, identificación, proceso | `Garantias/E139176N21 - Glosa no esencial en GSO.md` |
| - | 2021 | 27-10-2021 | OPTIMA | La decisión adoptada por la Dirección de Compras se ajustó a lo dispuesto en las bases. | Procede declarar inadmisible la oferta cuando la garantía no cumple con la vigencia mínima prevista en las bases modificadas. | inadmisibilidad, vigencia mínima, bases modificadas, convenio marco | `Garantias/E150913N21 - Inadmisibilidad por falta de vigencia GSO.md` |
| - | 2021 | 09-12-2021 | OPTIMA | La decisión adoptada se ajustó a lo dispuesto en las bases que rigieron el proceso concursal. | Procede declarar inadmisible cuando la garantía no cumple la vigencia mínima aunque las bases fueron modificadas. | inadmisibilidad, vigencia mínima, modificación bases, 60 días | `Garantias/E163668N21 - Inadmisibilidad por falta de vigencia GSO.md` |
| - | 2020 | 16-12-2020 | OPTIMA | Se desestima la solicitud de reconsideración deducida por la Municipalidad de San Miguel. | La garantía de seriedad puede otorgarse de forma física o electrónica. | electrónica, forma garantía, física o electrónica, competencia | `Garantias/E60399N20 - Vale GSO electronica.md` |

### Grandes Compras  (31 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 394 | 2014 | 03-01-2014 | OPTIMA | Se ajustó a derecho actuación del Ministerio de Educación que excluyó oferta por incumplimiento de requerimiento técnico mínimo en proceso de gran compra | La entidad pública puede establecer requerimientos técnicos mínimos específicos en la intención de compra para garantizar adecuación a sus necesidades concretas. | grandes compras, requerimientos técnicos, exclusión ofertas, intención compra | `Grandes Compras/GC - Def. de EETT va en la IC 2.md` |
| ⚠ 1.199 | 2019 | 14-01-2019 | OPTIMA | en la medida que los bienes suministrados por la recurrente cumplan con los requerimientos específicos señalados en la intención de compra -con exclusión de sus marcas-, procede que la JUNJI adopte las medidas tendientes a la recepción de los mismos | En grandes compras, las entidades deben comunicar la intención a todos los proveedores adjudicados sin restringir la selección solo a aquellos con productos de marca específica; las marcas solo pueden indicarse de manera referencial. | grandes compras, marcas equivalentes, requerimientos específicos, convenio marco | `Grandes Compras/1.199-2019_ Acepto en evaluacion, rechazo por marca.md` |
| ⚠ 1.199 | 2019 | 14-01-2019 | OPTIMA | al efectuar grandes compras las entidades deben comunicar la intención a todos los proveedores adjudicados en la respectiva categoría, sin que puedan restringir la selección solo a aquellos que, estando allí catalogados, tengan productos de una marca específica | En grandes compras deben invitarse todos los proveedores adjudicados en la categoría; las marcas solo pueden indicarse de manera referencial, permitiendo equivalentes. | grandes compras, marcas equivalentes, invitación proveedores, igualdad | `Grandes Compras/GC - Se invita a todos, aunque no tengan marca.md` |
| ⚠ 4.509 | 2017 | 07-02-2017 | OPTIMA | El Ministerio de Educación se ajustó a derecho al no considerarla en su evaluación, pues la manera en que debía subirse la información requerida fue establecida en la intención de compra | Los anexos de ofertas en grandes compras deben subirse según lo establecido en la intención de compra mediante el módulo correspondiente; no se puede utilizar otro medio. | grandes compras, anexos ofertas, módulo Grandes Compras, intención compra | `Grandes Compras/GC - Anx. deben subirse de acuerdo a IC.md` |
| ⚠ 4.509 | 2017 | 07-02-2017 | OPTIMA | la manera en que debía subirse la información requerida, esto es, la oferta y los anexos, fue establecida en la intención de compra realizada por el MINEDUC | Las ofertas en grandes compras deben presentarse según los medios y procedimientos especificados en la intención de compra. | grandes compras, presentación ofertas, intención compra, módulo Grandes Compras | `Grandes Compras/GC - Of. x portal, como diga IC.md` |
| ⚠ 7.640 | 2013 | 01-02-2013 | OPTIMA | de haberse verificado efectivamente un incumplimiento que dé lugar a una multa por retraso, debe aplicarse la sanción prevista al efecto en las bases administrativas de la propuesta del convenio marco | Las multas por atraso en grandes compras deben aplicarse conforme a las bases del convenio marco; no pueden alterarse sustancialmente mediante términos de referencia especiales. | grandes compras, multas atraso, bases convenio marco, sanciones | `Grandes Compras/GC - Multas del CM aplican.md` |
| ⚠ 12.125 | 2019 | 03-05-2019 | OPTIMA | Carabineros de Chile está obligado a contratar a través de un convenio marco cuando determine que los bienes y servicios que va a adquirir no requieren condiciones técnicas ni de seguridad específicas | Las Fuerzas de Orden y Seguridad Pública están obligadas a usar convenios marco para bienes y servicios que no requieren condiciones técnicas o de seguridad especiales, cuando el monto supera 1.000 UTM. | grandes compras, convenio marco, Carabineros, obligatoriedad | `Grandes Compras/12.125-2019_ Obligacion de CM.md` |
| ⚠ 12.424 | 2017 | 12-04-2017 | OPTIMA | En adquisiciones vía convenio marco los servicios deben pedir que se acredite el cumplimiento de los requisitos para contratar con la administración del Estado previstos en el artículo 4°, inciso sexto, de la ley N° 19.886 | En grandes compras, al emitir la intención de compra o la orden de compra, debe solicitarse acreditación de ausencia de inhabilidades para contratar con el Estado. | grandes compras, inhabilidades, requisitos contratación, convenio marco | `Grandes Compras/GC - Declaracion de inhabilidades.md` |
| ⚠ 13.915 | 2013 | 01-03-2013 | OPTIMA | La entidad deberá seleccionar la oferta más conveniente según resultado del cuadro comparativo que deberá confeccionar sobre la base de los criterios de evaluación y ponderaciones definidas en las bases de licitación del convenio marco | En grandes compras, criterios de evaluación y ponderaciones del convenio marco deben mantenerse; solo ajustes complementarios conciliables con naturaleza del bien son permitidos. | grandes compras, criterios evaluación, cuadro comparativo, bases licitación | `Grandes Compras/GC - Evaluacion, cuadro comparativo.md` |
| ⚠ 18.983 | 2018 | 27-07-2018 | OPTIMA | No procedió que municipalidad fragmentara la compra de los bienes que se indica, pues con ello modificó el procedimiento de contratación que correspondía aplicar | La Administración no puede fragmentar sus contrataciones para eludir el procedimiento de grandes compras cuando el monto total supera 1.000 UTM. | grandes compras, fraccionamiento, prohibición, municipalidad | `Grandes Compras/18.983-2018_ Fracc GC, Municipalidad.md` |
| ⚠ 18.983 | 2018 | 27-07-2018 | OPTIMA | No procedió que municipalidad fragmentara la compra de los bienes que se indica, pues con ello modificó el procedimiento de contratación que correspondía aplicar | La Administración no puede fragmentar compras para evitar el procedimiento de grandes compras; infracción a prohibición de fraccionamiento cuando el monto total supera 1.000 UTM. | grandes compras, fraccionamiento, prohibición, convenio marco | `Grandes Compras/18.983-2018_ Fraccionamiento, CM, grandes compras.md` |
| ⚠ 30.836 | 2019 | 28-11-2019 | OPTIMA | No resultó procedente que la Fuerza Aérea de Chile omitiera, al comunicar la respectiva intención de compra, los requerimientos específicos de las tenidas de combate que adquirió a través del convenio marco | En grandes compras, la intención de compra debe comunicar explícitamente los requerimientos específicos del bien, no solo referencias a fichas de catálogo de un proveedor específico. | grandes compras, requerimientos técnicos, intención de compra, Fuerza Aérea | `Grandes Compras/30.836-2019_ Ob. de comunicar EETT.md` |
| 32.065 | 2013 | 24-05-2013 | OPTIMA | ni la ampliación del plazo de entrega habrían tenido expresión formal en una modificación de contrato, así como tampoco fueron sancionadas por acto administrativo alguno | La posibilidad de modificar plazos en grandes compras debe estar expresamente establecida en la intención de compra y formalizarse por acto administrativo. | grandes compras, plazos entrega, prórroga, modificación contrato | `Grandes Compras/GC - Posibilidad de modificar plazos debe estar en IC.md` |
| ⚠ 36.519 | 2016 | 17-05-2016 | OPTIMA | Actuación del Ministerio de Salud en los procesos de adquisición que indica, a través de grandes compras, se ajustó a derecho | La entidad licitante tiene atribución discrecional para fijar requerimientos técnicos mínimos en la intención de compra conforme a sus necesidades específicas. | grandes compras, especificaciones técnicas, requerimientos mínimos, Ministerio Salud | `Grandes Compras/GC - Def. de EETT va en la IC.md` |
| ⚠ 43.119 | 2014 | 13-06-2014 | OPTIMA | Las ofertas presentadas en un proceso de grandes compras son públicas y no pueden superar el presupuesto disponible | En grandes compras solo pueden ofrecerse bienes o servicios incorporados en el catálogo del convenio marco; las ofertas no pueden exceder presupuesto disponible. | grandes compras, catálogo convenio, presupuesto disponible, bienes catalogados | `Grandes Compras/GC - Si hay 30_ solo a bienes del CM.md` |
| ⚠ 45.237 | 2014 | 20-06-2014 | OPTIMA | Municipalidad de Peñaflor no se ajustó a derecho al establecer criterios de evaluación y ponderaciones distintos de los previstos en las bases de licitación del convenio marco respectivo | Los criterios de evaluación y ponderaciones en grandes compras no pueden alterarse sustancialmente; solo cambios complementarios para adaptar a naturaleza del bien son permitidos. | grandes compras, criterios de evaluación, ponderaciones, bases licitación | `Grandes Compras/45.237-2014_ Criterios de Evaluación, no fuera de bases GC.md` |
| ⚠ 47.370 | 2015 | 15-06-2015 | OPTIMA | La JUNJI no actuó con sujeción a derecho en la materia, por lo que deberá, en lo sucesivo, adoptar las medidas tendientes a ajustar sus procesos de compras superiores a 1.000 UTM | No puede emitirse múltiples órdenes de compra para eludir el procedimiento de grandes compras; debe aplicarse cuando la adquisición total supera 1.000 UTM. | grandes compras, fraccionamiento, órdenes compra, JUNJI | `Grandes Compras/GC - Fraccionamiento OC elusion GC.md` |
| ⚠ 49.703 | 2016 | 05-07-2016 | OPTIMA | Autoridad cuenta con atribuciones para invalidar actos administrativos que seleccionan ofertas en procesos de grandes compras | La Administración puede invalidar resoluciones de selección en grandes compras aplicando supletoriamente normas de procedimiento administrativo de la Ley 19.880 cuando existan errores de evaluación. | grandes compras, invalidación, actos administrativos, procedimiento administrativo | `Grandes Compras/49.703 - GC, despues de seleccion OC.md` |
| ⚠ 49.703 | 2016 | 05-07-2016 | OPTIMA | Autoridad cuenta con atribuciones para invalidar actos administrativos que seleccionan ofertas en procesos de grandes compras | Supletoriamente aplica Ley 19.880 para invalidar resoluciones de selección en procesos de grandes compras regulados por Ley 19.886. | grandes compras, invalidación, revocación, selección ofertas | `Grandes Compras/49.703-2016_ Revocación no desercion ni inadmisibilidad en CG.md` |
| ⚠ 49.703 | 2016 | 05-07-2016 | OPTIMA | Autoridad cuenta con atribuciones para invalidar actos administrativos que seleccionan ofertas en procesos de grandes compras | La Ley 19.880 se aplica supletoriamente para invalidar resoluciones de selección en grandes compras cuando concurren errores de evaluación y se cumplen requisitos procedimentales. | grandes compras, invalidación, Ley 19.880, supletoriedad | `Grandes Compras/GC - Se puede invalidar por 19.880.md` |
| ⚠ 51.205 | 2014 | 07-07-2014 | OPTIMA | Se omite establecer respecto de los adjudicatarios la obligación de rendir la garantía de fiel y oportuno cumplimiento del contrato | Las bases de licitación de convenios marco deben especificar requisitos de garantía de cumplimiento y su vigencia conforme a normas reglamentarias. | grandes compras, garantía cumplimiento, bases licitación, convenio marco | `Grandes Compras/GC - DCP inclinate!.md` |
| ⚠ 54.690 | 2013 | 26-08-2013 | OPTIMA | Confirma y complementa el dictamen N° 13.915, de 2013, que se pronunció acerca de eventuales irregularidades cometidas por ciertos órganos administrativos en unos procesos para la contratación de servicios de publicidad | Los criterios de evaluación en grandes compras deben mantener el sistema previsto en bases del convenio marco; solo ajustes complementarios compatibles con naturaleza del bien son permitidos. | grandes compras, criterios evaluación, servicios publicidad, ponderaciones | `Grandes Compras/54.690-2013_ Supletoriedad licitación a GC.md` |
| ⚠ 67.377 | 2016 | 13-09-2016 | OPTIMA | Antecedentes de carácter formal pueden ser solicitados a quienes hayan presentado ofertas en los procedimientos de grandes compras | En grandes compras, pueden solicitarse aclaraciones de errores u omisiones formales siempre que no confieran privilegio a oferentes y se comunique a todos. | grandes compras, aclaraciones, errores formales, oferentes | `Grandes Compras/GC - Se pueden solicitar aclaraciones necesarias.md` |
| ⚠ 73.049 | 2014 | 23-09-2014 | OPTIMA | No procede que en un proceso de grandes compras se efectúen invitaciones fuera del sistema de información de compras y contrataciones de la Administración | Invitaciones en grandes compras deben realizarse por el Sistema de Información, no por correo electrónico; criterios de evaluación no pueden incluir factores no contemplados en bases del convenio marco. | grandes compras, Sistema Información, invitaciones, criterios evaluación | `Grandes Compras/73.049-2014_ Crit. Fuera de Bases GC.md` |
| ⚠ 73.049 | 2014 | 23-09-2014 | OPTIMA | el proceso de grandes compras realizado por el SERVEL no se ajustó a derecho, de manera que dicho servicio deberá adoptar las medidas tendientes a ajustar sus procesos de compras superiores a 1.000 UTM | Invitaciones en grandes compras deben comunicarse por Sistema de Información; criterios de exclusión deben estar previstos en las bases del convenio marco. | grandes compras, invitaciones, Sistema Información, exclusión oferentes | `Grandes Compras/GC - Inv. solo por MP, no excluir por criterios q no existen en IC.md` |
| ⚠ 78.428 | 2012 | 18-12-2012 | OPTIMA | La entidad deberá publicar un informe que dé cuenta del proceso, incluyendo el análisis de las ofertas recibidas y estará obligada a adjuntar dicho cuadro comparativo a la orden de compra respectiva | En grandes compras, el cuadro comparativo de evaluación debe confeccionarse según criterios de las bases del convenio marco y adjuntarse a la orden de compra. | grandes compras, cuadro comparativo, evaluación ofertas, orden compra | `Grandes Compras/GC - Evaluacion, cuadro comparativo 2.md` |
| ⚠ 85.901 | 2016 | 28-11-2016 | OPTIMA | No procede que a través de acuerdos complementarios se modifiquen las condiciones establecidas en la pertinente intención de compra | El acuerdo complementario en grandes compras no puede modificar lo regulado en las bases del convenio marco ni alterar condiciones de la intención de compra. | grandes compras, acuerdo complementario, intención compra, Carabineros | `Grandes Compras/GC - AC no puede ser dif a IC, bases y oferta.md` |
| ⚠ 85.901 | 2016 | 28-11-2016 | OPTIMA | No resultó pertinente que la intención de compra modificara lo regulado en ese pliego de condiciones | La intención de compra puede establecer formas particulares de entrega compatibles con las bases del convenio marco, pero no puede alterar condiciones sustanciales. | grandes compras, condiciones entrega, intención compra, convenio marco | `Grandes Compras/GC - IC puede establecer formas de entrega perticulares.md` |
| ⚠ 86.827 | 2016 | 30-11-2016 | OPTIMA | el servicio se ha ajustado a lo señalado en dicha intención para contabilizar el plazo mencionado, por lo que no existe reproche que formular sobre el particular | Las multas por atraso en entrega previstas en bases del convenio marco se aplican conforme se establece en la intención de compra. | grandes compras, multas, atraso entrega, convenio marco | `Grandes Compras/GC - Multas del CM aplican, OC aceptada.md` |
| 89.567 | 2016 | 14-12-2016 | OPTIMA | Los criterios consignados en los términos de referencia difieren de los establecidos en el convenio marco, lo que no guarda armonía con lo previsto en los dictámenes N°s. 7.640 y 21.801, ambos de 2013 | En grandes compras solo es factible fijar condiciones de carácter complementario a las bases del convenio marco; no pueden alterarse sustancialmente los criterios de evaluación. | grandes compras, criterios, términos referencia, convenio marco | `Grandes Compras/89.567-2016 - (GC) Criterios desproporcionados al CM.md` |
| 91843 | 2016 | 21-12-2016 | OPTIMA | no procede que CGR se pronuncie mientras haya recurso de reposición pendiente ante la administración activa | CGR no sustituye a administración activa en ponderación de alegaciones durante recurso de reposición pendiente | grandes compras, recurso reposición, competencia CGR | `Grandes Compras/GC - Si hay rec de rep pendiente, CGR no se pronuncia.md` |

### Inadmisibilidad  (1 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 65.771 | 2013 | 11-10-2013 | OPTIMA | No corresponde que el Servicio de Salud Metropolitano Central haya hecho efectiva la caución en comento, puesto que el referido cobro no se condice con la naturaleza y fin de la garantía de seriedad de la oferta. | No procede cobrar boleta de garantía de seriedad cuando oferta es declarada inadmisible; garantía respalda obligación de cumplimiento de contrato, que no existe si oferta es rechazada por incumplimiento de requisitos técnicos. | inadmisibilidad, boleta garantía, especificaciones técnicas | `Inadmisibilidad/Oferta Inadmisible por EETT.md` |

### Objeto de compra  (1 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 14.250 | 2018 | 07-06-2018 | OPTIMA | El Hospital Clínico de la Universidad de Chile puede contemplar la inclusión de bienes reacondicionados en los procedimientos concursales que lleve a cabo para el suministro de los equipos que necesite, en la medida que con ello no se transgredan los principios que deben regir el proceso. | Entidad licitante tiene facultad discrecional de incluir bienes reacondicionados en bases, pero debe ejercerla razonada y fundadamente según necesidades concretas; decisión debe propender a eficacia, eficiencia y ahorro sin vulnerar igualdad de oferentes. | bienes reacondicionados, facultad discrecional, especificaciones técnicas | `Objeto de compra/14.250-2018, Bienes reacondicionados. Decision de merito fundada.md` |

### Ofertas  (11 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 3.566 | 2004 | 27-I-2004 | OPTIMA | no cabe suponer una intención en torno a aspectos que, conforme a las bases pertinentes, debieron manifestarse expresamente. | La omisión de un ítem presupuestado en la oferta (como imprevistos) constituye incumplimiento de bases cuando esta debía ser explícitamente valorizada. | imprevistos, vicio formal, oferta | `Ofertas/3.566-2004_ Oferta debe manifestarse expresamente, partida vacia.md` |
| 12.142 | 2019 | 03-V-2019 | OPTIMA | la sola circunstancia que las aludidas Facultades de la Universidad de Chile presentaron sus ofertas bajo un mismo RUT no permite sostener que sean un mismo proponente, en especial, atendidas las particularidades del funcionamiento independiente de éstas. | Dos facultades de la misma universidad que funcionan de forma independiente, aunque usen el mismo RUT, pueden ser consideradas como proponentes distintos en una licitación. | múltiples ofertas, mismo RUT, libre concurrencia | `Ofertas/12.142-2019_ UCh., mismo rut no una sola oferta.md` |
| 14.140 | 2009 | 18-III-2009 | OPTIMA | la omisión de los tres decimales indicada resulta irrelevante en el objeto perseguido en el procedimiento pertinente, por lo que se desecha la reconsideración presentada. | La omisión de decimales en una oferta presenta un carácter formal no esencial, pues la Administración debe entender que cifras enteras tienen decimales iguales a cero. | vicio formal, decimales, oferta | `Ofertas/14.140-2009_ Oferta decimales, vicio formal.md` |
| ⚠ 17.584 | 2018 | 12-VII-2018 | OPTIMA | no existe impedimento para que en las bases de licitación las entidades contemplen la posibilidad de que un proveedor pueda presentar más de una oferta. | Las entidades licitantes pueden autorizar que un mismo proveedor presente múltiples ofertas en una licitación, respetando principios de estricta sujeción, igualdad y libre concurrencia. | múltiples ofertas, proveedor, bases licitación | `Ofertas/17.584-2018_ Multiples ofertas merito-ESB.md` |
| 20.687 | 1990 | 20-07-1990 | BUENA | - | - | oferta, plazo, basesexpecialesdeproposicion | `Ofertas/20.687-1990_ Oferta debe manifestarse expresamente, partida vacia.md` |
| ⚠ 82.062 | 2013 | 13-XII-2013 | OPTIMA | si bien no se daba cumplimiento a la exigencia prevista en el punto 3.6 de las bases administrativas, en orden a que la totalidad de la oferta debía presentarse en idioma español, aquello no constituye un impedimento para entender que la propuesta se ajusta a las bases. | Documentos anexos en idioma extranjero que no son evaluados ni constituyen elementos esenciales pueden ser desestimados sin declarar inadmisible la oferta completa. | idioma, idioma inglés, libre concurrencia | `Ofertas/82.062-2013_ Vale oferta en Ingles.md` |
| 88.499 | 2015 | 06-XI-2015 | OPTIMA | es dable concluir que no se aprecia irregularidad alguna en la decisión de la Policía de Investigaciones de Chile en orden a aceptar la propuesta de Cramick S.A. | La presentación de oferta en valores brutos en lugar de netos constituye error formal no esencial si mediante simple operación aritmética se puede obtener el valor neto. | oferta económica, valores brutos, valores netos | `Ofertas/88.499-2015_ Oferta Bruta debio ser neta, valida.md` |
| ⚠ 076516N12 | 2012 | 10-XII-2012 | OPTIMA | la inscripción de los proponentes en el mencionado registro no constituye un requisito indispensable para participar en los procedimientos administrativos que preceden a la conclusión de los convenios, sino una exigencia que puede formularse a los oferentes para proceder a la celebración definitiva de los contratos respectivos. | La inscripción en el registro electrónico de contratistas es exigible solo para celebrar el contrato definitivo, no para participar en la licitación pública, conforme al principio de libre concurrencia. | registro contratistas, libre concurrencia, licitación pública | `Ofertas/076516N12 - No procede exigencia de registro para participar.md` |
| 076749N13 | 2013 | 22-XI-2013 | OPTIMA | la exigencia de encontrarse inscrito en el Registro Nacional de Consultores del Ministerio de Vivienda y Urbanismo solo podrá requerirse para efectos de celebrar el respectivo contrato. | El registro de consultores o contratistas es exigible para la celebración del contrato, no como requisito previo de participación en licitación, conforme a normativa especial por órgano. | registro nacional consultores, SERVIU, licitación obras | `Ofertas/076749N13 - Reg. Solo exigible por norma particular.md` |
| - | 2021 | 04-V-2021 | OPTIMA | esta Sede de Control no advierte irregularidad en lo obrado por la DOH en cuanto dejó sin efecto el proceso licitatorio, toda vez que su decisión se encuentra debidamente fundada y no afectó derechos adquiridos de terceros. | La revocación de un proceso licitatorio antes de adjudicación es procedente cuando vulnera el principio de libre concurrencia, sin afectar derechos consolidados de terceros. | libre concurrencia, categoría inferior, licitación obras | `Ofertas/E102329N21 - LC, registro.md` |
| - | 2018 | - | OPTIMA | el Tribunal de Contratación al rechazar la demanda, considerando que la empresa adjudicataria se encontraba en el imperativo de aceptar regirse por el artículo cuarto de las bases administrativas, debiendo ajustar algunos aspectos técnicos de su oferta. | La libre concurrencia de oferentes permite desestimar errores sin trascendencia no esenciales en la presentación de ofertas. | boleta garantía, glosa, ofertas | `Ofertas/GSO Glosa, Aumento, Glosa, Ofertas C. A..md` |

### Ordenes de Compra  (1 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 003485N14 | 2014 | 15-01-2014 | OPTIMA | El plazo de entrega se contabilizaría desde la emisión de la orden de compra efectuada por la Dirección Nacional de Logística de Carabineros, no desde la fecha de su aceptación. | La orden de compra es documento comercial cuya notificación no es requisito obligatorio para su vigencia; los plazos se cuentan desde emisión según bases de licitación. | orden compra, plazo entrega, multas, carabineros | `Ordenes de Compra/OC Documento comercial.md` |

### Pagos  (4 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 7.561 | 2018 | 19-03-2018 | OPTIMA | Imparte instrucciones sobre el pago oportuno a los proveedores en los procesos de contratación pública regulados por la ley N° 19.886. | Los pagos a proveedores deben efectuarse dentro de 30 días corridos desde recepción factura; las entidades deben contar con presupuesto previo; manual de procedimientos debe garantizar pago oportuno. | pago oportuno, 30 días, presupuesto, procedimiento pago | `Pagos/7.561-2018_ Pago oportuno de proveedores.md` |
| 8.664 | 2017 | 14-03-2017 | OPTIMA | La Municipalidad de Puerto Octay deberá regularizar registro de la caldera ante la SEREMI de Salud y pagar deuda de combustible a proveedor a la brevedad. | El principio del devengado requiere registro contable de las obligaciones; el pago debe efectuarse dentro de 30 días desde aceptación factura conforme ley 19.983. | principio devengado, pago inoportuno, enriquecimiento sin causa, combustible | `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md` |
| ⚠ 20.453 | 2019 | 02-08-2019 | OPTIMA | No existe reproche que formular a la decisión de Carabineros de Chile de poner término anticipado al contrato que motiva el reclamo del rubro. | La recepción conforme de bienes adquiridos debe ser efectuada por la administración, siendo solo antecedente las certificaciones del proveedor conforme a bases. | recepción conforme, incumplimiento grave, término anticipado, garantía oportuno cumplimiento | `Pagos/20.453-2019_ Reqs. Pago.md` |
| ⚠ 20.456 | 2019 | 02-08-2019 | OPTIMA | Corresponde a la entidad compradora efectuar la recepción conforme de los bienes adquiridos. | La administración es responsable de recibir conforme los bienes; las certificaciones del proveedor son solo antecedentes; debe efectuarse inspección física. | recepción conforme, informe técnico, multas por incumplimiento, especificaciones técnicas | `Pagos/20.456-2019_ Reqs. Pago.md` |

### Plazos no fatales  (5 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 7.626 | 2014 | 30-01-2014 | OPTIMA | No procede enterar retroactivamente los estipendios reclamados, debiendo desestimarse su pretensión. | Los plazos no son fatales para la Administración ni su vencimiento implica caducidad o invalidacion del acto respectivo salvo disposición legal expresa. | plazo no fatal, traspaso personal, atencion primaria salud, remuneraciones | `Plazos no fatales/Plazos no fatales 2.md` |
| ⚠ 37.867 | 2014 | 29-05-2014 | OPTIMA | Las anotadas inobservancias revisten un carácter formal y no esencial al no guardar relación con aspectos a evaluar ni significar una contravención al principio de igualdad. | Incumplimiento plazos administrativos en licitaciones no vicia validez proceso si reviste caracter formal no esencial. | plazo administrativo, vicio formal, licitacion publica, grupos electrogenos | `Plazos no fatales/Plazos no fatales con art 41.md` |
| ⚠ 75.501 | 2013 | 20-11-2013 | OPTIMA | La inobservancia de los plazos no tiene incidencia en la validez del proceso licitatorio por cuanto reviste un carácter formal y no constituye un error esencial. | Incumplimiento de plazos adjudicacion es vicio formal no esencial si no afecta evaluacion ni igualdad oferentes; debe comunicarse razon del retraso. | plazo adjudicacion, vicio formal, licitacion publica, bases administrativas | `Plazos no fatales/Plazos no fatales con art 41 2.md` |
| - | - | - | PARCIAL | - | - |  | `Plazos no fatales/Plazos no fatales 3.md` |
| - | - | - | PARCIAL | - | - |  | `Plazos no fatales/Plazos no fatales.md` |

### Preguntas y Respuestas  (2 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 003688N18 | 2018 | 31-01-2018 | OPTIMA | Se abstiene de dar curso al instrumento por encontrarse que el adjudicatario fue suspendido del Registro de Obras Mayores durante proceso licitatorio, contraviendo requisito de inscripción vigente. | Para participar en licitación y adjudicación de contrato de obra pública, el contratista debe estar inscrito vigente en el registro de obras mayores. | obra publica, registro obras mayores, toma de razon, adjudicacion | `Preguntas y Respuestas/3.688-2018_ Preguntas y rpta vinculantes.md` |
| 076920N15 | 2015 | 28-09-2015 | OPTIMA | De los antecedentes tenidos a la vista no se aprecia irregularidad en la licitación privada N° 44-2013, convocada por el Comando de apoyo a la Fuerza del Ejército de Chile. | La facultad de la administración de declarar desierto un concurso no puede ejercerse con discrecionalidad absoluta sino obedeciendo a causa sustantiva, expresada en acto administrativo conforme principios de certeza y seguridad jurídica. | licitacion privada, ejercito, visores nocturnos, apuntadores laser | `Preguntas y Respuestas/76.920-2015_ Preguntas y rpta vinculantes.md` |

### Presupuesto  (3 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 39.228 | 2009 | 22-07-2009 | OPTIMA | La Contraloría General ha debido abstenerse de dar curso a la resolución N° 467, de 2009, por cuanto ha merecido diversos reparos. | Las bases administrativas deben especificar presupuesto estimativo de contratación, procedimiento de contratación, glosa de garantía, y parámetros de evaluación con claridad. | bases administrativas, presupuesto estimativo, criterios evaluación, deficiencias procedimiento | `Presupuesto/Art. 11 DS 250 2.md` |
| ⚠ 50.110 | 2013 | 08-08-2013 | OPTIMA | No ha resultado procedente que mediante el proceso licitatorio en análisis se entregue el ejercicio de una función pública a un particular. | Las funciones municipales privativas deben ser ejecutadas por personal municipal; la entrega a terceros es improcedente; el precio debe ser determinado o determinable para propósitos presupuestarios. | función pública, personal municipal, indeterminación precio, acuerdo concejo | `Presupuesto/Art. 11 DS 250.md` |
| ⚠ 71.953 | 2011 | 17-11-2011 | OPTIMA | Esa Contraloría Regional debe abstenerse de tomar razón de la indicada resolución, en atención a diversas consideraciones técnicas, administrativas y especificaciones. | Las bases administrativas de licitación deben contener todos los antecedentes íntegros, criterios de evaluación claros, especificaciones técnicas completas y presupuesto estimativo. | bases administrativas, especificaciones técnicas, presupuesto estimativo, requisitos mínimos | `Presupuesto/Art. 11 DS 250 (Funcion publica).md` |

### TD  (2 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ Resolucion Exenta N 04483 | 2009 | 15-12-2009 | OPTIMA | Autorízase, proceder mediante trato directo con Producciones Concorde Limitada, a fin contratar la organización y producción del evento de Bienestar para todos los funcionarios de la sede central de la Contraloría General de la República. | Procede trato directo por confianza cuando por la naturaleza de la negociación se deba recurrir a proveedor específico cuya experiencia comprobada en servicios similares ofrezca seguridad; se requiere acreditación de que otros proveedores no ofrecen esa seguridad y confianza. | trato directo, confianza, evento bienestar, producción de eventos | `TD/Res. Ex. N° 04483-2009 (TD Confianza)_ Ap. Ctto. CGR con Concorde Ltda..md` |
| ⚠ 24.268 | 2017 | 04-07-2017 | OPTIMA | Con los alcances que anteceden, se ha tomado razón de la resolución del epígrafe. | El contratista debe acreditar por escrito que no ha incurrido en inhabilidades para contratar con el Estado, de conformidad con la Ley 20.393 y Ley 19.886. | trato directo, inhabilidad para contratar, caución fiel cumplimiento | `TD/24.268-2017_ TD, debe acompañar anexo de que no es inhabil para contratar.md` |

### TD/Art. 10, N° 3  (1 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| - | - | - | PARCIAL | - | - |  | `TD/Art. 10, N° 3/TD - 10 N° 3 - Fundamentacion urgencia.md` |

### TD/Art. 10, N° 7, a)/TA  (2 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 54.869 | 2015 | 09-07-2015 | OPTIMA | Esta Contraloría General ha debido abstenerse de dar curso al instrumento del rubro, que contrata por trato directo la ejecución de las obras. | No se puede contratar mediante trato directo obras ya ejecutadas sin acompañar informe técnico que acredite su estado y sin verificar que el contratista tiene capacidad económica disponible. | trato directo, obras construidas, partidas pagadas, SERVIU | `TD/Art. 10, N° 7, a)/TA/54869-2015_ TD por partidas ya pagadas.md` |
| ⚠ 63.558 | 2015 | 11-08-2015 | OPTIMA | En consecuencia, no es atendible la argumentación entregada por el municipio en orden a sostener la procedencia de la contratación de la continuación de los trabajos de la Clínica Cordillera de la Solidaridad, directamente con la aludida empresa. | Un contrato de obras a precios unitarios debe especificar completamente las faenas a ejecutar mediante un proyecto definitivo, no puede permitir incorporar obras nuevas sin licitación previa ni admitir repactación de precios de partidas previamente convenidas. | trato directo, contratación obras, precios unitarios, adendum ilegal, licitación pública | `TD/Art. 10, N° 7, a)/TA/63.558-2015_ TD no TD (Clinica Cordillera).md` |

### TD/Art. 10, N° 7, f)  (36 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 839 | 2006 | 06-01-2006 | OPTIMA | En efecto, debe observarse que la mencionada Secretaría de Estado entiende justificada la adopción del procedimiento excepcional del trato o contratación directa en los casos y criterios contenidos en el artículo 10°, número 7, letras d), e) y f) del Decreto N° 250, de 2004. | La sola mención de normas legales y reglamentarias no basta; debe acreditarse que los requisitos copulativos de la norma concurren, particularmente que no existen otros proveedores que otorguen la seguridad y confianza requeridas. | trato directo, mobiliario, servicios, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 839 - 2006.md` |
| ⚠ 2.368 | 2008 | 18-01-2008 | OPTIMA | La Contraloría General ha debido abstenerse de dar curso a la resolución 370, de 2007, del Instituto de Desarrollo Agropecuario, que aprueba el contrato de prestación de servicios para el Desarrollo de un Programa Piloto de Mejoramiento Genético en la Región de la Araucanía. | No basta la sola referencia a disposiciones legales, la mención a la experiencia de trabajo en el sector, ni la simple referencia a programas existentes; se requiere acreditación efectiva y documentada de que no existen otros proveedores. | trato directo, desarrollo agropecuario, servicios, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 2.368 - 2008.md` |
| ⚠ 2410 | 2017 | 23-01-2017 | OPTIMA | Esta Contraloria General ha debido abstenerse de dar curso a la resolucion del epigrafe, por medio de la cual se regulariza la prestacion de servicios que indica y se aprueba el convenio suscrito via trato directo con la empresa Indra Sistemas Chile S.A. | La sola alusión a razones vinculadas con la tecnología y la continuidad en la prestación del servicio no es suficiente para invocar la causal; debe acreditarse fundadamente que no existen otros proveedores. | trato directo, sistemas de informacion, sirh, confianza y seguridad | `TD/Art. 10, N° 7, f)/2410-17.md` |
| ⚠ 3871 | 2011 | 20-01-2011 | OPTIMA | Esta Entidad de Control ha debido abstenerse de dar curso a la resolucion N° 26, de 2010, del Servicio de Impuestos Internos, que aprueba el contrato, en la modalidad de trato directo, entre el Servicio de Impuestos Internos y la empresa Policomp S.A. | La sola mención de normas legales, la buena impresión del servicio contratante respecto de la empresa, o la circunstancia de haber suscrito contratos similares previos no es suficiente; se requiere acreditar efectiva y documentadamente la inexistencia de otros proveedores. | trato directo, contact center, sii, confianza y seguridad | `TD/Art. 10, N° 7, f)/3871-11.md` |
| ⚠ 6381 | 2018 | 02-03-2018 | OPTIMA | Así, es a la institución a la que le debe resultar indispensable la contratación de un prestador determinado basada en su propia confianza y seguridad, sin que sea suficiente invocar únicamente la opinión de las funcionarias requirentes. | Aunque la opinión de las madres trabajadoras puede considerarse como un elemento, es la institución la que debe fundamentar su propia confianza y seguridad en la causal de trato directo, acreditando que no existen otros proveedores. | trato directo, sala cuna, servicios sociales, confianza y seguridad | `TD/Art. 10, N° 7, f)/6381-18.md` |
| ⚠ 9.405 | 2006 | 24-02-2006 | ESCANEADO_VISION | Por consiguiente, debe reiterarse que el decreto citado no se ajusta a derecho. | No se ha acreditado que la decisión de recurrir al trato directo haya derivado de haberse estimado fundadamente que no existen otros proveedores que otorguen esa seguridad y confianza, pese a que el ministerio cotizó a otros profesionales del ramo. | trato directo, mobiliario, decoración, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 9.405 - 2006.md` |
| ⚠ 10172 | 2017 | 23-03-2017 | OPTIMA | Esta Contraloria General ha debido abstenerse de dar curso a la resolucion del epigrafe, que aprueba el contrato suscrito via trato directo con la empresa Lavanderia Industrial Uriarte Ltda. | Debe estimarse fundadamente que no existen otros proveedores que otorguen seguridad y confianza; la sola existencia de experiencia previa no es suficiente. | trato directo, lavanderia, servicios, confianza y seguridad | `TD/Art. 10, N° 7, f)/10172-17.md` |
| ⚠ 11.189 | 2008 | 11-03-2008 | OPTIMA | Esta Contraloría General ha debido abstenerse de tomar razón del Dto 291, de 2007, del Ministerio de Relaciones Exteriores, mediante el cual se aprueba el contrato de suministro para la adquisición de pasajes aéreos, nacionales e internacionales, celebrado con la agencia de viajes Turismo Cocha S.A. | No basta la sola referencia a las disposiciones legales y reglamentarias, ni la mención a la 'gran eficiencia' del proveedor, ni un descuento comercial ofrecido; debe acreditarse fundadamente que no existen otros proveedores. | trato directo, pasajes aéreos, agencia de viajes, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 11.189 - 2008.md` |
| ⚠ 12798 | 2016 | 17-02-2016 | OPTIMA | Esta Contraloria General ha debido abstenerse nuevamente de dar curso a la resolucion singularizada en el epigrafe, mediante la cual se aprueba el contrato suscrito via trato directo para proveer el servicio de alimentacion. | La norma exige que se estime fundadamente que no existen otros proveedores que otorguen seguridad y confianza; la sola experiencia previa y servicio de excelencia no es suficiente. | trato directo, alimentacion, hospital, confianza y seguridad | `TD/Art. 10, N° 7, f)/12798-16.md` |
| ⚠ 14232 | 2016 | 23-02-2016 | OPTIMA | Esta Contraloria General ha dado curso a los documentos de la suma, mediante los cuales se aprueban los contratos suscritos via trato directo con las entidades que en cada caso se individualizan, para la prestacion de los servicios que se indican, por ajustarse a derecho. | El trato directo puede proceder cuando se estima fundadamente que no existen otros proveedores que otorguen la seguridad y confianza, particularmente en servicios ubicados geograficamente o con requisitos especiales. | trato directo, fondos de salud, servicios medicos, confianza y seguridad | `TD/Art. 10, N° 7, f)/14232-16.md` |
| ⚠ 18.355 | 2007 | 25-04-2007 | OPTIMA | Esta Contraloría General ha debido abstenerse de dar curso regular a la resolución N° 18, de 2007, de la Dirección Nacional del Servicio Civil, a través del cual se aprueba el convenio de prestación de servicios celebrado con la fundación Instituto de Estudios Laborales (FIEL). | No basta la simple referencia a disposiciones legales que contemplen la causal de trato directo; se requiere acreditación efectiva y documentada de las razones que motivan su procedencia. | trato directo, capacitación, servicios, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 18.355 - 2007.md` |
| ⚠ 21.470 | 2007 | 15-05-2007 | OPTIMA | Esta Contraloría General se ha abstenido de dar curso regular a la Resoluciones 25, 26, 27 y 68 de 2007 de la Junta Nacional de Auxilio Escolar y Becas, a través de las cuales se aprueban los contratos de prestación de servicios para la fabricación y administración de la Tarjeta Nacional del Estudiante. | La documentación relativa a la experiencia del proveedor no es idónea para estimar fundadamente que no existen otros proveedores que otorguen seguridad y confianza, en particular si no consta que las entidades contratantes tengan experticia en la materia. | trato directo, tarjeta nacional del estudiante, servicios, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 21.470 - 2007.md` |
| ⚠ 23220 | 2011 | 15-04-2011 | OPTIMA | Esta Entidad de Control ha debido abstenerse de dar curso a la resolucion N° 128 de 2011, de la Junta nacional de Auxilio Escolar y Becas, que aprueba los Terminos de Referencia, sus Anexos y el contrato, suscrito mediante trato directo. | Es necesario acreditar de manera suficiente y documentada que no existen otros proveedores que otorguen la seguridad y confianza requeridas; las consultas a participantes o impedimentos procedimentales no justifican el trato directo. | trato directo, alimentacion escolar, junaeb, confianza y seguridad | `TD/Art. 10, N° 7, f)/23220-11.md` |
| ⚠ 24243 | 2019 | 05-09-2019 | OPTIMA | Esta Contraloria General no ha dado curso a la resolucion del epigrafe, que aprueba el contrato suscrito via trato directo entre la Policia de Investigaciones de Chile y la empresa Entel Telefonía Local S.A., para la prestacion del servicio de comunicaciones. | El hecho de ser proveedor actual desde hace años no es suficiente para acreditar la causal; debe estimarse fundadamente que no existen otros proveedores que otorguen seguridad y confianza. | trato directo, comunicaciones, policia, confianza y seguridad | `TD/Art. 10, N° 7, f)/24243-19.md` |
| ⚠ 26006 | 2016 | 08-04-2016 | OPTIMA | De este modo, resulta util indicar que las resoluciones exentas por las que se consulta no se encuentran ajustadas a derecho, ya que las consideraciones descritas en ellas no han sido suficientes para configurar la causal de trato directo. | Para sustentar el trato directo no basta la sola referencia a disposiciones legales, ni la buena impresión que se haya formado el servicio respecto de la empresa, ni siquiera contratos similares previos; se requiere acreditación de que no existen otros proveedores. | trato directo, servicios de salud, arquitectura, confianza y seguridad | `TD/Art. 10, N° 7, f)/26006-16.md` |
| ⚠ 27.818 | 2008 | 16-06-2008 | OPTIMA | Esta Contraloría General ha debido abstenerse de tomar razón del Decreto 123/2008, del Ministerio de Vivienda y Urbanismo, mediante el cual se aprueba un contrato de prestación de servicios suscrito entre la Secretaría Regional Ministerial Metropolitana de Vivienda y Urbanismo y la Sociedad de Profesionales Kronos Limitada. | El vínculo de confianza generado entre la empresa y los vecinos, la buena calificación en fase previa, y las capacidades del equipo profesional no justifican por sí solos el trato directo si no se acredita que otros prestadores no podrían otorgar igual seguridad y confianza. | trato directo, recuperación de barrios, servicios de consultoría, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 27.818 - 2008.md` |
| ⚠ 27.848 | 2005 | 14-06-2005 | OPTIMA | Esta Contraloría General ha debido abstenerse de dar curso a decretos del Ministerio de Relaciones Exteriores, mediante los cuales se aprueban, respectivamente, el contrato de prestación de servicios de impresión de tarjetas de identificación y el contrato de prestación de servicio integral de modulación. | No se acredita la concurrencia de las circunstancias de confianza, seguridad y no existencia de otros proveedores que justifiquen el trato directo; estas deben ser explicitadas en el acto administrativo que las fundamenta. | trato directo, servicios de impresión, tarjetas, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 27.848 - 2005.md` |
| ⚠ 30471 | 2016 | 22-04-2016 | OPTIMA | Esta Contraloria General ha debido abstenerse de dar curso a los documentos del rubro, mediante los cuales se aprueban los contratos celebrados bajo la modalidad de trato directo entre el Hospital Militar de Santiago y diversos proveedores. | La sola mención de que los proveedores cumplen estándares de calidad clinica no es suficiente para acreditar la causal; debe acreditarse fundadamente que no existen otros proveedores que otorguen la seguridad y confianza. | trato directo, suministro medico, implantes, confianza y seguridad | `TD/Art. 10, N° 7, f)/30471-16.md` |
| ⚠ 35861 | 2016 | 16-05-2016 | OPTIMA | Por consiguiente, esa entidad edilicia, en lo sucesivo, deberá tener en consideración los criterios normativos y jurisprudenciales mencionados a fin de evitar que situaciones como la observada se repitan a futuro. | El ahorro de recursos y menor tiempo procedural, aunque sean reales, no son razones suficientes para justificar el trato directo; debe acreditarse fundadamente la inexistencia de otros proveedores que otorguen seguridad y confianza. | trato directo, martillero publico, municipalidad, confianza y seguridad | `TD/Art. 10, N° 7, f)/35861-16.md` |
| ⚠ 35.907 | 2005 | 15-07-2005 | OPTIMA | En consecuencia, se devuelve sin tramitar el decreto del rubro. | No se ha acreditado ni explicitado en el respectivo decreto la concurrencia de las circunstancias de confianza y seguridad, ni que no existen otros proveedores que otorguen esa seguridad y confianza como requiere el trato directo. | trato directo, servicios de consultoría, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 35.907 - 2005.md` |
| ⚠ 42470 | 2015 | 28-05-2015 | OPTIMA | Esta Contraloria General ha debido abstenerse de dar curso al acto administrativo de la suma, mediante el cual se aprueba el contrato para la prestacion de servicios de seguridad privada suscrito mediante trato directo. | Las circunstancias de que se necesite una empresa de prestigio y solidez económica no son suficientes para configurar la causal; debe acreditarse fundadamente que no existen otros proveedores que otorguen seguridad y confianza. | trato directo, seguridad privada, universidad, confianza y seguridad | `TD/Art. 10, N° 7, f)/42470-15.md` |
| ⚠ 44.043 | 2010 | 04-08-2010 | OPTIMA | Como se puede apreciar, la habilitación para excluirse de un convenio marco no constituye, por sí misma, una causal de trato directo o licitación privada, debiendo concurrir entonces, además de las aludidas condiciones más ventajosas, alguna de las causales que la ley N° 19.886 y el reglamento contemplan. | Condiciones económicas más ventajosas respecto de bienes o servicios contenidos en un convenio marco no configuran por sí solas la causal de trato directo; debe concurrir alguna causal expresa de la ley. | trato directo, convenio marco, franqueo, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 44.043 - 2010.md` |
| ⚠ 44.411 | 2007 | 04-10-2007 | OPTIMA | La Contraloría General ha debido abstenerse de dar curso a la resolución N° 263, de 2007, del Instituto de Desarrollo Agropecuario, INDAP, que aprueba el contrato de prestación de servicios de Capacitación en Operación de Equipos Agrícolas. | No basta la simple referencia a disposiciones legales, la mención a la experiencia de la entidad en el rubro, ni la alusión a antecedentes que acreditaría tal circunstancia; se requiere acreditación efectiva y documentada de la inexistencia de otros proveedores. | trato directo, capacitación agrícola, servicios, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 44.411 - 2007.md` |
| ⚠ 44.888 | 2009 | 18-08-2009 | OPTIMA | La Contraloría General se abstiene de dar curso a la resolución N° 97, de 2009, de la Subsecretaría de Transportes, que autoriza contratacion directa y aprueba el contrato de fecha 1 de junio de 2009, para los servicios de asesoría para el proceso de implementación del sistema de gestión de flota. | No basta con la mención de las normas legales y reglamentarias, la buena impresión del ente contratante, ni la circunstancia de haber suscrito anteriores contratos similares; se requiere acreditar efectiva y documentadamente la inexistencia de otros proveedores. | trato directo, asesoría transporte publico, servicios, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 44.888 - 2009.md` |
| ⚠ 46564 | 2011 | 22-07-2011 | OPTIMA | Esta Entidad de Control ha debido abstenerse de dar curso al decreto N° 1.132, de 2011, de la Universidad de Santiago de Chile, que autoriza la contratacion directa con la empresa ENTEL Telefonía Local S.A., y aprueba contrato de prestacion de servicios de telefonía y sus anexos. | No basta la sola referencia a disposiciones legales y reglamentarias; se requiere demostración efectiva y documentada de los motivos que justifican el trato directo, en especial que no existen otros proveedores que otorguen la seguridad y confianza. | trato directo, telefonía, universidad, confianza y seguridad | `TD/Art. 10, N° 7, f)/46564-11.md` |
| ⚠ 46.819 | 2005 | 10-06-2005 | OPTIMA | La Contraloría General ha debido abstenerse de dar curso al Decreto N° 133, de 2005, del Ministerio de Relaciones Exteriores, que aprueba un contrato con la entidad que indica para el arriendo de una impresora. | Cuando se acuda al trato directo por razón de que la magnitud e importancia hace indispensable un proveedor determinado, debe acreditarse la concurrencia de los requisitos copulativos: confianza y seguridad derivadas de experiencia comprobada, y fundadamente que no existen otros proveedores. | trato directo, arriendo, impresora, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictmane 46.819 - 2005.md` |
| ⚠ 65.505 | 2010 | 08-11-2010 | OPTIMA | Esta Contraloría General se ha abstenido, nuevamente, de dar curso a la resolución N° 1.018, de 2010, del Complejo Asistencial Dr. Sótero del Río, que aprueba el contrato celebrado, bajo la modalidad de trato directo, con la Sociedad de Profesionales Médicos Morpheus S.A. | Por el carácter excepcional del trato directo, es preciso acreditar efectiva y documentadamente las razones que motivan su procedencia, en especial las que permiten estimar fundadamente que no existen otros proveedores que otorguen la seguridad y confianza. | trato directo, servicios medicos, hospital, confianza y seguridad | `TD/Art. 10, N° 7, f)/dictamen 65.505 - 2010.md` |
| ⚠ 66231 | 2015 | 19-08-2015 | OPTIMA | Esta Entidad de Control ha debido abstenerse de dar curso al documento del epigrafe, que autoriza y aprueba el contrato de adquisicion de un vehículo blindado mediante trato directo, celebrado entre Gendarmería de Chile y Comercial Kaufmann S.A. | La experiencia previa del proveedor en otros tipos de vehículos no demuestra que sea necesario recurrir a ese proveedor específico para vehículos blindados; debe acreditarse la inexistencia de otros proveedores con igual seguridad y confianza. | trato directo, adquisición, vehículos blindados, confianza y seguridad | `TD/Art. 10, N° 7, f)/66231-15.md` |
| ⚠ 69865 | 2012 | 09-11-2012 | OPTIMA | Esta Entidad de Control ha debido abstenerse de dar curso a la resolucion N° 963, de 2012, de la Subsecretaría de Salud Pública, que regulariza la contratacion de los Servicios de Mantención, Continuidad y Desarrollo de trámites de apoyo a las SEREMI e Interoperabilidad del RAKIN. | No basta que una empresa haya prestado servicios previamente sin proceso licitatorio; se requiere cumplir con las causales expresas del trato directo, acreditando fundamentadamente que no existen otros proveedores. | trato directo, servicios de mantención, salud, confianza y seguridad | `TD/Art. 10, N° 7, f)/69865-12.md` |
| ⚠ 72385 | 2016 | 04-10-2016 | OPTIMA | Así, es a la institución a la que le debe resultar indispensable la contratación de un prestador determinado basada en su propia confianza y seguridad, sin que sea suficiente invocar únicamente la opinión de las madres trabajadoras. | Aunque la opinión de las madres trabajadoras puede considerarse, es el empleador el que debe demostrar su propia confianza y seguridad en la causal de trato directo, acreditando fundadamente que no existen otros proveedores. | trato directo, sala cuna, servicios sociales, confianza y seguridad | `TD/Art. 10, N° 7, f)/72385-16.md` |
| ⚠ 80806 | 2013 | 09-12-2013 | OPTIMA | No obstante lo anterior, se comprobó que mediante las citadas resoluciones exentas Nos 343 y 367, ambas de 4 de febrero de 2013, prorrogó nuevamente dichos contratos mediante trato directo, invocando la causal del artículo 10, N° 7, letra f). | Las sucesivas prórrogas mediante trato directo, si bien pueden justificarse individualmente, no pueden convertirse en un mecanismo indefinido de contratación que evite los procesos licitatorios que la ley exige. | trato directo, concesión, servicios, confianza y seguridad | `TD/Art. 10, N° 7, f)/80806-13.md` |
| ⚠ 89541 | 2014 | 17-11-2014 | OPTIMA | Esta Contraloria General ha debido abstenerse de dar curso al acto administrativo de la suma, que aprueba el contrato de Servicio de Aseo Integral, para dependencias del Hospital de Carabineros de Chile, Dirección de Salud y Sanidad e Instalaciones Anexas, suscrito mediante trato directo con la empresa Servicios Generales Full Clean S.A. | El hecho de que el proveedor haya ejecutado el servicio permanentemente no es suficiente para invocar la causal; debe acreditarse fundadamente que no existen otros proveedores que otorguen seguridad y confianza. | trato directo, aseo integral, carabineros, confianza y seguridad | `TD/Art. 10, N° 7, f)/89541-14.md` |
| ⚠ 89918 | 2016 | 15-12-2016 | OPTIMA | En consecuencia, en mérito de lo expuesto, se reconsidera parcialmente el oficio N° 1.769, de 2016, de la Contraloria Regional de Aysén del General Carlos Ibáñez del Campo, en los términos anotados en el presente pronunciamiento. | Aunque el trato directo no estuviera debidamente fundamentado, si el proveedor prestó efectivamente los servicios, la municipalidad debe pagar las facturas correspondientes para evitar enriquecimiento sin causa. | trato directo, recuperación de subsidios, municipalidad, confianza y seguridad | `TD/Art. 10, N° 7, f)/89918-16.md` |
| ⚠ 90268 | 2015 | 13-11-2015 | OPTIMA | En mérito de lo expuesto, se representa el acto administrativo del rubro. | La circunstancia de que el proveedor haya prestado servicios de excelencia durante veinticuatro meses no es suficiente; debe acreditarse fundadamente que no existen otros proveedores que otorguen seguridad y confianza. | trato directo, alimentación, hospital, confianza y seguridad | `TD/Art. 10, N° 7, f)/90268-15.md` |
| ⚠ 91012 | 2016 | 20-12-2016 | OPTIMA | En consecuencia, al tenor de lo expuesto, cabe concluir que no aparece suficientemente justificado que la Municipalidad de Lampa haya contratado de manera directa los servicios en estudio. | La sola alusión a la eficiencia del servicio y la confianza generada en la prestación, basada en experiencia comprobada, no son suficientes; debe acreditarse fundadamente que no existen otros proveedores que otorguen seguridad y confianza. | trato directo, eventos municipales, publicidad, confianza y seguridad | `TD/Art. 10, N° 7, f)/91012-16.md` |
| ⚠ 100098 | 2014 | 24-12-2014 | OPTIMA | Por todo lo antes expuesto, no procede reconsiderar la observacion N°2, Contratacion mediante trato directo de la empresa TERMIKA S.A., del aludido acapite, del informe final de auditoria en comento. | El trato directo requiere fundamentacion efectiva y documentada que no existen otros proveedores que otorguen la seguridad y confianza atribuida a la entidad contratada. | trato directo, contratacion, confianza y seguridad, proveedor determinado, facultad de derecho | `TD/Art. 10, N° 7, f)/100098-14.md` |

### TD/Art. 10, N° 7, g)  (11 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 24.685 | 2010 | 10-05-2010 | OPTIMA | Esta Contraloría General ha debido abstenerse de tomar razón de la resolución N° 1.235, de 2009, de la Policía de Investigaciones de Chile. | Para aplicar el causal de trato directo por reposición o complementación de equipamiento accesorios, se requiere acreditación efectiva y documentada de que los servicios son complementarios a contrataciones anteriores del mismo proyecto, no basta la sola referencia a las disposiciones legales. | trato directo, complementación equipamiento, sistema informático, PDI | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (10).md` |
| ⚠ 31.356 | 2013 | 22-05-2013 | OPTIMA | De lo expuesto, es dable concluir que de concurrir los hechos que sirven de fundamento para la contratación mediante trato directo, corresponde a la respectiva autoridad administrativa ponderarlos y efectuar la contratación en la forma indicada, sin que esta Contraloría General pueda calificar su pertinencia en forma previa. | La Contraloría no puede pronunciarse anticipadamente sobre si concurren los requisitos de trato directo; ese análisis lo realiza en el control preventivo cuando el acto administrativo se somete a toma de razón. | trato directo, pronunciamiento anticipado, capacidad técnica | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (2).md` |
| ⚠ 44.145 | 2010 | 04-08-2010 | OPTIMA | Con los alcances que anteceden, se ha tomado razón del acto administrativo. | Las cláusulas de renovación tácita y automática de contratos previos a la Ley 19.886 pugnan con los principios de transparencia y libre concurrencia; en lo sucesivo debe convocarse a licitación pública para nuevas contrataciones de bienes y servicios. | trato directo, telefonía, Ministerio Interior, renovación automática | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (9).md` |
| ⚠ 46.564 | 2011 | 22-07-2011 | OPTIMA | Por lo tanto, atendidas las consideraciones expuestas, se devuelve sin tramitar el decreto N° 1.132, de 2011, de la Universidad de Santiago de Chile. | No basta que una entidad haya adquirido un equipo compatible con un proveedor para justificar trato directo posterior; el contrato debe especificar claramente su objeto, prohibir cesión sin autorización y exigir garantía de fiel cumplimiento. | trato directo, USACH, servicios telefonía, equipamiento previo | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (5).md` |
| ⚠ 48.093 | 2010 | 19-08-2010 | OPTIMA | En mérito de lo expuesto, se devuelve sin tramitar el señalado acto administrativo. | Cuando el acto administrativo es devuelto por defectos, las enmiendas deben salvarse al margen con timbre y media firma de la autoridad competente; debe precisarse qué montos son anticipables y qué cauciones corresponden por cada uno; los gastos del año siguiente deben quedar condicionados a existencia de recursos. | trato directo, PDI, sistema informático, correcciones acto administrativo | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (8).md` |
| ⚠ 57.416 | 2016 | 04-08-2016 | OPTIMA | Atendido lo expuesto, se representa el decreto del rubro. | Para justificar trato directo por reposición o complementación de servicios accesorios debe constar que existe un equipo o servicio principal previo al cual se complementen o accedan; no basta que el servicio sea accesorio. | trato directo, USACH, plataforma informática, idioma inglés | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g.md` |
| ⚠ 59.946 | 2010 | 07-10-2010 | OPTIMA | Atendido lo expuesto, se representa el acto administrativo. | El contrato de suministro con precio indeterminado no puede permitir incorporar reactivos no considerados en anexos ni posibilidad de reemplazo de equipos sin someterse a toma de razón; las cláusulas de término anticipado deben ser precisas y especificar los incumplimientos. | trato directo, suministro reactivos, FACH, Hospital Clínico, Roche | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (7).md` |
| ⚠ 59946 | 2010 | 07-10-2010 | OPTIMA | contrato no acredita concurrencia de elementos de causal trato directo por reposición o complementación de equipamiento necesariamente compatible | trato directo por reposición requiere demostrar existencia de equipo principal al cual complementen servicios accesorios; continuar solo con proveedor anterior no justifica procedimiento | trato directo, reposición equipamiento, libre concurrencia, licitación pública | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (6).md` |
| ⚠ 63.669 | 2011 | 07-10-2011 | OPTIMA | Esta Entidad de Control ha debido abstenerse de dar curso a la resolución N° 24, de 2011, del Servicio de Impuestos Internos. | Para aplicar el causal de reposición o complementación de servicios accesorios, debe existir un equipo o servicio principal previo al cual se complementen o accedan; la intención de mantener vinculación con proveedor anterior no justifica trato directo. | trato directo, servicios telefonía, SII, libre concurrencia | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (4).md` |
| 70.620 | 2013 | 30-10-2013 | OPTIMA | De modo tal que la citada disposición contenida en el inciso segundo del artículo 3° de la ley N° 20.309, ha derogado tácitamente aquellos preceptos, tanto de rango legal como reglamentario, que brindaban exclusividad. | La Ley 20.309 que convierte Casa de Moneda en sociedad anónima deroga tácitamente la exclusividad en la confección de licencias de conductor y certificados de revisión técnica; por tanto, esas contrataciones deben efectuarse mediante licitación pública a menos que concurran causales de licitación privada o trato directo. | proveedor único, Casa Moneda, derogación tácita, licencias de conductor | `TD/Art. 10, N° 7, g)/Casa moneda no es proveedor unico.md` |
| ⚠ 79.494 | 2011 | 21-12-2011 | OPTIMA | Esta Contraloría General ha debido abstenerse de dar curso a la resolución N° 233, de 2011, de la Subsecretaría de Transportes. | El causal de trato directo para consultorías de especialidad única requiere acreditación efectiva de que el consultor reúne capacidades especiales; no es suficiente argumentar experiencia, conocimiento indiscutido o metodología única sin documentación específica. | trato directo, consultoría especialidad única, capacidad especial, Subsecretaría Transportes | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (3).md` |

### TD/Art. 10, N° 7, m)  (1 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ Resolucion Exenta N 04675 | 2013 | 24-09-2013 | ESCANEADO_VISION | Autorízase proceder mediante trato directo con la Pontificia Universidad Católica de Chile a fin de contratar la prestación de servicios personales especializados de Diplomado en Derecho Administrativo. | Para servicios personales especializados de capacitación con especialidad única en el mercado, cuando el monto es inferior a 1.000 UTM, procede trato directo conforme al artículo 10 N°7 letra m) del DTO 250/2004, previa invitación al proveedor y verificación de su idoneidad. | trato directo, servicios personales especializados, diplomado derecho administrativo, capacitación funcionarios | `TD/Art. 10, N° 7, m)/CGR hace contrato antes del trato directo.md` |

### Termino Anticipado  (2 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 3.481 | 2018 | 26-01-2018 | OPTIMA | Se ajustó a derecho la decisión de poner término anticipado a la respectiva contratación. | El pago de servicios contratados está supeditado a que el producto entregado se ajuste a lo comprometido; el solo haber trabajado no genera derecho a pago si producto no cumple. | término anticipado, software no cumple, cumplimiento servicios, convenio marco | `Termino Anticipado/3481-2018_ Haber trabajado no basta, es entregar lo que se pidio.md` |
| ⚠ - | 2016 | - | OPTIMA | Ese servicio deberá en lo sucesivo aprobar oportunamente por resolución sometida al trámite de toma de razón las adiciones y aclaraciones que impliquen modificar lo establecido en bases. | Las modificaciones a contrato deben interpretarse en armonía con el principio de estricta sujeción a bases y solo proceden si están previstas en pliego de condiciones. | modificación contrato, estricta sujeción, bases licitación, resciliación | `Termino Anticipado/Deben estar las condiciones para la resciliacion.md` |

### UTP  (3 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| 10.706 | 2019 | 17-04-2019 | OPTIMA | Se ha tomado razón de la resolución del epígrafe. | La escritura pública de unión temporal solo procede para contratar, no para presentar oferta; se exigen por miembros, no por apoderado. | unión temporal, escritura pública, momento contratar, requisitos | `UTP/10706-2019_ UTP EP al momento de contratar.md` |
| 20.715 | 2018 | 17-08-2018 | OPTIMA | Se ha tomado razón de la resolución del epígrafe. | La escritura pública de constitución de UTP solo es exigible al momento de contratar cuando el convenio sea igual o superior a 1.000 UTM. | unión temporal, escritura pública, 1.000 UTM, documento público privado | `UTP/20715-2018_ UTP EP al momento de contratar.md` |
| 22.469 | 2016 | 23-03-2016 | OPTIMA | Se ha tomado razón de la resolución del epígrafe. | La escritura pública de unión temporal solo es exigible al momento de contratar cuando sea igual o superior a 1.000 UTM. | unión temporal, documento público, 1.000 UTM, contratación | `UTP/22469-2016_ UTP EP al momento de contratar.md` |

### Varios  (2 documentos)

| N° | Año | Fecha | Ext. | Cita/conclusión | Criterio aplicable | Tags | Archivo |
|---|---|---|---|---|---|---|---|
| ⚠ 002453N18 | 2018 | 22-I-2018 | OPTIMA | Imparte instrucciones sobre el cumplimiento del principio de probidad en materia de contratación pública de suministro de bienes muebles y prestación de servicios. | El principio de probidad obliga a funcionarios en todas las etapas de contratación pública, desde estimación de gasto hasta gestión de contratos. | probidad, contratación pública, suministro servicios | `Varios/Dictamen CGR N° 2453-2018, Probidad y Compras.md` |
| - | 2021 | 29-XI-2021 | OPTIMA | Corporaciones municipales se encuentran sujetas a las regulaciones establecidas en las leyes Nºs. 19.880, 19.886, 20.285, 20.730 y 20.880. | Corporaciones municipales que ejercen funciones públicas con financiamiento fiscal deben cumplir Ley 19.886 sobre contratación pública. | corporaciones municipales, ley compras, probidad | `Varios/160316N21 - Corporaciones Municipales, Ley de Compras.md` |

## Índice alfanumérico por número de dictamen/norma

| N° | Año | Categoría | Archivo |
|---|---|---|---|
| 6 | 2025 | Directivas | `Directivas/568-B_Res_Directiva6_2025_PAC.md` |
| 10 | 2025 | Directivas | `Directivas/565-B-Res.-Aprueba-Directiva-de-Contratacion-Publica-N°-10-2025-sobre-Trato-Directo.md` |
| 14 | 2026 | Directivas | `Directivas/054-B-Res.-Aprueba-Directiva-de-Contratacion-N°-14-2026-Comisiones-Evaluadoras.md` |
| 28 | 2025 | Directivas | `Directivas/557BRes-Directiva28-2025-CodigodeEtica.md` |
| 31 | 2026 | Directivas | `Directivas/037-B-Res.-Aprueba-Directiva-de-Contratacion-N-31-2026-Codigo-etica-proveedores.md` |
| 298 | 2008 | Evaluacion | `Evaluacion/www.contraloria.cl_LegisJuri_DictamenesGeneralesMunicipales.md` |
| 394 | 2014 | Grandes Compras | `Grandes Compras/GC - Def. de EETT va en la IC 2.md` |
| 661 | 2024 | Normas marco (raiz del proyecto) | `Decreto-661_12-DIC-2024.md` |
| 661 | 2024 | Normas macro | `Normas macro/Decreto-661_12-DIC-2024 (1).md` |
| 839 | 2006 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 839 - 2006.md` |
| 1.199 | 2019 | Grandes Compras | `Grandes Compras/1.199-2019_ Acepto en evaluacion, rechazo por marca.md` |
| 1.199 | 2019 | Grandes Compras | `Grandes Compras/GC - Se invita a todos, aunque no tengan marca.md` |
| 1395 | 2021 | Evaluacion | `Evaluacion/1.395-2021_ No se apega a criterios de las bases.md` |
| 2.368 | 2008 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 2.368 - 2008.md` |
| 2410 | 2017 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/2410-17.md` |
| 3117 | 2015 | Evaluacion | `Evaluacion/Mas del ppto DISPONIBLE NO.md` |
| 3.481 | 2018 | Termino Anticipado | `Termino Anticipado/3481-2018_ Haber trabajado no basta, es entregar lo que se pidio.md` |
| 3.566 | 2004 | Ofertas | `Ofertas/3.566-2004_ Oferta debe manifestarse expresamente, partida vacia.md` |
| 3871 | 2011 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/3871-11.md` |
| Resolucion Exenta N 04483 | 2009 | TD | `TD/Res. Ex. N° 04483-2009 (TD Confianza)_ Ap. Ctto. CGR con Concorde Ltda..md` |
| 4.509 | 2017 | Grandes Compras | `Grandes Compras/GC - Anx. deben subirse de acuerdo a IC.md` |
| 4.509 | 2017 | Grandes Compras | `Grandes Compras/GC - Of. x portal, como diga IC.md` |
| Resolucion Exenta N 04675 | 2013 | TD/Art. 10, N° 7, m) | `TD/Art. 10, N° 7, m)/CGR hace contrato antes del trato directo.md` |
| 4797 | 2017 | Evaluacion | `Evaluacion/ESB.md` |
| 5.448 | 2015 | Derechos Consolidados | `Derechos Consolidados/Dictamen 5448 - Derechos consolidados contrato tramitado.md` |
| 6.365 | 2012 | Garantias | `Garantias/006365N12 - Inadmisible oferta no entrega GSO.md` |
| 6.365 | 2012 | Garantias | `Garantias/6.365-2012_ Inadmisible por no renovación GSO.md` |
| 6381 | 2018 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/6381-18.md` |
| 6810 | 2018 | Evaluacion | `Evaluacion/6.810-2018 - Aclaraciones a todos.md` |
| 6.810 | 2018 | Foro Inverso | `Foro Inverso/6.810-2018_ Igualdad de los oferentes, exclusion.md` |
| 7.561 | 2018 | Pagos | `Pagos/7.561-2018_ Pago oportuno de proveedores.md` |
| 7.626 | 2014 | Plazos no fatales | `Plazos no fatales/Plazos no fatales 2.md` |
| 7.640 | 2013 | Grandes Compras | `Grandes Compras/GC - Multas del CM aplican.md` |
| 7948 | 2018 | Evaluacion | `Evaluacion/79.48-2018 - Precios neto y bruto.md` |
| 8.664 | 2017 | Pagos | `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md` |
| D87N26 | 2026 | Compras agiles | `Compras agiles/contraloria (14).md` |
| 9.405 | 2006 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 9.405 - 2006.md` |
| 10172 | 2017 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/10172-17.md` |
| 10.706 | 2019 | UTP | `UTP/10706-2019_ UTP EP al momento de contratar.md` |
| 10.957 | 2017 | Experiencia | `Experiencia/10957-2017.md` |
| 11.189 | 2008 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 11.189 - 2008.md` |
| 11.274 | 2018 | Foro Inverso | `Foro Inverso/11.274-2018_ Ob. consultar foro inverso del proveedor.md` |
| 11358 | 2017 | Evaluacion | `Evaluacion/011358N17 - Acta Fundada2.md` |
| 11.400 | 2017 | Foro Inverso | `Foro Inverso/11.400-2017_ Suspensión del acto.md` |
| 11.409 | 2018 | Experiencia | `Experiencia/11.409-2018, Exp. Fundada.md` |
| 12.125 | 2019 | Grandes Compras | `Grandes Compras/12.125-2019_ Obligacion de CM.md` |
| 12.142 | 2019 | Ofertas | `Ofertas/12.142-2019_ UCh., mismo rut no una sola oferta.md` |
| 12.424 | 2017 | Grandes Compras | `Grandes Compras/GC - Declaracion de inhabilidades.md` |
| 12798 | 2016 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/12798-16.md` |
| 13.915 | 2013 | Grandes Compras | `Grandes Compras/GC - Evaluacion, cuadro comparativo.md` |
| 14.005 | 2011 | Garantias | `Garantias/14.005-2011_ Objetivo GSO resguardar la firma del contrato.md` |
| 14.140 | 2009 | Ofertas | `Ofertas/14.140-2009_ Oferta decimales, vicio formal.md` |
| 14.200 | 2018 | Bases | `Bases/14.200-2018, Experiencia no exigible, evaluable.md` |
| 14.200 | 2018 | Experiencia | `Experiencia/14.200-2018.md` |
| 14.202 | 2018 | Bases | `Bases/14.202-2018, No weiwer derechos Administracion.md` |
| 14232 | 2016 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/14232-16.md` |
| 14.236 | 2018 | Fragmentacion | `Fragmentacion/14.236-2018, Frag. GC. Ordena sumario.md` |
| 14.238 | 2018 | Foro Inverso | `Foro Inverso/14.238-2018_ Igualdad de los oferentes, que no hacer.md` |
| 14238 | 2018 | Derechos Consolidados | `Derechos Consolidados/14.238-2018, ESB e IOf, invalidación ctto ejec. No hay Ds C.md` |
| 14.250 | 2018 | Objeto de compra | `Objeto de compra/14.250-2018, Bienes reacondicionados. Decision de merito fundada.md` |
| 14.813 | 2019 | Criterios de evaluacion | `Criterios de evaluacion/14.813-2019_ Pautas para evaluar criterios que haga comision valen.md` |
| 14.828 | 2018 | Bases | `Bases/14.828-2018, Cuarta copia factura.md` |
| 15.331 | 2018 | Adjudicacion | `Adjudicacion/15.331-2018 - Supletoria 19.880, experiencia (Bases no definen nada, igual CGR esta bien).md` |
| 17.584 | 2018 | Ofertas | `Ofertas/17.584-2018_ Multiples ofertas merito-ESB.md` |
| 17585 | 2018 | Evaluacion | `Evaluacion/17.585-2018 - Excepcion en dejar vacio item oferta.md` |
| 18.355 | 2007 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 18.355 - 2007.md` |
| 18.889 | 2018 | Foro Inverso | `Foro Inverso/18.889-2018_ Igualdad, foro inverso.md` |
| 18.983 | 2018 | Grandes Compras | `Grandes Compras/18.983-2018_ Fracc GC, Municipalidad.md` |
| 18.983 | 2018 | Grandes Compras | `Grandes Compras/18.983-2018_ Fraccionamiento, CM, grandes compras.md` |
| 19.265 | 2013 | Foro Inverso | `Foro Inverso/19.265-2013_ FI, ley pareja.md` |
| 19.886 | 2003 | Normas marco (raiz del proyecto) | `LEY-19886_30-JUL-2003.md` |
| 19886 | 2003 | Normas macro | `Normas macro/LEY-19886_30-JUL-2003 (2).md` |
| 20.061 | 2015 | Derechos Consolidados | `Derechos Consolidados/20.061-2015.md` |
| 20.061 | 2017 | Adjudicacion | `Adjudicacion/20.061-2017_ Necesidad de motivacion hecho derecho en acto.md` |
| 20.203 | 1999 | Criterios de evaluacion | `Criterios de evaluacion/20.203-1999_ CGR no se puede meter con evaluación.md` |
| 20.341 | 2013 | Garantias | `Garantias/20.341-2013_ Error en la glosa no esencial GSO.md` |
| 20.453 | 2019 | Pagos | `Pagos/20.453-2019_ Reqs. Pago.md` |
| 20.456 | 2019 | Pagos | `Pagos/20.456-2019_ Reqs. Pago.md` |
| 20678 | 2014 | Evaluacion | `Evaluacion/Mas del ppto estimado OK.md` |
| 20.687 | 1990 | Ofertas | `Ofertas/20.687-1990_ Oferta debe manifestarse expresamente, partida vacia.md` |
| 20.715 | 2018 | UTP | `UTP/20715-2018_ UTP EP al momento de contratar.md` |
| 21.246 | 2016 | Garantias | `Garantias/Como calcula plazo - GSO.md` |
| 21.470 | 2007 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 21.470 - 2007.md` |
| 21.503 | 2003 | Bases | `Bases/21.503-2003_ Renuncia debe tener objeto claro.md` |
| 21634 | 2023 | Normas macro | `Normas macro/Ley-21634_11-DIC-2023 (3).md` |
| 21.663 | 2024 | Normas marco (raiz del proyecto) | `Ley-21663_08-ABR-2024.md` |
| 21.674 | 2018 | Bases | `Bases/21.674-2018_ Min discapacidad, evaluacion.md` |
| 21.719 | 2024 | Normas marco (raiz del proyecto) | `Ley-21719_13-DIC-2024.md` |
| 22.161 | 2017 | Foro Inverso | `Foro Inverso/22.161-2017_ FI no es posibilidad de contraoferta.md` |
| 22.161 | 2017 | Derechos Consolidados | `Derechos Consolidados/22161-2017_ Invalidacion mala adjudicacion.md` |
| 22.469 | 2016 | UTP | `UTP/22469-2016_ UTP EP al momento de contratar.md` |
| 23220 | 2011 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/23220-11.md` |
| 24243 | 2019 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/24243-19.md` |
| 24.268 | 2017 | TD | `TD/24.268-2017_ TD, debe acompañar anexo de que no es inhabil para contratar.md` |
| 24.337 | 2002 | Derechos Consolidados | `Derechos Consolidados/24337-2002_ Limite a invalidacion (Ramiro!).md` |
| 24469 | 2012 | Evaluacion | `Evaluacion/024469N12 - Acta fundada.md` |
| 24.685 | 2010 | TD/Art. 10, N° 7, g) | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (10).md` |
| 25.674 | 2017 | Foro Inverso | `Foro Inverso/25.674-2017_ Foro Inverso, antecedente que no cumple.md` |
| 26006 | 2016 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/26006-16.md` |
| 27.386 | 2018 | Garantias | `Garantias/027386N18 - Falsedad de documentos habilita para cobrar GSO cuando esta en bases.md` |
| 27.818 | 2008 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 27.818 - 2008.md` |
| 27.848 | 2005 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 27.848 - 2005.md` |
| 28.251 | 2016 | Derechos Consolidados | `Derechos Consolidados/28251-2016_ Inv. por malas bases.md` |
| 29281 | 2013 | Evaluacion | `Evaluacion/Mas del ppto estimado NO.md` |
| 29.349 | 2017 | Foro Inverso | `Foro Inverso/29.349-2017_ Foro inverso, no mutables.md` |
| 29.549 | 2000 | Acta Apertura de Ofertas | `Acta Apertura de Ofertas/29.549-2000.md` |
| 30471 | 2016 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/30471-16.md` |
| 30.836 | 2019 | Grandes Compras | `Grandes Compras/30.836-2019_ Ob. de comunicar EETT.md` |
| 31.356 | 2013 | TD/Art. 10, N° 7, g) | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (2).md` |
| 31.421 | 2018 | Garantias | `Garantias/031421N18- Causales para cobrar GSO deben estar en bases.md` |
| 31433 | 2018 | Evaluacion | `Evaluacion/31.433-2018_ Inad si no cumple req tec min.md` |
| 31725 | 2013 | Evaluacion | `Evaluacion/31.725-2013, valor portal distinto anexo oferta, inadmisible.md` |
| 31.798 | 2013 | Garantias | `Garantias/031798N13 - Error GSO y derechos consolidados.md` |
| 32.065 | 2013 | Grandes Compras | `Grandes Compras/GC - Posibilidad de modificar plazos debe estar en IC.md` |
| 32.073 | 2013 | Estricta Sujecion a las Bases | `Estricta Sujecion a las Bases/PESB - Certificado de Ob. Previsionales.md` |
| 32.261 | 1989 | Criterios de evaluacion | `Criterios de evaluacion/32.261-1989_ CGR no se puede meter con evaluación.md` |
| 33.246 | 2017 | Bases | `Bases/33.246-2017, Cuarta copia factura, sin condiciones a credito.md` |
| 35.087 | 2014 | Derechos Consolidados | `Derechos Consolidados/Dictamen 35.087-2014 - Derechos consolidados contrato tramitado.md` |
| 35861 | 2016 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/35861-16.md` |
| 35.907 | 2005 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 35.907 - 2005.md` |
| 36.248 | 2016 | Foro Inverso | `Foro Inverso/36.248-2016_ FI, complemenatción de antecedentes no evaluables.md` |
| 36.519 | 2016 | Grandes Compras | `Grandes Compras/GC - Def. de EETT va en la IC.md` |
| 36.593 | 2016 | Derechos Consolidados | `Derechos Consolidados/36.593-2016.md` |
| 37.221 | 1994 | Derechos Consolidados | `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md` |
| 37.260 | 2014 | Adjudicacion | `Adjudicacion/37.260-2014_ Operacion aritmetica.md` |
| 37397 | 2017 | Evaluacion | `Evaluacion/37.397-2017_ Retraso en evaluacion rompe equilibrio economico. Perjuicios a trib.md` |
| 37397 | 2017 | Evaluacion | `Evaluacion/37.397-2017_ Retraso en evaluacion rompe equilibrio economico (6 meses).md` |
| 37405 | 2017 | Evaluacion | `Evaluacion/37.405-2017_ Retraso Eval. rompe EE, pero no se reajusta of si consiente ex mantenerla.md` |
| 37409 | 2017 | Evaluacion | `Evaluacion/37.409-2017_ Retraso en evaluacion rompe equilibrio economico (9 meses).md` |
| 37412 | 2017 | Evaluacion | `Evaluacion/37.412-2017_ Retraso en evaluacion rompe equilibrio economico (9 meses).md` |
| 37.465 | 2013 | Bases | `Bases/37.465-2013_ Informacion, retencion y subrogacion.md` |
| 37515 | 2017 | Evaluacion | `Evaluacion/37.515-2017_ Retraso en evaluacion rompe equilibrio economico (7 meses).md` |
| 37.573 | 2011 | Garantias | `Garantias/37.573-2011_ Menciones obligatorias GSO.md` |
| 37.613 | 2017 | Adjudicacion | `Adjudicacion/37.613-2017_ Ofertas e IVA.md` |
| 37.867 | 2014 | Plazos no fatales | `Plazos no fatales/Plazos no fatales con art 41.md` |
| 39.228 | 2009 | Presupuesto | `Presupuesto/Art. 11 DS 250 2.md` |
| 39705 | 2013 | Evaluacion | `Evaluacion/39.705-2013_ Si hay error pero no cambia el tenor de la evaluación, vale igual.md` |
| 41236 | 2017 | Evaluacion | `Evaluacion/41.236-2017, valor portal distinto anexo oferta, lo que digan las bases.md` |
| 41.236 | 2017 | Foro Inverso | `Foro Inverso/41.236-2017_ Def. Vicio Formal.md` |
| 42421 | 2001 | Evaluacion | `Evaluacion/Modificacion Formulario.md` |
| 42.421 | 2001 | Errores no esenciales | `Errores no esenciales/Modificacion Formulario.md` |
| 42.462 | 2011 | Foro Inverso | `Foro Inverso/42.462-2011_ Reqs formales elevados a esenciales, bases.md` |
| 42.462 | 2011 | Bases | `Bases/42.462-2011_ Reqs formales elevados a esenciales, bases.md` |
| 42470 | 2015 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/42470-15.md` |
| 43.119 | 2014 | Grandes Compras | `Grandes Compras/GC - Si hay 30_ solo a bienes del CM.md` |
| 44.043 | 2010 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 44.043 - 2010.md` |
| 44.145 | 2010 | TD/Art. 10, N° 7, g) | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (9).md` |
| 44.411 | 2007 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 44.411 - 2007.md` |
| 44.460 | 2010 | Experiencia | `Experiencia/44.460-10_ Experiencia sociedades filiales.md` |
| 44.888 | 2009 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 44.888 - 2009.md` |
| 45041 | 2017 | Evaluacion | `Evaluacion/45.041-2017 Se pidio pdf, subio word, no vicia.md` |
| 45.237 | 2014 | Grandes Compras | `Grandes Compras/45.237-2014_ Criterios de Evaluación, no fuera de bases GC.md` |
| 45.487 | 2016 | Derechos Consolidados | `Derechos Consolidados/45.487-2016.md` |
| 46564 | 2011 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/46564-11.md` |
| 46.564 | 2011 | TD/Art. 10, N° 7, g) | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (5).md` |
| 46.819 | 2005 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictmane 46.819 - 2005.md` |
| 47.370 | 2015 | Grandes Compras | `Grandes Compras/GC - Fraccionamiento OC elusion GC.md` |
| 47.664 | 2012 | Bases | `Bases/47.664-2012_ no puedo exigir inscripcion en reg especial.md` |
| 48.093 | 2010 | TD/Art. 10, N° 7, g) | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (8).md` |
| 48.929 | 2012 | Bases | `Bases/48.929-2012_ Ob de entregar toda la info.md` |
| 49.345 | 2016 | Experiencia | `Experiencia/49.345-2016.md` |
| 49409 | 2012 | Evaluacion | `Evaluacion/49.409-2012_ Retraso en evaluacion rompe equilibrio economico (primero).md` |
| 49.703 | 2016 | Grandes Compras | `Grandes Compras/49.703 - GC, despues de seleccion OC.md` |
| 49.703 | 2016 | Grandes Compras | `Grandes Compras/49.703-2016_ Revocación no desercion ni inadmisibilidad en CG.md` |
| 49.703 | 2016 | Grandes Compras | `Grandes Compras/GC - Se puede invalidar por 19.880.md` |
| 50.110 | 2013 | Presupuesto | `Presupuesto/Art. 11 DS 250.md` |
| 51.205 | 2014 | Grandes Compras | `Grandes Compras/GC - DCP inclinate!.md` |
| 51404 | 2016 | Evaluacion | `Evaluacion/ESB - Criterio Finalista.md` |
| 52709 | 2011 | Evaluacion | `Evaluacion/Igualdad Oferentes - Definicion.md` |
| 53.300 | 2016 | Foro Inverso | `Foro Inverso/53.300-2016_ FI no pa pedir evaluables.md` |
| 54.426 | 2007 | Estricta Sujecion a las Bases | `Estricta Sujecion a las Bases/54.426-2007_ Incongruencias bases se salvan con mismas bases.md` |
| 54.690 | 2013 | Grandes Compras | `Grandes Compras/54.690-2013_ Supletoriedad licitación a GC.md` |
| 54.869 | 2015 | TD/Art. 10, N° 7, a)/TA | `TD/Art. 10, N° 7, a)/TA/54869-2015_ TD por partidas ya pagadas.md` |
| 55.867 | 2016 | Bases | `Bases/Art. 22, N° 9, Sin gente a cargo.md` |
| 57.416 | 2016 | TD/Art. 10, N° 7, g) | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g.md` |
| 57.470 | 2012 | Garantias | `Garantias/57.470-2012_ Debe consignarse monto y plazo GSO.md` |
| 58.646 | 2013 | Garantias | `Garantias/058646N13 - GSO, doctrina.md` |
| 58.646 | 2013 | Garantias | `Garantias/58.646-2013_ Plazo menor GSO vicio formal mientras firmen contrato en plazo.md` |
| OF59317 | 2026 | Compras agiles | `Compras agiles/contraloria (9).md` |
| 59.946 | 2010 | TD/Art. 10, N° 7, g) | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (7).md` |
| 59946 | 2010 | TD/Art. 10, N° 7, g) | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (6).md` |
| 61067 | 2016 | Evaluacion | `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md` |
| 61067 | 2016 | Evaluacion | `Evaluacion/Criterio que limita precio minimo NO!.md` |
| 61067 | 2016 | Evaluacion | `Evaluacion/MERITO! Eval. Experiencia.md` |
| 61.067 | 2016 | Bases | `Bases/Criticas a Bases, competencia TCP.md` |
| 61.067 | 2016 | Experiencia | `Experiencia/61067-2016.md` |
| 61.067 | 2016 | Criterios de evaluacion | `Criterios de evaluacion/61.067-2016_ Criterio que limita precio minimo NO!.md` |
| 63.391 | 2014 | Bases | `Bases/63.391-2014, Cuarta copia factura, sin condiciones a credito.md` |
| 63418 | 2014 | Evaluacion | `Evaluacion/Mas del ppto estimado.md` |
| 63.558 | 2015 | TD/Art. 10, N° 7, a)/TA | `TD/Art. 10, N° 7, a)/TA/63.558-2015_ TD no TD (Clinica Cordillera).md` |
| 63.669 | 2011 | TD/Art. 10, N° 7, g) | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (4).md` |
| 65449 | 2015 | Criterios de evaluacion | `Criterios de evaluacion/65.449-2015_ Regla de tres, experiencia.md` |
| 65.505 | 2010 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/dictamen 65.505 - 2010.md` |
| 65.731 | 2013 | Bases | `Bases/65.731-2013_ Explicar razones de EETT.md` |
| 65.771 | 2013 | Inadmisibilidad | `Inadmisibilidad/Oferta Inadmisible por EETT.md` |
| 65942 | 2013 | Evaluacion | `Evaluacion/065942N13 - Acta Fundada3.md` |
| 66064 | 2016 | Evaluacion | `Evaluacion/66.064-2016_ Orden de los factores no altera, reclamo.md` |
| 66231 | 2015 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/66231-15.md` |
| 66.909 | 2015 | Foro Inverso | `Foro Inverso/66.909-2015_ Se pide esencial por foro inverso.md` |
| 67.377 | 2016 | Grandes Compras | `Grandes Compras/GC - Se pueden solicitar aclaraciones necesarias.md` |
| 67.555 | 2015 | Foro Inverso | `Foro Inverso/67.555-2015_ FI, necesidad de descontar ptje.md` |
| 67.557 | 2015 | Foro Inverso | `Foro Inverso/67.557-2015_ FI, necesidad de descontar ptje.md` |
| 68010 | 2012 | Evaluacion | `Evaluacion/Omisión de los valores unitarios con IVA.md` |
| 68.010 | 2012 | Errores no esenciales | `Errores no esenciales/Omisión de los valores unitarios con IVA.md` |
| 68.755 | 2013 | Garantias | `Garantias/68.755-2013_ Error en la glosa no esencial GSO.md` |
| 69865 | 2012 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/69865-12.md` |
| 70019 | 2011 | Evaluacion | `Evaluacion/Doc. No esenciales.md` |
| 70.019 | 2011 | Errores no esenciales | `Errores no esenciales/Doc. No esenciales.md` |
| 70.620 | 2013 | TD/Art. 10, N° 7, g) | `TD/Art. 10, N° 7, g)/Casa moneda no es proveedor unico.md` |
| 71923 | 2013 | Evaluacion | `Evaluacion/71.923-2013_ Debio subir F30, no lo hizo, inadmisible.md` |
| 71.953 | 2011 | Presupuesto | `Presupuesto/Art. 11 DS 250 (Funcion publica).md` |
| 72362 | 2014 | Evaluacion | `Evaluacion/Errores no esenciales.md` |
| 72.362 | 2014 | Errores no esenciales | `Errores no esenciales/72.362-2014_ PNF - Formatos diferentes.md` |
| 72.362 | 2014 | Errores no esenciales | `Errores no esenciales/Errores no esenciales.md` |
| 72385 | 2016 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/72385-16.md` |
| 73.049 | 2014 | Grandes Compras | `Grandes Compras/73.049-2014_ Crit. Fuera de Bases GC.md` |
| 73.049 | 2014 | Grandes Compras | `Grandes Compras/GC - Inv. solo por MP, no excluir por criterios q no existen en IC.md` |
| 73.183 | 2013 | Garantias | `Garantias/73.183-2013_ Error glosa No esencial, No inadmisible!.md` |
| 73183 | 2013 | Evaluacion | `Evaluacion/ESB - Error en glosa no esencial.md` |
| 73638 | 2015 | Evaluacion | `Evaluacion/Mas del ppto estimado OK si no esta en base limite.md` |
| 73.638 | 2015 | Adjudicacion | `Adjudicacion/73.638-2015_ Adjudicación sobre presupuesto disponible.md` |
| 74.223 | 2016 | Foro Inverso | `Foro Inverso/74.223-2016_ FI no es posibilidad de contraoferta.md` |
| 74523 | 2015 | Evaluacion | `Evaluacion/74.523-2015_ Mod. Oferta no se puede.md` |
| 75.501 | 2013 | Plazos no fatales | `Plazos no fatales/Plazos no fatales con art 41 2.md` |
| 76.032 | 2015 | Derechos Consolidados | `Derechos Consolidados/76.032-2015.md` |
| 76.032 | 2015 | Derechos Consolidados | `Derechos Consolidados/76.032-2015_ Ds Consolidados por caducidad de plazo invalidacion.md` |
| 77815 | 2016 | Evaluacion | `Evaluacion/Merito.md` |
| 78.428 | 2012 | Grandes Compras | `Grandes Compras/GC - Evaluacion, cuadro comparativo 2.md` |
| 79.494 | 2011 | TD/Art. 10, N° 7, g) | `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (3).md` |
| 80806 | 2013 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/80806-13.md` |
| 82.062 | 2013 | Ofertas | `Ofertas/82.062-2013_ Vale oferta en Ingles.md` |
| 83.993 | 2016 | Foro Inverso | `Foro Inverso/83.993-2016_ FI, omision de solicitar documentos (Asumo societarios).md` |
| 84.775 | 2013 | Garantias | `Garantias/065771N13 - No se puede cobrar GSO a inadmisibles.md` |
| 84937 | 2016 | Evaluacion | `Evaluacion/Debe indicar mot rech experiencia.md` |
| 84.990 | 2016 | Comisiones de Evaluacion | `Comisiones de Evaluacion/Se puede por acto previo.md` |
| 85.901 | 2016 | Grandes Compras | `Grandes Compras/GC - AC no puede ser dif a IC, bases y oferta.md` |
| 85.901 | 2016 | Grandes Compras | `Grandes Compras/GC - IC puede establecer formas de entrega perticulares.md` |
| 86.827 | 2016 | Grandes Compras | `Grandes Compras/GC - Multas del CM aplican, OC aceptada.md` |
| 88.499 | 2015 | Ofertas | `Ofertas/88.499-2015_ Oferta Bruta debio ser neta, valida.md` |
| 89409 | 2016 | Evaluacion | `Evaluacion/Merito2.md` |
| 89541 | 2014 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/89541-14.md` |
| 89.567 | 2016 | Grandes Compras | `Grandes Compras/89.567-2016 - (GC) Criterios desproporcionados al CM.md` |
| 89.567 | 2016 | Convenio Marco | `Convenio Marco/Grandes Compras - No MOD CRITERIOS!.md` |
| 89918 | 2016 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/89918-16.md` |
| 89.921 | 2016 | Contratacion | `Contratacion/Deja sin efecto contratacion por papel faltante.md` |
| 89.921 | 2016 | Contratacion | `Contratacion/www.contraloria.cl_LegisJuri_DictamenesGeneralesMunicipales.md` |
| 90268 | 2015 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/90268-15.md` |
| 90883 | 2015 | Evaluacion | `Evaluacion/Calculo.md` |
| 91012 | 2016 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/91012-16.md` |
| 91843 | 2016 | Grandes Compras | `Grandes Compras/GC - Si hay rec de rep pendiente, CGR no se pronuncia.md` |
| 96.610 | 2015 | Derechos Consolidados | `Derechos Consolidados/96.610-2015.md` |
| 100098 | 2014 | TD/Art. 10, N° 7, f) | `TD/Art. 10, N° 7, f)/100098-14.md` |
| 100.441 | 2015 | Garantias | `Garantias/100.441-2015_ Garantia por tercero.md` |
| 002453N18 | 2018 | Varios | `Varios/Dictamen CGR N° 2453-2018, Probidad y Compras.md` |
| 002659N21 | 2021 | Compras agiles | `Compras agiles/contraloria (23).md` |
| 003485N14 | 2014 | Ordenes de Compra | `Ordenes de Compra/OC Documento comercial.md` |
| 003688N18 | 2018 | Preguntas y Respuestas | `Preguntas y Respuestas/3.688-2018_ Preguntas y rpta vinculantes.md` |
| 005380N00 | 2000 | Acta Apertura de Ofertas | `Acta Apertura de Ofertas/5380-2000.md` |
| 007948N18 | 2018 | Adjudicacion | `Adjudicacion/007948N18 - Tribunales inclinense!.md` |
| E11631N25 | 2025 | Compras agiles | `Compras agiles/contraloria (18).md` |
| 011782N18 | 2018 | Adjudicacion | `Adjudicacion/011782N18 - Evaluaciones suscritas por todos los nombrados.md` |
| 061067N16 | 2016 | Adjudicacion | `Adjudicacion/MERITO! Eval. Experiencia.md` |
| 067134N16 | 2016 | Adjudicacion | `Adjudicacion/Publicar razones de demora adj.md` |
| E68062N25 | 2025 | Compras agiles | `Compras agiles/contraloria (17).md` |
| E72886N25 | 2025 | Compras agiles | `Compras agiles/contraloria (16).md` |
| 076516N12 | 2012 | Ofertas | `Ofertas/076516N12 - No procede exigencia de registro para participar.md` |
| 076749N13 | 2013 | Ofertas | `Ofertas/076749N13 - Reg. Solo exigible por norma particular.md` |
| 076920N15 | 2015 | Preguntas y Respuestas | `Preguntas y Respuestas/76.920-2015_ Preguntas y rpta vinculantes.md` |
| 084937N16 | 2016 | Adjudicacion | `Adjudicacion/Debe indicar mot rech experiencia.md` |
| OF87469N26 | 2026 | Compras agiles | `Compras agiles/contraloria (13).md` |
| OF93103N26 | 2026 | Compras agiles | `Compras agiles/contraloria (12).md` |
| E108767N21 | 2021 | Compras agiles | `Compras agiles/contraloria (25).md` |
| OF120447N26 | 2026 | Compras agiles | `Compras agiles/contraloria (11).md` |
| E141710N25 | 2025 | Compras agiles | `Compras agiles/contraloria (15).md` |
| E152886N21 | 2021 | Compras agiles | `Compras agiles/contraloria (24).md` |
| E189914N22 | 2022 | Compras agiles | `Compras agiles/contraloria (22).md` |
| E240653N22 | 2022 | Compras agiles | `Compras agiles/contraloria (21).md` |
| E287821N22 | 2022 | Compras agiles | `Compras agiles/contraloria (20).md` |
| E464046N24 | 2024 | Compras agiles | `Compras agiles/contraloria (19).md` |

**Documentos sin número identificado con certeza (30):**

- `Evaluacion/Error no esencial.md` (categoría: Evaluacion)
- `Evaluacion/Mod de cronograma por acto distinto al que las aprobo.md` (categoría: Evaluacion)
- `Garantias/17407-2017_ Garantia por tercero.md` (categoría: Garantias)
- `Garantias/18872-2016_ Garantia por tercero.md` (categoría: Garantias)
- `Garantias/45257-2013_ Tercero si, pero debe ser a nombre de el.md` (categoría: Garantias)
- `Garantias/E139176N21 - Glosa no esencial en GSO.md` (categoría: Garantias)
- `Garantias/E150913N21 - Inadmisibilidad por falta de vigencia GSO.md` (categoría: Garantias)
- `Garantias/E163668N21 - Inadmisibilidad por falta de vigencia GSO.md` (categoría: Garantias)
- `Garantias/E60399N20 - Vale GSO electronica.md` (categoría: Garantias)
- `Estricta Sujecion a las Bases/Mod de cronograma por acto distinto al que las aprobo.md` (categoría: Estricta Sujecion a las Bases)
- `Compras agiles/contraloria (10).md` (categoría: Compras agiles)
- `Bases/Art. 22, N° 2.md` (categoría: Bases)
- `Termino Anticipado/Deben estar las condiciones para la resciliacion.md` (categoría: Termino Anticipado)
- `Directivas/561BRes-Directiva26-eficiencia.md` (categoría: Directivas)
- `Directivas/563BRes-Directiva35CompraAgil.md` (categoría: Directivas)
- `Directivas/72-B-directiva-pago-oportuno.md` (categoría: Directivas)
- `Directivas/Actualizacion-Directiva20.md` (categoría: Directivas)
- `Directivas/Directiva-44-Ciencia-de-Datos-IA.md` (categoría: Directivas)
- `Directivas/directiva-compras-coordinadas.md` (categoría: Directivas)
- `Directivas/Directiva45.md` (categoría: Directivas)
- `TD/Art. 10, N° 3/TD - 10 N° 3 - Fundamentacion urgencia.md` (categoría: TD/Art. 10, N° 3)
- `Ofertas/E102329N21 - LC, registro.md` (categoría: Ofertas)
- `Ofertas/GSO Glosa, Aumento, Glosa, Ofertas C. A..md` (categoría: Ofertas)
- `Varios/160316N21 - Corporaciones Municipales, Ley de Compras.md` (categoría: Varios)
- `Errores no esenciales/Error no esencial.md` (categoría: Errores no esenciales)
- `Errores no esenciales/Res. 7 CGR (Nva 1600).md` (categoría: Errores no esenciales)
- `Errores no esenciales/Res. 8 CGR (Fija montos para Nva 1600).md` (categoría: Errores no esenciales)
- `Plazos no fatales/Plazos no fatales 3.md` (categoría: Plazos no fatales)
- `Plazos no fatales/Plazos no fatales.md` (categoría: Plazos no fatales)
- `Normas macro/ICG-N-6.md` (categoría: Normas macro)

## Índice por artículo de ley/reglamento citado

Agrupa los dictámenes según los artículos de leyes/decretos que citan explícitamente
en su propio texto (extracción literal, no interpretada).

### CCI art. 1438  (1 citas en 1 variantes de artículo/inciso)

**CCI art. 1438** (1):
- 63.558 (2015) - `TD/Art. 10, N° 7, a)/TA/63.558-2015_ TD no TD (Clinica Cordillera).md`

### CCI art. 1547  (1 citas en 1 variantes de artículo/inciso)

**CCI art. 1547** (1):
- 31.421 (2018) - `Garantias/031421N18- Causales para cobrar GSO deben estar en bases.md`

### CCI art. 1608  (1 citas en 1 variantes de artículo/inciso)

**CCI art. 1608** (1):
- 37.465 (2013) - `Bases/37.465-2013_ Informacion, retencion y subrogacion.md`

### CCI art. 3 inc. fin  (1 citas en 1 variantes de artículo/inciso)

**CCI art. 3 inc. fin** (1):
- 007948N18 (2018) - `Adjudicacion/007948N18 - Tribunales inclinense!.md`

### CCI art. 3 inc. final  (1 citas en 1 variantes de artículo/inciso)

**CCI art. 3 inc. final** (1):
- 7948 (2018) - `Evaluacion/79.48-2018 - Precios neto y bruto.md`

### CPC art. 345  (1 citas en 1 variantes de artículo/inciso)

**CPC art. 345** (1):
- 25.674 (2017) - `Foro Inverso/25.674-2017_ Foro Inverso, antecedente que no cumple.md`

### CTR art. 157 bis  (1 citas en 1 variantes de artículo/inciso)

**CTR art. 157 bis** (1):
- 21.674 (2018) - `Bases/21.674-2018_ Min discapacidad, evaluacion.md`

### CTR art. 183-A  (2 citas en 1 variantes de artículo/inciso)

**CTR art. 183-A** (2):
- 37.465 (2013) - `Bases/37.465-2013_ Informacion, retencion y subrogacion.md`
- 55.867 (2016) - `Bases/Art. 22, N° 9, Sin gente a cargo.md`

### CTR art. 183-B  (2 citas en 1 variantes de artículo/inciso)

**CTR art. 183-B** (2):
- 37.465 (2013) - `Bases/37.465-2013_ Informacion, retencion y subrogacion.md`
- 55.867 (2016) - `Bases/Art. 22, N° 9, Sin gente a cargo.md`

### CTR art. 183-C  (2 citas en 1 variantes de artículo/inciso)

**CTR art. 183-C** (2):
- 37.465 (2013) - `Bases/37.465-2013_ Informacion, retencion y subrogacion.md`
- 55.867 (2016) - `Bases/Art. 22, N° 9, Sin gente a cargo.md`

### CTR art. 183-D  (1 citas en 1 variantes de artículo/inciso)

**CTR art. 183-D** (1):
- 37.465 (2013) - `Bases/37.465-2013_ Informacion, retencion y subrogacion.md`

### Codigo Procedimiento Civil art. 7 inc. 2  (1 citas en 1 variantes de artículo/inciso)

**Codigo Procedimiento Civil art. 7 inc. 2** (1):
- 44.460 (2010) - `Experiencia/44.460-10_ Experiencia sociedades filiales.md`

### Codigo del Trabajo art. 203  (1 citas en 1 variantes de artículo/inciso)

**Codigo del Trabajo art. 203** (1):
- 72385 (2016) - `TD/Art. 10, N° 7, f)/72385-16.md`

### Constitucion Politica art. 98  (2 citas en 1 variantes de artículo/inciso)

**Constitucion Politica art. 98** (2):
- 61.067 (2016) - `Experiencia/61067-2016.md`
- 61.067 (2016) - `Criterios de evaluacion/61.067-2016_ Criterio que limita precio minimo NO!.md`

### Constitucion Politica art. 98 y 99  (2 citas en 1 variantes de artículo/inciso)

**Constitucion Politica art. 98 y 99** (2):
- (sin número) (2019) - `Errores no esenciales/Res. 7 CGR (Nva 1600).md`
- (sin número) (2019) - `Errores no esenciales/Res. 8 CGR (Fija montos para Nva 1600).md`

### Constitución Política art. 100  (2 citas en 1 variantes de artículo/inciso)

**Constitución Política art. 100** (2):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`

### Constitución Política art. 32 num. 8  (1 citas en 1 variantes de artículo/inciso)

**Constitución Política art. 32 num. 8** (1):
- 24.337 (2002) - `Derechos Consolidados/24337-2002_ Limite a invalidacion (Ramiro!).md`

### Constitución Política art. 6  (1 citas en 1 variantes de artículo/inciso)

**Constitución Política art. 6** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`

### Constitución Política art. 6 inc. 1 y 2  (1 citas en 1 variantes de artículo/inciso)

**Constitución Política art. 6 inc. 1 y 2** (1):
- 24.337 (2002) - `Derechos Consolidados/24337-2002_ Limite a invalidacion (Ramiro!).md`

### Constitución Política art. 7  (1 citas en 1 variantes de artículo/inciso)

**Constitución Política art. 7** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`

### Constitución Política art. 87  (1 citas en 1 variantes de artículo/inciso)

**Constitución Política art. 87** (1):
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`

### Constitución Política art. 88  (2 citas en 1 variantes de artículo/inciso)

**Constitución Política art. 88** (2):
- 24.337 (2002) - `Derechos Consolidados/24337-2002_ Limite a invalidacion (Ramiro!).md`
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`

### Constitución Política art. 98  (1 citas en 1 variantes de artículo/inciso)

**Constitución Política art. 98** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`

### Código Civil art. 1.461 inc. 2  (1 citas en 1 variantes de artículo/inciso)

**Código Civil art. 1.461 inc. 2** (1):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`

### Código Civil art. 1.793  (1 citas en 1 variantes de artículo/inciso)

**Código Civil art. 1.793** (1):
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`

### Código Civil art. 1.801 inc. 1  (1 citas en 1 variantes de artículo/inciso)

**Código Civil art. 1.801 inc. 1** (1):
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`

### Código Civil art. 9  (1 citas en 1 variantes de artículo/inciso)

**Código Civil art. 9** (1):
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`

### Código de Comercio art. 160  (1 citas en 1 variantes de artículo/inciso)

**Código de Comercio art. 160** (1):
- 8.664 (2017) - `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md`

### DFL 1/1965 art. 10  (1 citas en 1 variantes de artículo/inciso)

**DFL 1/1965 art. 10** (1):
- 24.337 (2002) - `Derechos Consolidados/24337-2002_ Limite a invalidacion (Ramiro!).md`

### DFL 1/1965 art. 2  (2 citas en 1 variantes de artículo/inciso)

**DFL 1/1965 art. 2** (2):
- 24.337 (2002) - `Derechos Consolidados/24337-2002_ Limite a invalidacion (Ramiro!).md`
- 39.228 (2009) - `Presupuesto/Art. 11 DS 250 2.md`

### DFL 1/19653/2000  (2 citas en 1 variantes de artículo/inciso)

**DFL 1/19653/2000** (2):
- 59.946 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (7).md`
- 44.145 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (9).md`

### DFL 1/2000 art. 10  (1 citas en 1 variantes de artículo/inciso)

**DFL 1/2000 art. 10** (1):
- 24.337 (2002) - `Derechos Consolidados/24337-2002_ Limite a invalidacion (Ramiro!).md`

### DFL 1/2000 art. 2  (1 citas en 1 variantes de artículo/inciso)

**DFL 1/2000 art. 2** (1):
- 24.337 (2002) - `Derechos Consolidados/24337-2002_ Limite a invalidacion (Ramiro!).md`

### DFL 1/3063/80 Inter art. 12  (1 citas en 1 variantes de artículo/inciso)

**DFL 1/3063/80 Inter art. 12** (1):
- (sin número) (2021) - `Varios/160316N21 - Corporaciones Municipales, Ley de Compras.md`

### DFL 458/75 VIVIE art. 116  (1 citas en 1 variantes de artículo/inciso)

**DFL 458/75 VIVIE art. 116** (1):
- 66.909 (2015) - `Foro Inverso/66.909-2015_ Se pide esencial por foro inverso.md`

### DFL 458/75 VIVIE art. 159 bis inc. 3  (1 citas en 1 variantes de artículo/inciso)

**DFL 458/75 VIVIE art. 159 bis inc. 3** (1):
- 41.236 (2017) - `Foro Inverso/41.236-2017_ Def. Vicio Formal.md`

### DFL 458/75 VIVIENDA art. 159 bis inc. 3  (1 citas en 1 variantes de artículo/inciso)

**DFL 458/75 VIVIENDA art. 159 bis inc. 3** (1):
- 41236 (2017) - `Evaluacion/41.236-2017, valor portal distinto anexo oferta, lo que digan las bases.md`

### DFL 458/75 art. 116  (1 citas en 1 variantes de artículo/inciso)

**DFL 458/75 art. 116** (1):
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`

### DFL 7912/27 art. 17  (1 citas en 1 variantes de artículo/inciso)

**DFL 7912/27 art. 17** (1):
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`

### DFL N°1/19.653/2000  (1 citas en 1 variantes de artículo/inciso)

**DFL N°1/19.653/2000** (1):
- 19.886 (2003) - `LEY-19886_30-JUL-2003.md`

### DL 1.263/75 art. 4 inc. 1  (1 citas en 1 variantes de artículo/inciso)

**DL 1.263/75 art. 4 inc. 1** (1):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`

### DL 1.305/75 art. 25  (1 citas en 1 variantes de artículo/inciso)

**DL 1.305/75 art. 25** (1):
- 20.687 (1990) - `Ofertas/20.687-1990_ Oferta debe manifestarse expresamente, partida vacia.md`

### DL 1.762/77  (1 citas en 1 variantes de artículo/inciso)

**DL 1.762/77** (1):
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`

### DL 3.464/80  (2 citas en 1 variantes de artículo/inciso)

**DL 3.464/80** (2):
- 24.337 (2002) - `Derechos Consolidados/24337-2002_ Limite a invalidacion (Ramiro!).md`
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`

### DL 557/74  (1 citas en 1 variantes de artículo/inciso)

**DL 557/74** (1):
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`

### DL 825/74  (1 citas en 1 variantes de artículo/inciso)

**DL 825/74** (1):
- 20.687 (1990) - `Ofertas/20.687-1990_ Oferta debe manifestarse expresamente, partida vacia.md`

### Decreto 1/2005  (1 citas en 1 variantes de artículo/inciso)

**DTO 1/2005 Salud art. 31 inc. 5** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`

### Decreto 10/2012  (2 citas en 2 variantes de artículo/inciso)

**DTO 10/2012 Salud art. 3** (1):
- 8.664 (2017) - `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md`
**DTO 10/2012 Salud art. 5** (1):
- 8.664 (2017) - `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md`

### Decreto 100/2005  (1 citas en 1 variantes de artículo/inciso)

**DTO 100/2005 SEPRE** (1):
- 42.462 (2011) - `Foro Inverso/42.462-2011_ Reqs formales elevados a esenciales, bases.md`

### Decreto 135  (1 citas en 1 variantes de artículo/inciso)

**DTO 135/78 Vivie** (1):
- 076749N13 (2013) - `Ofertas/076749N13 - Reg. Solo exigible por norma particular.md`

### Decreto 156/1990  (1 citas en 1 variantes de artículo/inciso)

**DTO 156/1990 art. 14** (1):
- 70.620 (2013) - `TD/Art. 10, N° 7, g)/Casa moneda no es proveedor unico.md`

### Decreto 174/2005  (1 citas en 1 variantes de artículo/inciso)

**DTO 174/2005 art. 43** (1):
- 37.573 (2011) - `Garantias/37.573-2011_ Menciones obligatorias GSO.md`

### Decreto 2/2005  (3 citas en 3 variantes de artículo/inciso)

**DTO 2/2005 DEFEN art. 6 inc. 1** (1):
- 11.400 (2017) - `Foro Inverso/11.400-2017_ Suspensión del acto.md`
**DTO 2/2005 DEFEN art. 6 inc. 3** (1):
- 11.400 (2017) - `Foro Inverso/11.400-2017_ Suspensión del acto.md`
**DTO 2/2005 DEFEN art. 6 inc. 4** (1):
- 11.400 (2017) - `Foro Inverso/11.400-2017_ Suspensión del acto.md`

### Decreto 236/2002  (4 citas en 4 variantes de artículo/inciso)

**DTO 236/2002 VIVIENDA art. 2** (1):
- 49409 (2012) - `Evaluacion/49.409-2012_ Retraso en evaluacion rompe equilibrio economico (primero).md`
**DTO 236/2002 Vivie** (1):
- 076749N13 (2013) - `Ofertas/076749N13 - Reg. Solo exigible por norma particular.md`
**DTO 236/2002 Vivie art. 31 num. 2.2 lt. a** (1):
- 14.140 (2009) - `Ofertas/14.140-2009_ Oferta decimales, vicio formal.md`
**DTO 236/2002 Vivie art. 31 num. 2.2 lt. b** (1):
- 14.140 (2009) - `Ofertas/14.140-2009_ Oferta decimales, vicio formal.md`

### Decreto 250/2002  (1 citas en 1 variantes de artículo/inciso)

**DTO 250/2002 art. 29** (1):
- 54.869 (2015) - `TD/Art. 10, N° 7, a)/TA/54869-2015_ TD por partidas ya pagadas.md`

### Decreto 250/2004  (332 citas en 161 variantes de artículo/inciso)

> [!WARNING] Reglamento DEROGADO por el Decreto 661/2024 (ver 'ALERTA DE VIGENCIA
> NORMATIVA' al inicio de este índice). El criterio interpretativo puede seguir
> siendo aplicable; verificar la disposición correlativa en el Decreto 661/2024
> antes de citar el artículo antiguo como vigente.

**DTO 250/2004 HACIE art. 13 ter** (1):
- 14.250 (2018) - `Objeto de compra/14.250-2018, Bienes reacondicionados. Decision de merito fundada.md`
**DTO 250/2004 HACIE art. 20 inc. 1** (1):
- 14.250 (2018) - `Objeto de compra/14.250-2018, Bienes reacondicionados. Decision de merito fundada.md`
**DTO 250/2004 HACIE art. 20 inc. 2** (2):
- 14.250 (2018) - `Objeto de compra/14.250-2018, Bienes reacondicionados. Decision de merito fundada.md`
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`
**DTO 250/2004 HACIE art. 20 inc. 3** (1):
- 14.250 (2018) - `Objeto de compra/14.250-2018, Bienes reacondicionados. Decision de merito fundada.md`
**DTO 250/2004 HACIE art. 22 num. 2** (1):
- 14.250 (2018) - `Objeto de compra/14.250-2018, Bienes reacondicionados. Decision de merito fundada.md`
**DTO 250/2004 HACIE art. 22 num. 7** (1):
- 084937N16 (2016) - `Adjudicacion/Debe indicar mot rech experiencia.md`
**DTO 250/2004 HACIE art. 32 inc. 2** (1):
- 41.236 (2017) - `Foro Inverso/41.236-2017_ Def. Vicio Formal.md`
**DTO 250/2004 HACIE art. 37** (2):
- 6.810 (2018) - `Foro Inverso/6.810-2018_ Igualdad de los oferentes, exclusion.md`
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`
**DTO 250/2004 HACIE art. 37 inc. 1** (1):
- 41.236 (2017) - `Foro Inverso/41.236-2017_ Def. Vicio Formal.md`
**DTO 250/2004 HACIE art. 38** (1):
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`
**DTO 250/2004 HACIE art. 40** (1):
- 41.236 (2017) - `Foro Inverso/41.236-2017_ Def. Vicio Formal.md`
**DTO 250/2004 HACIE art. 40 bis num. 4** (1):
- 084937N16 (2016) - `Adjudicacion/Debe indicar mot rech experiencia.md`
**DTO 250/2004 HACIE art. 40 inc. 1** (1):
- 74.223 (2016) - `Foro Inverso/74.223-2016_ FI no es posibilidad de contraoferta.md`
**DTO 250/2004 HACIE art. 40 inc. 2** (1):
- 29.349 (2017) - `Foro Inverso/29.349-2017_ Foro inverso, no mutables.md`
**DTO 250/2004 HACIE art. 41** (1):
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`
**DTO 250/2004 HACIE art. 66 inc. 2** (1):
- 076516N12 (2012) - `Ofertas/076516N12 - No procede exigencia de registro para participar.md`
**DTO 250/2004 HACIE art. 66 inc. 3** (1):
- 076516N12 (2012) - `Ofertas/076516N12 - No procede exigencia de registro para participar.md`
**DTO 250/2004 HACIENDA art. 20 inc. 2** (1):
- 61067 (2016) - `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md`
**DTO 250/2004 HACIENDA art. 20 inc. final** (1):
- 7948 (2018) - `Evaluacion/79.48-2018 - Precios neto y bruto.md`
**DTO 250/2004 HACIENDA art. 32 inc. 2** (1):
- 41236 (2017) - `Evaluacion/41.236-2017, valor portal distinto anexo oferta, lo que digan las bases.md`
**DTO 250/2004 HACIENDA art. 37** (1):
- 61067 (2016) - `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md`
**DTO 250/2004 HACIENDA art. 37 inc. 1** (1):
- 41236 (2017) - `Evaluacion/41.236-2017, valor portal distinto anexo oferta, lo que digan las bases.md`
**DTO 250/2004 HACIENDA art. 37 inc. 3** (1):
- 7948 (2018) - `Evaluacion/79.48-2018 - Precios neto y bruto.md`
**DTO 250/2004 HACIENDA art. 38** (1):
- 61067 (2016) - `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md`
**DTO 250/2004 HACIENDA art. 40** (1):
- 41236 (2017) - `Evaluacion/41.236-2017, valor portal distinto anexo oferta, lo que digan las bases.md`
**DTO 250/2004 HACIENDA art. 40 inc. 1** (2):
- 71923 (2013) - `Evaluacion/71.923-2013_ Debio subir F30, no lo hizo, inadmisible.md`
- 3117 (2015) - `Evaluacion/Mas del ppto DISPONIBLE NO.md`
**DTO 250/2004 HACIENDA art. 40 inc. 2** (1):
- 71923 (2013) - `Evaluacion/71.923-2013_ Debio subir F30, no lo hizo, inadmisible.md`
**DTO 250/2004 HACIENDA art. 41** (1):
- 61067 (2016) - `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md`
**DTO 250/2004 HACIENDA art. 45** (1):
- 52709 (2011) - `Evaluacion/Igualdad Oferentes - Definicion.md`
**DTO 250/2004 Hacie art. 13** (1):
- 14.236 (2018) - `Fragmentacion/14.236-2018, Frag. GC. Ordena sumario.md`
**DTO 250/2004 Hacie art. 14 bis inc. 1** (1):
- 14.236 (2018) - `Fragmentacion/14.236-2018, Frag. GC. Ordena sumario.md`
**DTO 250/2004 Hacie art. 14 bis inc. fin** (1):
- 14.236 (2018) - `Fragmentacion/14.236-2018, Frag. GC. Ordena sumario.md`
**DTO 250/2004 Hacie art. 16 inc. 1** (1):
- 11.274 (2018) - `Foro Inverso/11.274-2018_ Ob. consultar foro inverso del proveedor.md`
**DTO 250/2004 Hacie art. 19** (2):
- 11.274 (2018) - `Foro Inverso/11.274-2018_ Ob. consultar foro inverso del proveedor.md`
- 15.331 (2018) - `Adjudicacion/15.331-2018 - Supletoria 19.880, experiencia (Bases no definen nada, igual CGR esta bien).md`
**DTO 250/2004 Hacie art. 2 num. 14** (1):
- 11.274 (2018) - `Foro Inverso/11.274-2018_ Ob. consultar foro inverso del proveedor.md`
**DTO 250/2004 Hacie art. 20** (1):
- 82.062 (2013) - `Ofertas/82.062-2013_ Vale oferta en Ingles.md`
**DTO 250/2004 Hacie art. 20 inc. 1** (1):
- 15.331 (2018) - `Adjudicacion/15.331-2018 - Supletoria 19.880, experiencia (Bases no definen nada, igual CGR esta bien).md`
**DTO 250/2004 Hacie art. 20 inc. 2** (1):
- 17.584 (2018) - `Ofertas/17.584-2018_ Multiples ofertas merito-ESB.md`
**DTO 250/2004 Hacie art. 20 inc. 3** (1):
- 15.331 (2018) - `Adjudicacion/15.331-2018 - Supletoria 19.880, experiencia (Bases no definen nada, igual CGR esta bien).md`
**DTO 250/2004 Hacie art. 20 inc. fin** (1):
- 007948N18 (2018) - `Adjudicacion/007948N18 - Tribunales inclinense!.md`
**DTO 250/2004 Hacie art. 22 num. 2** (2):
- 18.889 (2018) - `Foro Inverso/18.889-2018_ Igualdad, foro inverso.md`
- 37.260 (2014) - `Adjudicacion/37.260-2014_ Operacion aritmetica.md`
**DTO 250/2004 Hacie art. 22 num. 7** (3):
- 14.238 (2018) - `Foro Inverso/14.238-2018_ Igualdad de los oferentes, que no hacer.md`
- 18.889 (2018) - `Foro Inverso/18.889-2018_ Igualdad, foro inverso.md`
- 15.331 (2018) - `Adjudicacion/15.331-2018 - Supletoria 19.880, experiencia (Bases no definen nada, igual CGR esta bien).md`
**DTO 250/2004 Hacie art. 23 num. 4** (1):
- 17.584 (2018) - `Ofertas/17.584-2018_ Multiples ofertas merito-ESB.md`
**DTO 250/2004 Hacie art. 37** (1):
- 011782N18 (2018) - `Adjudicacion/011782N18 - Evaluaciones suscritas por todos los nombrados.md`
**DTO 250/2004 Hacie art. 37 inc. 2** (1):
- 14.238 (2018) - `Foro Inverso/14.238-2018_ Igualdad de los oferentes, que no hacer.md`
**DTO 250/2004 Hacie art. 37 inc. 3** (1):
- 007948N18 (2018) - `Adjudicacion/007948N18 - Tribunales inclinense!.md`
**DTO 250/2004 Hacie art. 38** (1):
- 37.260 (2014) - `Adjudicacion/37.260-2014_ Operacion aritmetica.md`
**DTO 250/2004 Hacie art. 4** (1):
- 002453N18 (2018) - `Varios/Dictamen CGR N° 2453-2018, Probidad y Compras.md`
**DTO 250/2004 Hacie art. 40** (2):
- 25.674 (2017) - `Foro Inverso/25.674-2017_ Foro Inverso, antecedente que no cumple.md`
- 36.248 (2016) - `Foro Inverso/36.248-2016_ FI, complemenatción de antecedentes no evaluables.md`
**DTO 250/2004 Hacie art. 40 inc. 2** (3):
- 14.238 (2018) - `Foro Inverso/14.238-2018_ Igualdad de los oferentes, que no hacer.md`
- 18.889 (2018) - `Foro Inverso/18.889-2018_ Igualdad, foro inverso.md`
- 19.265 (2013) - `Foro Inverso/19.265-2013_ FI, ley pareja.md`
**DTO 250/2004 Hacie art. 41 inc. 2** (1):
- 067134N16 (2016) - `Adjudicacion/Publicar razones de demora adj.md`
**DTO 250/2004 Hacie art. 41 inc. 4** (1):
- 19.265 (2013) - `Foro Inverso/19.265-2013_ FI, ley pareja.md`
**DTO 250/2004 Hacie art. 54** (1):
- 11.274 (2018) - `Foro Inverso/11.274-2018_ Ob. consultar foro inverso del proveedor.md`
**DTO 250/2004 Hacie art. 79 bis** (1):
- 53.300 (2016) - `Foro Inverso/53.300-2016_ FI no pa pedir evaluables.md`
**DTO 250/2004 Hacienda art. 41** (1):
- 17585 (2018) - `Evaluacion/17.585-2018 - Excepcion en dejar vacio item oferta.md`
**DTO 250/2004 Hacienda art. 41 inc. 1** (1):
- 11358 (2017) - `Evaluacion/011358N17 - Acta Fundada2.md`
**DTO 250/2004 Hacienda art. 63 inc. 1** (1):
- 17585 (2018) - `Evaluacion/17.585-2018 - Excepcion en dejar vacio item oferta.md`
**DTO 250/2004 art. 10 num. 4** (1):
- 31.356 (2013) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (2).md`
**DTO 250/2004 art. 10 num. 7 letra f** (1):
- Resolucion Exenta N 04483 (2009) - `TD/Res. Ex. N° 04483-2009 (TD Confianza)_ Ap. Ctto. CGR con Concorde Ltda..md`
**DTO 250/2004 art. 10 num. 7 letra g** (7):
- 24.685 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (10).md`
- 79.494 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (3).md`
- 63.669 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (4).md`
- 59.946 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (7).md`
- 48.093 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (8).md`
- 44.145 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (9).md`
- 57.416 (2016) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g.md`
**DTO 250/2004 art. 10 num. 7 letra m** (1):
- Resolucion Exenta N 04675 (2013) - `TD/Art. 10, N° 7, m)/CGR hace contrato antes del trato directo.md`
**DTO 250/2004 art. 10 num. 7 letras e, f, g** (1):
- 46.564 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (5).md`
**DTO 250/2004 art. 10 num. 7 letras e, f, g, h** (1):
- 31.356 (2013) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (2).md`
**DTO 250/2004 art. 10, num. 3** (1):
- 44.888 (2009) - `TD/Art. 10, N° 7, f)/dictamen 44.888 - 2009.md`
**DTO 250/2004 art. 10, num. 4** (1):
- 65.505 (2010) - `TD/Art. 10, N° 7, f)/dictamen 65.505 - 2010.md`
**DTO 250/2004 art. 10, num. 7, letra a)** (1):
- 80806 (2013) - `TD/Art. 10, N° 7, f)/80806-13.md`
**DTO 250/2004 art. 10, num. 7, letra f)** (34):
- 100098 (2014) - `TD/Art. 10, N° 7, f)/100098-14.md`
- 10172 (2017) - `TD/Art. 10, N° 7, f)/10172-17.md`
- 12798 (2016) - `TD/Art. 10, N° 7, f)/12798-16.md`
- 14232 (2016) - `TD/Art. 10, N° 7, f)/14232-16.md`
- 23220 (2011) - `TD/Art. 10, N° 7, f)/23220-11.md`
- 2410 (2017) - `TD/Art. 10, N° 7, f)/2410-17.md`
- 24243 (2019) - `TD/Art. 10, N° 7, f)/24243-19.md`
- 26006 (2016) - `TD/Art. 10, N° 7, f)/26006-16.md`
- 30471 (2016) - `TD/Art. 10, N° 7, f)/30471-16.md`
- 35861 (2016) - `TD/Art. 10, N° 7, f)/35861-16.md`
- 3871 (2011) - `TD/Art. 10, N° 7, f)/3871-11.md`
- 42470 (2015) - `TD/Art. 10, N° 7, f)/42470-15.md`
- 6381 (2018) - `TD/Art. 10, N° 7, f)/6381-18.md`
- 66231 (2015) - `TD/Art. 10, N° 7, f)/66231-15.md`
- 69865 (2012) - `TD/Art. 10, N° 7, f)/69865-12.md`
- 72385 (2016) - `TD/Art. 10, N° 7, f)/72385-16.md`
- 80806 (2013) - `TD/Art. 10, N° 7, f)/80806-13.md`
- 89541 (2014) - `TD/Art. 10, N° 7, f)/89541-14.md`
- 89918 (2016) - `TD/Art. 10, N° 7, f)/89918-16.md`
- 90268 (2015) - `TD/Art. 10, N° 7, f)/90268-15.md`
- 91012 (2016) - `TD/Art. 10, N° 7, f)/91012-16.md`
- 11.189 (2008) - `TD/Art. 10, N° 7, f)/dictamen 11.189 - 2008.md`
- 18.355 (2007) - `TD/Art. 10, N° 7, f)/dictamen 18.355 - 2007.md`
- 2.368 (2008) - `TD/Art. 10, N° 7, f)/dictamen 2.368 - 2008.md`
- 21.470 (2007) - `TD/Art. 10, N° 7, f)/dictamen 21.470 - 2007.md`
- 27.818 (2008) - `TD/Art. 10, N° 7, f)/dictamen 27.818 - 2008.md`
- 27.848 (2005) - `TD/Art. 10, N° 7, f)/dictamen 27.848 - 2005.md`
- 35.907 (2005) - `TD/Art. 10, N° 7, f)/dictamen 35.907 - 2005.md`
- 44.043 (2010) - `TD/Art. 10, N° 7, f)/dictamen 44.043 - 2010.md`
- 44.411 (2007) - `TD/Art. 10, N° 7, f)/dictamen 44.411 - 2007.md`
- 44.888 (2009) - `TD/Art. 10, N° 7, f)/dictamen 44.888 - 2009.md`
- 65.505 (2010) - `TD/Art. 10, N° 7, f)/dictamen 65.505 - 2010.md`
- 9.405 (2006) - `TD/Art. 10, N° 7, f)/dictamen 9.405 - 2006.md`
- 46.819 (2005) - `TD/Art. 10, N° 7, f)/dictmane 46.819 - 2005.md`
**DTO 250/2004 art. 10, num. 7, letras d, e, f)** (1):
- 839 (2006) - `TD/Art. 10, N° 7, f)/dictamen 839 - 2006.md`
**DTO 250/2004 art. 10, num. 7, letras e, f, g** (1):
- 46564 (2011) - `TD/Art. 10, N° 7, f)/46564-11.md`
**DTO 250/2004 art. 105 num. 2** (1):
- Resolucion Exenta N 04675 (2013) - `TD/Art. 10, N° 7, m)/CGR hace contrato antes del trato directo.md`
**DTO 250/2004 art. 107** (2):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
- Resolucion Exenta N 04675 (2013) - `TD/Art. 10, N° 7, m)/CGR hace contrato antes del trato directo.md`
**DTO 250/2004 art. 11** (2):
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`
- 39.228 (2009) - `Presupuesto/Art. 11 DS 250 2.md`
**DTO 250/2004 art. 11 inc. 2** (1):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
**DTO 250/2004 art. 12** (3):
- 14.828 (2018) - `Bases/14.828-2018, Cuarta copia factura.md`
- 22.161 (2017) - `Derechos Consolidados/22161-2017_ Invalidacion mala adjudicacion.md`
- 36.593 (2016) - `Derechos Consolidados/36.593-2016.md`
**DTO 250/2004 art. 12 bis** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**DTO 250/2004 art. 13** (3):
- 18.983 (2018) - `Grandes Compras/18.983-2018_ Fracc GC, Municipalidad.md`
- 18.983 (2018) - `Grandes Compras/18.983-2018_ Fraccionamiento, CM, grandes compras.md`
- (sin número) (2016) - `Termino Anticipado/Deben estar las condiciones para la resciliacion.md`
**DTO 250/2004 art. 14** (1):
- 43.119 (2014) - `Grandes Compras/GC - Si hay 30_ solo a bienes del CM.md`
**DTO 250/2004 art. 14 bis** (8):
- 74523 (2015) - `Evaluacion/74.523-2015_ Mod. Oferta no se puede.md`
- 1.199 (2019) - `Grandes Compras/1.199-2019_ Acepto en evaluacion, rechazo por marca.md`
- 4.509 (2017) - `Grandes Compras/GC - Anx. deben subirse de acuerdo a IC.md`
- 36.519 (2016) - `Grandes Compras/GC - Def. de EETT va en la IC.md`
- 78.428 (2012) - `Grandes Compras/GC - Evaluacion, cuadro comparativo 2.md`
- 7.640 (2013) - `Grandes Compras/GC - Multas del CM aplican.md`
- 4.509 (2017) - `Grandes Compras/GC - Of. x portal, como diga IC.md`
- 1.199 (2019) - `Grandes Compras/GC - Se invita a todos, aunque no tengan marca.md`
**DTO 250/2004 art. 14 bis inc. 1** (16):
- 12.125 (2019) - `Grandes Compras/12.125-2019_ Obligacion de CM.md`
- 18.983 (2018) - `Grandes Compras/18.983-2018_ Fracc GC, Municipalidad.md`
- 18.983 (2018) - `Grandes Compras/18.983-2018_ Fraccionamiento, CM, grandes compras.md`
- 30.836 (2019) - `Grandes Compras/30.836-2019_ Ob. de comunicar EETT.md`
- 45.237 (2014) - `Grandes Compras/45.237-2014_ Criterios de Evaluación, no fuera de bases GC.md`
- 49.703 (2016) - `Grandes Compras/49.703 - GC, despues de seleccion OC.md`
- 49.703 (2016) - `Grandes Compras/49.703-2016_ Revocación no desercion ni inadmisibilidad en CG.md`
- 54.690 (2013) - `Grandes Compras/54.690-2013_ Supletoriedad licitación a GC.md`
- 73.049 (2014) - `Grandes Compras/73.049-2014_ Crit. Fuera de Bases GC.md`
- 394 (2014) - `Grandes Compras/GC - Def. de EETT va en la IC 2.md`
- 47.370 (2015) - `Grandes Compras/GC - Fraccionamiento OC elusion GC.md`
- 73.049 (2014) - `Grandes Compras/GC - Inv. solo por MP, no excluir por criterios q no existen en IC.md`
- 86.827 (2016) - `Grandes Compras/GC - Multas del CM aplican, OC aceptada.md`
- 49.703 (2016) - `Grandes Compras/GC - Se puede invalidar por 19.880.md`
- 67.377 (2016) - `Grandes Compras/GC - Se pueden solicitar aclaraciones necesarias.md`
- 43.119 (2014) - `Grandes Compras/GC - Si hay 30_ solo a bienes del CM.md`
**DTO 250/2004 art. 14 bis inc. 3** (6):
- 45.237 (2014) - `Grandes Compras/45.237-2014_ Criterios de Evaluación, no fuera de bases GC.md`
- 54.690 (2013) - `Grandes Compras/54.690-2013_ Supletoriedad licitación a GC.md`
- 85.901 (2016) - `Grandes Compras/GC - AC no puede ser dif a IC, bases y oferta.md`
- 13.915 (2013) - `Grandes Compras/GC - Evaluacion, cuadro comparativo.md`
- 47.370 (2015) - `Grandes Compras/GC - Fraccionamiento OC elusion GC.md`
- 85.901 (2016) - `Grandes Compras/GC - IC puede establecer formas de entrega perticulares.md`
**DTO 250/2004 art. 14 bis inc. 4** (3):
- 49.703 (2016) - `Grandes Compras/49.703 - GC, despues de seleccion OC.md`
- 49.703 (2016) - `Grandes Compras/49.703-2016_ Revocación no desercion ni inadmisibilidad en CG.md`
- 49.703 (2016) - `Grandes Compras/GC - Se puede invalidar por 19.880.md`
**DTO 250/2004 art. 14 bis inc. final** (5):
- 18.983 (2018) - `Grandes Compras/18.983-2018_ Fracc GC, Municipalidad.md`
- 18.983 (2018) - `Grandes Compras/18.983-2018_ Fraccionamiento, CM, grandes compras.md`
- 73.049 (2014) - `Grandes Compras/73.049-2014_ Crit. Fuera de Bases GC.md`
- 73.049 (2014) - `Grandes Compras/GC - Inv. solo por MP, no excluir por criterios q no existen en IC.md`
- 43.119 (2014) - `Grandes Compras/GC - Si hay 30_ solo a bienes del CM.md`
**DTO 250/2004 art. 14 bis inc. penúltimo** (1):
- 30.836 (2019) - `Grandes Compras/30.836-2019_ Ob. de comunicar EETT.md`
**DTO 250/2004 art. 14 inc. 4** (2):
- 30.836 (2019) - `Grandes Compras/30.836-2019_ Ob. de comunicar EETT.md`
- 86.827 (2016) - `Grandes Compras/GC - Multas del CM aplican, OC aceptada.md`
**DTO 250/2004 art. 14 inc. 6** (1):
- 86.827 (2016) - `Grandes Compras/GC - Multas del CM aplican, OC aceptada.md`
**DTO 250/2004 art. 15** (1):
- 12.125 (2019) - `Grandes Compras/12.125-2019_ Obligacion de CM.md`
**DTO 250/2004 art. 16 inc. 1** (3):
- 1.199 (2019) - `Grandes Compras/1.199-2019_ Acepto en evaluacion, rechazo por marca.md`
- 1.199 (2019) - `Grandes Compras/GC - Se invita a todos, aunque no tengan marca.md`
- 67.377 (2016) - `Grandes Compras/GC - Se pueden solicitar aclaraciones necesarias.md`
**DTO 250/2004 art. 18** (1):
- 7.640 (2013) - `Grandes Compras/GC - Multas del CM aplican.md`
**DTO 250/2004 art. 18 inc. 1** (4):
- 1.199 (2019) - `Grandes Compras/1.199-2019_ Acepto en evaluacion, rechazo por marca.md`
- 85.901 (2016) - `Grandes Compras/GC - AC no puede ser dif a IC, bases y oferta.md`
- 85.901 (2016) - `Grandes Compras/GC - IC puede establecer formas de entrega perticulares.md`
- 1.199 (2019) - `Grandes Compras/GC - Se invita a todos, aunque no tengan marca.md`
**DTO 250/2004 art. 18 inc. 2** (2):
- 85.901 (2016) - `Grandes Compras/GC - AC no puede ser dif a IC, bases y oferta.md`
- 85.901 (2016) - `Grandes Compras/GC - IC puede establecer formas de entrega perticulares.md`
**DTO 250/2004 art. 2** (1):
- 55.867 (2016) - `Bases/Art. 22, N° 9, Sin gente a cargo.md`
**DTO 250/2004 art. 2 num. 14** (6):
- 49.703 (2016) - `Grandes Compras/49.703 - GC, despues de seleccion OC.md`
- 49.703 (2016) - `Grandes Compras/49.703-2016_ Revocación no desercion ni inadmisibilidad en CG.md`
- 12.424 (2017) - `Grandes Compras/GC - Declaracion de inhabilidades.md`
- 47.370 (2015) - `Grandes Compras/GC - Fraccionamiento OC elusion GC.md`
- 86.827 (2016) - `Grandes Compras/GC - Multas del CM aplican, OC aceptada.md`
- 49.703 (2016) - `Grandes Compras/GC - Se puede invalidar por 19.880.md`
**DTO 250/2004 art. 2 num. 3** (1):
- 31.798 (2013) - `Garantias/031798N13 - Error GSO y derechos consolidados.md`
**DTO 250/2004 art. 20** (3):
- 31.421 (2018) - `Garantias/031421N18- Causales para cobrar GSO deben estar en bases.md`
- 65.731 (2013) - `Bases/65.731-2013_ Explicar razones de EETT.md`
- (sin número) (2016) - `Bases/Art. 22, N° 2.md`
**DTO 250/2004 art. 20 inc. 2** (3):
- 61067 (2016) - `Evaluacion/Criterio que limita precio minimo NO!.md`
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
- 36.519 (2016) - `Grandes Compras/GC - Def. de EETT va en la IC.md`
**DTO 250/2004 art. 20 inc. 3** (1):
- 36.519 (2016) - `Grandes Compras/GC - Def. de EETT va en la IC.md`
**DTO 250/2004 art. 20 inc. final** (2):
- 45041 (2017) - `Evaluacion/45.041-2017 Se pidio pdf, subio word, no vicia.md`
- 72362 (2014) - `Evaluacion/Errores no esenciales.md`
**DTO 250/2004 art. 22** (5):
- 31.421 (2018) - `Garantias/031421N18- Causales para cobrar GSO deben estar en bases.md`
- 65.731 (2013) - `Bases/65.731-2013_ Explicar razones de EETT.md`
- (sin número) (2016) - `Bases/Art. 22, N° 2.md`
- 55.867 (2016) - `Bases/Art. 22, N° 9, Sin gente a cargo.md`
- 84.990 (2016) - `Comisiones de Evaluacion/Se puede por acto previo.md`
**DTO 250/2004 art. 22 num. 2** (2):
- 1.199 (2019) - `Grandes Compras/1.199-2019_ Acepto en evaluacion, rechazo por marca.md`
- 1.199 (2019) - `Grandes Compras/GC - Se invita a todos, aunque no tengan marca.md`
**DTO 250/2004 art. 22 num. 3** (1):
- 57.470 (2012) - `Garantias/57.470-2012_ Debe consignarse monto y plazo GSO.md`
**DTO 250/2004 art. 22 num. 4** (2):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**DTO 250/2004 art. 22 num. 6** (3):
- 58.646 (2013) - `Garantias/058646N13 - GSO, doctrina.md`
- 58.646 (2013) - `Garantias/58.646-2013_ Plazo menor GSO vicio formal mientras firmen contrato en plazo.md`
- 3.481 (2018) - `Termino Anticipado/3481-2018_ Haber trabajado no basta, es entregar lo que se pidio.md`
**DTO 250/2004 art. 22 num. 7** (5):
- 1395 (2021) - `Evaluacion/1.395-2021_ No se apega a criterios de las bases.md`
- 31433 (2018) - `Evaluacion/31.433-2018_ Inad si no cumple req tec min.md`
- 84937 (2016) - `Evaluacion/Debe indicar mot rech experiencia.md`
- 22.161 (2017) - `Derechos Consolidados/22161-2017_ Invalidacion mala adjudicacion.md`
- 36.593 (2016) - `Derechos Consolidados/36.593-2016.md`
**DTO 250/2004 art. 22 num. 8** (1):
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`
**DTO 250/2004 art. 25** (1):
- 14.828 (2018) - `Bases/14.828-2018, Cuarta copia factura.md`
**DTO 250/2004 art. 3** (2):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**DTO 250/2004 art. 31** (4):
- 58.646 (2013) - `Garantias/058646N13 - GSO, doctrina.md`
- 37.573 (2011) - `Garantias/37.573-2011_ Menciones obligatorias GSO.md`
- 57.470 (2012) - `Garantias/57.470-2012_ Debe consignarse monto y plazo GSO.md`
- 58.646 (2013) - `Garantias/58.646-2013_ Plazo menor GSO vicio formal mientras firmen contrato en plazo.md`
**DTO 250/2004 art. 33 lt. c** (1):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
**DTO 250/2004 art. 37** (5):
- 61067 (2016) - `Evaluacion/Criterio que limita precio minimo NO!.md`
- 6810 (2018) - `Evaluacion/6.810-2018 - Aclaraciones a todos.md`
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
- 84.990 (2016) - `Comisiones de Evaluacion/Se puede por acto previo.md`
- 63.558 (2015) - `TD/Art. 10, N° 7, a)/TA/63.558-2015_ TD no TD (Clinica Cordillera).md`
**DTO 250/2004 art. 37 inc. 1** (2):
- 31433 (2018) - `Evaluacion/31.433-2018_ Inad si no cumple req tec min.md`
- 36.519 (2016) - `Grandes Compras/GC - Def. de EETT va en la IC.md`
**DTO 250/2004 art. 37 inc. 2** (4):
- 77815 (2016) - `Evaluacion/Merito.md`
- 36.519 (2016) - `Grandes Compras/GC - Def. de EETT va en la IC.md`
- 22.161 (2017) - `Derechos Consolidados/22161-2017_ Invalidacion mala adjudicacion.md`
- 36.593 (2016) - `Derechos Consolidados/36.593-2016.md`
**DTO 250/2004 art. 37 inc. 3** (1):
- 45041 (2017) - `Evaluacion/45.041-2017 Se pidio pdf, subio word, no vicia.md`
**DTO 250/2004 art. 38** (10):
- 61067 (2016) - `Evaluacion/Criterio que limita precio minimo NO!.md`
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
- 31.421 (2018) - `Garantias/031421N18- Causales para cobrar GSO deben estar en bases.md`
- 31.798 (2013) - `Garantias/031798N13 - Error GSO y derechos consolidados.md`
- 14.200 (2018) - `Bases/14.200-2018, Experiencia no exigible, evaluable.md`
- 65.731 (2013) - `Bases/65.731-2013_ Explicar razones de EETT.md`
- 20.061 (2015) - `Derechos Consolidados/20.061-2015.md`
- 39.228 (2009) - `Presupuesto/Art. 11 DS 250 2.md`
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
- 63.558 (2015) - `TD/Art. 10, N° 7, a)/TA/63.558-2015_ TD no TD (Clinica Cordillera).md`
**DTO 250/2004 art. 38 inc. 3** (3):
- 36.519 (2016) - `Grandes Compras/GC - Def. de EETT va en la IC.md`
- 22.161 (2017) - `Derechos Consolidados/22161-2017_ Invalidacion mala adjudicacion.md`
- 36.593 (2016) - `Derechos Consolidados/36.593-2016.md`
**DTO 250/2004 art. 38 inc. 5** (1):
- 36.519 (2016) - `Grandes Compras/GC - Def. de EETT va en la IC.md`
**DTO 250/2004 art. 39** (3):
- 74523 (2015) - `Evaluacion/74.523-2015_ Mod. Oferta no se puede.md`
- 4.509 (2017) - `Grandes Compras/GC - Anx. deben subirse de acuerdo a IC.md`
- 4.509 (2017) - `Grandes Compras/GC - Of. x portal, como diga IC.md`
**DTO 250/2004 art. 4** (2):
- 20.453 (2019) - `Pagos/20.453-2019_ Reqs. Pago.md`
- 20.456 (2019) - `Pagos/20.456-2019_ Reqs. Pago.md`
**DTO 250/2004 art. 4 inc. 1** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**DTO 250/2004 art. 4 inc. 2** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**DTO 250/2004 art. 4 inc. 3** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**DTO 250/2004 art. 40** (2):
- 57.470 (2012) - `Garantias/57.470-2012_ Debe consignarse monto y plazo GSO.md`
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`
**DTO 250/2004 art. 40 bis num. 4** (1):
- 84937 (2016) - `Evaluacion/Debe indicar mot rech experiencia.md`
**DTO 250/2004 art. 40 inc. 1** (1):
- 67.377 (2016) - `Grandes Compras/GC - Se pueden solicitar aclaraciones necesarias.md`
**DTO 250/2004 art. 40 inc. 2** (1):
- 39705 (2013) - `Evaluacion/39.705-2013_ Si hay error pero no cambia el tenor de la evaluación, vale igual.md`
**DTO 250/2004 art. 41** (1):
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
**DTO 250/2004 art. 41 inc. 3** (1):
- 1395 (2021) - `Evaluacion/1.395-2021_ No se apega a criterios de las bases.md`
**DTO 250/2004 art. 41 inc. 4** (3):
- 1395 (2021) - `Evaluacion/1.395-2021_ No se apega a criterios de las bases.md`
- 54.690 (2013) - `Grandes Compras/54.690-2013_ Supletoriedad licitación a GC.md`
- 13.915 (2013) - `Grandes Compras/GC - Evaluacion, cuadro comparativo.md`
**DTO 250/2004 art. 42** (2):
- 51404 (2016) - `Evaluacion/ESB - Criterio Finalista.md`
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`
**DTO 250/2004 art. 43** (1):
- 48.929 (2012) - `Bases/48.929-2012_ Ob de entregar toda la info.md`
**DTO 250/2004 art. 57 lt. a** (1):
- 86.827 (2016) - `Grandes Compras/GC - Multas del CM aplican, OC aceptada.md`
**DTO 250/2004 art. 57 lt. b num. 9** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**DTO 250/2004 art. 57 lt. c num. 10** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**DTO 250/2004 art. 57 lt. d num. 6** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**DTO 250/2004 art. 62** (1):
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`
**DTO 250/2004 art. 62 inc. final** (1):
- 12.424 (2017) - `Grandes Compras/GC - Declaracion de inhabilidades.md`
**DTO 250/2004 art. 64** (3):
- 10172 (2017) - `TD/Art. 10, N° 7, f)/10172-17.md`
- 12798 (2016) - `TD/Art. 10, N° 7, f)/12798-16.md`
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
**DTO 250/2004 art. 68** (6):
- 10172 (2017) - `TD/Art. 10, N° 7, f)/10172-17.md`
- 51.205 (2014) - `Grandes Compras/GC - DCP inclinate!.md`
- 39.228 (2009) - `Presupuesto/Art. 11 DS 250 2.md`
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
- 3.481 (2018) - `Termino Anticipado/3481-2018_ Haber trabajado no basta, es entregar lo que se pidio.md`
- 46.564 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (5).md`
**DTO 250/2004 art. 68 inc. 1** (1):
- 51404 (2016) - `Evaluacion/ESB - Criterio Finalista.md`
**DTO 250/2004 art. 68 inc. 6** (1):
- 51404 (2016) - `Evaluacion/ESB - Criterio Finalista.md`
**DTO 250/2004 art. 69** (1):
- 51404 (2016) - `Evaluacion/ESB - Criterio Finalista.md`
**DTO 250/2004 art. 7 inc. 1** (2):
- 12.424 (2017) - `Grandes Compras/GC - Declaracion de inhabilidades.md`
- 67.377 (2016) - `Grandes Compras/GC - Se pueden solicitar aclaraciones necesarias.md`
**DTO 250/2004 art. 70** (2):
- 51.205 (2014) - `Grandes Compras/GC - DCP inclinate!.md`
- 47.664 (2012) - `Bases/47.664-2012_ no puedo exigir inscripcion en reg especial.md`
**DTO 250/2004 art. 71** (1):
- 24.268 (2017) - `TD/24.268-2017_ TD, debe acompañar anexo de que no es inhabil para contratar.md`
**DTO 250/2004 art. 74** (1):
- 46.564 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (5).md`
**DTO 250/2004 art. 77** (2):
- 3.481 (2018) - `Termino Anticipado/3481-2018_ Haber trabajado no basta, es entregar lo que se pidio.md`
- (sin número) (2016) - `Termino Anticipado/Deben estar las condiciones para la resciliacion.md`
**DTO 250/2004 art. 79 bis** (3):
- 20.453 (2019) - `Pagos/20.453-2019_ Reqs. Pago.md`
- 20.456 (2019) - `Pagos/20.456-2019_ Reqs. Pago.md`
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**DTO 250/2004 art. 79 ter** (1):
- 24243 (2019) - `TD/Art. 10, N° 7, f)/24243-19.md`
**DTO 250/2004 art. 9** (3):
- 2410 (2017) - `TD/Art. 10, N° 7, f)/2410-17.md`
- 63.669 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (4).md`
- 59.946 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (7).md`
**DTO 250/2004 hacie art. 10 bis** (2):
- E68062N25 (2025) - `Compras agiles/contraloria (17).md`
- E152886N21 (2021) - `Compras agiles/contraloria (24).md`
**DTO 250/2004 hacie art. 10 bis inc. 1** (6):
- OF87469N26 (2026) - `Compras agiles/contraloria (13).md`
- E11631N25 (2025) - `Compras agiles/contraloria (18).md`
- E287821N22 (2022) - `Compras agiles/contraloria (20).md`
- E240653N22 (2022) - `Compras agiles/contraloria (21).md`
- E189914N22 (2022) - `Compras agiles/contraloria (22).md`
- E108767N21 (2021) - `Compras agiles/contraloria (25).md`
**DTO 250/2004 hacie art. 10 bis inc. 3** (2):
- E240653N22 (2022) - `Compras agiles/contraloria (21).md`
- E108767N21 (2021) - `Compras agiles/contraloria (25).md`
**DTO 250/2004 hacie art. 6** (1):
- 003485N14 (2014) - `Ordenes de Compra/OC Documento comercial.md`
**Decreto 250/2004 Ministerio Hacienda art. 20 inc. 2, 37, 38, 41** (2):
- 61.067 (2016) - `Experiencia/61067-2016.md`
- 61.067 (2016) - `Criterios de evaluacion/61.067-2016_ Criterio que limita precio minimo NO!.md`
**Decreto 250/2004 Ministerio Hacienda art. 20 inc. final** (2):
- 72.362 (2014) - `Errores no esenciales/72.362-2014_ PNF - Formatos diferentes.md`
- 72.362 (2014) - `Errores no esenciales/Errores no esenciales.md`
**Decreto 250/2004 Ministerio Hacienda art. 20, 38, 22 num. 3, 41 inc. 2** (1):
- 75.501 (2013) - `Plazos no fatales/Plazos no fatales con art 41 2.md`
**Decreto 250/2004 Ministerio Hacienda art. 22 inc. 1 num. 3, 27, 41, 43** (1):
- 37.867 (2014) - `Plazos no fatales/Plazos no fatales con art 41.md`
**Decreto 250/2004 Ministerio Hacienda art. 38** (2):
- 14.200 (2018) - `Experiencia/14.200-2018.md`
- 44.460 (2010) - `Experiencia/44.460-10_ Experiencia sociedades filiales.md`
**Decreto 250/2004 Ministerio Hacienda art. 38 inc. 3** (1):
- 14.813 (2019) - `Criterios de evaluacion/14.813-2019_ Pautas para evaluar criterios que haga comision valen.md`
**decreto 250/2004 hacienda art/10 num/7 lt/g** (1):
- 59946 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (6).md`
**decreto 250/2004 hacienda art/22 num/7** (1):
- 14238 (2018) - `Derechos Consolidados/14.238-2018, ESB e IOf, invalidación ctto ejec. No hay Ds C.md`
**decreto 250/2004 hacienda art/40 inc/2** (1):
- 73183 (2013) - `Evaluacion/ESB - Error en glosa no esencial.md`

### Decreto 294  (1 citas en 1 variantes de artículo/inciso)

**DTO 294/95 Defen art. 34 inc. 2** (1):
- 067134N16 (2016) - `Adjudicacion/Publicar razones de demora adj.md`

### Decreto 319/2006  (1 citas en 1 variantes de artículo/inciso)

**DTO 319/2006 art. 23** (1):
- 37.465 (2013) - `Bases/37.465-2013_ Informacion, retencion y subrogacion.md`

### Decreto 331  (2 citas en 2 variantes de artículo/inciso)

**DTO 331/75 VIVIENDA art. 20** (1):
- 42421 (2001) - `Evaluacion/Modificacion Formulario.md`
**DTO 331/75 Vivie** (1):
- 3.566 (2004) - `Ofertas/3.566-2004_ Oferta debe manifestarse expresamente, partida vacia.md`

### Decreto 331/1975  (1 citas en 1 variantes de artículo/inciso)

**Decreto 331/1975 Ministerio Vivienda art. 20** (1):
- 42.421 (2001) - `Errores no esenciales/Modificacion Formulario.md`

### Decreto 355  (1 citas en 1 variantes de artículo/inciso)

**DTO 355/76 Vivie** (1):
- 20.687 (1990) - `Ofertas/20.687-1990_ Oferta debe manifestarse expresamente, partida vacia.md`

### Decreto 47  (1 citas en 1 variantes de artículo/inciso)

**DTO 47/92 art. 4** (1):
- 48.929 (2012) - `Bases/48.929-2012_ Ob de entregar toda la info.md`

### Decreto 50/2002  (1 citas en 1 variantes de artículo/inciso)

**DTO 50/2002 art. 53** (1):
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`

### Decreto 51/2008  (1 citas en 1 variantes de artículo/inciso)

**DTO 51/2008** (1):
- 37.573 (2011) - `Garantias/37.573-2011_ Menciones obligatorias GSO.md`

### Decreto 548  (1 citas en 1 variantes de artículo/inciso)

**DTO 548/88 Educación art. 9 num. 7** (1):
- 8.664 (2017) - `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md`

### Decreto 59  (1 citas en 1 variantes de artículo/inciso)

**DTO 59/94 TELEC** (1):
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`

### Decreto 61/2008  (1 citas en 1 variantes de artículo/inciso)

**Decreto 61/2008 Ministerio Salud** (1):
- 7.626 (2014) - `Plazos no fatales/Plazos no fatales 2.md`

### Decreto 661/2024  (18 citas en 5 variantes de artículo/inciso)

**DTO 661/2024 hacie art. 97 inc. 1** (1):
- OF120447N26 (2026) - `Compras agiles/contraloria (11).md`
**DTO 661/2024 hacie art. 97 inc. 3** (1):
- OF93103N26 (2026) - `Compras agiles/contraloria (12).md`
**DTO 661/2024 hacie art. 98 inc. 1** (3):
- D87N26 (2026) - `Compras agiles/contraloria (14).md`
- E141710N25 (2025) - `Compras agiles/contraloria (15).md`
- E72886N25 (2025) - `Compras agiles/contraloria (16).md`
**Decreto N°661/2024** (12):
- 31 (2026) - `Directivas/037-B-Res.-Aprueba-Directiva-de-Contratacion-N-31-2026-Codigo-etica-proveedores.md`
- 14 (2026) - `Directivas/054-B-Res.-Aprueba-Directiva-de-Contratacion-N°-14-2026-Comisiones-Evaluadoras.md`
- 28 (2025) - `Directivas/557BRes-Directiva28-2025-CodigodeEtica.md`
- (sin número) (?) - `Directivas/561BRes-Directiva26-eficiencia.md`
- (sin número) (?) - `Directivas/563BRes-Directiva35CompraAgil.md`
- 10 (2025) - `Directivas/565-B-Res.-Aprueba-Directiva-de-Contratacion-Publica-N°-10-2025-sobre-Trato-Directo.md`
- 6 (2025) - `Directivas/568-B_Res_Directiva6_2025_PAC.md`
- (sin número) (?) - `Directivas/72-B-directiva-pago-oportuno.md`
- (sin número) (?) - `Directivas/Actualizacion-Directiva20.md`
- (sin número) (?) - `Directivas/Directiva-44-Ciencia-de-Datos-IA.md`
- (sin número) (?) - `Directivas/directiva-compras-coordinadas.md`
- (sin número) (?) - `Directivas/Directiva45.md`
**decreto 661/2024 hacienda art/97 inc/1** (1):
- OF59317 (2026) - `Compras agiles/contraloria (9).md`

### Decreto 662/1992  (1 citas en 1 variantes de artículo/inciso)

**Decreto 662/1992 Ministerio Interior** (1):
- 20.203 (1999) - `Criterios de evaluacion/20.203-1999_ CGR no se puede meter con evaluación.md`

### Decreto 66765/2016  (1 citas en 1 variantes de artículo/inciso)

**decreto 66765/2016** (1):
- 91843 (2016) - `Grandes Compras/GC - Si hay rec de rep pendiente, CGR no se pronuncia.md`

### Decreto 71/2014  (2 citas en 2 variantes de artículo/inciso)

**DTO 71/2014 Sepre art. 5** (1):
- (sin número) (2021) - `Varios/160316N21 - Corporaciones Municipales, Ley de Compras.md`
**DTO 71/2014 Sepre art. 6** (1):
- (sin número) (2021) - `Varios/160316N21 - Corporaciones Municipales, Ley de Compras.md`

### Decreto 746/2011  (3 citas en 3 variantes de artículo/inciso)

**DTO 746/2011 DEFEN art. 1 inc. 2** (1):
- 076920N15 (2015) - `Preguntas y Respuestas/76.920-2015_ Preguntas y rpta vinculantes.md`
**DTO 746/2011 DEFEN art. 13 inc. 1** (1):
- 076920N15 (2015) - `Preguntas y Respuestas/76.920-2015_ Preguntas y rpta vinculantes.md`
**DTO 746/2011 DEFEN art. 13 inc. 2** (1):
- 076920N15 (2015) - `Preguntas y Respuestas/76.920-2015_ Preguntas y rpta vinculantes.md`

### Decreto 75/2004  (16 citas en 13 variantes de artículo/inciso)

**DTO 75/2004 MOOPP art. 69 inc. 5** (1):
- (sin número) (2021) - `Ofertas/E102329N21 - LC, registro.md`
**DTO 75/2004 MOOPP art. 76 num. 1 lit. a** (1):
- 42.462 (2011) - `Foro Inverso/42.462-2011_ Reqs formales elevados a esenciales, bases.md`
**DTO 75/2004 MOOPP art. 86** (2):
- 37409 (2017) - `Evaluacion/37.409-2017_ Retraso en evaluacion rompe equilibrio economico (9 meses).md`
- 37515 (2017) - `Evaluacion/37.515-2017_ Retraso en evaluacion rompe equilibrio economico (7 meses).md`
**DTO 75/2004 MOOPP art. 87 inc. 2** (1):
- 20.061 (2017) - `Adjudicacion/20.061-2017_ Necesidad de motivacion hecho derecho en acto.md`
**DTO 75/2004 Moopp art. 69** (1):
- 003688N18 (2018) - `Preguntas y Respuestas/3.688-2018_ Preguntas y rpta vinculantes.md`
**DTO 75/2004 art. 108** (1):
- 37412 (2017) - `Evaluacion/37.412-2017_ Retraso en evaluacion rompe equilibrio economico (9 meses).md`
**DTO 75/2004 art. 2 inc. 2** (1):
- 63.558 (2015) - `TD/Art. 10, N° 7, a)/TA/63.558-2015_ TD no TD (Clinica Cordillera).md`
**DTO 75/2004 art. 2 num. 31** (1):
- 63.558 (2015) - `TD/Art. 10, N° 7, a)/TA/63.558-2015_ TD no TD (Clinica Cordillera).md`
**DTO 75/2004 art. 4 num. 24** (1):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
**DTO 75/2004 art. 76** (1):
- 42.462 (2011) - `Bases/42.462-2011_ Reqs formales elevados a esenciales, bases.md`
**DTO 75/2004 art. 77 inc. 2** (1):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
**DTO 75/2004 art. 78** (1):
- 63.558 (2015) - `TD/Art. 10, N° 7, a)/TA/63.558-2015_ TD no TD (Clinica Cordillera).md`
**DTO 75/2004 art. 86** (3):
- 37397 (2017) - `Evaluacion/37.397-2017_ Retraso en evaluacion rompe equilibrio economico (6 meses).md`
- 37405 (2017) - `Evaluacion/37.405-2017_ Retraso Eval. rompe EE, pero no se reajusta of si consiente ex mantenerla.md`
- 37412 (2017) - `Evaluacion/37.412-2017_ Retraso en evaluacion rompe equilibrio economico (9 meses).md`

### Decreto 900  (1 citas en 1 variantes de artículo/inciso)

**DTO 900/96** (1):
- 21.503 (2003) - `Bases/21.503-2003_ Renuncia debe tener objeto claro.md`

### Decreto 95/2006  (5 citas en 5 variantes de artículo/inciso)

**DTO 95/2006 art. 10** (1):
- 12.125 (2019) - `Grandes Compras/12.125-2019_ Obligacion de CM.md`
**DTO 95/2006 art. 11** (1):
- 12.125 (2019) - `Grandes Compras/12.125-2019_ Obligacion de CM.md`
**DTO 95/2006 art. 53** (1):
- 12.125 (2019) - `Grandes Compras/12.125-2019_ Obligacion de CM.md`
**DTO 95/2006 art. 66 num. 2** (1):
- 20.453 (2019) - `Pagos/20.453-2019_ Reqs. Pago.md`
**DTO 95/2006 art. final** (1):
- 20.456 (2019) - `Pagos/20.456-2019_ Reqs. Pago.md`

### Decreto Supremo N°792/2023  (3 citas en 1 variantes de artículo/inciso)

**Decreto Supremo N°792/2023** (3):
- (sin número) (?) - `Directivas/Directiva-44-Ciencia-de-Datos-IA.md`
- (sin número) (?) - `Directivas/directiva-compras-coordinadas.md`
- (sin número) (?) - `Directivas/Directiva45.md`

### Ley 10.336  (48 citas en 26 variantes de artículo/inciso)

**Ley 10.336** (2):
- Resolucion Exenta N 04675 (2013) - `TD/Art. 10, N° 7, m)/CGR hace contrato antes del trato directo.md`
- Resolucion Exenta N 04483 (2009) - `TD/Res. Ex. N° 04483-2009 (TD Confianza)_ Ap. Ctto. CGR con Concorde Ltda..md`
**Ley 10.336 art. 1** (2):
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`
**Ley 10.336 art. 10** (1):
- 36.248 (2016) - `Foro Inverso/36.248-2016_ FI, complemenatción de antecedentes no evaluables.md`
**Ley 10.336 art. 10 inc. 1** (1):
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`
**Ley 10.336 art. 11** (1):
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`
**Ley 10.336 art. 131-139** (1):
- 78.428 (2012) - `Grandes Compras/GC - Evaluacion, cuadro comparativo 2.md`
**Ley 10.336 art. 154** (1):
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`
**Ley 10.336 art. 16** (3):
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
- 37.221 (1994) - `Derechos Consolidados/37.221-1994_ D. Con Ctto tramitado. Voluntad Adm.md`
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`
**Ley 10.336 art. 21 A** (1):
- 78.428 (2012) - `Grandes Compras/GC - Evaluacion, cuadro comparativo 2.md`
**Ley 10.336 art. 21A** (2):
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`
**Ley 10.336 art. 21B** (2):
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`
**Ley 10.336 art. 56** (2):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**Ley 10.336 art. 56 inc. 1** (2):
- 24.685 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (10).md`
- 59.946 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (7).md`
**Ley 10.336 art. 6 inc. 3** (8):
- 73.049 (2014) - `Grandes Compras/73.049-2014_ Crit. Fuera de Bases GC.md`
- 73.049 (2014) - `Grandes Compras/GC - Inv. solo por MP, no excluir por criterios q no existen en IC.md`
- 32.065 (2013) - `Grandes Compras/GC - Posibilidad de modificar plazos debe estar en IC.md`
- 11.400 (2017) - `Foro Inverso/11.400-2017_ Suspensión del acto.md`
- 76.032 (2015) - `Derechos Consolidados/76.032-2015.md`
- 76.032 (2015) - `Derechos Consolidados/76.032-2015_ Ds Consolidados por caducidad de plazo invalidacion.md`
- 96.610 (2015) - `Derechos Consolidados/96.610-2015.md`
- 3.481 (2018) - `Termino Anticipado/3481-2018_ Haber trabajado no basta, es entregar lo que se pidio.md`
**Ley 10.336 art. 9** (2):
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`
**Ley 10336 art. 1** (2):
- 61067 (2016) - `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md`
- 61.067 (2016) - `Bases/Criticas a Bases, competencia TCP.md`
**Ley 10336 art. 1, 6** (1):
- 32.261 (1989) - `Criterios de evaluacion/32.261-1989_ CGR no se puede meter con evaluación.md`
**Ley 10336 art. 10** (1):
- (sin número) (2019) - `Errores no esenciales/Res. 8 CGR (Fija montos para Nva 1600).md`
**Ley 10336 art. 16** (2):
- 61067 (2016) - `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md`
- 61.067 (2016) - `Bases/Criticas a Bases, competencia TCP.md`
**Ley 10336 art. 21-B** (1):
- 61.067 (2016) - `Bases/Criticas a Bases, competencia TCP.md`
**Ley 10336 art. 21A** (1):
- 61067 (2016) - `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md`
**Ley 10336 art. 21B** (1):
- 61067 (2016) - `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md`
**Ley 10336 art. 21B, 1, 9, 16, 21A** (2):
- 61.067 (2016) - `Experiencia/61067-2016.md`
- 61.067 (2016) - `Criterios de evaluacion/61.067-2016_ Criterio que limita precio minimo NO!.md`
**Ley 10336 art. 5, 10 siguientes** (1):
- (sin número) (2019) - `Errores no esenciales/Res. 7 CGR (Nva 1600).md`
**Ley 10336 art. 6 inc. 3** (3):
- 65942 (2013) - `Evaluacion/065942N13 - Acta Fundada3.md`
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`
- 14.813 (2019) - `Criterios de evaluacion/14.813-2019_ Pautas para evaluar criterios que haga comision valen.md`
**Ley 10336 art. 9** (2):
- 61067 (2016) - `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md`
- 61.067 (2016) - `Bases/Criticas a Bases, competencia TCP.md`

### Ley 17.798  (1 citas en 1 variantes de artículo/inciso)

**Ley 17798 art. 1** (1):
- 002659N21 (2021) - `Compras agiles/contraloria (23).md`

### Ley 18.046  (1 citas en 1 variantes de artículo/inciso)

**Ley 18046 art. 1, 86 inc. 1, 121, 122, 124** (1):
- 44.460 (2010) - `Experiencia/44.460-10_ Experiencia sociedades filiales.md`

### Ley 18.091  (3 citas en 3 variantes de artículo/inciso)

**Ley 18.091 art. 16 inc. 1** (1):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
**Ley 18.091 art. 16 inc. 2** (1):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
**Ley 18.091 art. 16 inc. 3** (1):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`

### Ley 18.290  (1 citas en 1 variantes de artículo/inciso)

**Ley 18.290 art. 27** (1):
- 70.620 (2013) - `TD/Art. 10, N° 7, g)/Casa moneda no es proveedor unico.md`

### Ley 18.575  (70 citas en 26 variantes de artículo/inciso)

**Ley 18.575** (1):
- Resolucion Exenta N 04483 (2009) - `TD/Res. Ex. N° 04483-2009 (TD Confianza)_ Ap. Ctto. CGR con Concorde Ltda..md`
**Ley 18.575 art. 1** (1):
- 31.356 (2013) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (2).md`
**Ley 18.575 art. 10** (3):
- 24.337 (2002) - `Derechos Consolidados/24337-2002_ Limite a invalidacion (Ramiro!).md`
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`
- 39.228 (2009) - `Presupuesto/Art. 11 DS 250 2.md`
**Ley 18.575 art. 11 bis inc. 2** (1):
- 005380N00 (2000) - `Acta Apertura de Ofertas/5380-2000.md`
**Ley 18.575 art. 11 bis inc. 3** (2):
- 29.549 (2000) - `Acta Apertura de Ofertas/29.549-2000.md`
- 005380N00 (2000) - `Acta Apertura de Ofertas/5380-2000.md`
**Ley 18.575 art. 13 inc. 2** (1):
- 067134N16 (2016) - `Adjudicacion/Publicar razones de demora adj.md`
**Ley 18.575 art. 2** (2):
- 24.337 (2002) - `Derechos Consolidados/24337-2002_ Limite a invalidacion (Ramiro!).md`
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**Ley 18.575 art. 3** (6):
- 42470 (2015) - `TD/Art. 10, N° 7, f)/42470-15.md`
- 89541 (2014) - `TD/Art. 10, N° 7, f)/89541-14.md`
- 45.487 (2016) - `Derechos Consolidados/45.487-2016.md`
- 5.448 (2015) - `Derechos Consolidados/Dictamen 5448 - Derechos consolidados contrato tramitado.md`
- 8.664 (2017) - `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md`
- (sin número) (2021) - `Varios/160316N21 - Corporaciones Municipales, Ley de Compras.md`
**Ley 18.575 art. 3 inc. 2** (1):
- 067134N16 (2016) - `Adjudicacion/Publicar razones de demora adj.md`
**Ley 18.575 art. 33** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
**Ley 18.575 art. 5** (3):
- 44.145 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (9).md`
- 067134N16 (2016) - `Adjudicacion/Publicar razones de demora adj.md`
- (sin número) (2021) - `Varios/160316N21 - Corporaciones Municipales, Ley de Compras.md`
**Ley 18.575 art. 52 inc. 2** (1):
- 002453N18 (2018) - `Varios/Dictamen CGR N° 2453-2018, Probidad y Compras.md`
**Ley 18.575 art. 53** (1):
- 002453N18 (2018) - `Varios/Dictamen CGR N° 2453-2018, Probidad y Compras.md`
**Ley 18.575 art. 6** (1):
- 100098 (2014) - `TD/Art. 10, N° 7, f)/100098-14.md`
**Ley 18.575 art. 62 inc. 2 num. 6** (2):
- 12.424 (2017) - `Grandes Compras/GC - Declaracion de inhabilidades.md`
- 002453N18 (2018) - `Varios/Dictamen CGR N° 2453-2018, Probidad y Compras.md`
**Ley 18.575 art. 8** (2):
- 8.664 (2017) - `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md`
- 44.145 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (9).md`
**Ley 18.575 art. 8 inc. 1** (1):
- 11.400 (2017) - `Foro Inverso/11.400-2017_ Suspensión del acto.md`
**Ley 18.575 art. 9** (8):
- 72362 (2014) - `Evaluacion/Errores no esenciales.md`
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
- 31.356 (2013) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (2).md`
- 63.669 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (4).md`
- 59.946 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (7).md`
- 44.145 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (9).md`
- 82.062 (2013) - `Ofertas/82.062-2013_ Vale oferta en Ingles.md`
- 15.331 (2018) - `Adjudicacion/15.331-2018 - Supletoria 19.880, experiencia (Bases no definen nada, igual CGR esta bien).md`
**Ley 18.575 art. 9 inc. 1** (1):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
**Ley 18.575 art. 9 inc. 2** (4):
- 29.349 (2017) - `Foro Inverso/29.349-2017_ Foro inverso, no mutables.md`
- 076516N12 (2012) - `Ofertas/076516N12 - No procede exigencia de registro para participar.md`
- 12.142 (2019) - `Ofertas/12.142-2019_ UCh., mismo rut no una sola oferta.md`
- (sin número) (2018) - `Ofertas/GSO Glosa, Aumento, Glosa, Ofertas C. A..md`
**Ley 18575** (2):
- (sin número) (2019) - `Errores no esenciales/Res. 7 CGR (Nva 1600).md`
- (sin número) (2019) - `Errores no esenciales/Res. 8 CGR (Fija montos para Nva 1600).md`
**Ley 18575 art. 2-3** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`
**Ley 18575 art. 3, 5** (1):
- 61.067 (2016) - `Criterios de evaluacion/61.067-2016_ Criterio que limita precio minimo NO!.md`
**Ley 18575 art. 9** (6):
- D87N26 (2026) - `Compras agiles/contraloria (14).md`
- 63.391 (2014) - `Bases/63.391-2014, Cuarta copia factura, sin condiciones a credito.md`
- 65.731 (2013) - `Bases/65.731-2013_ Explicar razones de EETT.md`
- (sin número) (2016) - `Bases/Art. 22, N° 2.md`
- 72.362 (2014) - `Errores no esenciales/72.362-2014_ PNF - Formatos diferentes.md`
- 72.362 (2014) - `Errores no esenciales/Errores no esenciales.md`
**Ley 18575 art. 9 inc. 2** (4):
- 37397 (2017) - `Evaluacion/37.397-2017_ Retraso en evaluacion rompe equilibrio economico. Perjuicios a trib.md`
- 70019 (2011) - `Evaluacion/Doc. No esenciales.md`
- 3117 (2015) - `Evaluacion/Mas del ppto DISPONIBLE NO.md`
- 70.019 (2011) - `Errores no esenciales/Doc. No esenciales.md`
**Ley N°18.575** (13):
- 31 (2026) - `Directivas/037-B-Res.-Aprueba-Directiva-de-Contratacion-N-31-2026-Codigo-etica-proveedores.md`
- 14 (2026) - `Directivas/054-B-Res.-Aprueba-Directiva-de-Contratacion-N°-14-2026-Comisiones-Evaluadoras.md`
- 28 (2025) - `Directivas/557BRes-Directiva28-2025-CodigodeEtica.md`
- (sin número) (?) - `Directivas/561BRes-Directiva26-eficiencia.md`
- (sin número) (?) - `Directivas/563BRes-Directiva35CompraAgil.md`
- 10 (2025) - `Directivas/565-B-Res.-Aprueba-Directiva-de-Contratacion-Publica-N°-10-2025-sobre-Trato-Directo.md`
- 6 (2025) - `Directivas/568-B_Res_Directiva6_2025_PAC.md`
- (sin número) (?) - `Directivas/72-B-directiva-pago-oportuno.md`
- (sin número) (?) - `Directivas/Actualizacion-Directiva20.md`
- (sin número) (?) - `Directivas/Directiva-44-Ciencia-de-Datos-IA.md`
- (sin número) (?) - `Directivas/directiva-compras-coordinadas.md`
- (sin número) (?) - `Directivas/Directiva45.md`
- 19.886 (2003) - `LEY-19886_30-JUL-2003.md`

### Ley 18.695  (37 citas en 33 variantes de artículo/inciso)

**Ley 18.695 art. 129** (1):
- (sin número) (2021) - `Varios/160316N21 - Corporaciones Municipales, Ley de Compras.md`
**Ley 18.695 art. 21 inc. 1** (1):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
**Ley 18.695 art. 21 inc. 2 lt. e** (1):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
**Ley 18.695 art. 3** (1):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
**Ley 18.695 art. 65** (1):
- 89918 (2016) - `TD/Art. 10, N° 7, f)/89918-16.md`
**Ley 18.695 art. 65 inc. 3** (1):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
**Ley 18.695 art. 65 lit. j** (1):
- 22.161 (2017) - `Foro Inverso/22.161-2017_ FI no es posibilidad de contraoferta.md`
**Ley 18.695 art. 65 lt. i** (1):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
**Ley 18.695 art. 65 lt. j** (2):
- 22.161 (2017) - `Derechos Consolidados/22161-2017_ Invalidacion mala adjudicacion.md`
- 36.593 (2016) - `Derechos Consolidados/36.593-2016.md`
**Ley 18.695 art. 65 lt. l** (1):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
**Ley 18.695 art. 66** (2):
- 35861 (2016) - `TD/Art. 10, N° 7, f)/35861-16.md`
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
**Ley 18.695 art. 66 inc. 1** (2):
- 51404 (2016) - `Evaluacion/ESB - Criterio Finalista.md`
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
**Ley 18.695 art. 8** (1):
- 37.573 (2011) - `Garantias/37.573-2011_ Menciones obligatorias GSO.md`
**Ley 18.695 art. 8 inc. 2** (1):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
**Ley 18.695 art. 8 inc. 4** (1):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
**Ley 18.695 art. 8 inc. 5** (1):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
**Ley 18.695 art. 8 inc. 6** (2):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
- 63.558 (2015) - `TD/Art. 10, N° 7, a)/TA/63.558-2015_ TD no TD (Clinica Cordillera).md`
**Ley 18.695 art. 81 inc. 1** (1):
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
**Ley 18695** (1):
- 20.203 (1999) - `Criterios de evaluacion/20.203-1999_ CGR no se puede meter con evaluación.md`
**Ley 18695 art. 29 lt. d** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`
**Ley 18695 art. 3 lt. f** (1):
- D87N26 (2026) - `Compras agiles/contraloria (14).md`
**Ley 18695 art. 4 lt. j** (1):
- 002659N21 (2021) - `Compras agiles/contraloria (23).md`
**Ley 18695 art. 51** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`
**Ley 18695 art. 6** (1):
- 32.261 (1989) - `Criterios de evaluacion/32.261-1989_ CGR no se puede meter con evaluación.md`
**Ley 18695 art. 65 lt. h** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`
**Ley 18695 art. 66** (1):
- E152886N21 (2021) - `Compras agiles/contraloria (24).md`
**Ley 18695 art. 66 inc. 2** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`
**Ley 18695 art. 79 lt. I** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`
**Ley 18695 art. 79 lt. b** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`
**Ley 18695 art. 79 lt. h** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`
**Ley 18695 art. 8 inc. 4-6** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`
**Ley 18695 art. 81 inc. 1** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`
**Ley 18695 art. 87** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`

### Ley 18.785  (1 citas en 1 variantes de artículo/inciso)

**Ley 18.785 art. 1 inc. 1** (1):
- 067134N16 (2016) - `Adjudicacion/Publicar razones de demora adj.md`

### Ley 18.834  (1 citas en 1 variantes de artículo/inciso)

**Ley 18.834 art. 64** (1):
- 100098 (2014) - `TD/Art. 10, N° 7, f)/100098-14.md`

### Ley 18.883  (4 citas en 4 variantes de artículo/inciso)

**Ley 18.883 art. 156 inc. 1** (1):
- 73.638 (2015) - `Adjudicacion/73.638-2015_ Adjudicación sobre presupuesto disponible.md`
**Ley 18.883 art. 88 A** (1):
- 73.638 (2015) - `Adjudicacion/73.638-2015_ Adjudicación sobre presupuesto disponible.md`
**Ley 18883 art. 156 inc. 1** (1):
- 73638 (2015) - `Evaluacion/Mas del ppto estimado OK si no esta en base limite.md`
**Ley 18883 art. 88 A** (1):
- 73638 (2015) - `Evaluacion/Mas del ppto estimado OK si no esta en base limite.md`

### Ley 18.928  (2 citas en 2 variantes de artículo/inciso)

**Ley 18.928 art. 1** (1):
- 20.453 (2019) - `Pagos/20.453-2019_ Reqs. Pago.md`
**Ley 18.928 art. 11** (1):
- 12.125 (2019) - `Grandes Compras/12.125-2019_ Obligacion de CM.md`

### Ley 19.378  (2 citas en 2 variantes de artículo/inciso)

**Ley 19378** (1):
- 7.626 (2014) - `Plazos no fatales/Plazos no fatales 2.md`
**Ley 19378 art. 5** (1):
- 7.626 (2014) - `Plazos no fatales/Plazos no fatales 2.md`

### Ley 19.628  (1 citas en 1 variantes de artículo/inciso)

**Ley N°19.628** (1):
- (sin número) (?) - `Directivas/Directiva45.md`

### Ley 19.799  (1 citas en 1 variantes de artículo/inciso)

**Ley 19799** (1):
- (sin número) (2019) - `Errores no esenciales/Res. 7 CGR (Nva 1600).md`

### Ley 19.880  (78 citas en 31 variantes de artículo/inciso)

**Ley 19.880 art. 1 inc. 1** (4):
- 49.703 (2016) - `Grandes Compras/49.703 - GC, despues de seleccion OC.md`
- 49.703 (2016) - `Grandes Compras/49.703-2016_ Revocación no desercion ni inadmisibilidad en CG.md`
- 49.703 (2016) - `Grandes Compras/GC - Se puede invalidar por 19.880.md`
- 15.331 (2018) - `Adjudicacion/15.331-2018 - Supletoria 19.880, experiencia (Bases no definen nada, igual CGR esta bien).md`
**Ley 19.880 art. 13** (6):
- 72362 (2014) - `Evaluacion/Errores no esenciales.md`
- 22.161 (2017) - `Foro Inverso/22.161-2017_ FI no es posibilidad de contraoferta.md`
- 42.462 (2011) - `Foro Inverso/42.462-2011_ Reqs formales elevados a esenciales, bases.md`
- 22.161 (2017) - `Derechos Consolidados/22161-2017_ Invalidacion mala adjudicacion.md`
- 36.593 (2016) - `Derechos Consolidados/36.593-2016.md`
- 14.140 (2009) - `Ofertas/14.140-2009_ Oferta decimales, vicio formal.md`
**Ley 19.880 art. 13 inc. 2** (2):
- 39705 (2013) - `Evaluacion/39.705-2013_ Si hay error pero no cambia el tenor de la evaluación, vale igual.md`
- 90883 (2015) - `Evaluacion/Calculo.md`
**Ley 19.880 art. 15** (1):
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`
**Ley 19.880 art. 2 inc. 1** (1):
- (sin número) (2021) - `Varios/160316N21 - Corporaciones Municipales, Ley de Compras.md`
**Ley 19.880 art. 3** (2):
- 72362 (2014) - `Evaluacion/Errores no esenciales.md`
- 32.065 (2013) - `Grandes Compras/GC - Posibilidad de modificar plazos debe estar en IC.md`
**Ley 19.880 art. 30 lt. b** (1):
- 36.593 (2016) - `Derechos Consolidados/36.593-2016.md`
**Ley 19.880 art. 4** (1):
- 8.664 (2017) - `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md`
**Ley 19.880 art. 41 inc. 4** (1):
- 54.690 (2013) - `Grandes Compras/54.690-2013_ Supletoriedad licitación a GC.md`
**Ley 19.880 art. 51** (1):
- 11.400 (2017) - `Foro Inverso/11.400-2017_ Suspensión del acto.md`
**Ley 19.880 art. 53** (9):
- 49.703 (2016) - `Grandes Compras/49.703 - GC, despues de seleccion OC.md`
- 49.703 (2016) - `Grandes Compras/49.703-2016_ Revocación no desercion ni inadmisibilidad en CG.md`
- 49.703 (2016) - `Grandes Compras/GC - Se puede invalidar por 19.880.md`
- 31.798 (2013) - `Garantias/031798N13 - Error GSO y derechos consolidados.md`
- 22.161 (2017) - `Foro Inverso/22.161-2017_ FI no es posibilidad de contraoferta.md`
- 20.061 (2015) - `Derechos Consolidados/20.061-2015.md`
- 22.161 (2017) - `Derechos Consolidados/22161-2017_ Invalidacion mala adjudicacion.md`
- 96.610 (2015) - `Derechos Consolidados/96.610-2015.md`
- 82.062 (2013) - `Ofertas/82.062-2013_ Vale oferta en Ingles.md`
**Ley 19.880 art. 53 inc. 1** (4):
- 14.238 (2018) - `Foro Inverso/14.238-2018_ Igualdad de los oferentes, que no hacer.md`
- 28.251 (2016) - `Derechos Consolidados/28251-2016_ Inv. por malas bases.md`
- 76.032 (2015) - `Derechos Consolidados/76.032-2015.md`
- 76.032 (2015) - `Derechos Consolidados/76.032-2015_ Ds Consolidados por caducidad de plazo invalidacion.md`
**Ley 19.880 art. 57 inc. 1** (1):
- 11.400 (2017) - `Foro Inverso/11.400-2017_ Suspensión del acto.md`
**Ley 19.880 art. 57 inc. 2** (1):
- 11.400 (2017) - `Foro Inverso/11.400-2017_ Suspensión del acto.md`
**Ley 19.880 art. 61** (4):
- 36.593 (2016) - `Derechos Consolidados/36.593-2016.md`
- 96.610 (2015) - `Derechos Consolidados/96.610-2015.md`
- 5.448 (2015) - `Derechos Consolidados/Dictamen 5448 - Derechos consolidados contrato tramitado.md`
- 15.331 (2018) - `Adjudicacion/15.331-2018 - Supletoria 19.880, experiencia (Bases no definen nada, igual CGR esta bien).md`
**Ley 19.880 art. 61 inc. 2 lt. a** (1):
- 45.487 (2016) - `Derechos Consolidados/45.487-2016.md`
**Ley 19.880 art. 61 inc. 2 lt. b** (1):
- 45.487 (2016) - `Derechos Consolidados/45.487-2016.md`
**Ley 19.880 art. 61 inc. 2 lt. c** (1):
- 45.487 (2016) - `Derechos Consolidados/45.487-2016.md`
**Ley 19.880 art. 61 lt. a** (2):
- 76.032 (2015) - `Derechos Consolidados/76.032-2015.md`
- 76.032 (2015) - `Derechos Consolidados/76.032-2015_ Ds Consolidados por caducidad de plazo invalidacion.md`
**Ley 19.880 art. 62** (1):
- 96.610 (2015) - `Derechos Consolidados/96.610-2015.md`
**Ley 19.880 art. 7** (4):
- 11.400 (2017) - `Foro Inverso/11.400-2017_ Suspensión del acto.md`
- 8.664 (2017) - `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md`
- 44.145 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (9).md`
- Resolucion Exenta N 04483 (2009) - `TD/Res. Ex. N° 04483-2009 (TD Confianza)_ Ap. Ctto. CGR con Concorde Ltda..md`
**Ley 19.880 art. 8** (2):
- 11.400 (2017) - `Foro Inverso/11.400-2017_ Suspensión del acto.md`
- 8.664 (2017) - `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md`
**Ley 19.880 art. 9** (1):
- 11.400 (2017) - `Foro Inverso/11.400-2017_ Suspensión del acto.md`
**Ley 19880 art. 13** (6):
- 70019 (2011) - `Evaluacion/Doc. No esenciales.md`
- 42.462 (2011) - `Bases/42.462-2011_ Reqs formales elevados a esenciales, bases.md`
- 72.362 (2014) - `Errores no esenciales/72.362-2014_ PNF - Formatos diferentes.md`
- 70.019 (2011) - `Errores no esenciales/Doc. No esenciales.md`
- (sin número) (2002) - `Errores no esenciales/Error no esencial.md`
- 72.362 (2014) - `Errores no esenciales/Errores no esenciales.md`
**Ley 19880 art. 13 inc. 2** (1):
- (sin número) (2009) - `Evaluacion/Error no esencial.md`
**Ley 19880 art. 3** (3):
- 65942 (2013) - `Evaluacion/065942N13 - Acta Fundada3.md`
- 72.362 (2014) - `Errores no esenciales/72.362-2014_ PNF - Formatos diferentes.md`
- 72.362 (2014) - `Errores no esenciales/Errores no esenciales.md`
**Ley 19880 art. 45** (1):
- 003485N14 (2014) - `Ordenes de Compra/OC Documento comercial.md`
**Ley 19880 art. 51** (1):
- 003485N14 (2014) - `Ordenes de Compra/OC Documento comercial.md`
**Ley 19880 art. 53** (1):
- E141710N25 (2025) - `Compras agiles/contraloria (15).md`
**Ley 19880 art. 53 inc. 1** (1):
- E68062N25 (2025) - `Compras agiles/contraloria (17).md`
**Ley N°19.880** (12):
- 31 (2026) - `Directivas/037-B-Res.-Aprueba-Directiva-de-Contratacion-N-31-2026-Codigo-etica-proveedores.md`
- 14 (2026) - `Directivas/054-B-Res.-Aprueba-Directiva-de-Contratacion-N°-14-2026-Comisiones-Evaluadoras.md`
- 28 (2025) - `Directivas/557BRes-Directiva28-2025-CodigodeEtica.md`
- (sin número) (?) - `Directivas/561BRes-Directiva26-eficiencia.md`
- (sin número) (?) - `Directivas/563BRes-Directiva35CompraAgil.md`
- 10 (2025) - `Directivas/565-B-Res.-Aprueba-Directiva-de-Contratacion-Publica-N°-10-2025-sobre-Trato-Directo.md`
- 6 (2025) - `Directivas/568-B_Res_Directiva6_2025_PAC.md`
- (sin número) (?) - `Directivas/72-B-directiva-pago-oportuno.md`
- (sin número) (?) - `Directivas/Actualizacion-Directiva20.md`
- (sin número) (?) - `Directivas/Directiva-44-Ciencia-de-Datos-IA.md`
- (sin número) (?) - `Directivas/directiva-compras-coordinadas.md`
- (sin número) (?) - `Directivas/Directiva45.md`

### Ley 19.886  (247 citas en 82 variantes de artículo/inciso)

**Ley 19.886** (4):
- 3871 (2011) - `TD/Art. 10, N° 7, f)/3871-11.md`
- 27.848 (2005) - `TD/Art. 10, N° 7, f)/dictamen 27.848 - 2005.md`
- 394 (2014) - `Grandes Compras/GC - Def. de EETT va en la IC 2.md`
- 70.620 (2013) - `TD/Art. 10, N° 7, g)/Casa moneda no es proveedor unico.md`
**Ley 19.886 art. 1** (4):
- 12.424 (2017) - `Grandes Compras/GC - Declaracion de inhabilidades.md`
- 50.110 (2013) - `Presupuesto/Art. 11 DS 250.md`
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
- 15.331 (2018) - `Adjudicacion/15.331-2018 - Supletoria 19.880, experiencia (Bases no definen nada, igual CGR esta bien).md`
**Ley 19.886 art. 1 inc. 1** (6):
- 49.703 (2016) - `Grandes Compras/49.703 - GC, despues de seleccion OC.md`
- 49.703 (2016) - `Grandes Compras/49.703-2016_ Revocación no desercion ni inadmisibilidad en CG.md`
- 49.703 (2016) - `Grandes Compras/GC - Se puede invalidar por 19.880.md`
- 67.377 (2016) - `Grandes Compras/GC - Se pueden solicitar aclaraciones necesarias.md`
- 14.250 (2018) - `Objeto de compra/14.250-2018, Bienes reacondicionados. Decision de merito fundada.md`
- 17.584 (2018) - `Ofertas/17.584-2018_ Multiples ofertas merito-ESB.md`
**Ley 19.886 art. 1 inc. 2** (1):
- 31.356 (2013) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (2).md`
**Ley 19.886 art. 1 lt. d** (1):
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`
**Ley 19.886 art. 10** (7):
- 45041 (2017) - `Evaluacion/45.041-2017 Se pidio pdf, subio word, no vicia.md`
- 72362 (2014) - `Evaluacion/Errores no esenciales.md`
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
- 20.061 (2015) - `Derechos Consolidados/20.061-2015.md`
- 28.251 (2016) - `Derechos Consolidados/28251-2016_ Inv. por malas bases.md`
- 007948N18 (2018) - `Adjudicacion/007948N18 - Tribunales inclinense!.md`
- 15.331 (2018) - `Adjudicacion/15.331-2018 - Supletoria 19.880, experiencia (Bases no definen nada, igual CGR esta bien).md`
**Ley 19.886 art. 10 inc. 2** (2):
- 1395 (2021) - `Evaluacion/1.395-2021_ No se apega a criterios de las bases.md`
- 14.238 (2018) - `Foro Inverso/14.238-2018_ Igualdad de los oferentes, que no hacer.md`
**Ley 19.886 art. 10 inc. 3** (20):
- 31433 (2018) - `Evaluacion/31.433-2018_ Inad si no cumple req tec min.md`
- 6810 (2018) - `Evaluacion/6.810-2018 - Aclaraciones a todos.md`
- 84937 (2016) - `Evaluacion/Debe indicar mot rech experiencia.md`
- 4797 (2017) - `Evaluacion/ESB.md`
- 36.519 (2016) - `Grandes Compras/GC - Def. de EETT va en la IC.md`
- 31.421 (2018) - `Garantias/031421N18- Causales para cobrar GSO deben estar en bases.md`
- 31.798 (2013) - `Garantias/031798N13 - Error GSO y derechos consolidados.md`
- 14.238 (2018) - `Foro Inverso/14.238-2018_ Igualdad de los oferentes, que no hacer.md`
- 18.889 (2018) - `Foro Inverso/18.889-2018_ Igualdad, foro inverso.md`
- 25.674 (2017) - `Foro Inverso/25.674-2017_ Foro Inverso, antecedente que no cumple.md`
- 41.236 (2017) - `Foro Inverso/41.236-2017_ Def. Vicio Formal.md`
- 6.810 (2018) - `Foro Inverso/6.810-2018_ Igualdad de los oferentes, exclusion.md`
- 76.032 (2015) - `Derechos Consolidados/76.032-2015.md`
- 76.032 (2015) - `Derechos Consolidados/76.032-2015_ Ds Consolidados por caducidad de plazo invalidacion.md`
- (sin número) (2016) - `Termino Anticipado/Deben estar las condiciones para la resciliacion.md`
- 12.142 (2019) - `Ofertas/12.142-2019_ UCh., mismo rut no una sola oferta.md`
- 17.584 (2018) - `Ofertas/17.584-2018_ Multiples ofertas merito-ESB.md`
- (sin número) (2018) - `Ofertas/GSO Glosa, Aumento, Glosa, Ofertas C. A..md`
- 011782N18 (2018) - `Adjudicacion/011782N18 - Evaluaciones suscritas por todos los nombrados.md`
- 084937N16 (2016) - `Adjudicacion/Debe indicar mot rech experiencia.md`
**Ley 19.886 art. 10 inc. 4** (1):
- 17.584 (2018) - `Ofertas/17.584-2018_ Multiples ofertas merito-ESB.md`
**Ley 19.886 art. 11** (4):
- 58.646 (2013) - `Garantias/058646N13 - GSO, doctrina.md`
- 58.646 (2013) - `Garantias/58.646-2013_ Plazo menor GSO vicio formal mientras firmen contrato en plazo.md`
- 3.481 (2018) - `Termino Anticipado/3481-2018_ Haber trabajado no basta, es entregar lo que se pidio.md`
- 46.564 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (5).md`
**Ley 19.886 art. 11 inc. 1** (1):
- 51404 (2016) - `Evaluacion/ESB - Criterio Finalista.md`
**Ley 19.886 art. 11 inc. 2** (1):
- 37.573 (2011) - `Garantias/37.573-2011_ Menciones obligatorias GSO.md`
**Ley 19.886 art. 13 lt. b** (1):
- 3.481 (2018) - `Termino Anticipado/3481-2018_ Haber trabajado no basta, es entregar lo que se pidio.md`
**Ley 19.886 art. 14** (1):
- 46.564 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (5).md`
**Ley 19.886 art. 16 inc. 4** (2):
- 37.573 (2011) - `Garantias/37.573-2011_ Menciones obligatorias GSO.md`
- 076516N12 (2012) - `Ofertas/076516N12 - No procede exigencia de registro para participar.md`
**Ley 19.886 art. 16 inc. 7** (1):
- 076749N13 (2013) - `Ofertas/076749N13 - Reg. Solo exigible por norma particular.md`
**Ley 19.886 art. 17** (1):
- 076516N12 (2012) - `Ofertas/076516N12 - No procede exigencia de registro para participar.md`
**Ley 19.886 art. 18** (3):
- 11.274 (2018) - `Foro Inverso/11.274-2018_ Ob. consultar foro inverso del proveedor.md`
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`
- 17.584 (2018) - `Ofertas/17.584-2018_ Multiples ofertas merito-ESB.md`
**Ley 19.886 art. 19** (1):
- 43.119 (2014) - `Grandes Compras/GC - Si hay 30_ solo a bienes del CM.md`
**Ley 19.886 art. 2** (1):
- 14.250 (2018) - `Objeto de compra/14.250-2018, Bienes reacondicionados. Decision de merito fundada.md`
**Ley 19.886 art. 20** (1):
- 19.265 (2013) - `Foro Inverso/19.265-2013_ FI, ley pareja.md`
**Ley 19.886 art. 20 inc. 1** (1):
- 067134N16 (2016) - `Adjudicacion/Publicar razones de demora adj.md`
**Ley 19.886 art. 24** (2):
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`
**Ley 19.886 art. 3 inc. 1 lt. e** (1):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
**Ley 19.886 art. 3 lt. e** (2):
- 076749N13 (2013) - `Ofertas/076749N13 - Reg. Solo exigible por norma particular.md`
- 067134N16 (2016) - `Adjudicacion/Publicar razones de demora adj.md`
**Ley 19.886 art. 30 letra d)** (1):
- 44.043 (2010) - `TD/Art. 10, N° 7, f)/dictamen 44.043 - 2010.md`
**Ley 19.886 art. 30 lit. d** (1):
- 11.274 (2018) - `Foro Inverso/11.274-2018_ Ob. consultar foro inverso del proveedor.md`
**Ley 19.886 art. 30 lt. d** (12):
- 1.199 (2019) - `Grandes Compras/1.199-2019_ Acepto en evaluacion, rechazo por marca.md`
- 18.983 (2018) - `Grandes Compras/18.983-2018_ Fracc GC, Municipalidad.md`
- 18.983 (2018) - `Grandes Compras/18.983-2018_ Fraccionamiento, CM, grandes compras.md`
- 30.836 (2019) - `Grandes Compras/30.836-2019_ Ob. de comunicar EETT.md`
- 49.703 (2016) - `Grandes Compras/49.703 - GC, despues de seleccion OC.md`
- 49.703 (2016) - `Grandes Compras/49.703-2016_ Revocación no desercion ni inadmisibilidad en CG.md`
- 12.424 (2017) - `Grandes Compras/GC - Declaracion de inhabilidades.md`
- 7.640 (2013) - `Grandes Compras/GC - Multas del CM aplican.md`
- 1.199 (2019) - `Grandes Compras/GC - Se invita a todos, aunque no tengan marca.md`
- 49.703 (2016) - `Grandes Compras/GC - Se puede invalidar por 19.880.md`
- 67.377 (2016) - `Grandes Compras/GC - Se pueden solicitar aclaraciones necesarias.md`
- 43.119 (2014) - `Grandes Compras/GC - Si hay 30_ solo a bienes del CM.md`
**Ley 19.886 art. 4** (9):
- 39705 (2013) - `Evaluacion/39.705-2013_ Si hay error pero no cambia el tenor de la evaluación, vale igual.md`
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
- 2410 (2017) - `TD/Art. 10, N° 7, f)/2410-17.md`
- 11.274 (2018) - `Foro Inverso/11.274-2018_ Ob. consultar foro inverso del proveedor.md`
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`
- 39.228 (2009) - `Presupuesto/Art. 11 DS 250 2.md`
- 076749N13 (2013) - `Ofertas/076749N13 - Reg. Solo exigible por norma particular.md`
- 12.142 (2019) - `Ofertas/12.142-2019_ UCh., mismo rut no una sola oferta.md`
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`
**Ley 19.886 art. 4 inc. 1** (4):
- 24.268 (2017) - `TD/24.268-2017_ TD, debe acompañar anexo de que no es inhabil para contratar.md`
- 076516N12 (2012) - `Ofertas/076516N12 - No procede exigencia de registro para participar.md`
- 007948N18 (2018) - `Adjudicacion/007948N18 - Tribunales inclinense!.md`
- 002453N18 (2018) - `Varios/Dictamen CGR N° 2453-2018, Probidad y Compras.md`
**Ley 19.886 art. 4 inc. 6** (1):
- 12.424 (2017) - `Grandes Compras/GC - Declaracion de inhabilidades.md`
**Ley 19.886 art. 4 inc. 8** (2):
- 12.424 (2017) - `Grandes Compras/GC - Declaracion de inhabilidades.md`
- 002453N18 (2018) - `Varios/Dictamen CGR N° 2453-2018, Probidad y Compras.md`
**Ley 19.886 art. 4 inc. 9** (1):
- 12.424 (2017) - `Grandes Compras/GC - Declaracion de inhabilidades.md`
**Ley 19.886 art. 5** (2):
- 63.669 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (4).md`
- 59.946 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (7).md`
**Ley 19.886 art. 6** (10):
- 39705 (2013) - `Evaluacion/39.705-2013_ Si hay error pero no cambia el tenor de la evaluación, vale igual.md`
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
- 23220 (2011) - `TD/Art. 10, N° 7, f)/23220-11.md`
- 57.470 (2012) - `Garantias/57.470-2012_ Debe consignarse monto y plazo GSO.md`
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`
- 076749N13 (2013) - `Ofertas/076749N13 - Reg. Solo exigible por norma particular.md`
- 12.142 (2019) - `Ofertas/12.142-2019_ UCh., mismo rut no una sola oferta.md`
- 82.062 (2013) - `Ofertas/82.062-2013_ Vale oferta en Ingles.md`
- (sin número) (2018) - `Ofertas/GSO Glosa, Aumento, Glosa, Ofertas C. A..md`
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`
**Ley 19.886 art. 6 inc. 1** (9):
- 1395 (2021) - `Evaluacion/1.395-2021_ No se apega a criterios de las bases.md`
- 84937 (2016) - `Evaluacion/Debe indicar mot rech experiencia.md`
- 77815 (2016) - `Evaluacion/Merito.md`
- 36.519 (2016) - `Grandes Compras/GC - Def. de EETT va en la IC.md`
- 14.238 (2018) - `Foro Inverso/14.238-2018_ Igualdad de los oferentes, que no hacer.md`
- 14.250 (2018) - `Objeto de compra/14.250-2018, Bienes reacondicionados. Decision de merito fundada.md`
- 17.584 (2018) - `Ofertas/17.584-2018_ Multiples ofertas merito-ESB.md`
- 007948N18 (2018) - `Adjudicacion/007948N18 - Tribunales inclinense!.md`
- 084937N16 (2016) - `Adjudicacion/Debe indicar mot rech experiencia.md`
**Ley 19.886 art. 6 inc. 6** (1):
- 31433 (2018) - `Evaluacion/31.433-2018_ Inad si no cumple req tec min.md`
**Ley 19.886 art. 6 inc. fin** (1):
- 14.250 (2018) - `Objeto de compra/14.250-2018, Bienes reacondicionados. Decision de merito fundada.md`
**Ley 19.886 art. 7 inc. fin** (1):
- 14.236 (2018) - `Fragmentacion/14.236-2018, Frag. GC. Ordena sumario.md`
**Ley 19.886 art. 7 inc. final** (2):
- 18.983 (2018) - `Grandes Compras/18.983-2018_ Fracc GC, Municipalidad.md`
- 18.983 (2018) - `Grandes Compras/18.983-2018_ Fraccionamiento, CM, grandes compras.md`
**Ley 19.886 art. 8** (4):
- 100098 (2014) - `TD/Art. 10, N° 7, f)/100098-14.md`
- 12798 (2016) - `TD/Art. 10, N° 7, f)/12798-16.md`
- 6381 (2018) - `TD/Art. 10, N° 7, f)/6381-18.md`
- 31.356 (2013) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (2).md`
**Ley 19.886 art. 8 letra d** (2):
- 69865 (2012) - `TD/Art. 10, N° 7, f)/69865-12.md`
- 65.505 (2010) - `TD/Art. 10, N° 7, f)/dictamen 65.505 - 2010.md`
**Ley 19.886 art. 8 letra g** (22):
- 23220 (2011) - `TD/Art. 10, N° 7, f)/23220-11.md`
- 26006 (2016) - `TD/Art. 10, N° 7, f)/26006-16.md`
- 46564 (2011) - `TD/Art. 10, N° 7, f)/46564-11.md`
- 66231 (2015) - `TD/Art. 10, N° 7, f)/66231-15.md`
- 80806 (2013) - `TD/Art. 10, N° 7, f)/80806-13.md`
- 90268 (2015) - `TD/Art. 10, N° 7, f)/90268-15.md`
- 91012 (2016) - `TD/Art. 10, N° 7, f)/91012-16.md`
- 11.189 (2008) - `TD/Art. 10, N° 7, f)/dictamen 11.189 - 2008.md`
- 2.368 (2008) - `TD/Art. 10, N° 7, f)/dictamen 2.368 - 2008.md`
- 21.470 (2007) - `TD/Art. 10, N° 7, f)/dictamen 21.470 - 2007.md`
- 27.818 (2008) - `TD/Art. 10, N° 7, f)/dictamen 27.818 - 2008.md`
- 44.411 (2007) - `TD/Art. 10, N° 7, f)/dictamen 44.411 - 2007.md`
- 44.888 (2009) - `TD/Art. 10, N° 7, f)/dictamen 44.888 - 2009.md`
- 24.685 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (10).md`
- 79.494 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (3).md`
- 63.669 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (4).md`
- 46.564 (2011) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (5).md`
- 59.946 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (7).md`
- 48.093 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (8).md`
- 44.145 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (9).md`
- Resolucion Exenta N 04675 (2013) - `TD/Art. 10, N° 7, m)/CGR hace contrato antes del trato directo.md`
- Resolucion Exenta N 04483 (2009) - `TD/Res. Ex. N° 04483-2009 (TD Confianza)_ Ap. Ctto. CGR con Concorde Ltda..md`
**Ley 19.886 art. 9** (6):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`
- 51.205 (2014) - `Grandes Compras/GC - DCP inclinate!.md`
- 84.775 (2013) - `Garantias/065771N13 - No se puede cobrar GSO a inadmisibles.md`
- 19.265 (2013) - `Foro Inverso/19.265-2013_ FI, ley pareja.md`
- 74.223 (2016) - `Foro Inverso/74.223-2016_ FI no es posibilidad de contraoferta.md`
- 65.771 (2013) - `Inadmisibilidad/Oferta Inadmisible por EETT.md`
**Ley 19.886 art. 9 inc. 1** (2):
- 31433 (2018) - `Evaluacion/31.433-2018_ Inad si no cumple req tec min.md`
- 4797 (2017) - `Evaluacion/ESB.md`
**Ley 19886** (3):
- 14.202 (2018) - `Bases/14.202-2018, No weiwer derechos Administracion.md`
- 48.929 (2012) - `Bases/48.929-2012_ Ob de entregar toda la info.md`
- 44.460 (2010) - `Experiencia/44.460-10_ Experiencia sociedades filiales.md`
**Ley 19886 art. 1** (1):
- 003485N14 (2014) - `Ordenes de Compra/OC Documento comercial.md`
**Ley 19886 art. 1 inc. 1** (3):
- E287821N22 (2022) - `Compras agiles/contraloria (20).md`
- E240653N22 (2022) - `Compras agiles/contraloria (21).md`
- E189914N22 (2022) - `Compras agiles/contraloria (22).md`
**Ley 19886 art. 10** (6):
- 7948 (2018) - `Evaluacion/79.48-2018 - Precios neto y bruto.md`
- 298 (2008) - `Evaluacion/www.contraloria.cl_LegisJuri_DictamenesGeneralesMunicipales.md`
- 72.362 (2014) - `Errores no esenciales/72.362-2014_ PNF - Formatos diferentes.md`
- (sin número) (2002) - `Errores no esenciales/Error no esencial.md`
- 72.362 (2014) - `Errores no esenciales/Errores no esenciales.md`
- 42.421 (2001) - `Errores no esenciales/Modificacion Formulario.md`
**Ley 19886 art. 10 inc. 1** (1):
- 17585 (2018) - `Evaluacion/17.585-2018 - Excepcion en dejar vacio item oferta.md`
**Ley 19886 art. 10 inc. 2** (1):
- 17585 (2018) - `Evaluacion/17.585-2018 - Excepcion en dejar vacio item oferta.md`
**Ley 19886 art. 10 inc. 3** (3):
- 37397 (2017) - `Evaluacion/37.397-2017_ Retraso en evaluacion rompe equilibrio economico. Perjuicios a trib.md`
- 41236 (2017) - `Evaluacion/41.236-2017, valor portal distinto anexo oferta, lo que digan las bases.md`
- 3117 (2015) - `Evaluacion/Mas del ppto DISPONIBLE NO.md`
**Ley 19886 art. 12 bis inc. 2** (1):
- E72886N25 (2025) - `Compras agiles/contraloria (16).md`
**Ley 19886 art. 24** (2):
- 61067 (2016) - `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md`
- 61.067 (2016) - `Bases/Criticas a Bases, competencia TCP.md`
**Ley 19886 art. 24, 6, 4** (1):
- 61.067 (2016) - `Experiencia/61067-2016.md`
**Ley 19886 art. 35 bis** (1):
- E464046N24 (2024) - `Compras agiles/contraloria (19).md`
**Ley 19886 art. 35 ter** (1):
- E464046N24 (2024) - `Compras agiles/contraloria (19).md`
**Ley 19886 art. 4** (5):
- 61067 (2016) - `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md`
- OF87469N26 (2026) - `Compras agiles/contraloria (13).md`
- 14.200 (2018) - `Bases/14.200-2018, Experiencia no exigible, evaluable.md`
- 14.828 (2018) - `Bases/14.828-2018, Cuarta copia factura.md`
- 47.664 (2012) - `Bases/47.664-2012_ no puedo exigir inscripcion en reg especial.md`
**Ley 19886 art. 4 inc. 1** (2):
- 7948 (2018) - `Evaluacion/79.48-2018 - Precios neto y bruto.md`
- 10.957 (2017) - `Experiencia/10957-2017.md`
**Ley 19886 art. 4 y 6** (1):
- 14.200 (2018) - `Experiencia/14.200-2018.md`
**Ley 19886 art. 5** (3):
- E68062N25 (2025) - `Compras agiles/contraloria (17).md`
- E11631N25 (2025) - `Compras agiles/contraloria (18).md`
- E287821N22 (2022) - `Compras agiles/contraloria (20).md`
**Ley 19886 art. 5 inc. 1** (2):
- OF87469N26 (2026) - `Compras agiles/contraloria (13).md`
- E108767N21 (2021) - `Compras agiles/contraloria (25).md`
**Ley 19886 art. 56 inc. 2** (1):
- OF93103N26 (2026) - `Compras agiles/contraloria (12).md`
**Ley 19886 art. 6** (8):
- 61067 (2016) - `Evaluacion/61.067-2016_ MERITO! Eval. Experiencia.md`
- 61067 (2016) - `Evaluacion/Criterio que limita precio minimo NO!.md`
- OF87469N26 (2026) - `Compras agiles/contraloria (13).md`
- 14.200 (2018) - `Bases/14.200-2018, Experiencia no exigible, evaluable.md`
- 47.664 (2012) - `Bases/47.664-2012_ no puedo exigir inscripcion en reg especial.md`
- 65.731 (2013) - `Bases/65.731-2013_ Explicar razones de EETT.md`
- (sin número) (2016) - `Bases/Art. 22, N° 2.md`
- 49.345 (2016) - `Experiencia/49.345-2016.md`
**Ley 19886 art. 6 inc. 1** (1):
- 7948 (2018) - `Evaluacion/79.48-2018 - Precios neto y bruto.md`
**Ley 19886 art. 6, 24, 4** (1):
- 61.067 (2016) - `Criterios de evaluacion/61.067-2016_ Criterio que limita precio minimo NO!.md`
**Ley 19886 art. 7** (2):
- E141710N25 (2025) - `Compras agiles/contraloria (15).md`
- E464046N24 (2024) - `Compras agiles/contraloria (19).md`
**Ley 19886 art. 7 inc. 1 lt. d num. 1** (2):
- D87N26 (2026) - `Compras agiles/contraloria (14).md`
- E72886N25 (2025) - `Compras agiles/contraloria (16).md`
**Ley 19886 art. 7 letra a, 9** (1):
- 75.501 (2013) - `Plazos no fatales/Plazos no fatales con art 41 2.md`
**Ley 19886 art. 7 lt. d num. 1** (1):
- OF93103N26 (2026) - `Compras agiles/contraloria (12).md`
**Ley 19886 art. 7 lt. d num. 1 inc. 1** (1):
- OF120447N26 (2026) - `Compras agiles/contraloria (11).md`
**Ley 19886 art. 9** (5):
- 11358 (2017) - `Evaluacion/011358N17 - Acta Fundada2.md`
- 65942 (2013) - `Evaluacion/065942N13 - Acta Fundada3.md`
- 71923 (2013) - `Evaluacion/71.923-2013_ Debio subir F30, no lo hizo, inadmisible.md`
- 3117 (2015) - `Evaluacion/Mas del ppto DISPONIBLE NO.md`
- 298 (2008) - `Evaluacion/www.contraloria.cl_LegisJuri_DictamenesGeneralesMunicipales.md`
**Ley 19886 art. 9 inc. 1 y 2** (1):
- 37.867 (2014) - `Plazos no fatales/Plazos no fatales con art 41.md`
**Ley N°19.886** (12):
- 31 (2026) - `Directivas/037-B-Res.-Aprueba-Directiva-de-Contratacion-N-31-2026-Codigo-etica-proveedores.md`
- 14 (2026) - `Directivas/054-B-Res.-Aprueba-Directiva-de-Contratacion-N°-14-2026-Comisiones-Evaluadoras.md`
- 28 (2025) - `Directivas/557BRes-Directiva28-2025-CodigodeEtica.md`
- (sin número) (?) - `Directivas/561BRes-Directiva26-eficiencia.md`
- (sin número) (?) - `Directivas/563BRes-Directiva35CompraAgil.md`
- 10 (2025) - `Directivas/565-B-Res.-Aprueba-Directiva-de-Contratacion-Publica-N°-10-2025-sobre-Trato-Directo.md`
- 6 (2025) - `Directivas/568-B_Res_Directiva6_2025_PAC.md`
- (sin número) (?) - `Directivas/72-B-directiva-pago-oportuno.md`
- (sin número) (?) - `Directivas/Actualizacion-Directiva20.md`
- (sin número) (?) - `Directivas/Directiva-44-Ciencia-de-Datos-IA.md`
- (sin número) (?) - `Directivas/directiva-compras-coordinadas.md`
- (sin número) (?) - `Directivas/Directiva45.md`
**ley 19886** (3):
- 91843 (2016) - `Grandes Compras/GC - Si hay rec de rep pendiente, CGR no se pronuncia.md`
- 661 (2024) - `Normas macro/Decreto-661_12-DIC-2024 (1).md`
- 21634 (2023) - `Normas macro/Ley-21634_11-DIC-2023 (3).md`
**ley 19886 art/10 inc/2** (1):
- 14238 (2018) - `Derechos Consolidados/14.238-2018, ESB e IOf, invalidación ctto ejec. No hay Ds C.md`
**ley 19886 art/10 inc/3** (2):
- 73183 (2013) - `Evaluacion/ESB - Error en glosa no esencial.md`
- 14238 (2018) - `Derechos Consolidados/14.238-2018, ESB e IOf, invalidación ctto ejec. No hay Ds C.md`
**ley 19886 art/5** (1):
- 59946 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (6).md`
**ley 19886 art/6** (1):
- 65449 (2015) - `Criterios de evaluacion/65.449-2015_ Regla de tres, experiencia.md`
**ley 19886 art/6 inc/1** (1):
- 14238 (2018) - `Derechos Consolidados/14.238-2018, ESB e IOf, invalidación ctto ejec. No hay Ds C.md`
**ley 19886 art/7** (1):
- OF59317 (2026) - `Compras agiles/contraloria (9).md`
**ley 19886 art/8 lt/g** (1):
- 59946 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (6).md`

### Ley 19.983  (6 citas en 3 variantes de artículo/inciso)

**Ley 19.983 art. 2** (1):
- 8.664 (2017) - `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md`
**Ley 19.983 art. 3** (2):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`
- 8.664 (2017) - `Pagos/8.664-2017_ Principio de devengado_ pago inoportuno.md`
**Ley 19983 art. 4** (3):
- 14.828 (2018) - `Bases/14.828-2018, Cuarta copia factura.md`
- 33.246 (2017) - `Bases/33.246-2017, Cuarta copia factura, sin condiciones a credito.md`
- 63.391 (2014) - `Bases/63.391-2014, Cuarta copia factura, sin condiciones a credito.md`

### Ley 20.123  (1 citas en 1 variantes de artículo/inciso)

**Ley 20123 art. 3** (1):
- 37.465 (2013) - `Bases/37.465-2013_ Informacion, retencion y subrogacion.md`

### Ley 20.250  (1 citas en 1 variantes de artículo/inciso)

**Ley 20250 art. tercero transitorio inc. 1 y 3** (1):
- 7.626 (2014) - `Plazos no fatales/Plazos no fatales 2.md`

### Ley 20.285  (5 citas en 5 variantes de artículo/inciso)

**Ley 20.285** (1):
- Resolucion Exenta N 04483 (2009) - `TD/Res. Ex. N° 04483-2009 (TD Confianza)_ Ap. Ctto. CGR con Concorde Ltda..md`
**Ley 20.285 art. 1 art. 10** (1):
- 36.593 (2016) - `Derechos Consolidados/36.593-2016.md`
**Ley 20285 art. primero** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`
**Ley 20285 art. primero art. 10** (1):
- 75.501 (2013) - `Plazos no fatales/Plazos no fatales con art 41 2.md`
**Ley N°20.285** (1):
- (sin número) (?) - `Directivas/Directiva45.md`

### Ley 20.296  (2 citas en 2 variantes de artículo/inciso)

**Ley 20.296 art. 3** (1):
- 41.236 (2017) - `Foro Inverso/41.236-2017_ Def. Vicio Formal.md`
**Ley 20296 art. 3** (1):
- 41236 (2017) - `Evaluacion/41.236-2017, valor portal distinto anexo oferta, lo que digan las bases.md`

### Ley 20.309  (4 citas en 4 variantes de artículo/inciso)

**Ley 20.309 art. 2 transitorio** (1):
- 70.620 (2013) - `TD/Art. 10, N° 7, g)/Casa moneda no es proveedor unico.md`
**Ley 20.309 art. 3 inc. 1** (1):
- 70.620 (2013) - `TD/Art. 10, N° 7, g)/Casa moneda no es proveedor unico.md`
**Ley 20.309 art. 3 inc. 2** (1):
- 70.620 (2013) - `TD/Art. 10, N° 7, g)/Casa moneda no es proveedor unico.md`
**Ley 20.309 art. 6** (1):
- 70.620 (2013) - `TD/Art. 10, N° 7, g)/Casa moneda no es proveedor unico.md`

### Ley 20.314  (1 citas en 1 variantes de artículo/inciso)

**Ley 20.314** (1):
- Resolucion Exenta N 04483 (2009) - `TD/Res. Ex. N° 04483-2009 (TD Confianza)_ Ap. Ctto. CGR con Concorde Ltda..md`

### Ley 20.393  (2 citas en 2 variantes de artículo/inciso)

**Ley 20.393 art. 10** (1):
- 24.268 (2017) - `TD/24.268-2017_ TD, debe acompañar anexo de que no es inhabil para contratar.md`
**Ley 20.393 art. 8** (1):
- 24.268 (2017) - `TD/24.268-2017_ TD, debe acompañar anexo de que no es inhabil para contratar.md`

### Ley 20.407  (1 citas en 1 variantes de artículo/inciso)

**Ley 20.407 art. 6** (1):
- 29281 (2013) - `Evaluacion/Mas del ppto estimado NO.md`

### Ley 20.416  (2 citas en 1 variantes de artículo/inciso)

**ley 20416** (2):
- 661 (2024) - `Normas macro/Decreto-661_12-DIC-2024 (1).md`
- 21634 (2023) - `Normas macro/Ley-21634_11-DIC-2023 (3).md`

### Ley 20.557  (1 citas en 1 variantes de artículo/inciso)

**Ley 20557 art. 6** (1):
- 47.664 (2012) - `Bases/47.664-2012_ no puedo exigir inscripcion en reg especial.md`

### Ley 20.641  (1 citas en 1 variantes de artículo/inciso)

**Ley 20.641 art. presupuestario** (1):
- Resolucion Exenta N 04675 (2013) - `TD/Art. 10, N° 7, m)/CGR hace contrato antes del trato directo.md`

### Ley 20.720  (1 citas en 1 variantes de artículo/inciso)

**Ley 20.720 art. 401** (1):
- 11.274 (2018) - `Foro Inverso/11.274-2018_ Ob. consultar foro inverso del proveedor.md`

### Ley 20.730  (5 citas en 5 variantes de artículo/inciso)

**Ley 20.730 art. 4 num. 1** (1):
- (sin número) (2021) - `Varios/160316N21 - Corporaciones Municipales, Ley de Compras.md`
**Ley 20730 art. 3** (1):
- 84.990 (2016) - `Comisiones de Evaluacion/Se puede por acto previo.md`
**Ley 20730 art. 5** (1):
- 84.990 (2016) - `Comisiones de Evaluacion/Se puede por acto previo.md`
**Ley 20730 art. 7** (1):
- 84.990 (2016) - `Comisiones de Evaluacion/Se puede por acto previo.md`
**Ley 20730 art. 8** (1):
- 84.990 (2016) - `Comisiones de Evaluacion/Se puede por acto previo.md`

### Ley 20.880  (2 citas en 2 variantes de artículo/inciso)

**Ley 20.880 art. 1 inc. fin** (1):
- 002453N18 (2018) - `Varios/Dictamen CGR N° 2453-2018, Probidad y Compras.md`
**ley 20880** (1):
- 21634 (2023) - `Normas macro/Ley-21634_11-DIC-2023 (3).md`

### Ley 21.053  (1 citas en 1 variantes de artículo/inciso)

**Ley 21.053** (1):
- 7.561 (2018) - `Pagos/7.561-2018_ Pago oportuno de proveedores.md`

### Ley 21.634  (5 citas en 3 variantes de artículo/inciso)

**Ley 21634** (3):
- E141710N25 (2025) - `Compras agiles/contraloria (15).md`
- E72886N25 (2025) - `Compras agiles/contraloria (16).md`
- E464046N24 (2024) - `Compras agiles/contraloria (19).md`
**Ley N°21.634** (1):
- (sin número) (?) - `Directivas/Directiva45.md`
**ley 21634** (1):
- 661 (2024) - `Normas macro/Decreto-661_12-DIC-2024 (1).md`

### Ley 21.719  (1 citas en 1 variantes de artículo/inciso)

**Ley N°21.719** (1):
- (sin número) (?) - `Directivas/Directiva45.md`

### Ley 211  (2 citas en 2 variantes de artículo/inciso)

**decreto ley 211 art/18 num/3** (1):
- (sin número) (2024) - `Normas macro/ICG-N-6.md`
**decreto ley 211 art/18 num/4** (1):
- (sin número) (2024) - `Normas macro/ICG-N-6.md`

### POL art. 19 num. 2  (1 citas en 1 variantes de artículo/inciso)

**POL art. 19 num. 2** (1):
- 42.462 (2011) - `Foro Inverso/42.462-2011_ Reqs formales elevados a esenciales, bases.md`

### POL art. 19 num. 22  (1 citas en 1 variantes de artículo/inciso)

**POL art. 19 num. 22** (1):
- 42.462 (2011) - `Foro Inverso/42.462-2011_ Reqs formales elevados a esenciales, bases.md`

### POL art. 24  (1 citas en 1 variantes de artículo/inciso)

**POL art. 24** (1):
- 002659N21 (2021) - `Compras agiles/contraloria (23).md`

### POL art. 6-7  (1 citas en 1 variantes de artículo/inciso)

**POL art. 6-7** (1):
- 63418 (2014) - `Evaluacion/Mas del ppto estimado.md`

### POL art. 8  (3 citas en 1 variantes de artículo/inciso)

**POL art. 8** (3):
- 42.462 (2011) - `Foro Inverso/42.462-2011_ Reqs formales elevados a esenciales, bases.md`
- 067134N16 (2016) - `Adjudicacion/Publicar razones de demora adj.md`
- 002453N18 (2018) - `Varios/Dictamen CGR N° 2453-2018, Probidad y Compras.md`

### POL art. 8 inc. 1  (1 citas en 1 variantes de artículo/inciso)

**POL art. 8 inc. 1** (1):
- (sin número) (2021) - `Varios/160316N21 - Corporaciones Municipales, Ley de Compras.md`

### POL art. 98  (3 citas en 1 variantes de artículo/inciso)

**POL art. 98** (3):
- 61067 (2016) - `Evaluacion/MERITO! Eval. Experiencia.md`
- 36.248 (2016) - `Foro Inverso/36.248-2016_ FI, complemenatción de antecedentes no evaluables.md`
- 061067N16 (2016) - `Adjudicacion/MERITO! Eval. Experiencia.md`

### POL art. 99  (1 citas en 1 variantes de artículo/inciso)

**POL art. 99** (1):
- 36.248 (2016) - `Foro Inverso/36.248-2016_ FI, complemenatción de antecedentes no evaluables.md`

### RES 1600/2008  (2 citas en 1 variantes de artículo/inciso)

**RES 1600/2008** (2):
- 57.470 (2012) - `Garantias/57.470-2012_ Debe consignarse monto y plazo GSO.md`
- 48.929 (2012) - `Bases/48.929-2012_ Ob de entregar toda la info.md`

### RES 1600/2008 art. 5  (1 citas en 1 variantes de artículo/inciso)

**RES 1600/2008 art. 5** (1):
- 59.946 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (7).md`

### RES 1600/2008 art. 6  (5 citas en 1 variantes de artículo/inciso)

**RES 1600/2008 art. 6** (5):
- 71.953 (2011) - `Presupuesto/Art. 11 DS 250 (Funcion publica).md`
- 39.228 (2009) - `Presupuesto/Art. 11 DS 250 2.md`
- 24.685 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (10).md`
- 48.093 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (8).md`
- 57.416 (2016) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g.md`

### RES 1600/2008 art. 6 inc. 2  (1 citas en 1 variantes de artículo/inciso)

**RES 1600/2008 art. 6 inc. 2** (1):
- 59.946 (2010) - `TD/Art. 10, N° 7, g)/Art. 10, N° 7, Letra g (7).md`

### Resolucion 36/2024  (7 citas en 1 variantes de artículo/inciso)

**Resolución N°36/2024 (Contraloría)** (7):
- 31 (2026) - `Directivas/037-B-Res.-Aprueba-Directiva-de-Contratacion-N-31-2026-Codigo-etica-proveedores.md`
- 14 (2026) - `Directivas/054-B-Res.-Aprueba-Directiva-de-Contratacion-N°-14-2026-Comisiones-Evaluadoras.md`
- 28 (2025) - `Directivas/557BRes-Directiva28-2025-CodigodeEtica.md`
- 10 (2025) - `Directivas/565-B-Res.-Aprueba-Directiva-de-Contratacion-Publica-N°-10-2025-sobre-Trato-Directo.md`
- (sin número) (?) - `Directivas/Actualizacion-Directiva20.md`
- (sin número) (?) - `Directivas/Directiva-44-Ciencia-de-Datos-IA.md`
- (sin número) (?) - `Directivas/directiva-compras-coordinadas.md`

### Resoluciones 1.002 de 2011 y 102 de 2016  (1 citas en 1 variantes de artículo/inciso)

**Resoluciones 1.002 de 2011 y 102 de 2016** (1):
- (sin número) (2019) - `Errores no esenciales/Res. 8 CGR (Fija montos para Nva 1600).md`

### Resoluciones N°7 y N°14 (Contraloría)  (1 citas en 1 variantes de artículo/inciso)

**Resoluciones N°7 y N°14 (Contraloría)** (1):
- (sin número) (?) - `Directivas/Directiva45.md`

### Resolución Exenta N°537-B/2024  (3 citas en 1 variantes de artículo/inciso)

**Resolución Exenta N°537-B/2024** (3):
- 31 (2026) - `Directivas/037-B-Res.-Aprueba-Directiva-de-Contratacion-N-31-2026-Codigo-etica-proveedores.md`
- (sin número) (?) - `Directivas/Actualizacion-Directiva20.md`
- (sin número) (?) - `Directivas/Directiva45.md`

### constitución política  (1 citas en 1 variantes de artículo/inciso)

**constitución política** (1):
- 19886 (2003) - `Normas macro/LEY-19886_30-JUL-2003 (2).md`
