# Catálogo de referencia: Diseños 3D de Accessibilitas (Fundación ONCE)

Generado con `scripts/catalogar.py` a partir de los archivos de la colección (https://accessibilitas.es/disenos-3d/), que se distribuyen con licencia **CC BY-NC-SA 4.0**. Los extractos de parámetros e instrucciones pertenecen a Fundación ONCE / Accessibilitas y se reproducen con atribución y la misma licencia. Rutas relativas a `originales/`.

## adaptador-de-movil-para-cargador-de-silla-de-ruedas

- Ficha: https://accessibilitas.es/2021/12/adaptador-de-movil-para-cargador-de-silla-de-ruedas/
- Intencionalidad: El diseño de esta pieza está pensado para poder cargar un teléfono móvil o una Tablet aprovechando las baterías de la propia silla electrónica, ya que prácticamente todas ellas utilizan el mismo tipo de conector como puerto de carga. De esta forma las personas usuarias de sillas de ruedas electrónicas podrán tener siempre a mano un cargador para sus dispositivos.
- Parametrizable: no (solo STL)
- Archivos: `extraidos/adaptador-de-movil-para-cargador-de-silla-de-ruedas/Cargador_movil_silla_FO_cuerpo.stl`, `extraidos/adaptador-de-movil-para-cargador-de-silla-de-ruedas/Cargador_movil_silla_FO_cuerpo_V2.stl`, `extraidos/adaptador-de-movil-para-cargador-de-silla-de-ruedas/Cargador_movil_silla_adaptador_1.stl`, `extraidos/adaptador-de-movil-para-cargador-de-silla-de-ruedas/Cargador_movil_silla_adaptador_1_V2.stl`, `extraidos/adaptador-de-movil-para-cargador-de-silla-de-ruedas/Cargador_movil_silla_adaptador_2.stl`, `extraidos/adaptador-de-movil-para-cargador-de-silla-de-ruedas/Cargador_movil_silla_tope.stl`
- Impresión: Recomendamos que se imprima con 2-3 perímetros y un relleno del 10%. Se puede imprimir en cualquier material que se desee. La altura de capa recomendada para su impresión es de 0.1-0.2 mm. No es necesario el uso de soportes para su impresión.
- Instalación: En primer lugar, deberá disponer de los siguientes elementos (junto a cada uno encontrará un enlace de ejemplo de dónde lo puede adquirir, aunque los encontrará en muchísimos sitios tanto en tiendas de internet como en tiendas físicas de electrónica): 2.1. Conector macho XLR de 3 pines 2.2. Conversor 5V USB QC3.0 Para la completa realización de este cargador, además necesitará imprimir los siguientes archivos .stl: 2.3. Dependiendo del conversor que haya adquirido deberá imprimir el archivo Cargador_movil_silla_FO_cuerpo.stl si su conversor no tiene el conector USB introducido hasta el fondo d

## ayuda-para-jeringa-de-alimentacion

- Ficha: https://accessibilitas.es/2024/11/ayuda-para-jeringa-de-alimentacion/
- Intencionalidad: El diseño de esta pieza está pensado para mitigar la fatiga que produce en la musculatura de la mano a lo largo del tiempo el movimiento de presión que se realiza con el pulgar al empujar el émbolo de la jeringa a la hora de alimentar a la persona a través de un botón gástrico. Es por tanto una ayuda que va dirigida a la persona que asiste a aquellas personas que necesitan alimentarse mediante un botón gástrico.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/ayuda-para-jeringa-de-alimentacion/Jeringa.scad`, `extraidos/ayuda-para-jeringa-de-alimentacion/Jeringa_cuerpo_60ml.stl`, `extraidos/ayuda-para-jeringa-de-alimentacion/Jeringa_embolo_60ml.stl`, `extraidos/ayuda-para-jeringa-de-alimentacion/threads.scad`
- Parámetros de `Jeringa.scad`:
  - [Parte a mostrar] `Mostrar = "Cuerpo"` [Cuerpo:Cuerpo donde se encajará la jeringa, Embolo:Émbolo roscado que empujará la jeringa] — Elemento que desea mostrar en pantalla
  - [Parámetros de la jeringa] `Diametro = 31` — Diámetro del cuerpo de la jeringa
  - [Parámetros de la jeringa] `Diametro_E = 31` — Diámetro del empujador de pulgar
  - [Parámetros de la jeringa] `Ancho = 45` — Parte ancha para el apoyo de los dedos
  - [Parámetros de la jeringa] `Estrecho = 30` — Parte estrecha para el apoyo de los dedos
  - [Parámetros de la jeringa] `Largo = 123` — Largo desde el apoyo de los dedos hasta el extremo del émbolo
  - [Parámetros de la jeringa] `Grosor = 2` — Grosor del apoyo para los dedos
- Impresión: Recomendamos que se imprima con al menos 4 perímetros y un 20% de relleno. Se puede imprimir en cualquier material que se desee (PLA y PETG son adecuados). La altura de capa recomendada para su impresión es de 0.2mm. En el cuerpo deberá utilizar soportes única y exclusivamente en la parte marcada en azul de la siguiente imagen.

## bandeja-de-coctel-para-copa

- Ficha: https://accessibilitas.es/2020/06/bandeja-de-coctel-para-copa/
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/bandeja-de-coctel-para-copa/Bandeja de coctel para copa.scad`, `extraidos/bandeja-de-coctel-para-copa/Bandeja de coctel para copa.stl`

## caja-apilable-y-tirador

- Ficha: https://accessibilitas.es/2022/12/caja-apilable-y-tirador/
- Intencionalidad: El diseño de esta caja y tirador tiene como objetivo que aquellas personas con dificultades de aprehensión puedan imprimirse cajas de almacenaje pequeñas diseñadas a medida de sus necesidades de almacenamiento y con un tirador que se adecue a sus capacidades y les permita acceder a poder abrirlas con comodidad. Se trata de cajas que se pueden apilar y sujetar entre ellas para formar conjuntos más grandes, e igualmente permite de una forma muy simple poder compartimentar su interior en varias partes. El pomo también se puede utilizar de forma independiente para abrir otro tipo de cajones que no sean necesariamente los que se haya impreso la persona. Para facilitar el “auto diseño” tanto de la
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/caja-apilable-y-tirador/Caja_gancho.scad`, `extraidos/caja-apilable-y-tirador/Pomo_aro.scad`
- Parámetros de `Caja_gancho.scad`:
  - [Dimensiones] `Ancho = 160` — Anchura de la caja (Exterior)
  - [Dimensiones] `Profundidad = 200` — Profundidad de la caja (Exterior)
  - [Dimensiones] `Alto = 70` — Altura de la caja (Total)
  - [Dimensiones] `N_Largo = 4` — Numero de particiones del cajon a lo largo
  - [Dimensiones] `N_Ancho = 2` — Numero de particiones del cajon a lo ancho
  - [Dimensiones] `Grue = 1.5` — Grosor de las paredes externas
  - [Dimensiones] `GrueC = 1` — Grosor de las paredes internas
  - [Elementos mostrados] `GuiIz = "NO"` [SI,NO] — Muestra las guias del lado izquierdo
  - [Elementos mostrados] `GuiDe = "NO"` [SI,NO] — Muestra las guias del lado derecho
  - [Elementos mostrados] `GuiSu = "NO"` [SI,NO] — Muestra las guias superiores
  - [Elementos mostrados] `GuiIn = "NO"` [SI,NO] — Muestra las guias inferiores
  - [Elementos mostrados] `Caja = "NO"` [SI,NO] — Muestra la caja de alojamiento
  - [Elementos mostrados] `CajonS = "SI"` [SI,NO] — Muestra el cajon
  - [Colores (a efectos de previsualizacion)] `color1 = "yellow"` [yellow:Amarillo, blue:Azul, red:Rojo, orange:Naranja, green:Verde, brown:Marrón, pink:Rosa, grey:Gris, violet:Violeta] — Color de las guias "hembra"
  - [Colores (a efectos de previsualizacion)] `color2 = "blue"` [yellow:Amarillo, blue:Azul, red:Rojo, orange:Naranja, green:Verde, brown:Marrón, pink:Rosa, grey:Gris, violet:Violeta] — Color de las guias "macho"
  - [Colores (a efectos de previsualizacion)] `color3 = "red"` [yellow:Amarillo, blue:Azul, red:Rojo, orange:Naranja, green:Verde, brown:Marrón, pink:Rosa, grey:Gris, violet:Violeta] — Color de la caja
  - [Colores (a efectos de previsualizacion)] `color4 = "orange"` [yellow:Amarillo, blue:Azul, red:Rojo, orange:Naranja, green:Verde, brown:Marrón, pink:Rosa, grey:Gris, violet:Violeta] — Color del cajon
- Parámetros de `Pomo_aro.scad`:
  - [Parámetros del tirador] `Grueso = 10` [8:1:15] — Grosor del tirador
  - [Parámetros del tirador] `Largo = 80` [50:1:120] — Hueco interior a lo largo
  - [Parámetros del tirador] `Anchura = 30` [8:1:45] — Hueco interior a lo ancho
  - [Parte a mostrar] `Mostrar = "Aro"` [Aro:Aro que vamos a asir con la mano, Anclaje:Pieza donde se sujeta el gancho] — Elemento que desea mostrar en pantalla para su renderización
- Impresión: Recomendamos que se imprima con al menos 3 perímetros y un 20% de relleno para asegurar su resistencia. Se puede imprimir en cualquier material que se desee. La altura de capa recomendada para su impresión es de 0.2mm. No es necesario el uso de soportes para su impresión.
- Instalación: Una vez que tengamos todas las piezas impresas y la tornillería necesaria, procederemos al montaje del pomo para poder abrir los cajones. En primer lugar insertaremos la tuerca M5 en su alojamiento tal y como se muestra en la siguiente imagen. A continuación roscaremos el gancho (con la rosca ya cortada) en la tuerca que hemos insertado, pero desde el otro lado. Y por último roscaremos la pieza del gancho en el aro utilizando los 2 tornillos M3x12. El roscado lo haremos directamente sobre el plástico. Ahora ya podremos utilizarlo para abrir nuestros cajones con más comodidad.

## carcasa-glucometro

- Ficha: https://accessibilitas.es/2021/05/carcasa-glucometro/
- Intencionalidad: El objetivo de este protector, como su propio nombre indica es proteger de daños frente a una caída o golpe, en la medida de lo posible, del sistema de control y medición capilar e intersticial de glucosa modelo InsuLinx de Abbot
- Parametrizable: no (solo STL)
- Archivos: `extraidos/carcasa-glucometro/Archivos/Protector_glucometro.stl`
- Impresión: El protector se puede imprimir prácticamente en cualquier material que se desee (PLA, ABS, PETG, ASA, etc.). La altura de capa recomendada para su impresión es de 0.1mm, ya que esto permitirá por un lado que los bordes redondeados queden más suavizados, y por otro lado se conseguirá una mejor impresión de las pequeñas pestañas que mantienen el glucómetro en su posición Para poder realizar la impresión correctamente, al realizar el laminado del protector deberá utilizar soportes en la zona que se ve en color morado en la siguiente imagen. Imagen 1: Vista con corte inferior para observar la zona de los soportes

## carcasa-macbook-air

- Ficha: https://accessibilitas.es/2019/06/carcasa-macbook-air/
- Intencionalidad: Independiza cada una de las teclas del ordenador dejándolas encerradas, así se podrá apoyar la mano sobre el teclado sin activar ninguna tecla, ayudando a evitar pulsaciones equivocadas o la activación de varias teclas a la vez. Facilita la actividad a aquellas personas que necesitan apoyo de la mano para mejorar la precisión de sus movimientos al teclear. Montaje de la carcasa
- Parametrizable: no (solo STL)
- Archivos: `extraidos/carcasa-macbook-air/Carcasa MacBook Air/Enganche MacBook Air velcro.stl`, `extraidos/carcasa-macbook-air/Carcasa MacBook Air/Teclado  Enganche MacBook Air.stl`
- Impresión: Las piezas se pueden imprimir con un filamento del tipo PLA, ya que se trata de una pieza que no necesita soportar grandes esfuerzos. La altura de capa recomendada es de entre 0.2mm y 0.1mm. y el relleno de la impresión un 20% con estructura cúbica. No es necesario el uso de soportes para su impresión.

## carcasa-para-macbook-pro

- Ficha: https://accessibilitas.es/2019/06/carcasa-para-macbook-pro/
- Intencionalidad: Independiza cada una de las teclas del ordenador dejándolas encerradas, así se podrá apoyar la mano sobre el teclado sin activar ninguna tecla, ayudando a evitar pulsaciones equivocadas o la activación de varias teclas a la vez. Facilita la actividad a aquellas personas que necesitan apoyo de la mano para mejorar la precisión de sus movimientos al teclear. “Colocación” de la carcasa
- Parametrizable: no (solo STL)
- Archivos: `extraidos/carcasa-para-macbook-pro/Carcasa para MacBook Pro/Enganche MacBook Pro velcro.stl`, `extraidos/carcasa-para-macbook-pro/Carcasa para MacBook Pro/Teclado Enganche MacBook Pro.stl`
- Impresión: Las piezas se pueden imprimir con un filamento del tipo PLA, ya que se trata de una pieza que no necesita soportar grandes esfuerzos. La altura de capa recomendada es de entre 0.2mm y 0.1mm. y el relleno de la impresión un 20% con estructura cúbica. No es necesario el uso de soportes para su impresión.

## cartel-braille

- Ficha: https://accessibilitas.es/2021/05/cartel-braille/
- Parametrizable: no (solo STL)
- Archivos: `extraidos/cartel-braille/Cartel_braille.scad`, `extraidos/cartel-braille/Ejemplo cartel/Bandeja_de_coctel_Braille.stl`, `extraidos/cartel-braille/Ejemplo cartel/Bandeja_de_coctel_base.stl`

## engrosador-de-chupachups

- Ficha: https://accessibilitas.es/2023/12/engrosador-de-chupachups/
- Intencionalidad: El diseño de esta pieza está pensado para facilitar el sujetar los palitos de algunos tipos de caramelo (piruletas, chupachups) cuando éstos resultan demasiado finos para la capacidad de agarre de la persona.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/engrosador-de-chupachups/Asidero_ChupaChups.stl`, `extraidos/engrosador-de-chupachups/Asidero_ChupaChups_2.stl`, `extraidos/engrosador-de-chupachups/ChupaChups.scad`
- Parámetros de `ChupaChups.scad`:
  - [Mostrar] `Mostrar = "1cono"` [2cono:Con cono en los 2 extremos, 1cono:Con cono en un solo extremo] — Elementos que desea mostrar
  - [Mostrar] `Forma = "1pieza"` [1pieza:En una sola pieza, 2pieza:Partido en 2 piezas] — ¿Cómo desea que se muestre?
  - [Parámetros] `Grosor = 25`
  - [Parámetros] `Altura = 120`
  - [Parámetros] `Alto_Cono = 15`
  - [Parámetros] `Grosor_Palo = 4.2`
- Impresión: Recomendamos que se imprima con al menos 2 perímetros y un 10% de relleno. Se puede imprimir en cualquier material que se desee. La altura de capa recomendada para su impresión es de 0.2mm. No es necesario el uso de soportes para la impresión del engrosador.

## joystick

- Ficha: https://accessibilitas.es/2022/11/joystick/
- Intencionalidad: Este diseño está pensado para poder fabricar de forma muy económica un joystick que conectado al ordenador, funcione como un ratón. Ideado para aquellas personas que por sus problemas motóricos no puedan utilizar un ratón estándar, pero sí sean capaces de manejar un joystick como por ejemplo los de las sillas de ruedas electrónicas. Igualmente puede ser funcional para personas con discapacidad intelectual o con alteraciones en la orientación espacial, ya que podríamos darle la orientación necesaria para facilitar la tarea y permite trabajar solamente con las 4 direcciones principales (también se podrían añadir las 4 diagonales). Para el montaje de este joystick, además de las piezas impresas
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/joystick/Joystick.scad`, `extraidos/joystick/JoystickMouse.ino`, `extraidos/joystick/threads.scad`
- Parámetros de `Joystick.scad`:
  - [Parte a mostrar] `Mostrar = "Alta"` [Cajon:Caja competa para hacerse una idea de cómo quedará, Alta:Carcasa Superior, Baja:Carcasa inferior, Contrapeso:Cajeado inferior para su uso como contrapeso, Tapa:Tapa del joystick, Barra:Palanca del joystick, Agarre:Pomo del joystick, Tope:Tope del muelle, Casq:Casquillo inferior del joystick, Patas:Pata para la carcasa, Pres:Presilla para la palanca del joystick, Tope_Arduino:Tope para evitar que se desplace el Arduino] — Elemento que desea mostrar en pantalla
  - [Parámetros de la caja] `Largo = 175` [80:1:250] — Largo de la caja
  - [Parámetros de la caja] `Ancho = 120` [80:1:250] — Ancho de la caja
  - [Parámetros de la caja] `Alto = 70` [50:1:100] — Alto de la caja
  - [Parámetros de la caja] `Alto_Peso = 15` [15:1:50] — Alto de la caja para el contrapeso
  - [Parámetros de la caja] `Angulo = 8` — Ángulo de inclinación en la parte superior
  - [Parámetros de la caja] `Grosor = 2.5` [2:0.5:3] — Grosor de las paredes de la caja (nunca puede ser igual o superior a la mitad del valor de "Curvado")
  - [Parámetros de la caja] `Curvado = 10` [7:1:14] — Diámetro de curvatura de las aristas verticales
  - [Parámetros de la caja] `Pulsacon = "Ambos"` [Pulsadores:Pulsadores, Conectores:Conectores, Ambos:Ambos] — ¿Desea pulsadores o conectores para pulsadores externos?
  - [Parámetros del joystick] `Largo_Palanca = 25` — Longitud de la palanca (sin contar el pomo)
  - [Parámetros del joystick] `Dia_Pomo = 40` [25:1:60] — Diámetro del pomo de agarre
  - [Parámetros del joystick] `DIM = 21.5` [20:0.5:25] — Diámetro interior del muelle
  - [Parámetros del joystick] `LMC = 11` — Longitud del muelle cuando está totalmente comprimido
  - [Parámetros del joystick] `LMR = 45` — Longitud del muelle cuando está en reposo
  - [Parámetros del joystick] `DX = 0` — Desplazamiento del joystick en el eje X con respecto al centro
  - [Parámetros del joystick] `DY = 0` — Desplazamiento del joystick en el eje Y con respecto al centro
  - [Parámetros de los pulsadores] `Diametro_P1 = 28` — Diámetro del pulsador 1
  - [Parámetros de los pulsadores] `Diametro_P2 = 24` — Diámetro del pulsador 2
  - [Parámetros de los pulsadores] `Diametro_P3 = 28` — Diámetro del pulsador 3
  - [Parámetros de los pulsadores] `Diametro_P4 = 28` — Diámetro del pulsador 4
  - [Parámetros de los pulsadores] `DXP1 = -32` — Distancia en el eje X (ancho) desde el centro de la caja del pulsador 1
  - [Parámetros de los pulsadores] `DYP1 = 60` — Distancia en el eje Y (largo) desde el centro de la caja del pulsador 1
  - [Parámetros de los pulsadores] `DXP2 = 32` — Distancia en el eje X (ancho) desde el centro de la caja del pulsador 2
  - [Parámetros de los pulsadores] `DYP2 = 60` — Distancia en el eje Y (largo) desde el centro de la caja del pulsador 2
  - [Parámetros de los pulsadores] `DXP3 = -32` — Distancia en el eje X (ancho) desde el centro de la caja del pulsador 3
  - [Parámetros de los pulsadores] `DYP3 = -60` — Distancia en el eje Y (largo) desde el centro de la caja del pulsador 3
  - [Parámetros de los pulsadores] `DXP4 = 32` — Distancia en el eje X (ancho) desde el centro de la caja del pulsador 4
  - [Parámetros de los pulsadores] `DYP4 = -60` — Distancia en el eje Y (largo) desde el centro de la caja del pulsador 4
  - [Parámetros los conectores] `Diametro_C = 6.1` — Diámetro del conector
  - [Parámetros los conectores] `DXC1 = 20` — Distancia en el eje X (ancho) desde el centro de la caja del conector 1
  - [Parámetros los conectores] `DZC1 = 30` — Distancia en el eje Z (alto) desde el borde superior de la caja del conector 1
  - [Parámetros los conectores] `DXC2 = 40` — Distancia en el eje X (ancho) desde el centro de la caja del conector 2
  - [Parámetros los conectores] `DZC2 = 30` — Distancia en el eje Z (alto) desde el borde superior de la caja del conector 2
  - [Parámetros los conectores] `DXC3 = -20` — Distancia en el eje X (ancho) desde el centro de la caja del conector 3
  - [Parámetros los conectores] `DZC3 = 30` — Distancia en el eje Z (alto) desde el borde superior de la caja del conector 3
  - [Parámetros los conectores] `DXC4 = -40` — Distancia en el eje X (ancho) desde el centro de la caja del conector 4
  - [Parámetros los conectores] `DZC4 = 30` — Distancia en el eje Z (alto) desde el borde superior de la caja del conector 4
  - [Parámetros los conectores] `CArduino = "Detras"` [Izquierda:Izquierda, Derecha:Derecha, Detras:Detrás] — ¿En qué lado de la caja desea que se encuentre el conector del Arduino
  - [Parámetros los conectores] `DZA = 35` — Distancia en el eje Z (alto) desde el borde superior de la caja al conector del Arduino
  - [Parámetros los conectores] `DYA = 0` — Distancia en el eje Y (largo) desde el centro de la caja al conector del Arduino (solo en el caso de vaya en un lateral)
  - [Parámetros los conectores] `DXA = 0` — Distancia en el eje X (ancho) desde el centro de la caja al conector del Arduino (solo en el caso de vaya detrás)
- Impresión: Recomendamos que se impriman las piezas en la misma posición que se generan en el archivo “.stl”, con al menos 3 perímetros y no menos del 15% de relleno para asegurar su resistencia (excepto las patas, que es recomendable imprimirlas sin relleno para que sean más flexibles y puedan tener una mayor adherencia a la mesa o superficie donde se coloque el joystick. Se puede imprimir en cualquier material que se desee. La altura de capa recomendada para su impresión es de 0.2mm, excepto para la palanca y el pomo del joystick que se recomienda una altura de capa de 0.15mm para que la rosca quede más definida. No es necesario el uso de soportes para su impresión excepto en las siguientes piezas: “Tapa del joystick”, “Palanca del joystick” y “Tope del muelle”. Sea cuidadoso al retirar los soportes de la “Tapa del joystick”, ya que podría llegar a partir alguno de los anclajes para los finales de
- Instalación: Una vez que tengamos impresas todas las piezas y retirados los soportes de aquellas que los tuviesen, procederemos al montaje del joystick. En primer lugar colocaremos la carcasa superior boca arriba y situaremos sobre el agujero del joystick el tope del muelle tal y como se ve en la siguiente imagen. A continuación situaremos el muelle sobre el tope. Colocaremos la tapa del joystick sobre el muelle haciendo que el cilindro sobresaliente encaje dentro del muelle. Venciendo la fuerza del muelle, presionamos la tapa del joystick contra la carcasa superior del joystick hasta que encaje en su siti

## joystick-con-carcasa

- Ficha: https://accessibilitas.es/2024/11/joystick-con-carcasa/
- Intencionalidad: Este diseño está pensado para poder fabricar de forma muy económica un joystick que conectado al ordenador, funcione como un ratón. Ideado para aquellas personas que por sus problemas motóricos no puedan utilizar un ratón estándar, pero sí sean capaces de manejar un joystick como por ejemplo los de las sillas de ruedas electrónicas. Igualmente puede ser funcional para personas con discapacidad intelectual o con alteraciones en la orientación espacial, ya que podríamos darle la orientación necesaria para facilitar la tarea y permite trabajar solamente con las 4 direcciones principales (también se podrían añadir las 4 diagonales). A este joystick también se le puede añadir una carcasa para que
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/joystick-con-carcasa/Carcasa.stl`, `extraidos/joystick-con-carcasa/Carcasa_inferior.stl`, `extraidos/joystick-con-carcasa/Carcasa_superior.stl`, `extraidos/joystick-con-carcasa/Casquillo_inferior.stl`, `extraidos/joystick-con-carcasa/JoystickMouse.ino`, `extraidos/joystick-con-carcasa/Joystick_carcasa.scad`, `extraidos/joystick-con-carcasa/Palanca_joystick.stl`, `extraidos/joystick-con-carcasa/Pomo.stl`, `extraidos/joystick-con-carcasa/Presilla.stl`, `extraidos/joystick-con-carcasa/Separador.stl`, `extraidos/joystick-con-carcasa/Tapa_joystick.stl`, `extraidos/joystick-con-carcasa/Tope_arduino.stl` …
- Parámetros de `Joystick_carcasa.scad`:
  - [Parte a mostrar] `Mostrar = "Alta"` [Cajon:Caja competa para hacerse una idea de cómo quedará, Alta:Carcasa Superior, Baja:Carcasa inferior, Contrapeso:Cajeado inferior para su uso como contrapeso, Carcasa:Carcasa para que los pulsadores queden hundidos, Separador:Separador para la carcasa, Tapa:Tapa del joystick, Barra:Palanca del joystick, Agarre:Pomo del joystick, Tope:Tope del muelle, Casq:Casquillo inferior del joystick, Patas:Pata para la carcasa, Pres:Presilla para la palanca del joystick, Tope_Arduino:Tope para evitar que se desplace el Arduino] — Elemento que desea mostrar en pantalla
  - [Parámetros de la caja] `Largo = 175` [80:1:250] — Largo de la caja
  - [Parámetros de la caja] `Ancho = 120` [80:1:250] — Ancho de la caja
  - [Parámetros de la caja] `Alto = 70` [50:1:100] — Alto de la caja
  - [Parámetros de la caja] `Alto_Peso = 15` [15:1:50] — Alto de la caja para el contrapeso
  - [Parámetros de la caja] `Angulo = 8` — Ángulo de inclinación en la parte superior
  - [Parámetros de la caja] `Grosor = 2.5` [2:0.5:3] — Grosor de las paredes de la caja (nunca puede ser igual o superior a la mitad del valor de "Curvado")
  - [Parámetros de la caja] `Curvado = 10` [7:1:14] — Diámetro de curvatura de las aristas verticales
  - [Parámetros de la caja] `Pulsacon = "Ambos"` [Pulsadores:Pulsadores, Conectores:Conectores, Ambos:Ambos] — ¿Desea pulsadores o conectores para pulsadores externos?
  - [Parámetros de la carcasa] `Protector = "NO"` [SI:Sí, NO:No] — ¿Desea una carcasa para que no sobresalgan los pulsadores?
  - [Parámetros de la carcasa] `Grosor_Carcasa = 6` [4:0.5:8] — Grosor de la carcasa
  - [Parámetros de la carcasa] `Distancia = 5` [3:0.5:10] — Distancia entre la carcasa y el joystick
  - [Parámetros del joystick] `Largo_Palanca = 25` — Longitud de la palanca (sin contar el pomo)
  - [Parámetros del joystick] `Dia_Pomo = 40` [25:1:60] — Diámetro del pomo de agarre
  - [Parámetros del joystick] `DIM = 21.5` [20:0.5:25] — Diámetro interior del muelle
  - [Parámetros del joystick] `LMC = 11` — Longitud del muelle cuando está totalmente comprimido
  - [Parámetros del joystick] `LMR = 45` — Longitud del muelle cuando está en reposo
  - [Parámetros del joystick] `DX = 0` — Desplazamiento del joystick en el eje X con respecto al centro
  - [Parámetros del joystick] `DY = 0` — Desplazamiento del joystick en el eje Y con respecto al centro
  - [Parámetros de los pulsadores] `Diametro_P1 = 28` — Diámetro del pulsador 1
  - [Parámetros de los pulsadores] `Diametro_P2 = 24` — Diámetro del pulsador 2
  - [Parámetros de los pulsadores] `Diametro_P3 = 28` — Diámetro del pulsador 3
  - [Parámetros de los pulsadores] `Diametro_P4 = 28` — Diámetro del pulsador 4
  - [Parámetros de los pulsadores] `DXP1 = -32` — Distancia en el eje X (ancho) desde el centro de la caja del pulsador 1
  - [Parámetros de los pulsadores] `DYP1 = 60` — Distancia en el eje Y (largo) desde el centro de la caja del pulsador 1
  - [Parámetros de los pulsadores] `DXP2 = 32` — Distancia en el eje X (ancho) desde el centro de la caja del pulsador 2
  - [Parámetros de los pulsadores] `DYP2 = 60` — Distancia en el eje Y (largo) desde el centro de la caja del pulsador 2
  - [Parámetros de los pulsadores] `DXP3 = -32` — Distancia en el eje X (ancho) desde el centro de la caja del pulsador 3
  - [Parámetros de los pulsadores] `DYP3 = -60` — Distancia en el eje Y (largo) desde el centro de la caja del pulsador 3
  - [Parámetros de los pulsadores] `DXP4 = 32` — Distancia en el eje X (ancho) desde el centro de la caja del pulsador 4
  - [Parámetros de los pulsadores] `DYP4 = -60` — Distancia en el eje Y (largo) desde el centro de la caja del pulsador 4
  - [Parámetros de los conectores] `Diametro_C = 6.1` — Diámetro del conector
  - [Parámetros de los conectores] `DXC1 = 20` — Distancia en el eje X (ancho) desde el centro de la caja del conector 1
  - [Parámetros de los conectores] `DZC1 = 30` — Distancia en el eje Z (alto) desde el borde superior de la caja del conector 1
  - [Parámetros de los conectores] `DXC2 = 40` — Distancia en el eje X (ancho) desde el centro de la caja del conector 2
  - [Parámetros de los conectores] `DZC2 = 30` — Distancia en el eje Z (alto) desde el borde superior de la caja del conector 2
  - [Parámetros de los conectores] `DXC3 = -20` — Distancia en el eje X (ancho) desde el centro de la caja del conector 3
  - [Parámetros de los conectores] `DZC3 = 30` — Distancia en el eje Z (alto) desde el borde superior de la caja del conector 3
  - [Parámetros de los conectores] `DXC4 = -40` — Distancia en el eje X (ancho) desde el centro de la caja del conector 4
  - [Parámetros de los conectores] `DZC4 = 30` — Distancia en el eje Z (alto) desde el borde superior de la caja del conector 4
  - [Parámetros de los conectores] `CArduino = "Detras"` [Izquierda:Izquierda, Derecha:Derecha, Detras:Detrás] — ¿En qué lado de la caja desea que se encuentre el conector del Arduino
  - [Parámetros de los conectores] `DZA = 35` — Distancia en el eje Z (alto) desde el borde superior de la caja al conector del Arduino
  - [Parámetros de los conectores] `DYA = 0` — Distancia en el eje Y (largo) desde el centro de la caja al conector del Arduino (solo en el caso de vaya en un lateral)
  - [Parámetros de los conectores] `DXA = 0` — Distancia en el eje X (ancho) desde el centro de la caja al conector del Arduino (solo en el caso de vaya detrás)
- Impresión: Recomendamos que se impriman las piezas en la misma posición que se generan en el archivo “.stl”, con al menos 3 perímetros y no menos del 15% de relleno para asegurar su resistencia (excepto las patas, que es recomendable imprimirlas sin relleno para que sean más flexibles y puedan tener una mayor adherencia a la mesa o superficie donde se coloque el joystick). Se puede imprimir en cualquier material que se desee, y las patas en material flexible. La altura de capa recomendada para su impresión es de 0.2mm, excepto para la palanca y el pomo del joystick que se recomienda una altura de capa de 0.15mm para que la rosca quede más definida. No es necesario el uso de soportes para su impresión excepto en las siguientes piezas: “Tapa del joystick”, “Palanca del joystick” y “Tope del muelle”. Sea cuidadoso al retirar los soportes de la “Tapa del joystick”, ya que podría llegar a partir alguno 
- Instalación: Una vez que tengamos impresas todas las piezas y retirados los soportes de aquellas que los tuviesen, procederemos al montaje del joystick. En primer lugar colocaremos la carcasa superior boca arriba e introduciremos las cuatro tuercas M3 en sus correspondientes alojamientos. Tenga en cuenta que las tuercas entran a presión, por lo que es recomendable ayudarse con un tornillo desde el otro lado para poder tirar de las tuercas hasta que se encajen completamente. A continuación, con la carcasa superior boca arriba situaremos sobre el agujero del joystick el tope del muelle tal y como se ve en la

## mando-para-adaptive-controller

- Ficha: https://accessibilitas.es/2023/11/mando-para-adaptive-controller/
- Intencionalidad: Este diseño está pensado para poder fabricar de forma muy económica un mando que, conectado al Adaptive Controller de Microsoft, permita realizar las funciones del joystick izquierdo o derecho, así como las funciones de los botones “A” y “B” o “X” e “Y” de la consola de juegos XBox. Puede ser útil para algunas personas que no pueden manejar un mando estándar con movilidad reducida en miembros superiores, pero que sin embrago, sí que pueda controlar un mando con una sola mano. Para el montaje de este joystick, además de las piezas impresas se necesitan algunos componentes adicionales que se especifican en la sección 2 “Material y “habilidades” adicionales”.
- Parametrizable: no (solo STL)
- Archivos: `extraidos/mando-para-adaptive-controller/Boton.stl`, `extraidos/mando-para-adaptive-controller/Cierre_Arduino.stl`, `extraidos/mando-para-adaptive-controller/JoystickGamer_v2.ino`, `extraidos/mando-para-adaptive-controller/Nunchuck_inferior.stl`, `extraidos/mando-para-adaptive-controller/Nunchuck_superior.stl`
- Impresión: Recomendamos que se impriman las piezas en la misma posición que se encuentran en el archivo “.stl”, con al menos 3 perímetros. Se puede imprimir en cualquier material que se desee. La altura de capa recomendada para su impresión es de 0.2mm o inferior. Es necesario el uso de soportes para la impresión de todas las piezas, excepto en el “Boton”.
- Instalación: Una vez que tengamos impresas todas las piezas y retirados los soportes de aquellas que los tuviesen, procederemos al montaje del joystick. En primer lugar, debemos cortar 2 de las patillas del micro pulsador, dejando solamente las otras 2, y lo colocaremos en la carcasa inferior en el alojamiento hecho a tal efecto en la parte delantera con las 2 patillas que nos quedan mirando hacia arriba. Deberemos también abrir ligeramente las patillas para que dejen libre el pilar de alojamiento del tornillo tal y como se ve en la imagen. A continuación atornillaremos el módulo de joystick con los 4 torn

## mango-para-cubierto

- Ficha: https://accessibilitas.es/2021/05/mango-para-cubierto/
- Intencionalidad: El objetivo de este soporte es poder fijar a él cualquier tipo de cubierto, e incluso otro tipo de utensilios y que quede sujeto a la mano para aquellas personas que por sus dificultades motoras no puedan realizar una prensión con su mano o simplemente no pueden asir correctamente un cubierto. Está formado por un “cubo” hueco en el que se introduce el cubierto que se fija mediante un tornillo de palomilla para que no se mueva, y por una pieza que flexa que es la que permite su fijación a la mano.
- Parametrizable: no (solo STL)
- Archivos: `extraidos/mango-para-cubierto/Archivos/Palomilla_M5.stl`, `extraidos/mango-para-cubierto/Archivos/Soporte_cubierto.stl`
- Impresión: Tanto el soporte como la palomilla se pueden imprimir prácticamente en cualquier material que se desee (PLA, ABS, PETG, ASA, etc.). La altura de capa recomendada para su impresión es de 0.1-0.2mm, si bien es recomendable en el caso de laminar con una altura de capa de 0.2mm utilizar una altura de capa inferior (0.05-0.1mm) tanto al inicio como al final de la impresión para suavizar los bordes tanto como sea posible siempre que nuestro laminador nos lo permita (tanto en el soporte como en la palomilla). Utilizar 3 líneas de perímetro y un relleno del 10% que será más que suficiente puesto que no es un elemento que tenga que soportar grandes esfuerzos y a cambio nos ahorrará peso, salvo que busquemos precisamente el efecto contrario (lastrado), en cuyo caso se podría rellenar al 100%. No es necesario el uso de soportes para su impresión. Una vez impresa la palomilla, deberemos introducir e

## palanca-para-llave-de-paso-de-cisterna

- Ficha: https://accessibilitas.es/2020/03/palanca-para-llave-de-paso-de-cisterna/
- Intencionalidad: El objetivo de esta palanca es permitir a las personas que tienen limitada la destreza, movilidad o fuerza en las manos poder abrir y cerrar llaves de paso del agua de la cisterna del váter en caso de un mal funcionamiento de la misma. El mismo diseño se podría utilizar para otro tipo de llaves de paso del agua con una forma similar. Para mayor facilidad de uso, se le ha añadido la posibilidad de incorporarle dos hendiduras para facilitar el agarre o para utilizarla con un solo dedo de la mano.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/palanca-para-llave-de-paso-de-cisterna/Palanca-llave-paso-cisterna/palanca_llave_paso_cisterna.scad`, `extraidos/palanca-para-llave-de-paso-de-cisterna/Palanca-llave-paso-cisterna/palanca_llave_paso_cisterna_1.stl`, `extraidos/palanca-para-llave-de-paso-de-cisterna/Palanca-llave-paso-cisterna/palanca_llave_paso_cisterna_2.stl`
- Parámetros de `palanca_llave_paso_cisterna.scad`:
  - [Hole / Agujero] `HoleHeight = 28.8` — Hole height / Altura del agujero
  - [Hole / Agujero] `HoleThinWidth = 9` — Hole Upper Width / Anchura superior del agujero
  - [Hole / Agujero] `HoleThickWidth = 18.15` — Hole Central Width / Anchura central del agujero
  - [Handle / Mango] `HandleZ = 14` — Handle Thickness / Grosor del mango
  - [Handle / Mango] `HandleTopLengthFromHole = 60` — Length from hole top to handle top / Largo desde la parte superior del agujero hasta la parte superior del mango
  - [Handle / Mango] `HandleBottomLengthFromHole = 7` — Length from hole bottom to handle bottom / Largo desde la parte inferior del agujero hasta la parte inferior del mango
  - [Handle / Mango] `HandleSidesFromHole = 7` — Handle Sides Thickness / Grosor de los laterales del mango
  - [Handle / Mango] `HandleTotalLength = HoleHeight+HandleTopLengthFromHole+HandleBottomLengthFromHole`
  - [Handle / Mango] `Fillet = 2` — Rounded Edges / Cantos redondeados
  - [Slits / Hendiduras] `WithSlits = "Yes"` [Yes:Yes / Sí, No:No / No] — Do you want the lever to have slits? / ¿Quieres que la palanca tenga hendiduras?
  - [Slits / Hendiduras] `SlitWidth = 15` — Slit Width / Anchura de la hendidura
  - [Slits / Hendiduras] `SlitHeight = SlitWidth` — Slit depth / Profundidad de la hendidura
  - [Slits / Hendiduras] `SlitDistance = 7` — Distance from top of the handle / Distancia de la hendidura a la parte superior del mango
  - [Slits / Hendiduras] `Aux = ((HandleTotalLength)/2)-(HoleHeight/2)-HandleBottomLengthFromHole` — Rectangle shape with fillet
- Impresión: La palanca se puede imprimir con un filamento del tipo PLA. La altura de capa recomendada para su impresión es de 0.1-0.15mm y el relleno entre 15-20%. Es recomendable el uso de soporte para que el redondeado de los bordes de la cara de la palanca en contacto con la base de impresión quede bien definido. Una vez impresa la palanca, si al colocarla en la llave de paso el agujero es algo más ancho y la pieza baila, se puede pegar un trozo fino de cinta de doble en el lateral interior del agujero de la pieza para que quede sujeta a la llave de paso.

## parlanchinator

- Ficha: https://accessibilitas.es/2026/01/parlanchinator/
- Intencionalidad: Este diseño está pensado para utilizarse junto con los pictogramas 3D que llevan un tag en su interior, y así dar una salida de voz a los pictogramas actuando a modo de “comunicador” para personas con parálisis cerebral con gran afectación a nivel cognitivo y que además tienen una discapacidad visual muy severa o ceguera total. De esta forma las personas podrán disponer de una herramienta básica adicional a los pictogramas para mejorar su comunicación, ya que en la actualidad no existen herramientas para trabajar con ellas. Para el montaje del Parlanchín-ator, además de las piezas impresas se necesitan algunos componentes adicionales que se especifican en la sección 2 “Material y “habilidade
- Parametrizable: no (solo STL)
- Archivos: `extraidos/parlanchinator/Parlanchinator/Parlanchinator_base.stl`, `extraidos/parlanchinator/Parlanchinator/Parlanchinator_cartel.stl`, `extraidos/parlanchinator/Parlanchinator/Parlanchinator_pata.stl`, `extraidos/parlanchinator/Parlanchinator/Parlanchinator_tapa.stl`, `extraidos/parlanchinator/Parlanchinator/Parlanchinator_tapa_bateria.stl`, `extraidos/parlanchinator/Parlanchinator/Programador-parlanchinator.ino`, `extraidos/parlanchinator/Parlanchinator/Reproductor-parlanchinator.ino`
- Impresión: Recomendamos que se impriman las piezas en la misma posición en que están los archivos “.stl”, con al menos 2 perímetros y un 15% de relleno. Se puede imprimir en cualquier material que se desee. La altura de capa recomendada para su impresión es de 0.2mm. Será necesario el uso de soportes para su impresión en las siguientes piezas: “Parlanchinator_base”, “Parlanchinator_tapa” y “Parlanchinator_tapa_bateria”. En esta última se recomienda utilizar también 3 o 4 mm de balsa para evitar posibles desprendimientos de la base durante su impresión Sea cuidadoso al retirar los soportes de la “Tapa de la batería”, ya que podría llegar a partir alguna de las pestañas. En el caso del “cartel”, si desea que tenga las letras en otro color deberá introducir en su laminador un “cambio de color” a la altura de 1.2 mm.
- Instalación: Una vez que tengamos impresas todas las piezas y retirados los soportes de aquellas que los tuviesen, procederemos al montaje del Parlanchín-ator. En primer lugar, es muy importante, antes de empezar a hacer nada, que ajustemos el regulador de tensión a 5V exactamente mediante la resistencia variable que lleva integrada (marcada en un círculo rojo en la imagen), y para ello deberemos utilizar un polímetro o medidor de tensión. Este paso es fundamental, ya que si no podríamos dañar todos los componentes electrónicos del dispositivo. Una vez ajustada la tensión del regulador, soldaremos los cabe

## pastillero

- Ficha: https://accessibilitas.es/2019/06/pastillero/
- Intencionalidad: Este pastillero está pensado para que se puedan transportar con comodidad los medicamentos que la persona deba tomar durante el día. El pequeño cortador integrado facilitará el corte de pastillas. Montaje del pastillero
- Parametrizable: no (solo STL)
- Archivos: `extraidos/pastillero/Pastillero/Pastillero F. ONCE base.stl`, `extraidos/pastillero/Pastillero/Pastillero F. ONCE tapadera.stl`
- Impresión: Las piezas se deben imprimir con un filamento del tipo PETG, ya que este tipo de filamento está aprobado para su uso en la industria alimentaria (no debemos olvidar que las pastillas estarán en contacto con el plástico y posteriormente se ingerirán). La altura de capa recomendada es de entre 0.2mm y 0.1mm. y el relleno de la impresión un 20% con estructura cúbica. No es necesario el uso de soportes para su impresión. Nota: Si desea imprimir el pastillero en dos colores (tal y como se ve en las imágenes) y no dispone de una impresora con doble extrusor o un sistema de impresión para varios filamentos recuerde que cuando llegue a la capa correspondiente deberá cambiar el filamento en su impresora.

## pastillero-varias-tomas

- Ficha: https://accessibilitas.es/2021/05/pastillero-varias-tomas/
- Intencionalidad: Este diseño está pensado para poder facilitar la organización de las pastillas que una persona se debe tomar a lo largo del día en las diferentes tomas que debe hacer.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/pastillero-varias-tomas/Archivos/Pastillero_4_tomas.stl`, `extraidos/pastillero-varias-tomas/Archivos/Pastillero_caja_4_tomas.stl`, `extraidos/pastillero-varias-tomas/Archivos/Pastillero_tapa_4_tomas.stl`, `extraidos/pastillero-varias-tomas/Archivos/Pastillero_varias_tomas.scad`
- Parámetros de `Pastillero_varias_tomas.scad`:
  - [Medidas] `Largo = 110` — Longitud total del pastillero
  - [Medidas] `Ancho = 45` — Anchura total del pastillero
  - [Medidas] `Alto = 20` — Altura total del pastillero
  - [Medidas] `Divisiones = 4` [1:1:7] — Número de huecos que se desean en el pastillero
  - [Medidas] `Grosor_Paredes = 2` [1:0.5:3] — Grosor de las paredes externas del pastillero
  - [Medidas] `Grosor_Divisiones = 1` [1:0.5:2] — Grosor de las paredes divisoras del pastillero
  - [Medidas] `Grosor_Tapa = 2` [1.5:0.5:3] — Grosor de la tapa del pastillero
  - [Medidas] `Suavizado = 40` [20:4:120] — Suavizado de las partes curvas (afecta al tiempo de renderización)
  - [Medidas] `Holgura = 0.2` [0.1:0.1:0.5] — Holgura entre la tapa y la caja del pastillero
  - [Mostrar] `Mostrar = "Todo"` [Todo:Todos los elementos, Caja:Caja del pastillero, Tapa:Tapa del pastillero] — Elementos que desea mostrar
- Impresión: El pastillero recomendamos que se imprima en PETG, ya que con él va a estar en contacto un producto (pastilla) que después vamos a ingerir. La altura de capa recomendada para su impresión es de 0.1-0.2mm para la caja y de 0.1 para la tapa y el relleno de un 10%, ya que nos interesa que sea lo más ligero posible. No es necesario el uso de soportes para su impresión.

## pictogramas-3d

- Ficha: https://accessibilitas.es/2026/01/pictogramas-3d/
- Intencionalidad: El diseño de estos pictogramas está pensado para personas con parálisis cerebral con gran afectación a nivel cognitivo y que además tienen una discapacidad visual muy severa o ceguera total. Se ha tratado es crear una serie de pictogramas basados en objetos reales para necesidades muy básicas que puedan ser distinguibles al tacto para que así, puedan disponer de una herramienta básica para la comunicación.
- Parametrizable: no (solo STL)
- Archivos: `extraidos/pictogramas-3d/Pictogramas_3D/Picto_con_tag_ayuda.stl`, `extraidos/pictogramas-3d/Pictogramas_3D/Picto_con_tag_bano.stl`, `extraidos/pictogramas-3d/Pictogramas_3D/Picto_con_tag_beber.stl`, `extraidos/pictogramas-3d/Pictogramas_3D/Picto_con_tag_comer.stl`, `extraidos/pictogramas-3d/Pictogramas_3D/Picto_con_tag_cuento.stl`, `extraidos/pictogramas-3d/Pictogramas_3D/Picto_con_tag_musica.stl`, `extraidos/pictogramas-3d/Pictogramas_3D/Picto_con_tag_no.stl`, `extraidos/pictogramas-3d/Pictogramas_3D/Picto_con_tag_peluche.stl`, `extraidos/pictogramas-3d/Pictogramas_3D/Picto_con_tag_pompas.stl`, `extraidos/pictogramas-3d/Pictogramas_3D/Picto_con_tag_si.stl`, `extraidos/pictogramas-3d/Pictogramas_3D/Picto_sin_tag_ayuda.stl`, `extraidos/pictogramas-3d/Pictogramas_3D/Picto_sin_tag_bano.stl` …
- Impresión: Recomendamos que se imprima en la misma posición que se encuentran los archivos, con 2-3 perímetros y un 10-15% de relleno. Se puede imprimir en cualquier material que se desee, aunque se recomienda PLA excepto para el pictograma de “peluche”, que la base ha de ser igual que en el resto (PLA), pero la figura del osito se debería imprimir en un TPU lo más blando posible (SHORE 50-70A) con 2 perímetros y con muy poco relleno (5%). En todos los pictogramas, lo ideal sería que en su laminador introdujese un cambio de color a 8.20mm de altura para poder cambiar de filamento y que el pictograma destaque sobre el fondo para ayudar a aquellas personas que sí tengan un resto visual, tal y como se puede observar en las imágenes. En los pictogramas con tag, además deberá introducir en su laminador una pausa de impresión en la capa correspondiente a 6.20mm de altura para que le permita colocar el ta

## pomo-de-bola

- Ficha: https://accessibilitas.es/2025/12/pomo-de-bola/
- Intencionalidad: El diseño de esta pieza está pensado para poder encajarse a presión en el eje del joystick de una silla de ruedas electrónica. Se trata de un pomo esférico en forma de bola que se puede hacer liso o con “hendiduras” para un mejor agarre.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/pomo-de-bola/Pomo_bola/Casquillo_6mm.stl`, `extraidos/pomo-de-bola/Pomo_bola/Pomo_bola.scad`, `extraidos/pomo-de-bola/Pomo_bola/Pomo_bola_liso_40.stl`, `extraidos/pomo-de-bola/Pomo_bola/Pomo_bola_perforado_50.stl`
- Parámetros de `Pomo_bola.scad`:
  - [Parte a mostrar] `Mostrar = "Pomo"` [Pomo:Pomo, Casquillo:Casquillo] — Elemento que desea mostrar en pantalla
  - [Parámetros del pomo] `Diametro = 50` — Diámetro del pomo
  - [Parámetros del pomo] `Eje = 6` — Diámetro de del eje del joystick de la silla de ruedas
  - [Parámetros del pomo] `Superficie = "Lisa"` [Lisa, Perforada] — Superficie lisa o perforada
  - [Parámetros del pomo] `Agujero = 4` [2:6] — Diámetro de los agujeros (si la superficie es perforada)
  - [Parámetros del pomo] `Prof_Agujero = 0.2` [0.1:0.1:1] — Profundidad del agujero (si la superficie es perforada)
  - [Parámetros del pomo] `Bocado = 10` — ¿Cuánto desea recortar a la bola por la parte inferior? (Elija 0 para una esfera completa)
- Impresión: Recomendamos que se imprima en la misma posición que se genera el archivo, con al menos 3 perímetros y un 10-20% de relleno. Se puede imprimir en cualquier material que se desee, pero el casquillo se debe imprimir en un material flexible como el TPU para que el encaje a presión sea correcto. La altura de capa recomendada para su impresión es de 0.2mm No es necesario el uso de soportes para la impresión del pomo.
- Instalación: Una vez impreso el pomo, solamente deberá encajar el casquillo en el hueco del pomo. El casquillo entrará muy justo, pero al ser flexible el material del casquillo, entrará haciendo presión sobre él. Una vez encajado el casquillo, ya solo deberá retirar el pomo de su silla de ruedas y encajar a presión el nuevo pomo.

## pomo-de-palanca

- Ficha: https://accessibilitas.es/2023/11/pomo-de-palanca/
- Intencionalidad: El diseño de esta pieza está pensado para poder roscarse en la palanca del emulador de ratón por joystick que se encuentra igualmente disponible en la página web de accessibilitas.es. Se trata de un pomo recto con su parte superior redondeada.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/pomo-de-palanca/Pomo_palanca.scad`, `extraidos/pomo-de-palanca/Pomo_palanca_50x25x18.stl`
- Parámetros de `Pomo_palanca.scad`:
  - [Parámetros] `Alto = 50` — Altura del pomo
  - [Parámetros] `Diametro1 = 25` — Diámetro del pomo en la parte de arriba
  - [Parámetros] `Diametro2 = 18` [18:1:30] — Diámetro del pomo en la parte de abajo
- Impresión: Recomendamos que se imprima con al menos 3 perímetros y un 20% de relleno. Se puede imprimir en cualquier material que se desee. La altura de capa recomendada para su impresión es de 0.2mm o menos para asegurar que la rosca se imprima correctamente. No es necesario el uso de soportes para la impresión del pomo.
- Instalación: Una vez impreso el pomo, solamente deberá roscarlo a la palanca del joystick. Si lo considera necesario, para asegurarse de que no se desenroscará de la palanca, puede echar un par de gotas de adhesivo (Cianocrilato preferentemente) a la rosca cuando lo vaya a roscar.

## pomo-en-t

- Ficha: https://accessibilitas.es/2023/11/pomo-en-t/
- Intencionalidad: El diseño de esta pieza está pensado para poder roscarse en la palanca del emulador de ratón por joystick que se encuentra igualmente disponible en la página web de accessibilitas.es. En realidad se trata de un pomo horizontal recto, pero que junto con la palanca del joystick conformará un pomo en forma de “T”.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/pomo-en-t/Pomo_T_Joystick.scad`, `extraidos/pomo-en-t/Pomo_T_Joystick_100x25.stl`
- Parámetros de `Pomo_T_Joystick.scad`:
  - [Parámetros] `Largo = 100` — Longitud total del pomo
  - [Parámetros] `Diametro = 25` [25:1:50] — Diámetro del pomo
- Impresión: Recomendamos que se imprima con al menos 3 perímetros y un 10-20% de relleno. Se puede imprimir en cualquier material que se desee. La altura de capa recomendada para su impresión es de 0.2mm o menos para asegurar que la rosca se imprima correctamente. No es necesario el uso de soportes para la impresión del pomo.
- Instalación: Una vez impreso el pomo, solamente deberá roscarlo a la palanca del joystick. Si lo considera necesario, para asegurarse de que no se desenroscará de la palanca, puede echar un par de gotas de adhesivo (Cianocrilato preferentemente) a la rosca cuando lo vaya a roscar.

## pomo-en-t-para-silla-de-ruedas

- Ficha: https://accessibilitas.es/2024/11/pomo-en-t-para-silla-de-ruedas/
- Intencionalidad: El diseño de esta pieza está pensado para poder encajarse a presión en el eje del joystick de una silla de ruedas electrónicas. Se trata de un pomo en forma de “T” con el apoyo para la mano redondeado.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/pomo-en-t-para-silla-de-ruedas/Casquillo_6mm.stl`, `extraidos/pomo-en-t-para-silla-de-ruedas/Pomo_T.scad`, `extraidos/pomo-en-t-para-silla-de-ruedas/Pomo_T_100x25x30.stl`
- Parámetros de `Pomo_T.scad`:
  - [Parte a mostrar] `Mostrar = "Pomo"` [Pomo:Pomo, Casquillo:Casquillo] — Elemento que desea mostrar en pantalla
  - [Parámetros del pomo] `Ancho = 100` — Anchura del pomo
  - [Parámetros del pomo] `Diametro = 25` — Diámetro del pomo
  - [Parámetros del pomo] `Altura = 30` — Altura del encaje del pomo
  - [Parámetros del pomo] `Joystick = 6` — Diámetro del eje del joystick de la silla
- Impresión: Recomendamos que se imprima en la misma posición que se genera el archivo, con al menos 3 perímetros y un 10-20% de relleno. Se puede imprimir en cualquier material que se desee, pero el casquillo se debe imprimir en un material flexible como el TPU para que el encaje a presión sea correcto. La altura de capa recomendada para su impresión es de 0.2mm Necesitará el uso de soportes para la impresión del pomo. No es necesario el uso de soportes para el casquillo.
- Instalación: Una vez impreso el pomo, solamente deberá encajar el casquillo en el hueco del pomo. El casquillo entrará muy justo, pero al ser flexible el material del casquillo, entrará haciendo presión sobre él. Una vez encajado el casquillo, ya solo deberá retirar el pomo de su silla de ruedas y encajar a presión el nuevo pomo.

## pomo-en-u

- Ficha: https://accessibilitas.es/2020/03/pomo-en-u/
- Intencionalidad: Este diseño está pensado para que aquellas personas que necesitan que el pomo del joystick de su silla de ruedas proporcione un soporte lateral adicional a su mano. Por ejemplo, para personas que no pueden realizar una prensión eficaz de un pomo estándar. Ayuda a evitar que la mano caiga perdiendo la posición funcional de la misma
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/pomo-en-u/Pomo_joystick_en_U.scad`, `extraidos/pomo-en-u/Pomo_joystick_en_U.stl`
- Parámetros de `Pomo_joystick_en_U.scad`:
  - [Pomo] `Largo = 60` [20:1:110] — Longitud del pomo
  - [Pomo] `Ancho = 20` [14:1:70] — Anchura del pomo
  - [Pomo] `Alto = 35` [30:1:80] — Altura del pomo (sin el encaje para la silla)
  - [Pomo] `Grosor = 4` [2:0.5:8] — Grosor de las paredes del pomo
  - [Encaje para el joystick de la silla] `Alto_Encaje = 20` [10:1:80] — Altura del encaje para la silla
  - [Encaje para el joystick de la silla] `Dia_Ext = 10` [8:0.5:12] — Diámetro exterior del encaje para la silla
  - [Encaje para el joystick de la silla] `Dia_Int = 6` [4:0.5:8] — Diámetro interior del encaje para la silla
  - [Desplazamiento del pomo sobre el encaje] `Desp_Pomo = 0` [-40:1:40] — Milímetros que desea desplazar el pomo con respecto al centro del encaje
- Impresión: El pomo se puede imprimir con un filamento del tipo PLA, PETG o ASA, teniendo estos dos últimos mejores propiedades mecánicas que el PLA, por lo que son más resistentes. Si el usuario pasa muchas horas con su silla de ruedas en la calle el filamento más recomendable es el ASA por sus mejores propiedades térmicas y resistencia a los rayos UV. La altura de capa recomendada para su impresión es de 0.1-0.2mm y el relleno entre 10-20%. Se debe imprimir “tumbado” y para ello es necesario el uso de soportes para su correcta impresión, especialmente en el encaje. Una vez impreso el pomo no es necesario realizar ningún trabajo de post procesado a excepción de la retirada de los soportes. Para colocarlo en el joystick de su silla de ruedas simplemente encájelo a presión.

## pomo-en-u-2

- Ficha: https://accessibilitas.es/2023/11/pomo-en-u-2/
- Intencionalidad: El diseño de esta pieza está pensado para poder roscarse en la palanca del emulador de ratón por joystick que se encuentra igualmente disponible en la página web de accessibilitas.es. Se trata de un pomo en forma de “U” con el apoyo para la mano redondeado.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/pomo-en-u-2/Pomo_U_Joystick.scad`, `extraidos/pomo-en-u-2/Pomo_U_Joystick_100x30x4x30.stl`
- Parámetros de `Pomo_U_Joystick.scad`:
  - [Parámetros] `Largo = 100` — Longitud total del pomo
  - [Parámetros] `Diametro = 30` [22:1:50] — Diámetro del pomo
  - [Parámetros] `Grosor = 4` [3:1:6] — Grosor de las paredes del pomo
  - [Parámetros] `Lateral = 30` — Altura de los salientes laterales
- Impresión: Recomendamos que se imprima con al menos 3 perímetros y un 10-20% de relleno. Se puede imprimir en cualquier material que se desee. La altura de capa recomendada para su impresión es de 0.2mm o menos para asegurar que la rosca se imprima correctamente. No es necesario el uso de soportes para la impresión del pomo.
- Instalación: Una vez impreso el pomo, solamente deberá roscarlo a la palanca del joystick. Si lo considera necesario, para asegurarse de que no se desenroscará de la palanca, puede echar un par de gotas de adhesivo (Cianocrilato preferentemente) a la rosca cuando lo vaya a roscar.

## pomo-en-u-para-silla-de-ruedas

- Ficha: https://accessibilitas.es/2024/11/pomo-en-u-para-silla-de-ruedas/
- Intencionalidad: El diseño de esta pieza está pensado para poder encajarse a presión en el eje del joystick de una silla de ruedas electrónicas. Se trata de un pomo en forma de “U” con el apoyo para la mano redondeado.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/pomo-en-u-para-silla-de-ruedas/Casquillo_6mm.stl`, `extraidos/pomo-en-u-para-silla-de-ruedas/Pomo_U.scad`, `extraidos/pomo-en-u-para-silla-de-ruedas/Pomo_U_100x30x35.stl`
- Parámetros de `Pomo_U.scad`:
  - [Parte a mostrar] `Mostrar = "Pomo"` [Pomo:Pomo, Casquillo:Casquillo] — Elemento que desea mostrar en pantalla
  - [Parámetros del pomo] `Largo = 100` — Longitud total del pomo
  - [Parámetros del pomo] `Diametro = 30` — Diámetro del pomo
  - [Parámetros del pomo] `Grosor = 4` [3:1:6] — Grosor de las paredes del pomo
  - [Parámetros del pomo] `Lateral = 20` — Altura de los salientes laterales
  - [Parámetros del pomo] `Eje = 6` [5:1:6] — Diámetro del eje del joystick de la silla de ruedas
- Impresión: Recomendamos que se imprima en la misma posición que se genera el archivo, con al menos 3 perímetros y un 10-20% de relleno. Se puede imprimir en cualquier material que se desee, pero el casquillo se debe imprimir en un material flexible como el TPU para que el encaje a presión sea correcto. La altura de capa recomendada para su impresión es de 0.2mm No es necesario el uso de soportes para la impresión del pomo.
- Instalación: Una vez impreso el pomo, solamente deberá encajar el casquillo en el hueco del pomo. El casquillo entrará muy justo, pero al ser flexible el material del casquillo, entrará haciendo presión sobre él. Una vez encajado el casquillo, ya solo deberá retirar el pomo de su silla de ruedas y encajar a presión el nuevo pomo.

## pomo-silla-de-montar

- Ficha: https://accessibilitas.es/2020/03/pomo-silla-de-montar/
- Intencionalidad: Este pomo está pensado para ser utilizado por personas que manejan su silla de ruedas eléctrica con un mando de mentón. Permite que la barbilla quede mejor alojada, de manera que sea más difícil que se descoloque mientras se está manejando la silla.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/pomo-silla-de-montar/Pomo_joystick_silla_de_montar.scad`, `extraidos/pomo-silla-de-montar/Pomo_joystick_silla_de_montar.stl`
- Parámetros de `Pomo_joystick_silla_de_montar.scad`:
  - [Pomo] `Ancho = 50` [45:1:55] — Anchura del pomo
  - [Pomo] `Alto = 45` [30:1:80] — Altura del pomo (sin el encaje para la silla)
  - [Encaje para el joystick de la silla] `Alto_Encaje = 20` [10:1:80] — Altura del encaje para la silla
  - [Encaje para el joystick de la silla] `Dia_Ext = 12` [8:0.5:15] — Diámetro exterior del encaje para la silla
  - [Encaje para el joystick de la silla] `Dia_Int = 6` [4:0.5:8] — Diámetro interior del encaje para la silla
- Impresión: El pomo se puede imprimir con un filamento del tipo PLA, PETG o ASA, teniendo estos dos últimos mejores propiedades mecánicas que el PLA, por lo que son más resistentes. Si el usuario pasa muchas horas con su silla de ruedas en la calle el filamento más recomendable es el ASA por sus mejores propiedades térmicas y resistencia a los rayos UV. La altura de capa recomendada para su impresión es de 0.1-0.2mm y el relleno entre 10-20%. La mejor forma de impresión sería de pie y para ello es necesario el uso de soportes para su correcta impresión. Una vez impreso el pomo no es necesario realizar ningún trabajo de post procesado a excepción de la retirada de los soportes. Para colocarlo en el joystick de su silla de ruedas simplemente encájelo a presión.

## prolongador-de-asa-para-maleta

- Ficha: https://accessibilitas.es/2020/06/prolongador-de-asa-para-maleta/
- Intencionalidad: El diseño de esta pieza está pensado para poder prolongar el asa de una maleta pequeña (tipo cabina) de manera que aquellas personas que tengan una longitud de miembros superiores que no les permita agarrar un asa a una altura estándar, puedan acceder a la misma Está diseñado de tal forma que se pueda aflojar y apretar sin necesidad del uso de herramientas. El objetivo es que el prolongador se pueda abatir tanto para el plegado del asa de la maleta, sin que sobresalga, como para que se pueda tirar del asa original sin necesidad de quitar el prolongador.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/prolongador-de-asa-para-maleta/Prolongador_para_ asa_de_maleta.scad`, `extraidos/prolongador-de-asa-para-maleta/Prolongador_para_ asa_de_maleta.stl`
- Parámetros de `Prolongador_para_ asa_de_maleta.scad`:
  - [Parámetros de la mordaza para la maleta] `Diametro = 30` — Diámetro del asa de la maleta
  - [Parámetros de la mordaza para la maleta] `Ancho = 22` — Anchura de la mordaza
  - [Parámetros de la mordaza para la maleta] `Grosor = 8` — Grosor de las paredes del soporte
  - [Parámetros de la mordaza para la maleta] `Tornillo = 4` — Diámetro del tornillo que se va a utilizar
  - [Parámetros de la mordaza para la maleta] `Cabeza = 6.7` — Diámetro de la cabeza del tornillo
  - [Parámetros de la mordaza para la maleta] `Prof_Cabeza = 3` — Profundidad de la cabeza del tornillo
  - [Parámetros de la mordaza para la maleta] `Tuerca = 9` — Diámetro de la tuerca hexagonal que se va a utilizar (en su parte más ancha)
  - [Parámetros del nuevo asa] `Cubo = 40` — Lado del cubo de encaje
  - [Parámetros del nuevo asa] `Distancia = 30` — Distancia desde el centro del asa hasta el borde de la maleta
  - [Parámetros del nuevo asa] `Dia_Tubo = 20` — Diámetro que deseamos para el nuevo asa
  - [Parámetros del nuevo asa] `Largo_Tubo = 210` — Longitud del tubo extensor
  - [Parámetros del nuevo asa] `Largo_Tirador = 100` — Largo del asa por el que se agarrará la maleta
  - [Parámetros de la palanca de apriete] `Dia_Grande = 20` — Diámetro Exterior del eje de apriete
  - [Parámetros de la palanca de apriete] `Dia_Peque = 8` — Diámetro Interior del eje de apriete
  - [Parámetros de la palanca de apriete] `Desplazamiento = 2` — Desplazamiento del Diámeto interior con respecto al exterior
  - [Parámetros de la palanca de apriete] `Largo_Palanca = 50` — Longitud de la palanca de apriete
  - [Parámetros de la palanca de apriete] `Gru_Palanca = 5` — Grosor de la palanca
  - [Parámetros de la palanca de apriete] `Tolerancia = 0.2` — Tolerancia entre piezas
  - [Parámetros de la palanca de apriete] `Angulo = -45` — Ángulo de rotación de la palanca con respecto al eje
  - [Parámetros de la palanca de apriete] `Hueco = 8` — Ancho del hueco de la palanca
  - [Elemento a mostrar] `Mostrar = "Todas"` [Todas:Todas las partes, Mordaza:Mordaza para el asa de la maleta, Tirador:Tirador de la maleta, Palanca:Palanca de apriete, Pasador:Pasador de la palanca] — Elemento que desea mostrar para generar el archivo stl
  - [hidden] `Tubo = Diametro/2`
- Impresión: Para que esta pieza sea lo más funcional posible debe imprimirse la mordaza en material flexible de SHORE 98A, como por ejemplo el filamento Flexfill 98A, que tiene la rigidez suficiente como para sujetar bien el asa de la maleta y a la vez la flexibilidad suficiente como para que pueda encajarse y desencajarse el asa de la maleta sin tener que realizar grandes esfuerzos. El resto de las piezas pueden imprimirse en PLA, aunque se recomienda el uso de materiales como el PETG o el ABS ya que tienen unas mejores características mecánicas. La altura de capa recomendada para su impresión es de 0.2mm y el relleno de un 30% con estructura cúbica. Para la impresión de la mordaza, al tratarse de un filamento flexible, y dependiendo de su impresora, tenga en cuenta que quizás sea necesario eliminar la retracción del filamento y disminuir la presión que se ejerce sobre el filamento al empujarlo, ya

## prolongador-de-mesa

- Ficha: https://accessibilitas.es/2021/10/prolongador-de-mesa/
- Intencionalidad: El diseño de esta pieza está pensado para poder dar una prolongación a la mesa a la vez que elevarla o bajarla unos centímetros para aquellas personas que por diferentes motivos no tengan la posibilidad de llegar correctamente a la mesa por problemas de altura de la misma. Se ha diseñado para que su fijación a la mesa sea tan sencilla como encajarlo en el canto de la misma, por lo que tanto su colocación como retirada de la misma se puede realizar con gran facilidad y en pocos segundos. La finalidad de la pieza es poder apoyar algo sobre ella, y no se debe utilizar en ningún caso como sistema de apoyo a la hora de sentarse y/o levantarse de la mesa, ya que solamente está pensada para soporta
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/prolongador-de-mesa/Prolongador_mesa.scad`, `extraidos/prolongador-de-mesa/Prolongador_mesa_345x270_alto_Espacia.stl`, `extraidos/prolongador-de-mesa/Prolongador_mesa_345x270_bajo_Espacia.stl`
- Parámetros de `Prolongador_mesa.scad`:
  - [Parámetros de la mesa donde se va a colocar] `Borde = "Plano"` [Plano,Redondeado] — Borde de la mesa
  - [Parámetros de la mesa donde se va a colocar] `GrueMesa = 28` [10:0.1:50] — Grosor de la mesa
  - [Parámetros del prolongador de mesa] `ProfTotal = 345` [190:5:300] — Profundidad total del reposa antebrazos
  - [Parámetros del prolongador de mesa] `ProfVol = 260` [100:5:210] — Parte voladiza del reposa antebrazos (donde realmente se hace el apoyo)
  - [Parámetros del prolongador de mesa] `AnchoTotal = 270` [150:1:250] — Anchura del reposa antebrazos
  - [Parámetros del prolongador de mesa] `GrueSoMesa = 5` [4:0.5:10] — Grosor sobre la mesa
  - [Parámetros del prolongador de mesa] `GrueInf = 8` [5:0.5:12] — Grosor mínimo de la parte inferior
  - [Parámetros del prolongador de mesa] `Posicion = "Bajar"` [Elevar,Bajar]
  - [Parámetros del prolongador de mesa] `Diferencia = 90` [0:2:100] — Diferencia entre el borde superior de la mesa y la parte superior del prolongador (Valor entre 0 y 100)
- Impresión: Recomendamos que se imprima con al menos 3 perímetros y no menos del 15% de relleno para asegurar su resistencia. Se puede imprimir en cualquier material que se desee. La altura de capa recomendada para su impresión es de 0.2-0.3mm, y si se dispone de una boquilla de 0.6mm o 0.8mm le ayudará a reducir considerablemente el tiempo de impresión, ya que es una pieza de gran tamaño. No es necesario el uso de soportes para su impresión.

## puntero-para-teclear

- Ficha: https://accessibilitas.es/2020/03/puntero-para-teclear/
- Intencionalidad: Este diseño está pensado para que personas sin fuerza ni movilidad en los dedos suficiente como para teclear, con las articulaciones metacarpofalángicas en extensión o hiperextensión y las interfalángicas proximal y distal en flexión o felxión extrema y con posibilidad de utilizar la sinergia funcional de la muñeca, Por ejemplo, personas con parálisis del nervio cubital, polineuropatías o mano tetrapléjica Para uso con teclados convencionales de ordenador. Compuesto por un aro que se sujeta a la falange que se necesite, y un pequeño puntero que es el que presionará las teclas.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/puntero-para-teclear/Puntero_para_teclear.scad`, `extraidos/puntero-para-teclear/Puntero_para_teclear1.stl`, `extraidos/puntero-para-teclear/Puntero_para_teclear2.stl`
- Parámetros de `Puntero_para_teclear.scad`:
  - [Fijación al dedo] `Fijacion = "Pinza"` [Aro:Cerrada, Pinza:Abierta] — ¿Desea que la fijación al dedo sea cerrada o abierta?
  - [Fijación al dedo] `Dia_Interior = 22` — Diámetro interior de la fijación al dedo
  - [Fijación al dedo] `Grosor_Aro = 2` — Grosor de la fijación al dedo
  - [Fijación al dedo] `Largo_Aro = 22` — Longitud de la fijación al dedo
  - [Puntero] `Largo_Puntero = 40` — Longitud de la varilla del puntero
  - [Puntero] `Grosor_Puntero = 7` — Diámetro de la varilla del puntero
- Impresión: El puntero para teclear se puede imprimir prácticamente con cualquier material no flexible que desee, ya que no va a realizar grandes esfuerzos mecánicos (PLA, PETG, ABS, etc,). La altura de capa recomendada para su impresión es de 0.1-0.2mm y el relleno de un 15-20%, ya que nos interesa que sea lo más ligero posible. No es necesario el uso de soportes para su impresión. Una vez impreso el puntero para teclear no es necesario realizar ningún trabajo de post procesado ni instalación.

## reposa-antebrazos

- Ficha: https://accessibilitas.es/2019/06/reposa-antebrazos/
- Intencionalidad: El diseño de esta pieza está pensado para poder dar un soporte adicional en los antebrazos a aquellas personas que por diferentes motivos no tengan la posibilidad de mantenerlos por sus propios medios cuando trabajan sobre una mesa. Se ha diseñado para que su fijación a la mesa sea tan sencilla como encajarlo en el canto de la misma, por lo que tanto su colocación como retirada se puede realizar con gran facilidad y en pocos segundos. No se debe utilizar en ningún caso como sistema de apoyo a la hora de sentarse y/o levantarse de la mesa, ya que solamente está pensada para soportar el peso de un brazo, y no la carga de un cuerpo entero. Si se imprime con escotadura, permitirá que el usuario 
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/reposa-antebrazos/Reposa_antebrazos_v2.scad`
- Parámetros de `Reposa_antebrazos_v2.scad`:
  - [Parámetros de la mesa donde se va a colocar] `Borde = "Plano"` [Plano,Redondeado] — Borde de la mesa
  - [Parámetros de la mesa donde se va a colocar] `GrueMesa = 30` [10:0.1:40] — Grosor de la mesa
  - [Parámetros del reposa antebrazos] `Escotadura = "Derecha"` [Derecha:Derecha, Izquierda:Izquierda, Sin:Sin escotadura] — Si se desea que el reposa antebrazos dé un mayor acceso al cuerpo
  - [Parámetros del reposa antebrazos] `ProfTotal = 245` [190:5:300] — Profundidad total del reposa antebrazos
  - [Parámetros del reposa antebrazos] `ProfVol = 160` [100:5:210] — Parte voladiza del reposa antebrazos (donde realmente se hace el apoyo)
  - [Parámetros del reposa antebrazos] `AnchoTotal = 200` [150:1:250] — Anchura del reposa antebrazos
  - [Parámetros del reposa antebrazos] `GrueSoMesa = 5` [4:0.5:10] — Grosor sobre la mesa
  - [Parámetros del reposa antebrazos] `GrosMinInf = 6` [4:0.5:10] — Grosor mínimo de la parte inferior
  - [Parámetros del reposa antebrazos] `GrosMaxInf = 10` [6:0.5:30] — Grosor máximo de la parte inferior (Valor entre 6 y 35)
  - [Parámetros del reposa antebrazos] `Suavizado = 100` [40:4:160] — Redondeo que se desea para el hueco de la escotadura
- Impresión: Para que la impresión sea lo más funcional posible se recomienda el uso de un filamento del tipo PLA o si es posible PETG, ya que sus propiedades mecánicas son superiores e igualmente fácil de imprimir. La altura de capa recomendada es de entre 0.2mm y 0.1mm. y el relleno de la impresión entre el 20% y el 30% con estructura cúbica. No es necesario el uso de soportes para su impresión.

## reposabrazos-giratorio

- Ficha: https://accessibilitas.es/2019/06/reposabrazos-giratorio/
- Intencionalidad: Este reposabrazos giratorio se ha diseñado pensando en aquellas personas que tengan dificultad a la hora de mover el brazo al realizar tareas manipulativas sobre una mesa (uso de teclado, ratón o actividades manuales en general) o que cuando lo hacen durante un determinado periodo de tiempo presentan gran fatiga muscular. Este dispositivo disminuye el trabajo muscular que hay que realizar para desplazar el brazo, permitiendo además mantener el antebrazo apoyado. Montaje del reposabrazos giratorio
- Parametrizable: no (solo STL)
- Archivos: `extraidos/reposabrazos-giratorio/Reposabrazos giratorio/Boton Cierre eje 1.stl`, `extraidos/reposabrazos-giratorio/Reposabrazos giratorio/Boton Cierre eje 2.stl`, `extraidos/reposabrazos-giratorio/Reposabrazos giratorio/Boton Cierre eje 3.stl`, `extraidos/reposabrazos-giratorio/Reposabrazos giratorio/Boton Cierre eje 4.stl`, `extraidos/reposabrazos-giratorio/Reposabrazos giratorio/PIEZA 01.stl`, `extraidos/reposabrazos-giratorio/Reposabrazos giratorio/PIEZA 02.stl`, `extraidos/reposabrazos-giratorio/Reposabrazos giratorio/PIEZA 03.stl`, `extraidos/reposabrazos-giratorio/Reposabrazos giratorio/PIEZA 04.stl`, `extraidos/reposabrazos-giratorio/Reposabrazos giratorio/PIEZA 05.stl`, `extraidos/reposabrazos-giratorio/Reposabrazos giratorio/PIEZA 06.stl`, `extraidos/reposabrazos-giratorio/Reposabrazos giratorio/PIEZA 07.stl`, `extraidos/reposabrazos-giratorio/Reposabrazos giratorio/PIEZA 08.stl` …
- Impresión: Las piezas se recomiendan imprimir con un filamento del tipo PETG, ya que este tipo de filamento tiene una mejor resistencia mecánica que el PLA, aunque también se podrían imprimir en este tipo de material. La altura de capa recomendada es de entre 0.2mm y 0.1mm. y el relleno de la impresión un 20% con estructura cúbica. En algunas de las piezas es necesario el uso de soportes para su impresión.

## salva-orejas-para-mascarillas

- Ficha: https://accessibilitas.es/2020/06/salva-orejas-para-mascarillas/
- Parametrizable: no (solo STL)
- Archivos: `extraidos/salva-orejas-para-mascarillas/Salvaorejas_castellano.stl`, `extraidos/salva-orejas-para-mascarillas/Salvaorejas_catalan.stl`, `extraidos/salva-orejas-para-mascarillas/Salvaorejas_euskera.stl`, `extraidos/salva-orejas-para-mascarillas/Salvaorejas_gallego.stl`

## soporte-maleta

- Ficha: https://accessibilitas.es/2019/06/soporte-maleta/
- Intencionalidad: El diseño de esta pieza está pensado para poder fijarse a un tubo horizontal del respaldo de la silla, de tal manera que permita transportar una maleta que no sea de grandes dimensiones ni demasiado peso. Se ha diseñado pensando en aquellas personas usuarias de silla de ruedas que en un momento dado puedan tener la necesidad de transportar una maleta sin ayuda en el interior de un aeropuerto, de una estación de tren, etc. En el caso de que su silla de ruedas no disponga de un tubo horizontal en el respaldo, puede imprimirse las piezas que se encuentran en el archivo Soporte_tubo_horizontal que le permitirán poder poner un tubo de este tipo a su silla de ruedas. No se recomienda en ningún cas
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/soporte-maleta/Soporte de maleta/Soporte_maleta.scad`
- Parámetros de `Soporte_maleta.scad`:
  - [None] `Diametro = 25` — //////////////////Parámetros definibles por el usuario////////////////////
  - [None] `Ancho = 20`
  - [None] `Grosor = 8`
  - [None] `Tornillo = 5`
  - [None] `Cabeza = 8`
  - [None] `Tuerca = 9`
  - [None] `Dia_Carro = 32`
  - [None] `Separacion = 10`
  - [None] `Tubo = Diametro/2` — ////////////////////////////Parámetros fijos (NO tocar)//////////////////////////////
  - [None] `Carro = Dia_Carro/2`
- Impresión: Para que esta pieza sea funcional debe imprimirse en material flexible de SHORE 98A, como por ejemplo el filamento Flexfill 98A, que tiene la rigidez suficiente como para mantener la maleta sin que se “escape” de su alojamiento y a la vez la flexibilidad suficiente como para que pueda encajarse y desencajarse el asa de la maleta sin tener que realizar grandes esfuerzos. La altura de capa recomendada para su impresión es de 0.2mm y el relleno de un 30% con estructura cúbica. Al tratarse de un filamento flexible, y dependiendo de su impresora, tenga en cuenta que quizás sea necesario eliminar la retracción del filamento y disminuir la presión que se ejerce sobre el filamento al empujarlo, ya que si no podría obstruirse la alimentación del extrusor. Igualmente deberá considerar disminuir notablemente la velocidad de impresión. No es necesario el uso de soportes para su impresión. Nota: Para

## soporte-para-bolso

- Ficha: https://accessibilitas.es/2019/06/soporte-para-bolso/
- Intencionalidad: El diseño de esta pieza está pensado para poder fijarse a un tubo vertical del reposapiés o de la parte delantera de la silla, para que se pueda colgar un pequeño bolso. Se ha diseñado pensando en aquellas personas usuarias de silla de ruedas que habitualmente utilizan un bolso de este tipo y siempre lo tienen que llevar sobre las piernas o pedir a otra persona que les ayude porque lo llevan colgado en el respaldo de la silla y no pueden acceder a él. Se necesitarán 2 soportes de este tipo para poder sujetar el bolso correctamente. Para una correcta colocación se debe pasar la correa del bolso por el hueco de cada uno de los soportes. A continuación, se debe ajustar la correa del bolso reduc
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/soporte-para-bolso/Soporte para bolso/Soporte_bolso.scad`
- Parámetros de `Soporte_bolso.scad`:
  - [None] `Diametro = 25` — ////////////////// Parámetros definibles por el usuario ////////////////////
  - [None] `Ancho = 30`
  - [None] `Grosor = 7`
  - [None] `Tornillo = 5`
  - [None] `Cabeza = 8`
  - [None] `Tuerca = 9`
  - [None] `Hueco_Bolso = 15`
  - [None] `Separacion = 0`
  - [None] `Tubo = Diametro/2` — //////////////////////// Parámetros fijos (NO tocar) //////////////////////////
  - [None] `Bolso = Hueco_Bolso/2`
- Impresión: Para que esta pieza sea funcional debe imprimirse en material flexible de SHORE 98A, como por ejemplo el filamento Flexfill 98A, que tiene la rigidez suficiente como para sujetar el peso del bolso y a la vez la flexibilidad suficiente como para que pueda introducirse y sacarse la correa del bolso sin tener que realizar grandes esfuerzos. La altura de capa recomendada para su impresión es de 0.2mm y el relleno de un 30% con estructura cúbica. Al tratarse de un filamento flexible, y dependiendo de su impresora, tenga en cuenta que quizás sea necesario eliminar la retracción del filamento y disminuir la presión que se ejerce sobre el mismo al empujarlo, ya que si no podría obstruirse la alimentación del extrusor. Igualmente deberá considerar disminuir notablemente la velocidad de impresión. Es necesario el uso de soportes para su impresión. Dependiendo de cómo se coloque la pieza para su im

## soporte-para-maleta-version-2

- Ficha: https://accessibilitas.es/2020/03/soporte-para-maleta-version-2/
- Intencionalidad: El diseño de esta pieza está pensado para poder fijarse a un tubo horizontal del respaldo de la silla, de tal manera que nos permita transportar una maleta o un carrito que no sea de grandes dimensiones. En el caso de que su silla de ruedas no disponga de un tubo horizontal en el respaldo, puede imprimirse las piezas disponibles en nuestro perfil de Thingiverse “Soporte_tubo_horizontal” que le permitirán poder poner un tubo de este tipo a su silla de ruedas. Se ha diseñado pensando en aquellas personas usuarias de silla de ruedas que realizan una vida activa y que en un momento dado puedan tener la necesidad de transportar una maleta (del tipo de las de equipaje de mano) en el interior de un
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/soporte-para-maleta-version-2/Soporte_maleta_V2.scad`, `extraidos/soporte-para-maleta-version-2/Soporte_maleta_V2.stl`, `extraidos/soporte-para-maleta-version-2/Soporte_maleta_maleta_V2.stl`, `extraidos/soporte-para-maleta-version-2/Soporte_maleta_silla_V2.stl`
- Parámetros de `Soporte_maleta_V2.scad`:
  - [Parámetros] `Diametro = 25` — Diámetro del tubo de la silla de ruedas a donde se va a fijar el soporte
  - [Parámetros] `Ancho = 20` — Anchura del soporte
  - [Parámetros] `Grosor = 8` — Grosor de las paredes del soporte
  - [Parámetros] `Tornillo = 5` — Diámetro del tornillo que se va a utilizar
  - [Parámetros] `Cabeza = 8` — Diámetro de la cabeza del tornillo
  - [Parámetros] `Tuerca = 9` — Diámetro de la tuerca hexagonal que se va a utilizar (en su parte más ancha)
  - [Parámetros] `Dia_Carro = 30` — Diámetro del asa del carro o maleta a transportar
  - [Mostrar] `Mostrar = "Ambas"` [Silla:Pieza que se fija a la silla, Maleta:Pieza a la que se sujeta la maleta, Ambas:Ambas piezas] — Elementos que desea mostrar
  - [Mostrar] `Tubo = Diametro/2` — ////////////////////////////Parámetros fijos (NO tocar)//////////////////////////////
  - [Mostrar] `Carro = Dia_Carro/2`
- Impresión: Para que esta pieza sea funcional debe imprimirse en material flexible de SHORE 98A, como por ejemplo el filamento Flexfill 98A, que tiene la rigidez suficiente como para mantener la maleta sin que se “escape” de su alojamiento y a la vez la flexibilidad suficiente como para que pueda encajarse y desencajarse el asa de la maleta sin tener que realizar grandes esfuerzos. La altura de capa recomendada para su impresión es de 0.2mm y el relleno de un 30% con estructura cúbica. Al tratarse de un filamento flexible, y dependiendo de su impresora, tenga en cuenta que quizás sea necesario eliminar la retracción del filamento y disminuir la presión que se ejerce sobre el filamento al empujarlo, ya que si no podría obstruirse la alimentación del extrusor. Igualmente deberá considerar disminuir notablemente la velocidad de impresión. No es necesario el uso de soportes para su impresión. Nota: Una 

## soporte-para-tablet

- Ficha: https://accessibilitas.es/2022/11/soporte-para-tablet/
- Intencionalidad: El diseño de este conjunto de piezas está pensado para poder sujetar un dispositivo tipo tablet y posicionarlo en el espacio de manera que permita a la persona la mayor funcionalidad posible. También permite colocar junto con la tablet un dispositivo de seguimiento visual para el control de la misma si fuese necesario. El diseño se ha pensado para mantener la tablet sobre un punto de fijación estable, como por ejemplo una mesa, pero en ningún caso para su uso sobre un punto de fijación en movimiento como una silla de ruedas. Su uso está pensado para aquellas personas que tienen buen control motor fino, es decir, que no golpean la tablet durante su uso, o para aquellas personas que acceden me
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/soporte-para-tablet/Moleteado.scad`, `extraidos/soporte-para-tablet/Mordaza.scad`, `extraidos/soporte-para-tablet/Piezas_soporte_tablet.stl`, `extraidos/soporte-para-tablet/Rotulas_de_union.scad`, `extraidos/soporte-para-tablet/Seguimiento_visual.stl`, `extraidos/soporte-para-tablet/Soporte_para_tablet.scad`, `extraidos/soporte-para-tablet/threads.scad`
- Parámetros de `Mordaza.scad`:
  - [Parámetros de la mordaza] `Largo_Mordaza = 60` — Largo de la mordaza
  - [Parámetros de la mordaza] `Ancho_Mordaza = 45` — Ancho de la mordaza
  - [Parámetros de la mordaza] `Alto_Mordaza = 55` — Alto de la mordaza
  - [Parámetros de la mordaza] `Grosor_Mordaza = 20` — Grosor de la mordaza
  - [Parámetros de la mordaza] `Tubo = 23.9` — Diámetro del tubo para fijación de la rótula
  - [Parámetros de la mordaza] `Largo_Tubo = 50` — Largo del tubo para fijación de la rótula
  - [Parámetros de la rosca] `Diametro_Rosca = 16` — Diámetro de la rosca
  - [Parámetros de la rosca] `Paso = 3` [2:0.5:4] — Paso de la rosca
  - [Parámetros de la rosca] `Diametro_Bola = 8` [7:1:12] — Diámetro de la bola
  - [Parámetros de la palomilla moleteada] `Alto_Palomilla = 12` — Altura de la palomilla
  - [Parámetros de la palomilla moleteada] `Diametro_Palomilla = 40` — Diámetro de la palomilla
  - [Parámetros de la palomilla moleteada] `Diametro = 25` [10:0.1:100] — Profundidad de las muescas
  - [Parámetros de la palomilla moleteada] `Numero_de_Muescas = 40` [15:1:50] — Número de muescas por fila
  - [Parámetros de la palomilla moleteada] `Profundidad_de_Muesca = 3.14*(Diametro/2)/Numero_de_Muescas`
  - [Parámetros de la palomilla moleteada] `Angulo_Moleteado = Alto_Palomilla/ (Diametro/2.5)*45`
  - [Parámetros de la palomilla moleteada] `Radio = Diametro_Palomilla/2`
  - [Parámetros de la presilla] `Tolerancia_Bola = 0.5` [0.1:0.1:1] — Tolerancia para el encaje de la bola
  - [Parámetros de la presilla] `Grosor_Presilla = 5` [3:0.5:5] — Grosor de la presilla
  - [Parámetros de la presilla] `Diametro_Presilla = 30` — Diámetro de la presilla
  - [Parámetros generales] `Redondeo = 4` [2:0.5:10] — Diámetro del redondeo de los bordes de la mordaza
  - [Parámetros generales] `Curva = 20` [5:1:40] — Diámetro de la curva de la mordaza
  - [Parámetros generales] `Suavizado = 8` [8:4:80] — Suavizado de las partes redondeadas
  - [Mostrar] `Mostrar = "Mordaza"` [Mordaza:Mordaza, Tornillo:Tornillo, Presilla:Presilla] — Elementos que desea mostrar para su impresión
- Parámetros de `Rotulas_de_union.scad`:
  - [Parámetros de la rótula] `Tubo_1 = 22.3` — Diámetro del primer tubo que va a utilizar (conviene darle entre 0.2 y 0.4mm de más)
  - [Parámetros de la rótula] `Tubo_2 = 16.3` — Diámetro del segundo tubo que va a utilizar (conviene darle entre 0.2 y 0.4mm de más)
  - [Parámetros de la rótula] `Diametro = 58` — Diámetro que desea para la mordaza (debe estar acorde con el diámetro del tubo que se va a utilizar)
  - [Parámetros de la rótula] `Plano = 3` — Milímetros de planificado que desea en los extremos (para facilitar su impresión sin soportes)
  - [Parámetros de la rótula] `Tornillo = 6.3` — Diámetro del tornillo que va a utilizar (conviene darle entre 0.2 y 0.4mm de más)
  - [Parámetros de la rótula] `Cabeza = 10` — Diámetro de la cabeza del tornillo que va a utilizar (conviene darle entre 0.2 y 0.4mm de más)
  - [Parámetros de la rótula] `Grosor_Cabeza = 6` — Grosor de la cabeza del tornillo que va a utilizar
  - [Parámetros de la rótula] `Tuerca = 11.5` — Diámetro de la tuerca que va a utilizar en su parte más ancha (conviene darle entre 0.2 y 0.4mm de más)
  - [Parámetros de la rótula] `Grosor_Tuerca = 5` — Grosor de la tuerca que va a utilizar
  - [Parámetros de la rótula] `Suavizado = 40` — Refinamiento que se desea para las partes redondeadas (a mayor refinamiento, mayor será el tiempo de renderización)
  - [Parámetros del tapón] `D_E = 12` — Diámetro exterior del tubo
  - [Parámetros del tapón] `D_I = 10` — Diámetro interior del tubo
  - [Mostrar] `Mostrar = "Hembra"` [Todo:Todos los elementos, Macho:Pieza que lleva el tornillo, Hembra:Pieza que lleva la tuerca, Soporte:Pieza de unión con el encaje del soporte de la tablet,Tapon:Tapón] — Elementos que desea mostrar para su impresión
- Parámetros de `Soporte_para_tablet.scad`:
  - [Medidas de la tablet] `Largo = 281` — Largo total de la tablet
  - [Medidas de la tablet] `Ancho = 216` — Ancho total de la tablet
  - [Medidas de la tablet] `Alto = 6.5` — Altura total de la tablet
  - [Medidas del soporte] `Grosor_Inferior = 4` — Grosor de la base del soporte
  - [Medidas del soporte] `Grosor_Superior = 3` — Grosor de la parte superior del soporte
  - [Medidas del soporte] `Reborde = 3` — Reborde que sujetará la tablet por arriba
  - [Medidas del soporte] `Redondeo = 3` — Radio del redondeo que se quiere en las esquinas (los laterales tendrán 1.5 veces este grosor)
  - [Aperturas laterales] `Sl1I = 40` — Largo de la apertura izquierda 1
  - [Aperturas laterales] `Dist1I = 25` — Distancia desde el extremo inferior de la tablet al principio de la apertura izquierda 1
  - [Aperturas laterales] `Sl2I = 58` — Largo de la apertura izquierda 2
  - [Aperturas laterales] `Dist2I = 148` — Distancia desde el extremo inferior de la tablet al principio de la apertura izquierda 2
  - [Aperturas laterales] `Sl3I = 16` — Largo de la apertura izquierda 3
  - [Aperturas laterales] `Dist3I = 100` — Distancia desde el extremo inferior de la tablet al principio de la apertura izquierda 3
  - [Aperturas laterales] `Sl1D = 40` — Largo de la apertura derecha 1
  - [Aperturas laterales] `Dist1D = 25` — Distancia desde el extremo inferior de la tablet al principio de la apertura derecha 1
  - [Aperturas laterales] `Sl2D = 40` — Largo de la apertura derecha 2
  - [Aperturas laterales] `Dist2D = 147` — Distancia desde el extremo inferior de la tablet al principio de la apertura derecha 2
  - [Aperturas laterales] `Sl3D = 0` — Largo de la apertura derecha 3
  - [Aperturas laterales] `Dist3D = 0` — Distancia desde el extremo inferior de la tablet al principio de la apertura derecha 3
  - [Aperturas laterales] `Sl1A = 7` — Largo de la apertura inferior 1
  - [Aperturas laterales] `Dist1A = 137` — Distancia desde el extremo inferior de la tablet al principio de la apertura inferior 1
  - [Aperturas laterales] `Sl2A = 0` — Largo de la apertura inferior 2
  - [Aperturas laterales] `Dist2A = 0` — Distancia desde el extremo inferior de la tablet al principio de la apertura inferior 2
  - [Aperturas laterales] `Dia_Camara = 15` — Diámetro de la apertura de la cámara
  - [Aperturas laterales] `Distx_Camara = 141` — Distancia desde el extremo izquierdo de la tablet al centro de la cámara
  - [Aperturas laterales] `Disty_Camara = 13` — Distancia desde el extremo superior de la tablet al centro de la cámara
  - [Elementos a mostrar] `Mostrar = "Soporte"` [ Soporte:Soporte para la tablet, Tope:Tope superior del soporte, Fijacion:Fijación del soporte, Encaje:Pieza de encaje para el soporte, Tirador:Tirador del tope, Casquillo:Casquillo para el tornillo, Cierre:Cierre superior del soporte] — Elementos que desea mostrar para su impresión
  - [Elementos a mostrar] `Suavizado = 40` — Suavizado para todas las partes redondeadas
- Impresión: Recomendamos que se imprima con al menos 3 perímetros y un 30% de relleno para asegurar su resistencia. Se puede imprimir en cualquier material que se desee, aunque para las “rótulas de unión” recomendamos que utilice un material con mejores propiedades mecánicas que el PLA, como p.e. el PETG o ABS. La altura de capa recomendada para su impresión es de 0.2mm, excepto en las piezas que llevan rosca (tope superior del soporte, pieza de encaje para el soporte, pasador roscado y el casquillo para el tornillo), que se recomienda una altura de capa de 0.15mm para que la rosca tenga una mayor definición. No es necesario el uso de soportes para su impresión a excepción de las piezas denominadas “Soporte para la tablet” y “Mordaza”.
- Instalación: Una vez que tengamos todas las piezas impresas y la tornillería necesaria, procederemos al montaje del brazo y el soporte para la tablet. En primer lugar montaremos el encaje para el soporte. Para ello necesitaremos las piezas impresas “Encaje para el soporte”, “Tirador del tope”, “casquillo para el tornillo” y “Tope superior del soporte”, así como un muelle de bolígrafo y un tornillo DIN912 M3x20mm. En primer lugar roscaremos el “Tope superior del soporte” en el “Encaje para el soporte”. Dependiendo de la precisión y ajustes de su impresora, a lo mejor necesita ayudarse de un alicate o herram

## soporte-para-tubo-horizontal

- Ficha: https://accessibilitas.es/2019/06/soporte-para-tubo-horizontal/
- Intencionalidad: El diseño de esta pieza está pensado para poder fijar un tubo horizontal al respaldo de aquellas sillas de ruedas que no dispongan de él. A este tubo horizontal se pueden sujetar los soportes de maleta o cualquier otro elemento que pueda ser de utilidad al usuario. Estos soportes permiten la colocación y retirada de un tubo horizontal de una forma muy simple y sin esfuerzo. Permite que las sillas de ruedas plegables, se puedan plegar aunque los soportes queden anclados en la silla. Si este tubo se va a utilizar como punto de anclaje para arrastrar una maleta o un carrito, No se recomienda en ningún caso su uso sobre pisos irregulares y/o bacheados como pueda ser la calle. Cómo configurar los
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/soporte-para-tubo-horizontal/Soporte para tubo horizontal/Soporte_tubo_horizontal.scad`
- Parámetros de `Soporte_tubo_horizontal.scad`:
  - [None] `Tubo_silla = 25` — ////////////////////////// Parámetros a definir //////////////////////////
  - [None] `Anchura = 60`
  - [None] `Altura = 80`
  - [None] `Grosor_pieza = 3`
  - [None] `Tubo_trasero = 25`
  - [None] `Tornillo = 5`
  - [None] `Cabeza = 8`
  - [None] `Tuerca = 9`
  - [None] `Grapa_Izqda = "SI"` — Si desea generar cualquiera de las piezas escriba "SI", o escriba "NO" si no desea que se generen(muy IMPORTANTE mantener siempre las comillas y las mayúsculas)
  - [None] `Grapa_Dcha = "SI"`
  - [None] `Barra_Izqda = "SI"`
  - [None] `Barra_Dcha = "SI"`
  - [None] `Tubo = Tubo_trasero/2` — ////////////////////// Parámetros fijos  (NO tocar) /////////////////////
  - [None] `Silla = Tubo_silla/2`
  - [None] `Pared = Grosor_pieza`
- Impresión: Para que la impresión sea lo más funcional posible se recomienda el uso de un filamento del tipo PLA o si es posible PETG, ya que sus propiedades mecánicas son superiores e igualmente fácil de imprimir. La altura de capa recomendada para su impresión es de 0.2mm y el relleno de un 30% con estructura cúbica. La altura de capa recomendada es de entre 0.2mm y 0.1mm. y el relleno de la impresión un 30% con estructura cúbica. No es necesario el uso de soportes para su impresión, excepto que el diámetro de los tubos sea excesivamente grande, en cuyo caso sí será conveniente el uso de soportes. Nota: Para poder fijarlo a la silla de ruedas necesitará de 4 tornillos y de 4 tuercas hexagonales. La longitud del tornillo debe ser acorde con el grosor que se le haya dado a la pieza, y recomendamos de sea de tipo DIN912 (tornillo de cabeza cilíndrica con hexágono interior). También necesitará un tubo

## sujeta-vasos

- Ficha: https://accessibilitas.es/2022/12/sujeta-vasos/
- Intencionalidad: El diseño de estas piezas está pensado para que las personas usuarias de silla de ruedas puedan disponer de un sujeta vasos de una forma cómoda y sin tener que llevarlo permanentemente anclado en la silla. El sujeta vasos está diseñado como si fuera un giróscopo, para poder mantener el vaso en posición vertical y que no se derrame el líquido, aunque la silla no se encuentre en una posición totalmente horizontal. Además, se puede retirar, de una forma muy simple, el sujeta vasos del soporte, por lo que no supondrá una molestia para el usuario si no lo está utilizando.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/sujeta-vasos/Sujeta_vasos.scad`
- Parámetros de `Sujeta_vasos.scad`:
  - [Dimensiones] `Dia_Vaso = 70` — Diámetro del vaso
  - [Dimensiones] `Dia_TuboX = 33` — Diámetro del tubo de la silla en X
  - [Dimensiones] `Dia_TuboY = 26.5` — Diámetro del tubo de la silla en Y
  - [Dimensiones] `Angulo = 0` — Ángulo de rotación de su tubo con respecto a la vertical (0 si está perpendicular al suelo)
  - [General] `Mostrar = "Sujeta"` [ Mordaza:Mordaza para fijar a la silla, Sujeta:Sujeta vasos]
  - [General] `Suavizado = 40` — Suavizado
- Impresión: Recomendamos que se imprima con al menos 2-3 perímetros y un 15-20% de relleno. Se puede imprimir en cualquier material que se desee. La altura de capa recomendada para su impresión es de 0.2mm. No es necesario el uso de soportes para la impresión del sujeta vasos, pero pudiera ser necesario el uso de soportes en la mordaza dependiendo del ángulo que tenga el tubo de la silla a la que se vaya a fijar.
- Instalación: Una vez que tengamos todas las piezas impresas y la tornillería necesaria, procederemos al montaje del sujeta vasos. En primer lugar insertaremos las tuercas M3 en sus correspondientes alojamientos tal y como se muestra en la siguiente imagen. A continuación roscaremos con los tornillos M3x10 el aro intermedio al aro interior hasta que la punta del tornillo sobresalga ligeramente del borde de la tuerca. Después atornillaremos de la misma forma el aro exterior al aro intermedio y ya tendremos el conjunto completo. Y por último ya solo tendremos que colocar el soporte en el tubo de la silla de r

## tapon-botella

- Ficha: https://accessibilitas.es/2022/09/tapon-botella/
- Intencionalidad: El objetivo de este tapón es facilitar la ingesta de agua a aquellas personas que por sus problemas de movilidad y/o deglución no puedan utilizar un vaso o los tapones habituales que se encuentran en el mercado principalmente dirigidos a deportistas. Este tapón está diseñado para las botellas de agua de la marca Font Vella (es una marca que se puede encontrar sin problemas en todo el territorio nacional), aunque es posible encontrar en el mercado otras marcas que utilizan la misma rosca en sus tapones.
- Parametrizable: no (solo STL)
- Archivos: `extraidos/tapon-botella/Tapon_agua.stl`
- Impresión: Se recomienda su impresión con PETG ya que es un material apto para uso alimenticio. La altura de capa recomendada para su impresión es de 0.2mm. Utilizar al menos 4 líneas de perímetro y un relleno del 100%, ya que esto nos ayudará a evitar filtraciones, aunque por el tipo de uso que tiene (no va a estar en continuo contacto con el líquido) no debería plantear ningún tipo de problema. Es necesario el uso de soportes para su impresión y se recomienda imprimir en la posición en la que está.

## vaso-con-escotadura

- Ficha: https://accessibilitas.es/2020/03/vaso-con-escotadura/
- Intencionalidad: El objetivo de este vaso es permitir a las personas que tienen limitada la extensión de cuello beber sin necesidad de llevar a cabo este movimiento. En su parte superior tiene una abertura que evita que el borde choque con la nariz de la persona que vaya a beber, aunque el vaso se incline, permitiendo verter mejor el líquido, aunque la persona no eche la cabeza hacia atrás. También se ha agregado la posibilidad de incorporarle una o dos asas para facilitar el agarre.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/vaso-con-escotadura/Vaso_escotadura.scad`, `extraidos/vaso-con-escotadura/Vaso_escotadura.stl`, `extraidos/vaso-con-escotadura/Vaso_escotadura_asas.stl`
- Parámetros de `Vaso_escotadura.scad`:
  - [Vaso] `Dia_Superior = 80` — Diámetro superior del vaso
  - [Vaso] `Dia_Inferior = 60` — Diámetro inferior del vaso
  - [Vaso] `Altura = 90` — Altura del vaso
  - [Vaso] `Grosor = 2.5` — Grosor de las paredes y el fondo del vaso
  - [Escotadura] `Escotadura = "SI"` [SI:SI, NO:NO] — ¿Desea que tenga hueco para la nariz?
  - [Escotadura] `Alto_Escotadura = 25` — Altura del hueco para la nariz
  - [Escotadura] `Ancho_Escotadura = 35` — Anchura para el hueco de la nariz
  - [Asas] `Asas = "No"` [No:Sin asas, Derecha:Derecha, Izquierda:Izquierda, Ambas:Ambas] — ¿Desea que el vaso tenga asas? (Solamente si la altura del vaso es superior a 100 mm)
- Impresión: El vaso se debe imprimir con un filamento del tipo PETG, ya que este tipo de filamento está aprobado para su uso en la industria alimentaria (no debemos olvidar que nuestros labios estarán en contacto con el plástico y se ingerirá el líquido que ha estado en contacto con el vaso). La altura de capa recomendada para su impresión es de 0.1-0.2mm y el relleno entre 10-20%. En un principio no es necesario el uso de soportes para su impresión excepto en el caso de que se incluyan asas, en cuyo caso sí es recomendable su uso. Una vez impreso el vaso no es necesario realizar ningún trabajo de post procesado ni instalación.

## vaso-conico

- Ficha: https://accessibilitas.es/2020/03/vaso-conico/
- Intencionalidad: El objetivo de este vaso es permitir a las personas que tienen limitada la extensión de cuello beber realizando una extensión de cuello menor a la habitual. Este vaso en su parte externa tiene el aspecto de cualquier vaso, pero sin embargo su parte interna tiene forma cónica, permitiendo que con una menor inclinación el líquido llegue antes al borde del mismo. También se ha agregado la posibilidad de incorporarle una o dos asas para facilitar el agarre.
- Parametrizable: sí (OpenSCAD)
- Archivos: `extraidos/vaso-conico/Vaso_conico.scad`, `extraidos/vaso-conico/Vaso_conico.stl`
- Parámetros de `Vaso_conico.scad`:
  - [Vaso] `Dia_Superior = 90` — Diámetro superior del vaso
  - [Vaso] `Dia_Inferior = 70` — Diámetro inferior del vaso
  - [Vaso] `Altura = 100` — Altura del vaso
  - [Vaso] `Grosor = 2.5` — Grosor de las paredes y el fondo del vaso
  - [Asas] `Asas = "No"` [No:Sin asas, Derecha:Derecha, Izquierda:Izquierda, Ambas:Ambas] — ¿Desea que el vaso tenga asas? (Solamente si la altura del vaso es superior a 100 mm)
- Impresión: El vaso se debe imprimir con un filamento del tipo PETG, ya que este tipo de filamento está aprobado para su uso en la industria alimentaria (no debemos olvidar que nuestros labios estarán en contacto con el plástico y se ingerirá el líquido que ha estado en contacto con el vaso). La altura de capa recomendada para su impresión es de 0.1-0.2mm y el relleno entre 10-20%. Si se desea que el vaso además de las ayudas incluidas sea un vaso “lastrado” para aumentar su peso solo deberá realizar un relleno muy superior para conseguir que la parte inferior del vaso sea bastante más pesada. En un principio no es necesario el uso de soportes para su impresión excepto en el caso de que se incluyan asas, en cuyo caso sí es recomendable su uso. Una vez impreso el vaso no es necesario realizar ningún trabajo de post procesado ni instalación.
