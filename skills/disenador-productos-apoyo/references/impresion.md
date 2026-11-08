# Impresión 3D: impresora, laminador y ajustes

La impresora y el laminador se toman de las preferencias de la persona usuaria (`preferencias-disenador-productos-apoyo.md`). Si no hay preferencias, se usa una **impresora FDM genérica**:
- cama de 220 × 220 mm y 250 mm de altura;
- boquilla de 0,4 mm;
- PLA, PETG y TPU.

## Datos que hacen falta de la impresora

| Dato | Para qué |
|---|---|
| Modelo y volumen útil (X × Y × Z) | `fabricar.py` comprueba que cada pieza quepa. Si no cabe, se parte en piezas unidas con cola de milano o tornillos. |
| Boquilla | Pared mínima (3 perímetros = 3 × boquilla) y detalle mínimo. |
| Cerrada o abierta | ABS y ASA necesitan cámara cerrada. Con cámara cerrada, el PLA prefiere la tapa abierta. |
| Extrusor directo o Bowden | El TPU blando (85A–90A) solo funciona bien con extrusor directo. |
| Materiales disponibles | Para no proponer un material que la persona no tiene. |
| Laminador | Para dar los pasos en su programa y abrir los archivos. |

## Perfiles de ejemplo

### Elegoo Centauri Carbon + Elegoo Slicer
- Volumen 256 × 256 × 256 mm, CoreXY cerrada, extrusor directo, boquilla de acero endurecido de 0,4 mm.
- Materiales: PLA, PETG, TPU 95A, ABS, ASA, PLA-CF, PETG-CF y PA-CF.
- Para PLA, abrir la tapa o subir la ventilación auxiliar.
- En el laminador: elegir el perfil «Elegoo Centauri Carbon 0.4 nozzle».

### Otras impresoras habituales
| Impresora | Volumen (mm) | Laminador |
|---|---|---|
| Bambu Lab A1 / P1S / X1C | 256 × 256 × 256 | Bambu Studio |
| Bambu Lab A1 mini | 180 × 180 × 180 | Bambu Studio |
| Prusa MK4 / Core One | 250 × 210 × 220 / 250 × 220 × 270 | PrusaSlicer |
| Creality Ender-3 V3 | 220 × 220 × 250 | Creality Print / Cura |
| Elegoo Neptune 4 | 225 × 225 × 265 | Elegoo Slicer / Cura |

Todos estos laminadores abren `.stl` y `.3mf`. Si la persona confirma, se pueden abrir con el sistema:
- macOS: `open -a "<Laminador>.app" archivo.3mf`
- Windows: `start "" "archivo.3mf"`
- Linux: `xdg-open archivo.3mf`

## Ajustes recomendados por tipo de pieza

Se basan en las instrucciones de Accessibilitas y valen para cualquier FDM con boquilla de 0,4 mm.

| Tipo de pieza | Material | Capa | Perímetros | Relleno | Notas |
|---|---|---|---|---|---|
| Pomos, mangos, engrosadores | PLA o PETG | 0,2 | 3–4 | 10–20 % giroide | Sin soportes si tiene base recortada |
| Casquillo de encaje a presión | **TPU 95A** | 0,2 | 3 | 20–40 % | Velocidad baja (≈ 30–40 mm/s) y retracción corta |
| Mordazas, soportes a tubo, piezas con carga | **PETG** | 0,2 | 4–5 | 25–40 % | Tuercas M3 cautivas: meterlas a presión o con una pausa |
| Vasos y recipientes | PETG | 0,2 | 3 | 15 % | El plástico impreso **no es apto para uso alimentario continuado**, por la porosidad entre capas |
| Carcasas finas con pestañas | PLA o PETG | 0,1–0,12 | 3 | 20 % | Soportes solo en la zona indicada |
| Uso exterior o con calor (coche, sol) | ASA (cámara cerrada) o PETG | 0,2 | 4 | 25 % | El PLA se deforma a unos 55 °C |
| Texto o braille en relieve | PLA | 0,12 | 2 | 15 % | Imprimir con el relieve hacia arriba |

## Temperaturas orientativas

Hay que confirmarlas con el fabricante del filamento.

| Material | Boquilla | Cama |
|---|---|---|
| PLA | 200–220 °C | 55–60 °C |
| PETG | 235–250 °C | 70–80 °C |
| TPU 95A | 215–230 °C | 40–50 °C |
| ABS/ASA | 245–260 °C | 90–100 °C |

## Comprobaciones antes de entregar

`fabricar.py` hace estas comprobaciones automáticamente:
- malla cerrada («manifold»);
- la pieza cabe en el volumen de la impresora;
- apoya en Z=0;
- volumen y peso macizo;
- avisos del diseño.

Estas se revisan a mano sobre la vista PNG:
- no hay voladizos de más de 45° sin un soporte previsto;
- las paredes miden al menos 3 × boquilla;
- en las piezas que soportan esfuerzo, las capas no quedan en la dirección de la fuerza. Por ejemplo, un gancho aguanta más impreso tumbado que de pie.
