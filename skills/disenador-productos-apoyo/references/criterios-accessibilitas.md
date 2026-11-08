# Qué hace que un diseño «sea de Accessibilitas»

Este documento resume los rasgos comunes de los 41 diseños de la colección (2019–2026). Sirve para que un diseño **nuevo** siga el mismo método sin copiar ninguno.

## 1. De dónde nacen los diseños

- Cada diseño parte de **una actividad cotidiana concreta que se ve bloqueada**, no de un objeto:
  - mover la silla eléctrica con un agarre limitado (los pomos para joystick: bola, T, U, silla de montar, palanca);
  - comer y beber (vaso con escotadura, vaso cónico, mango para cubierto, engrosador de chupachups, sujeta-vasos);
  - tomar la medicación (pastilleros);
  - alimentar por botón gástrico (ayuda para jeringa);
  - teclear y usar el ordenador (carcasas de teclado, puntero, joystick, mando para Adaptive Controller);
  - transportar cosas desde la silla (soporte de maleta, de bolso, de tubo, prolongador de asa);
  - abrir y alcanzar (palanca de cisterna, tapón de botella, caja con tirador, prolongador de mesa);
  - orientarse y comunicarse (cartel braille, pictogramas 3D, Parlanchinator).
- La colección se centra sobre todo en la **adaptación de puestos de trabajo y la vida diaria**, y los usuarios principales son personas con discapacidad física de miembro superior, usuarias de silla de ruedas y personas con discapacidad visual o de comunicación.
- **La persona que asiste también cuenta como usuaria.** La ayuda para jeringa, por ejemplo, está pensada para quien alimenta, no para quien es alimentado.

## 2. Principios de diseño

1. **Parametrizable para personalizar.** Una sola pieza sirve para muchas personas cambiando medidas: el diámetro del eje, el tubo de la silla, las medidas de la tablet o la jeringa, el tamaño del agarre. Si un diseño no se puede parametrizar, se indica explícitamente en la ficha («Este diseño no es parametrizable»).
2. **Se adapta al objeto que la persona ya tiene**, sin modificarlo:
   - encaje a presión sobre el eje del joystick;
   - mordaza sobre el tubo de la silla;
   - carcasa sobre la tablet o el glucómetro;
   - funda sobre el cubierto.
   Nada requiere taladrar ni dañar el objeto original.
3. **Reversible y sin herramientas especiales.** Las fijaciones son a presión con casquillo de TPU, con tornillería M3 estándar o con velcro, de modo que se puede quitar y volver a poner.
4. **Imprimible en casa.** Pensado para impresoras FDM domésticas: piezas pequeñas o partidas y, siempre que se puede, sin soportes. La base se recorta para que la pieza apoye plana (el «Bocado» del pomo de bola). Las recomendaciones son conservadoras: capa de 0,2 mm, 3–4 perímetros y 10–20 % de relleno.
5. **Agarre fácil.** Diámetros generosos, formas redondeadas y la opción de superficie lisa o con hendiduras. Hay variantes según el tipo de agarre: bola para agarre palmar, T para pinza o empuje lateral, U para mano sin agarre o dorso, silla de montar para apoyar la palma.
6. **Varias piezas, un archivo.** Las variantes y las piezas se eligen con el selector `Mostrar`, y cada pieza se exporta en su propio STL.
7. **Lo justo de complejidad.** Formas sencillas con primitivas de OpenSCAD. No se busca una estética escultórica, sino que la pieza funcione y se pueda entender y modificar.
8. **Hay electrónica abierta cuando hace falta.** En ese caso se usan Arduino con librerías abiertas, esquemas eléctricos en PDF y carcasa impresa (joystick, Parlanchinator, Adaptive Controller).
9. **Lo que acompaña al diseño es igual de importante que el diseño.** Cada producto incluye:
   - ficha web: nombre, una frase de propósito y descarga;
   - archivo `.scad` y STL por defecto;
   - PDF de instrucciones paso a paso para alguien que nunca ha usado OpenSCAD;
   - licencia CC BY-NC-SA 4.0, en versión completa y en versión de lectura fácil («inteligible»).

## 3. Estructura de la ficha y de las instrucciones

**Ficha (texto web):**
- `<Nombre>`;
- «El diseño de esta pieza está pensado para…» seguido de la necesidad y de quién se beneficia;
- si no es parametrizable, decirlo.

**Instrucciones en PDF:**
1. Intencionalidad del diseño.
2. Cómo configurar los parámetros. Incluye la instalación de OpenSCAD, abrir el archivo, ver el Customizer, elegir «Sólo descripción», F5 para previsualizar, F6 para renderizar y exportar STL.
3. Una imagen del Customizer o de la pieza.
4. Parámetros definibles por el usuario, numerados (4.1, 4.2…). Para cada uno: qué es, cómo medirlo y en qué afecta. Termina con el aviso «NO debe cambiar nada en el texto de programación…».
5. Recomendaciones de impresión: posición, perímetros, relleno, material (TPU para lo que encaja a presión), capa y soportes. Si hacen falta soportes, se marcan en una imagen.
6. Instalación o montaje.

## 4. Tono

- Español claro, en «usted», con frases completas y sin jerga.
- Se da por hecho que quien lee puede ser un familiar, una terapeuta o una persona voluntaria con impresora, no un ingeniero.
- Se explica el porqué de las recomendaciones. Por ejemplo: «un pequeño corte en la parte inferior no afectará al uso, pero facilitará tremendamente la impresión».

## 5. Lista de comprobación para un diseño nuevo

- [ ] Resuelve una **actividad** concreta y dice a quién va dirigida, incluida la persona que asiste si es el caso.
- [ ] No existe ya en la colección, o mejora claramente algo que sí existe.
- [ ] Se adapta a un objeto existente sin dañarlo y es reversible.
- [ ] Las medidas que varían entre personas u objetos son parámetros, con comentario y rango.
- [ ] Se imprime sin soportes, o los soportes están justificados y señalados.
- [ ] No tiene aristas vivas ni piezas pequeñas peligrosas, y la resistencia es adecuada al uso.
- [ ] Cada pieza está en la orientación de impresión, seleccionable con `Mostrar`.
- [ ] Se entrega con la ficha de una frase, el PDF de instrucciones con la estructura anterior, el STL por defecto y la licencia.
- [ ] Se puede explicar en una frase a alguien sin conocimientos técnicos.

## 6. Huecos de la colección (ideas para diseños nuevos)

Hay áreas poco cubiertas que encajan con el método de la colección:
- **Higiene y vestido:** abrochabotones, calzador para calcetines, soporte de cepillo de dientes o maquinilla, adaptador de grifo.
- **Cocina:** abrebotes con mordaza, tabla de cortar con sujeción, asa adaptable para tazas.
- **Escritura y ocio:** engrosador de lápiz con apoyo de dedos, sujetacartas, adaptador de pulsador para juegos.
- **Tecnología:** soporte de móvil para silla con rótula, lápiz táctil con engrosador, conmutadores adaptados, cubreteclados para teclados genéricos parametrizables.
- **Llaves y puertas:** giradores de llave, tiradores de cremallera, adaptador para manillas.
- **Orientación:** señalética táctil y en braille parametrizable, marcadores táctiles para electrodomésticos.
