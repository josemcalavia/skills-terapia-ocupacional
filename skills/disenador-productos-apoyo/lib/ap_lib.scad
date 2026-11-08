// ap_lib.scad — utilidades comunes para productos de apoyo imprimibles
// Recoge los recursos que se repiten en los diseños de Accessibilitas
// (holguras de 0.2 mm, tuercas M3 cautivas, colas de milano, mordazas a tubo).
// Uso:  use <ap_lib.scad>   (las constantes requieren include <ap_lib.scad>)

AP_HOLGURA       = 0.2;   // holgura de encaje deslizante / a presión
AP_HOLGURA_LIBRE = 0.4;   // holgura para piezas que deben girar o deslizar sin esfuerzo
AP_PARED_MIN     = 1.2;   // pared mínima (3 perímetros de 0.4 mm)
AP_M3_PASO       = 3.4;   // agujero pasante para tornillo M3
AP_M3_TUERCA     = 6.1;   // entre vértices del hexágono de tuerca M3 (+holgura)
AP_M3_CABEZA     = 6.2;   // diámetro de cabeza de tornillo M3 allen

// Aviso visible en la consola del Customizer (mismo estilo que los originales)
module aviso(texto) { echo(str("<font color='red'>ATENCIÓN: ", texto, "</font>")); }

// Hueco para tornillo M3 + tuerca cautiva (restar con difference)
module hueco_m3(largo = 20, prof_tuerca = 3, prof_cabeza = 3.2, fn = 40) {
    translate([0, 0, -largo/2]) cylinder(d = AP_M3_PASO, h = largo, $fn = fn);
    translate([0, 0, -largo/2 - 0.01]) cylinder(d = AP_M3_TUERCA, h = prof_tuerca, $fn = 6);
    translate([0, 0, largo/2 - prof_cabeza + 0.01]) cylinder(d = AP_M3_CABEZA, h = prof_cabeza, $fn = fn);
}

// Cola de milano macho (extruida en Z)
module cola_milano_m(ancho1 = 20, ancho2 = 12, prof = 4, alto = 30) {
    linear_extrude(height = alto)
        polygon([[-ancho2/2, 0], [ancho2/2, 0], [ancho1/2, prof], [-ancho1/2, prof]]);
}
// Cola de milano hembra: hueco a restar, con holgura
module cola_milano_h(ancho1 = 20, ancho2 = 12, prof = 4, alto = 30, holgura = AP_HOLGURA) {
    translate([0, -0.01, -0.01]) linear_extrude(height = alto + 0.02)
        polygon([[-ancho2/2 - holgura, 0], [ancho2/2 + holgura, 0],
                 [ancho1/2 + holgura, prof + holgura], [-ancho1/2 - holgura, prof + holgura]]);
}

// Cubo con aristas verticales redondeadas (apoyado en Z=0)
module cubo_redondeado(dim = [20, 20, 10], r = 2, fn = 40) {
    r2 = min(r, dim[0]/2 - 0.01, dim[1]/2 - 0.01);
    hull() for (x = [r2, dim[0] - r2], y = [r2, dim[1] - r2])
        translate([x, y, 0]) cylinder(r = r2, h = dim[2], $fn = fn);
}

// Abrazadera partida para tubo (silla de ruedas, mesa, andador).
// Tubo elíptico Dx x Dy a lo largo de Z. Mostrar mitad: "A", "B" o "Ambas".
// Se cierra con dos tornillos M3 por lado. La mitad "A" tiene la cara
// exterior en +Y para poder unir accesorios.
module mordaza_tubo(Dx = 25, Dy = 25, alto = 30, pared = 4, holgura = AP_HOLGURA,
                    mitad = "Ambas", separacion = 1, fn = 120) {
    ex = Dx + 2*holgura; ey = Dy + 2*holgura;
    oreja = AP_M3_TUERCA + 4;
    module cuerpo() difference() {
        hull() {
            scale([1, ey/ex, 1]) cylinder(d = ex + 2*pared, h = alto, $fn = fn);
            for (s = [-1, 1]) translate([s*(ex/2 + pared + oreja/2 - 1), 0, alto/2])
                cube([oreja, 2*pared + 6, alto], center = true);
        }
        translate([0, 0, -1]) scale([1, ey/ex, 1]) cylinder(d = ex, h = alto + 2, $fn = fn);
        for (s = [-1, 1], z = [alto*0.25, alto*0.75])
            translate([s*(ex/2 + pared + oreja/2 - 1), 0, z]) rotate([90, 0, 0])
                hueco_m3(largo = 2*pared + 6.02);
    }
    module medio(lado) intersection() {
        cuerpo();
        translate([-200, lado > 0 ? separacion/2 : -200 - separacion/2, -1]) cube([400, 200, alto + 2]);
    }
    if (mitad == "A" || mitad == "Ambas") medio(1);
    if (mitad == "B" || mitad == "Ambas") medio(-1);
}

// Superficie de agarre: anillos de hendiduras esféricas sobre un cilindro
module hendiduras_cilindro(d = 30, alto = 60, d_hueco = 4, prof = 0.6, paso = 8, fn = 24) {
    n = max(6, floor(PI*d/paso));
    for (z = [paso/2 : paso : alto - paso/2], i = [0 : n - 1])
        rotate([0, 0, i*360/n + (floor(z/paso) % 2)*180/n])
            translate([d/2 + d_hueco/2 - prof, 0, z]) sphere(d = d_hueco, $fn = fn);
}
