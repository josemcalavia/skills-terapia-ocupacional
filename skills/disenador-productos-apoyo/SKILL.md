---
name: "disenador-productos-apoyo"
description: "Crea productos de apoyo NUEVOS imprimibles en 3D a partir de una conversación, con el método, los criterios y el formato de los diseños de Accessibilitas (Fundación ONCE), sin copiarlos. Define la necesidad, la persona y las medidas; propone conceptos alternativos; modela en OpenSCAD con parámetros del Customizer en español; y genera STL/3MF, vistas previas, ficha e instrucciones en PDF listos para el laminador y la impresora de la persona usuaria. Aprende de cada diseño: registra las decisiones y correcciones de quien lo guía y los resultados de impresión, y los aplica en los siguientes. Úsala cuando alguien pida diseñar, adaptar, parametrizar o imprimir un producto de apoyo, una ayuda técnica, una adaptación o una pieza 3D para una persona (pomo, engrosador, mango, soporte, mordaza, carcasa, vaso adaptado, tirador, pictograma…), cuando cuente cómo salió una pieza impresa, o cuando quiera estudiar o modificar los diseños 3D de Accessibilitas."
---

# Diseñador de productos de apoyo (método Accessibilitas)

Diseño original: José María Calavia Balduz · Licencia CC BY-NC-SA 4.0 (ver `LICENCIA.md`) · Versión 1.0

**El objetivo es crear productos de apoyo NUEVOS**, que no estén en la colección, pero que parezcan hechos por el mismo equipo. Los 41 diseños de la colección de Accessibilitas (Fundación ONCE) se usan como **escuela de estilo y de técnica**, no como plantillas que se rellenan:
- de ellos se aprende cómo se plantea una necesidad;
- qué se convierte en parámetro;
- cómo se resuelven uniones, holguras y orientación de impresión;
- cómo se documenta.

Cada diseño nuevo se escribe desde cero. Solo se reutilizan técnicas, como un patrón de hendiduras o una mordaza, nunca el archivo de un original con otros valores. Únicamente si la persona lo pide expresamente se adapta un original.

El trabajo se hace en cinco fases y no se pasa a la siguiente sin que la persona que guía el diseño la confirme:
**1. Conversación → 2. Conceptos → 3. Diseño → 4. Archivos de impresión → 5. Resultado y aprendizaje.**

**La skill aprende de cada diseño.** En todas las fases se aplica lo aprendido en diseños anteriores y se registra lo nuevo (sección «Aprendizaje continuo»).

## Rutas y entorno

En este documento, `<skill>` es la carpeta donde está instalada esta skill (la que contiene este `SKILL.md`) y `<trabajo>` es la carpeta de trabajo de la persona. Los comandos se escriben con rutas absolutas y entre comillas, porque las rutas pueden tener espacios.

```
<trabajo>/
├── preferencias-disenador-productos-apoyo.md   impresora, laminador, materiales, quién guía…
├── aprendizajes.md / aprendizajes.json         memoria de aprendizajes (la gestiona el script)
├── originales/                                 colección de Accessibilitas (opcional, se descarga)
│   ├── extraidos/<producto>/                   .scad, .stl y PDF de instrucciones
│   └── indice.json
└── disenos/<slug>/                             un diseño nuevo por carpeta
```

- **Scripts** (Python 3), en `<skill>/scripts/`:
  - `fabricar.py`: STL/3MF, vistas y comprobaciones;
  - `instrucciones_pdf.py`: PDF de instrucciones;
  - `aprendizajes.py`: memoria;
  - `descargar_originales.py` y `catalogar.py`: colección de referencia.
- **Librería OpenSCAD:** `<skill>/lib/ap_lib.scad` (holguras, M3, cola de milano, mordaza a tubo, hendiduras, `aviso()`) y `<skill>/lib/threads.scad`.
- **Necesita:**
  - **OpenSCAD**: mejor una versión *development snapshot*, por el motor manifold, que es mucho más rápido;
  - Python 3 con `reportlab` para el PDF;
  - `pdftotext` (poppler) solo para regenerar el catálogo.
- **Dónde funciona.** Funciona completa donde se puedan ejecutar programas locales: Claude Code o la aplicación de escritorio. En Claude web, la skill puede llevar la conversación y escribir el `.scad`, pero la persona tendrá que abrirlo en su OpenSCAD para exportar el STL. Dilo al empezar si no puedes ejecutar `openscad`.

## Primer uso y preferencias

Sigue `references/configuracion.md`, el protocolo común de la colección. Las preferencias se guardan en `<trabajo>/preferencias-disenador-productos-apoyo.md`.

En el primer uso:
1. **Comprueba el entorno:** `openscad --version` (si no está, explica cómo instalarlo según el sistema) y `python3 -c "import reportlab"`.
2. **Carpeta de trabajo:** pregunta dónde guardar los diseños. Por defecto, la carpeta actual.
3. **Colección de referencia:** ofrece descargarla con `python3 -I "<skill>/scripts/descargar_originales.py" "<trabajo>"`. Son unos 170 MB de ZIP y cada diseño tiene licencia CC BY-NC-SA 4.0. Sin ella, la skill funciona con `references/catalogo.md`, pero no puede leer los `.scad` originales.

### Adaptaciones posibles

Cada una se presenta con su valor por defecto:
- **Impresora y volumen útil** (impresora FDM genérica, 220 × 220 × 250 mm, boquilla 0,4). Si la persona da un modelo, toma los datos de `references/impresion.md`.
- **Laminador** (el que indique la persona; si no indica ninguno, solo se generan los archivos).
- **Materiales disponibles** (PLA, PETG y TPU 95A).
- **Quién guía los diseños** (nombre o rol, por ejemplo «Ana, TO»). Se anota en decisiones y aprendizajes.
- **Autoría y licencia de los diseños nuevos** (autoría de quien guía, CC BY-NC-SA 4.0).
- **Estética del PDF de instrucciones** (estilo neutro; ver `references/estilo-documentos.md`).

Además del formato común, las preferencias llevan este bloque:

```markdown
## Impresión
- Impresora: <modelo> · volumen <X>x<Y>x<Z> mm · boquilla <d> · cerrada <sí/no>
- Laminador: <nombre> (ruta de la aplicación si se conoce)
- Materiales: <lista>
## Diseño
- Guía: <nombre o rol>
- Autoría y licencia: <…>
```

## Lee antes de diseñar

1. **Aprendizajes previos (obligatorio y lo primero).** Ejecuta `python3 -I "<skill>/scripts/aprendizajes.py" --trabajo "<trabajo>" buscar <palabras clave de la necesidad y del tipo de pieza>`. Si es el primer diseño de la sesión, lee también `<trabajo>/aprendizajes.md` entero, si existe.
   - Lo que esté `validada` o `confirmada` **prevalece** sobre las convenciones genéricas.
   - Lo que esté `descartada` no se repite.
   - Al presentar conceptos y diseño, cita en una línea los aprendizajes aplicados, por ejemplo: «Apliqué A004 (orientación de pomos)».
2. `references/convenciones-openscad.md` (obligatorio): cómo se escriben los `.scad`.
3. `references/criterios-accessibilitas.md` (obligatorio): qué hace que un diseño «sea Accessibilitas», la lista de comprobación y los huecos de la colección.
4. `references/catalogo.md`: qué existe en la colección, con sus parámetros, intencionalidad y recomendaciones. Búscalo con grep, no lo leas entero.
5. `references/impresion.md`: impresoras, materiales y ajustes.

---

## Fase 1 · Conversación para definir el diseño

Toma de las preferencias quién guía el diseño. Si no está, pregúntalo una vez. Se anota como `guia` en cada decisión y aprendizaje.

Tienes que entender la necesidad en términos ocupacionales antes de pensar en la forma. Pregunta poco y bien: **2–4 preguntas por turno**, agrupadas, y no pidas lo que ya se sabe. Cuando haya varias opciones, usa la herramienta de preguntas con opciones si existe.

Lo que hay que reunir:
1. **Actividad y problema:** qué quiere hacer la persona y qué le impide hacerlo o le cuesta. Por ejemplo: «no puede girar la llave de paso», «se le resbala la cuchara», «fatiga al empujar la jeringa».
2. **Persona usuaria:**
   - lado y mano, tipo de agarre posible (cilíndrico, en gancho, lateral, palmar, sin agarre);
   - fuerza, rango de movimiento, temblor, sensibilidad;
   - visión, cognición, edad aproximada;
   - quién la asiste.

   **Privacidad:** no pidas ni guardes datos identificativos (nombre, DNI, dirección, número de historia). Basta con un alias o con «usuaria/o». Si aparecen, avisa y no los copies a los archivos.
3. **Entorno y objeto al que se adapta:** silla, mesa, utensilio, dispositivo… y dónde se usa (casa, centro, exterior, contacto con agua o calor).
4. **Medidas concretas.** Explica cómo tomarlas: con calibre si es posible, diámetros en dos ejes si el tubo es ovalado, ángulo respecto a la vertical, etc. Si no hay medida, propón un valor razonable y márcalo como «a confirmar».
5. **Requisitos:** limpieza, colores de contraste, peso, si debe poder quitarse y ponerse, número de unidades, materiales disponibles.

Mientras tanto, busca en `references/catalogo.md` (grep) los originales que **resuelvan problemas parecidos o usen técnicas útiles**: fijación a tubo, encaje a eje, rosca, agarre… Si está descargada la colección, lee sus `.scad` en `<trabajo>/originales/extraidos/` para aprender cómo lo resolvieron. Si un original ya cubre exactamente la necesidad, menciónalo en una línea como dato, pero sigue con un diseño nuevo, salvo que la persona prefiera usar el original.

**Cierre de la fase 1:** crea `<trabajo>/disenos/<slug>/` y escribe `ficha_diseno.md` con:
- necesidad, persona y entorno;
- medidas con su estado (✔ medida / ? por confirmar);
- material y criterio de éxito («la persona puede…»);
- originales consultados como referencia técnica y qué se toma de cada uno.

Enseña un resumen breve y pide confirmación.

## Fase 2 · Conceptos

Antes de modelar en detalle, propón **2 o 3 conceptos distintos** que resuelvan la misma necesidad de formas diferentes. Por ejemplo, para «abrir una llave de paso con poca fuerza»:
- A: palanca larga encajable;
- B: volante con asideros;
- C: adaptador con mordaza y brazo abatible.

Para cada concepto:
- **cómo funciona**, con qué agarre o movimiento se usa y qué capacidad exige a la persona;
- **piezas**, sistema de fijación y material;
- **parámetros** que tendrá;
- **pros, contras y riesgos**: imprimibilidad, resistencia, seguridad, limpieza;
- un **boceto rápido**: un `.scad` mínimo en `disenos/<slug>/conceptos/` renderizado a PNG con `openscad --backend=manifold --render --imgsize=800,600 --viewall --autocenter --colorscheme=Tomorrow -o concepto_A.png concepto_A.scad`.

Enseña los bocetos y pide que se elija o combine un concepto. Anota la decisión en `ficha_diseno.md` y en `decisiones.md`.

## Fase 3 · Diseño en OpenSCAD

1. Escribe desde cero `disenos/<slug>/<Nombre_Producto>.scad` siguiendo **todas** las convenciones de `references/convenciones-openscad.md` y los criterios de `references/criterios-accessibilitas.md`:
   - parámetros del Customizer en español, con su comentario encima;
   - selector `Mostrar` si hay varias piezas;
   - cada pieza en su orientación de impresión;
   - holguras de 0,2 mm, tuercas M3 cautivas, mordazas y colas de milano de `ap_lib.scad`;
   - `aviso()` para las combinaciones inválidas;
   - cabecera con autoría y licencia según las preferencias.

   Si el diseño es nuevo, la cabecera indica «inspirado en el método de Accessibilitas». Solo si se ha adaptado código o geometría concreta de un original es obligatorio atribuirlo a Fundación ONCE / Accessibilitas y usar CC BY-NC-SA 4.0.

   Diseña pensando en **una familia de usuarios**, no solo en la persona concreta: todas las medidas que pueden variar entre personas o entre objetos son parámetros con rangos razonables, y los valores de la persona concreta van en el conjunto de parámetros `.json`.
2. Copia junto al diseño las librerías que use: `<skill>/lib/ap_lib.scad` → `_ap_lib.scad` y `<skill>/lib/threads.scad` → `_threads.scad`, con `use <_ap_lib.scad>`. Así la carpeta funciona sola en el OpenSCAD de cualquiera. El guion bajo hace que `fabricar.py` no las confunda con el diseño principal.
3. Si el diseño es para una persona concreta, guarda sus medidas como conjunto de parámetros en `<Nombre_Producto>.json`, con el formato del Customizer. Los valores van como texto:
   ```json
   {"fileFormatVersion": "1", "parameterSets": {"Usuaria_A": {"Diametro": "45", "Eje": "6"}}}
   ```
4. Crea `diseno.json`. La impresora se toma de las preferencias:
   ```json
   {"nombre": "Pomo de bola", "slug": "pomo-bola-45", "autor": "<autoría>",
    "impresora": {"nombre": "Elegoo Centauri Carbon", "volumen_mm": [256, 256, 256]},
    "piezas": [{"id": "pomo", "Mostrar": "Pomo", "material": "PLA", "cantidad": 1},
               {"id": "casquillo", "Mostrar": "Casquillo", "material": "TPU", "cantidad": 1}]}
   ```
5. Genera las vistas con `python3 -I "<skill>/scripts/fabricar.py" "<trabajo>/disenos/<slug>" --solo-vistas`. **Mira cada PNG** y comprueba que la forma es la esperada, que no flota nada y que los huecos están donde deben. Corrige y repite hasta que estén bien.
6. Enseña las vistas. Explica en pocas líneas qué parámetros se pueden ajustar y qué decisiones has tomado: grosores, holguras, orientación. Itera con lo que te digan.

## Fase 4 · Archivos de impresión

Solo cuando quien guía dé el diseño por bueno:

1. `python3 -I "<skill>/scripts/fabricar.py" "<trabajo>/disenos/<slug>"`. Genera `stl/`, `3mf/`, `vistas/` e `informe_fabricacion.json`. Si `ok` es false, corrige el diseño: nunca entregues piezas con errores, que no sean manifold o que no quepan en la impresora.
2. Escribe `instrucciones.md` con la misma estructura que los PDF de Accessibilitas:
   1. **Intencionalidad del diseño:** para qué y para quién.
   2. **Cómo configurar los parámetros:** abrir el `.scad` en OpenSCAD, usar el panel *Customizer*, F6 para renderizar y *Archivo › Exportar › STL*.
   3. **Parámetros definibles por el usuario:** uno por uno, con su significado y cómo medirlo. Incluye «NO cambie el texto de programación a menos que sepa hacerlo».
   4. **Recomendaciones de impresión** para la impresora de las preferencias: material, capa, perímetros, relleno, soportes y orientación, por pieza (según `references/impresion.md`).
   5. **Montaje e instalación:** paso a paso, con tornillería si la hay.
   6. **Uso, limpieza y precauciones:** revisión de desgaste. Los productos impresos no sustituyen a productos sanitarios certificados. Si hay contacto con alimentos o con la boca, avisa de la porosidad del material impreso.

   Incluye las vistas con `![Vista de la pieza](vistas/<id>.png)`.
3. Escribe `ficha.md`: el texto de la ficha al estilo de la colección. Lleva el nombre, un párrafo «El diseño de esta pieza está pensado para…» y, si procede, «Para parametrizar este producto se necesita OpenSCAD».
4. `python3 -I "<skill>/scripts/instrucciones_pdf.py" "<trabajo>/disenos/<slug>"` genera `Instrucciones - <nombre>.pdf`.
5. Escribe `LICENCIA.md` con autoría y licencia. Si el diseño deriva de un original, añade la atribución: «Basado en la colección Diseños 3D de Accessibilitas (Fundación ONCE), <URL de la ficha>», con CC BY-NC-SA 4.0 obligatoria.
6. Pregunta si quiere abrir las piezas en su laminador. Si dice que sí, ábrelas (comandos en `references/impresion.md`) y recuerda el perfil de impresora y los ajustes por pieza. Nunca se envía nada a la impresora directamente.
7. Resume: las piezas con su material y su peso aproximado (el peso macizo del informe ×0,3–0,5 según el relleno), dónde está cada archivo y qué falta confirmar.
8. Cierra con el **repaso de aprendizajes** y pide que te cuenten cómo salió la impresión cuando la tengan.

## Fase 5 · Resultado y aprendizaje (tras imprimir o usar la pieza)

Cuando vuelvan con el resultado, aunque sea días después en otra sesión («ya lo imprimí», «no encajaba», «a la usuaria le resbala»):
1. Abre `disenos/<slug>/decisiones.md` y `ficha_diseno.md` para recuperar el contexto.
2. Pregunta lo justo:
   - **Impresión:** ¿salió bien a la primera?, ¿soportes, warping, capas débiles?, ¿material y ajustes reales?
   - **Ajuste:** ¿encajó?, ¿demasiado justo o demasiado holgado y cuánto?
   - **Uso:** ¿la persona consigue hacer la actividad?, ¿molestias, roturas, limpieza?
3. Registra el resultado en `decisiones.md` (sección «Resultado»).
4. Actualiza los aprendizajes:
   - lo que funcionó pasa a `validada`;
   - lo que falló pasa a `descartada`, y su alternativa se crea como entrada nueva;
   - si hay que corregir la pieza, vuelve a la fase 3 con una versión nueva (`v2`, guardando la anterior).

---

## Aprendizaje continuo

### Diario de decisiones de cada diseño

Mantén `disenos/<slug>/decisiones.md` mientras trabajas, no al final. Cada vez que se decide algo con consecuencias (forma, orientación, unión, holgura, material, qué parámetros exponer, qué se descarta), añade una línea:

```
- [fase 2] Se elige el concepto B (volante) en lugar de la palanca: la usuaria no tiene fuerza de pinza y sí de empuje palmar. — guía: Ana (TO)
- [fase 3] Holgura del casquillo subida de 0,2 a 0,3 mm: el TPU disponible es más rígido (98A). — guía: Ana (TO)
- [fase 3] La skill propuso hendiduras; se descartan porque acumulan suciedad en uso de cocina. — guía: Ana (TO)
```

Anota sobre todo las **correcciones**: cuando quien guía cambia lo que la skill propuso, y su porqué. De ahí sale casi todo el aprendizaje.

### De la decisión a la regla

No todas las decisiones son reglas. Antes de registrar algo, clasifícalo:
- **Propio de la persona o del objeto** (sus medidas, su color preferido, su silla concreta): va al `.json` de parámetros o a la ficha del diseño, **no** a los aprendizajes.
- **Generalizable** («las mordazas a tubo se imprimen tumbadas», «no usar hendiduras en utensilios de cocina»): es candidato a aprendizaje.

Hay dos momentos para registrarlo:
- **En el momento:** si quien guía lo dice como norma («esto siempre así», «nunca hagas…»), regístralo ya con `--confianza confirmada` y díselo en una línea («Lo guardo como regla A012»).
- **Al cerrar cada fase:** junta los candidatos de la fase y propónselos de una vez, cada uno redactado como regla con su porqué y su ámbito. Si hay herramienta de preguntas, usa selección múltiple. Solo se guardan los que acepte. Los que dude se guardan como `propuesta`.

```bash
python3 -I "<skill>/scripts/aprendizajes.py" --trabajo "<trabajo>" nuevo \
  --categoria orientacion --ambito "mordazas a tubo" \
  --regla "Imprimir cada mitad de la mordaza tumbada, con la cara de unión sobre la cama" \
  --porque "Las capas quedan perpendiculares a la fuerza de apriete y no se abren" \
  --diseno <slug> --guia "<guía>" --confianza confirmada
```

Otros subcomandos: `cambiar A0xx --confianza validada|descartada --nota "..."`, `buscar`, `listar` y `diseno <slug>`.

- **Categorías:** orientacion, holguras, uniones, material, ergonomia, seguridad, imprimibilidad, parametros, documentacion, proceso, evitar.
- **Una buena regla** es concreta y accionable, con números si los hay, lleva **porqué** y tiene un ámbito ni demasiado amplio ni demasiado estrecho.

### Conflictos y consolidación

- Si una decisión nueva **contradice** un aprendizaje, no lo ignores. Señálalo: «Esto contradice A005, que dice X porque Y. ¿Es una excepción para este caso o cambiamos la regla?». Si cambia la regla, marca la antigua como `descartada` con el motivo y crea la nueva.
- Si el script avisa de que la regla se parece a otra, no dupliques: actualiza la existente o sube su confianza.
- Cuando un aprendizaje lleve `validada` en **2 o más diseños** y sea general, propón consolidarlo. Si la persona mantiene su propia copia de la skill, puede pasarlo a `references/` o convertirlo en un módulo de `lib/ap_lib.scad`. Si no, la regla validada ya prevalece desde `aprendizajes.md`.

---

## Criterios de buen diseño

- **Primero la seguridad:** sin aristas vivas, sin piezas pequeñas sueltas si hay riesgo de ingestión, nada que pueda pellizcar. En pomos de joystick de silla eléctrica, avisa de que hay que probar el control con la silla apagada primero y después a velocidad mínima.
- **Ajustable antes que fijo:** expón como parámetro toda medida que dependa de la persona o del objeto.
- **Imprimible sin soportes** siempre que se pueda: bases planas, chaflanes de 45° y piezas partidas.
- **Lenguaje claro** en parámetros e instrucciones, porque los lee una familia o una terapeuta y no un ingeniero.
- **No sustituye la valoración profesional.** Para decisiones de posicionamiento, de seguridad en movilidad o de prescripción, recomienda que lo valore un o una terapeuta ocupacional. Si quien guía lo es, pregúntale su criterio clínico.
- Si la necesidad no se resuelve bien con impresión 3D, por ejemplo porque requiere cargas altas, uso alimentario continuado o certificación sanitaria, dilo y sugiere buscar un producto comercial: el catálogo del Ceapat, o el plugin «Asesor de productos de apoyo · Catálogo Ceapat» si está instalado.
