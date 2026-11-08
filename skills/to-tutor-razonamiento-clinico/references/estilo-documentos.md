# Estética de los documentos

Se aplica a todo documento que genere la skill (Word, PDF, Markdown, HTML o texto en el chat). Primero se usan las preferencias de la persona. Lo que no haya definido se toma del estilo neutro.

## Estilo neutro (por defecto)

| Elemento | Valor |
|---|---|
| Formato de salida | Las respuestas van siempre en el chat. Solo se genera un documento (Word, PDF u otro formato) si lo pide la persona o sus preferencias |
| Página | A4, márgenes de 2,5 cm |
| Tipografía | Sans serif estándar: Calibri (Word); si no está disponible, Arial o Helvetica |
| Cuerpo | 11 pt, interlineado 1,15, color #222222 |
| Títulos | Título del documento a 20 pt; Título 1 a 16 pt; Título 2 a 13 pt; Título 3 a 11,5 pt; en negrita y color principal. La tipografía elegida se aplica a títulos y cuerpo |
| Color principal | Gris azulado #2E4A62 |
| Color secundario | Gris claro #E6EBF0 (fondos de cabecera de tabla y separadores) |
| Tablas | Texto a 10 pt, fila de cabecera con fondo secundario (repetida si la tabla pasa de página) y bordes finos grises. Las tablas muy anchas, como las rúbricas, en página horizontal |
| Cabecera | Texto breve del tipo de documento (por ejemplo, «Informe de Terapia Ocupacional»), sin repetir el título completo |
| Pie | Número de página |
| Nota de cierre | Al final del documento, una sola vez: la nota de revisión que indique el `SKILL.md`. En material de estudio o docente, usa «Material elaborado con apoyo de IA. Revísalo antes de usarlo o difundirlo» |
| Imágenes | Ninguna: sin logotipos ni elementos decorativos |

## Qué se puede personalizar

- **Formato de salida**: texto en el chat, Word (.docx), PDF, Markdown o HTML.
- **Colores**: un color principal y otro secundario (en hexadecimal o por nombre), o monocromo. Si la persona solo cambia el principal, usa como secundario un tono muy claro del principal (mezclado con un 89 % de blanco) en lugar del gris por defecto, y dilo.
- **Tipografía**: familia y tamaño del cuerpo y de los títulos.
- **Logotipo propio**: imagen que adjunta la persona (PNG o SVG), su posición en la cabecera (izquierda, centro o derecha) y su tamaño.
- **Cabecera y pie**: textos propios, como el nombre del servicio, datos de contacto profesional o el número de colegiado. Solo los que indique la persona.
- **Densidad**: compacta, estándar o espaciada.
- **Accesibilidad**: lectura fácil (frases cortas, 14 pt, más espacio) o alto contraste.
- **Plantilla propia**: si la persona adjunta un .docx de plantilla, úsalo como base y respeta sus estilos, cabecera y pie.

## Cómo aplicarla

- **Chat y documento a la vez**: si se genera un documento, en el chat da solo un resumen, la ruta del archivo y lo que queda pendiente. No repitas el contenido entero.
- **Firma y datos profesionales**: al final del documento, antes de la nota de cierre, con los datos o marcadores que indiquen las preferencias.

- Si dispones de herramientas para crear documentos (skills de docx o pdf, ejecución de código), aplica los valores exactos de las preferencias.
- Si no dispones de ellas, entrega el contenido en Markdown bien estructurado y explica que la estética se aplicará al exportarlo.
- Usa estilos de título reales (Título 1, Título 2), tablas con fila de cabecera y texto alternativo en el logotipo.
- El texto debe tener un contraste mínimo de 4,5:1 con el fondo. Si un color elegido no lo cumple, avísalo y propone una variante más oscura.
- No uses el color como único medio para transmitir información. Por ejemplo, un semáforo siempre va acompañado de su texto («alto», «medio», «bajo»).
- Nunca añadas logotipos, nombres de instituciones ni marcas que la persona no haya configurado.
