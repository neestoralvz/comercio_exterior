# Plan de Acción Mejorado (Iteración 14) - Diagnóstico y Cambio de Tema a “Book”

A continuación, se presenta una actualización del diagnóstico y la propuesta de mejoras, incluyendo la adopción del tema **“book”** para Sphinx. Se asume que ya se han aplicado correcciones importantes en la estructura de archivos y que los errores de compilación se han reducido.

---

## Diagnóstico Actualizado

1. **Estructura de Documentos y Toctree**  
   - Se han creado y/o corregido la mayoría de los `index.rst` para cada sección, incorporando los archivos `.rst` faltantes en la `toctree`.  
   - Los subtítulos y encabezados se han ajustado para respetar la longitud de subrayado.  
   - Se han removido o actualizado referencias obsoletas a archivos que no existían o que tenían nombres distintos.

2. **Sustituciones y Etiquetas**  
   - Se ha centralizado la mayoría de las definiciones de sustitución en `substitutions.rst`.  
   - Aun así, podrían existir etiquetas repetidas o definiciones de sustitución duplicadas en algunos archivos. Es necesario revisar a detalle cada sección.

3. **Errores de Compilación Pendientes**  
   - Persisten algunos *warnings* y posibles referencias rotas que deben revisarse.  
   - Podrían quedar archivos PDF faltantes o secciones mencionadas que aún no se han integrado.  
   - Los diagramas con `sphinxcontrib-mermaid` podrían requerir una última verificación para garantizar su correcta visualización.

4. **Estilo y Usabilidad**  
   - El CSS y JavaScript personalizados (`custom.css` y `custom.js`) están funcionando, pero podrían requerir ajustes mínimos al cambiar de tema.  
   - La documentación ya cuenta con un formato más coherente; sin embargo, la adopción de un nuevo tema (book) implicará verificar la consistencia visual y de navegación.

---

## Plan de Acción Mejorado

### 1. Cambiar el Tema de Sphinx a “Book”

- **Objetivo:** Adoptar el tema *sphinx-book-theme* (o un tema similar conocido como “book”) para mejorar la usabilidad y la navegación en la documentación.

- **Acciones:**
  1. **Instalar o habilitar el tema**  
     - Agregar la dependencia en el entorno (por ejemplo, `pip install sphinx-book-theme` o equivalente).  
     - En el `conf.py`, asignar `html_theme = "sphinx_book_theme"` (o el nombre del tema seleccionado).
  2. **Configurar el tema**  
     - Ajustar parámetros en `conf.py` para personalizar elementos como `html_theme_options`, `logo`, `favicon`, etc.  
     - Revisar cómo se integran los estilos propios (`custom.css`) con el nuevo tema, ajustando rutas o reglas de CSS si es necesario.
  3. **Compilar y Validar**  
     - Ejecutar `make html` para confirmar que la documentación se genera correctamente con el nuevo tema.  
     - Revisar la navegación lateral, el índice y la presentación general de cada página.

### 2. Revisión Final de Etiquetas y Sustituciones

- **Objetivo:** Asegurar que no existan duplicados ni etiquetas rotas que causen advertencias o errores de referencia.

- **Acciones:**
  1. **Identificar Etiquetas Duplicadas**  
     - Realizar una búsqueda global (`grep -r ".. _"` por ejemplo) para localizar definiciones repetidas.  
     - Unificar o cambiar el nombre de las etiquetas duplicadas para que cada una sea única.
  2. **Limpiar Sustituciones**  
     - Corroborar que todas las sustituciones estén en `substitutions.rst`.  
     - Eliminar definiciones redundantes que aparezcan en archivos individuales.
  3. **Compilar y Verificar**  
     - Tras cada corrección, ejecutar `make html` para comprobar que los errores desaparezcan.

### 3. Validación de Diagramas y Archivos Anexos

- **Objetivo:** Confirmar la correcta visualización de los diagramas Mermaid y la disponibilidad de archivos referenciados (PDF u otros).

- **Acciones:**
  1. **Diagramas Mermaid**  
     - Revisar la directiva utilizada (`.. mermaid::`) y las opciones (`:align:` u otras directivas).  
     - Asegurar que `sphinxcontrib-mermaid` esté bien configurado en `conf.py`.
  2. **Archivos Descargables**  
     - Verificar que los PDF (o documentos externos) referenciados existan y tengan la ruta correcta.  
     - Crear *placeholders* (archivos vacíos o de ejemplo) en caso de que todavía no exista el contenido final.
  3. **Compilar y Revisar**  
     - Confirmar en la salida HTML que los diagramas y enlaces a archivos funcionen adecuadamente.

### 4. Verificación y Validación de Contenido

- **Objetivo:** Garantizar que toda la información sea exacta, coherente y esté alineada con las buenas prácticas establecidas.

- **Acciones:**
  1. **Revisión Temática y Técnica**  
     - Involucrar a expertos o revisores que validen la veracidad de cada sección.  
     - Corroborar que los procedimientos, definiciones y ejemplos estén actualizados.
  2. **Estilo y Uniformidad**  
     - Aplicar lineamientos de estilo (tanto en redacción como en el uso de encabezados y listados) de manera homogénea.  
     - Revisar la consistencia de nomenclatura (nombres de archivos, títulos, referencias cruzadas).
  3. **Compilar Versión Final**  
     - Una vez validados los contenidos, generar la documentación HTML y/o PDF (si es parte de los objetivos) como entrega final.

### 5. Mantenimiento y Mejora Continua

- **Objetivo:** Asegurar que la documentación permanezca actualizada y siga evolucionando conforme cambien los procesos o el alcance del proyecto.

- **Acciones:**
  1. **Definir Responsables**  
     - Determinar quién mantendrá la documentación (equipo técnico, autores específicos, etc.).  
     - Establecer un flujo de control de versiones (Git) para registrar cambios de manera ordenada.
  2. **Programar Revisiones Periódicas**  
     - Proponer revisiones trimestrales o semestrales, según la frecuencia de cambios en la organización.  
     - Recopilar la retroalimentación de los usuarios finales para refinar la documentación.
  3. **Documentar Nuevos Requisitos**  
     - Al surgir nuevas secciones o normativas, crear los archivos correspondientes siguiendo las mismas directrices de estilo.  
     - Mantener el índice (toctree) siempre sincronizado con el contenido real.

---

## Próximos Pasos

1. **Implementar el Tema “Book”**  
   - Instalar y configurar el tema en `conf.py`. Ajustar `custom.css` y `custom.js` para que no entren en conflicto con el nuevo estilo.

2. **Completar la Limpieza de Etiquetas y Sustituciones**  
   - Asegurar que no queden referencias huérfanas o duplicadas.  
   - Eliminar advertencias y *warnings* restantes al compilar.

3. **Verificar Diagramas y Archivos Faltantes**  
   - Integrar los diagramas mermaid al nuevo tema y revisar que se muestren sin errores.  
   - Añadir los PDF y otros anexos (o placeholders) para evitar referencias rotas.

4. **Revisión y Validación de Contenido**  
   - Una vez que el proyecto compile sin fallos, realizar la validación con los interesados (revisores temáticos, expertos).  
   - Corregir o ampliar secciones según sea necesario.

5. **Publicar la Versión Final y Planificar Mantenimientos**  
   - Publicar la documentación en el formato deseado (HTML, PDF, etc.).  
   - Programar las revisiones periódicas y establecer canales de retroalimentación.

---

Este **Plan de Acción Mejorado** busca **consolidar** la documentación bajo el nuevo tema *“book”* de Sphinx, corrigiendo los problemas técnicos pendientes y garantizando que el contenido sea claro, navegable y actualizado. Con ello, la documentación alcanzará un nivel óptimo de usabilidad y alineamiento con las **mejores prácticas** de redacción técnica.