# Skills de Terapia Ocupacional

[![Licencia: CC BY-NC-SA 4.0](https://img.shields.io/badge/Licencia-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es)

Nueve skills para Claude dirigidas a terapeutas ocupacionales, docentes y estudiantes. Cada una es independiente: instala solo las que necesites. Versión 2.0.

| Skill | Para qué sirve | Descarga |
|---|---|---|
| Búsqueda de evidencia en TO | Acota la pregunta (PICO, PICo, SPIDER) y entrega tres estrategias de búsqueda por base de datos, con el registro de la búsqueda | [`to-busqueda-evidencia.skill`](descarga/to-busqueda-evidencia.skill) |
| Informe clínico de TO | Convierte notas clínicas en un informe con la terminología de la AOTA 2020 y de la CIF, con códigos CIF opcionales | [`to-informe-clinico.skill`](descarga/to-informe-clinico.skill) |
| Informe del Perfil Sensorial-2 | Redacta el informe del PS-2 (Dunn) a partir de las puntuaciones, con una plantilla adaptable | [`to-informe-perfil-sensorial-2.skill`](descarga/to-informe-perfil-sensorial-2.skill) |
| Escalas de evaluación en TO | Ayuda a elegir, administrar, puntuar e interpretar PASS, COPM, OSA, FIM+FAM, DASH, Barthel, Lawton y otras | [`to-escalas-evaluacion.skill`](descarga/to-escalas-evaluacion.skill) |
| Marco de Trabajo de la AOTA (2020) | Resuelve dudas y analiza casos con el dominio y el proceso del OTPF-4, y los relaciona con la CIF | [`to-marco-aota-2020.skill`](descarga/to-marco-aota-2020.skill) |
| Modelo de la Ocupación Humana (MOHO) | Analiza casos desde el MOHO y recomienda sus instrumentos de evaluación | [`to-moho.skill`](descarga/to-moho.skill) |
| Tutor de razonamiento clínico | Practica casos clínicos con preguntas socráticas y retroalimentación final, ajustado a tu nivel | [`to-tutor-razonamiento-clinico.skill`](descarga/to-tutor-razonamiento-clinico.skill) |
| Detector de barreras arquitectónicas | Analiza fotos de un espacio y detecta barreras según el CTE y el perfil de movilidad que elijas | [`detector-barreras-arquitectonicas.skill`](descarga/detector-barreras-arquitectonicas.skill) |
| Generador de exámenes y rúbricas | Convierte apuntes en un examen con solucionario y rúbrica, con el formato que define cada docente | [`generador-examenes-rubricas.skill`](descarga/generador-examenes-rubricas.skill) |

Para buscar productos de apoyo, existe el plugin [Asesor de productos de apoyo · Catálogo Ceapat](https://github.com/josemcalavia/ceapat-asistente).

## Cómo funcionan

1. **Primer uso.** La primera vez, la skill explica qué hace, cómo funciona y qué datos necesita. Después te pregunta si quieres adaptarla: tu ámbito, tu nivel, tus escalas o tu formato de informe o de examen. Si tienes prisa, responde «valores por defecto» y empieza ya.
2. **Estética de los documentos.** Por defecto, los documentos salen con un estilo neutro, sin logotipos ni marcas. Puedes elegir el formato (chat, Word, PDF, Markdown, HTML), los colores, la tipografía, tu propio logotipo, la cabecera y el pie, o usar tu plantilla .docx.
3. **Tus preferencias.** La skill te entrega un archivo `preferencias-<skill>.md`. Súbelo a los archivos de tu proyecto de Claude, o guárdalo en tu carpeta de trabajo, y se aplicará solo las próximas veces.
4. **Cambiarlas.** Di «cambiar preferencias» cuando quieras modificar algo.

## Qué necesitas

- Una cuenta de Claude con skills disponibles, en la web, en la aplicación de escritorio o en Claude Code.
- Para generar documentos Word o PDF, Claude necesita tener activada la creación de archivos (ejecución de código).

## Instalación

### En Claude (web o aplicación de escritorio)

1. Descarga el archivo `.skill` que quieras de la carpeta [`descarga/`](descarga).
2. En Claude, ve a **Ajustes**, **Capacidades**, sección de skills.
3. Pulsa para subir una skill y elige el archivo `.skill`.
4. Comprueba que aparece activada. Repite con cada skill que quieras usar.

### En Claude Code

Copia las carpetas que quieras de [`skills/`](skills) en `~/.claude/skills/`:

```bash
git clone https://github.com/josemcalavia/skills-terapia-ocupacional.git
cp -R skills-terapia-ocupacional/skills/to-moho ~/.claude/skills/
```

Reinicia Claude Code para que las detecte.

## Uso responsable

- **No introduzcas datos identificativos** de pacientes, familias o alumnado (nombre, DNI, dirección, número de historia). Las skills trabajan con iniciales y edad, y avisan si detectan datos personales.
- Revisa siempre lo que generen: están hechas con IA y quien las usa responde de su contenido. No sustituyen la valoración ni el criterio de un terapeuta ocupacional.
- Las skills no incluyen manuales, tablas de corrección ni ítems de instrumentos con derechos de autor. Si tienes tu copia de un manual o un protocolo, adjúntala en la conversación y la skill la usará como fuente principal.

## Qué hay en el repositorio

| Ruta | Para qué sirve |
|---|---|
| `skills/<nombre>/SKILL.md` | Instrucciones de cada skill |
| `skills/<nombre>/LICENCIA.md` | Condiciones de uso, dentro de cada skill |
| `skills/<nombre>/references/configuracion.md` | Primer uso, adaptación y preferencias (común a todas) |
| `skills/<nombre>/references/estilo-documentos.md` | Estilo neutro por defecto y opciones de estética (común a todas) |
| `skills/<nombre>/references/cif-referencia.md` | Guía rápida de la CIF y enlaces a las fuentes (informe clínico, AOTA y tutor) |
| `skills/to-marco-aota-2020/references/` | Síntesis propia del Marco de la AOTA 2020 (OTPF-4) |
| `skills/to-moho/references/` | Síntesis propia del MOHO: fundamentos e instrumentos |
| `skills/to-informe-perfil-sensorial-2/references/` | Síntesis propia del Perfil Sensorial-2 y plantilla del informe |
| `descarga/` | Paquetes `.skill` listos para subir a Claude |

## Autoría

Diseño original: **José María Calavia Balduz** ([ORCID 0009-0001-7105-2022](https://orcid.org/0009-0001-7105-2022)).

## Licencia

[Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es). Puedes usarlas, compartirlas y adaptarlas sin fines comerciales, manteniendo la autoría original y la misma licencia. Los modelos, normas e instrumentos citados pertenecen a sus autores y editores.
