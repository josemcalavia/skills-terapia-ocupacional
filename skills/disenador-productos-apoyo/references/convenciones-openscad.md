# Convenciones de los diseños de Accessibilitas

Estas reglas salen del análisis de los 37 `.scad` originales (`originales/extraidos/`). Un diseño nuevo debe poder abrirlo una persona sin conocimientos de programación, cambiar los valores en el **Customizer** de OpenSCAD y exportar el STL, igual que con los originales.

## Estructura del archivo

```openscad
// <Nombre del producto> — <para qué sirve, en una frase>
// Diseño: <autor> · <fecha> · Derivado de la colección Diseños 3D de Accessibilitas
// (Fundación ONCE) — CC BY-NC-SA 4.0
use <ap_lib.scad>          // opcional: utilidades comunes
use <threads.scad>         // solo si hay roscas

/* [Parte a mostrar] */
// Elemento que desea mostrar en pantalla
Mostrar = "Cuerpo";    //[Cuerpo:Cuerpo principal, Tapa:Tapa roscada]

/* [Parámetros del <producto>] */
// Diámetro del eje del joystick de la silla de ruedas
Eje = 6;
// Superficie lisa o con hendiduras
Superficie = "Lisa";   //[Lisa, Perforada]
// Profundidad de las hendiduras
Prof_Agujero = 0.6;    // [0.2:0.1:1.5]

/* [Hidden] */
Holgura = 0.2;
$fn = 120;

module Cuerpo() { ... }
module Tapa() { ... }

if (Mostrar == "Cuerpo") Cuerpo();
if (Mostrar == "Tapa") Tapa();

if (Eje > 10) aviso("El eje es mayor de lo habitual en joysticks (4-8 mm). Compruebe la medida.");
```

## Reglas

1. **Parámetros arriba y agrupados** en bloques `/* [Sección] */`, con nombres de sección en español que describan la pieza: «Parámetros del pomo», «Medidas de la tablet», «Dimensiones», «Aperturas laterales». Todo lo que el usuario no deba tocar va en `/* [Hidden] */`.
2. **Un comentario `//` justo encima de cada parámetro.** El Customizer lo muestra como descripción. Debe ser una frase completa en lenguaje llano que diga qué es y cómo se mide, por ejemplo «Diámetro del tubo de la silla en X».
3. **Los nombres de variable van en español**, con mayúscula inicial y guiones bajos: `Dia_Superior`, `Grosor_Inferior`, `Dist1I`. Las unidades siempre son **mm** y grados.
4. **Los controles del Customizer van al final de la línea:**
   - desplegable: `//[Valor:Etiqueta visible, ...]` o `//[Lisa, Perforada]`
   - deslizador: `// [min:max]` o `// [min:paso:max]`
   - sí/no: los originales usan `"SI"/"NO"` o `"Lisa"/"Perforada"`. Es preferible usar cadenas antes que booleanos, porque se entienden mejor.
5. **Selector `Mostrar`:** si el producto tiene varias piezas, se exporta un STL por pieza eligiendo la pieza en `Mostrar`. Cada pieza es un `module` con nombre en español.
6. **Cada pieza se genera en la orientación de impresión**, apoyada en Z=0 y sin voladizos de más de 45°. Si no hay más remedio, se indica en las instrucciones dónde hacen falta soportes. Para facilitar la impresión se recorta la parte que haría falta sostener, como el «Bocado» del pomo de bola.
7. **Holguras:** 0,2 mm para encajes y colas de milano y +0,2 mm sobre el diámetro del eje para encajes a presión. Son 0,4 mm si la pieza debe girar libre. Los encajes a presión sobre ejes metálicos se hacen con un **casquillo de TPU**, como en los pomos.
8. **Tornillería:** M3 con tuerca cautiva hexagonal (d=6,1, `$fn=6`), agujero pasante de 3,4 y cabeza de 6,2. Para fijar algo a un tubo se usa una **mordaza partida** con dos mitades y M3 (soporte de tubo, sujeta-vasos, soporte para tablet). Los accesorios se acoplan a la mordaza con **cola de milano**.
9. **Roscas:** se usa `threads.scad` (Dan Kirshner) con `metric_thread(diametro, paso, largo, internal=true)` para la hembra. Hay que dar 0,3–0,4 mm de holgura radial a la hembra.
10. **Resolución:** `$fn` alto en curvas visibles (120–360) y moderado en detalles (24–40). Si el render es lento se expone un parámetro `Suavizado`.
11. **Avisos:** las combinaciones inválidas se señalan con `echo()` en rojo. Sirve el módulo `aviso()` de `ap_lib.scad`, porque el usuario ve el mensaje en la consola del Customizer. Si un valor haría imposible la pieza, se limita con `min()`/`max()` y se avisa.
12. **Sin dependencias raras:** solo OpenSCAD y las librerías de `lib/`, que se copian junto al diseño al entregarlo.
13. **Ergonomía:** los mangos de agarre miden 25–45 mm de diámetro para agarre cilíndrico. Para agarre débil o en garra se recomiendan superficies con hendiduras, sin aristas vivas (`minkowski`, `hull` de esferas o `rotate_extrude` de perfiles redondeados) y bordes con un radio de al menos 1 mm.

## Técnicas de modelado que se repiten

- `difference()` con el negativo exacto del objeto que se adapta: eje, tubo, tablet o jeringa.
- `hull()` entre esferas o cilindros para formas orgánicas y redondeadas.
- `minkowski()` con un cilindro pequeño para suavizar asas y bordes. Es lento, así que se usa con moderación.
- `rotate_extrude()` de un perfil 2D para vasos, pomos y bordes con labio.
- Bucles `for` con `rotate` para patrones de hendiduras o de agujeros.
- Recortes `translate(...) cube(..., center=true)` para crear una base plana de impresión.

## Ejemplos que conviene leer antes de diseñar algo parecido

| Necesidad | Original de referencia |
|---|---|
| Pomo o mando para joystick de silla | `pomo-de-bola`, `pomo-en-t-para-silla-de-ruedas`, `pomo-en-u-para-silla-de-ruedas`, `pomo-silla-de-montar` |
| Fijación a tubo de silla, mesa o andador | `soporte-para-tubo-horizontal`, `sujeta-vasos`, `soporte-para-tablet` (Mordaza.scad) |
| Engrosador o mango | `engrosador-de-chupachups`, `puntero-para-teclear`, `palanca-para-llave-de-paso-de-cisterna` |
| Recipiente o vaso | `vaso-conico`, `vaso-con-escotadura`, `pastillero-varias-tomas`, `caja-apilable-y-tirador` |
| Rosca o émbolo | `ayuda-para-jeringa-de-alimentacion`, `joystick` |
| Carcasa a medida de un dispositivo | `soporte-para-tablet`, `joystick-con-carcasa` |
| Tirador o asa | `caja-apilable-y-tirador` (Pomo_aro.scad), `prolongador-de-asa-para-maleta` |
| Texto o braille en relieve | `cartel-braille` |
