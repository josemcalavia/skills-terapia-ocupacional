# Primer uso, adaptación y preferencias

Este protocolo es igual en todas las skills de la colección. Cada `SKILL.md` indica qué se puede adaptar en su sección **«Adaptaciones posibles»**.

## 1. Comprobar si ya hay preferencias

Antes de la primera respuesta, busca unas preferencias guardadas para esta skill, en este orden:

1. En la conversación actual: la persona las ha pegado o adjuntado.
2. Un archivo `preferencias-<nombre-de-la-skill>.md` en los archivos del proyecto, en la carpeta de trabajo o entre los adjuntos.
3. En la memoria o en las instrucciones personalizadas, si el entorno las ofrece.

- **Si las encuentras**, aplícalas sin volver a preguntar y dilo en una línea: «Uso tus preferencias guardadas (resumen breve). Di "cambiar preferencias" cuando quieras modificarlas».
- **Si no las encuentras**, es el primer uso: da la bienvenida (punto 2).

**Lo que se pide en el momento manda.** Si la persona pide algo distinto de sus preferencias (por ejemplo, un Word cuando sus preferencias dicen «solo en el chat»), hazlo así y ofrece en una línea actualizar las preferencias. Si la persona dice que es para siempre («a partir de ahora…»), actualízalas directamente y dilo.

**Sin preferencias, adapta el nivel a la pregunta.** Los valores por defecto son un punto de partida: si la forma de preguntar indica claramente otro nivel (por ejemplo, una duda básica de estudiante), ajústalo y dilo al ofrecer las adaptaciones.

## 2. Bienvenida del primer uso

Escribe un solo mensaje breve (unas 200 palabras como máximo), sin jerga, con estas partes:

1. **Qué hace la skill**, en dos o tres líneas.
2. **Cómo funciona**: los pasos principales numerados, en una línea cada uno.
3. **Qué necesita y qué no hace**: los datos que te pedirá, sus límites y la regla de privacidad (sin nombres, DNI, direcciones ni números de historia). Si la skill no trabaja con datos de personas (por ejemplo, búsquedas bibliográficas), basta con media línea.
4. **¿Quieres adaptarla?** Presenta las opciones de la sección de adaptaciones del `SKILL.md` («Adaptaciones posibles» o la que indique), una por línea, con su **valor por defecto** entre paréntesis y sin explicarlas.
5. **Estética de los documentos**: explica en dos líneas el estilo neutro por defecto y que se puede cambiar el formato de salida, los colores, la tipografía, el logotipo propio, la cabecera y el pie, o usar una plantilla propia (detalle en `references/estilo-documentos.md`).
6. Cierra con: «Dime lo que quieras cambiar, o responde "valores por defecto" para empezar ya».

Si el entorno ofrece una herramienta de preguntas con opciones, puedes usarla para las adaptaciones más importantes.

**No bloquees la tarea.** Si la persona ya ha pedido algo concreto en su primer mensaje, usa la **versión breve** (unas ocho líneas) y, en el mismo mensaje, **haz la tarea con los valores por defecto** si tienes los datos imprescindibles (los que define cada `SKILL.md`). Si faltan, pídelos en ese mismo mensaje. La versión breve tiene estas partes:

- una línea con lo que hace la skill y la regla de privacidad;
- los pasos en una sola línea;
- una línea con los **nombres** de las adaptaciones posibles, sin explicarlas;
- una línea sobre la estética (estilo neutro por defecto; se puede cambiar el formato, los colores, la tipografía, el logotipo o usar una plantilla);
- una línea final: «Lo hago con los valores por defecto; dime si quieres adaptar algo» (o, si antes necesitas datos, «Con tus respuestas lo hago con los valores por defecto»);
- si hacen falta datos para la tarea, pídelos en el mismo mensaje (la bienvenida breve y las primeras preguntas de la tarea pueden ir juntas).

Si la persona pide detalles de alguna adaptación, explícala entonces.

La regla de privacidad se dice una vez en la bienvenida. No la repitas en cada mensaje: vuelve a recordarla solo si detectas datos identificativos.

## 3. Guardar las preferencias

Cuando la persona responda a las adaptaciones, o dé indicaciones de estética o formato que quiera mantener, resume lo que ha elegido con este formato (cada skill puede añadir apartados propios, como `## Seguimiento`):

```markdown
# Preferencias · <nombre-de-la-skill>
Versión de la skill: 2.0
Fecha: AAAA-MM-DD

## Adaptaciones
- <opción>: <valor elegido>

## Estética de los documentos
- Respuestas: en el chat
- Documentos: <ninguno salvo que los pida (por defecto) | Word | PDF | Markdown | HTML>
- Estilo: <neutro | personalizado>
- Color principal: <#hex>   · Color secundario: <#hex>
- Tipografía: <fuente, tamaño>
- Logotipo: <ninguno | archivo propio: nombre, posición, tamaño>
- Cabecera: <texto | ninguno>   · Pie: <texto | ninguno>
- Plantilla propia: <ninguna | nombre del archivo>
- Accesibilidad: <estándar | lectura fácil | alto contraste>
```

Guárdalo según el entorno, en este orden (usa la primera opción que encaje):

1. **Hay una carpeta de trabajo** (por ejemplo, Claude Code, Cowork o Codex): guarda `preferencias-<nombre-de-la-skill>.md` en esa carpeta y dilo. Si la persona prefiere otro sitio, muévelo.
2. **Puedes crear archivos descargables** (Claude o ChatGPT en la web o en la aplicación): crea el archivo y recomienda subirlo a los archivos del proyecto donde se vaya a usar la skill (un proyecto de Claude, o un proyecto o un GPT de ChatGPT). Así se aplicará solo la próxima vez.
3. **Hay memoria disponible**: ofrece guardarlas también allí.
4. **No hay nada de lo anterior**: pide que copie el bloque en las instrucciones del proyecto o del GPT, o que lo pegue al empezar.

Las preferencias nunca contienen datos de pacientes, alumnado ni familias.

## 4. Cambiar las preferencias después

Si la persona dice «cambiar preferencias», «configurar», «ajustes», «cambia el estilo» o algo parecido, muestra las preferencias actuales, pregunta qué quiere cambiar y genera el bloque actualizado.

## 5. Neutralidad de marca

La skill no tiene identidad visual de ninguna institución, centro ni persona. Los documentos que genera no llevan logotipos, nombres de centros ni la firma de quien diseñó la skill. Solo llevan la marca, el logotipo o los datos profesionales que la persona usuaria configure.
