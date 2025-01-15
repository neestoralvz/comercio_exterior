# **Plan de Acción Mejorado (Iteración 15)**  
## **Diagnóstico Actualizado y Limpieza de Warnings Restantes**

A partir de los últimos resultados compartidos, se han realizado **avances significativos** en la organización de la documentación y en la reducción de errores de compilación. El número de _warnings_ bajó considerablemente al corregir:

- La inclusión de archivos `.rst` en las `toctree` correspondientes.  
- La duplicidad de etiquetas y sustituciones.  
- Los problemas de subrayado en títulos y subtítulos.  
- La adopción exitosa del tema `sphinx-book-theme`.

Aun así, persisten alrededor de **101 _warnings_** relacionados principalmente con:

1. **Formateo de títulos**  
   - Algunos archivos aún presentan **desajustes** entre la longitud del subrayado y el texto del título o subtítulo.  
   - Posibles inconsistencias en la jerarquía de encabezados (ej. `==========` vs `--------`).

2. **Documentos no incluidos en la `toctree`**  
   - Se mencionan específicamente:  
     - `docs/08_normativas_y_regulaciones/index.rst`  
     - `docs/09_requisitos_legales_y_aduaneros/index.rst`  
     - `docs/verificacion_documentacion.rst`

3. **Referencia de etiqueta indefinida**  
   - Se detectó una referencia a la etiqueta `normativas_internacionales` que no está definida en ningún archivo.

4. **Pequeños ajustes en Sustituciones/Referencias**  
   - Aunque se consolidaron muchas definiciones en `substitutions.rst`, podrían quedar restos de definiciones duplicadas o comentarios obsoletos.  
   - Se requiere verificar si todos los archivos incluyen correctamente el `substitutions.rst` donde sea necesario.

---

## **Objetivo Principal**

Terminar de **limpiar los _warnings_ restantes** para que la documentación compile sin errores y se muestre completamente funcional bajo el nuevo tema “book”. Con esto se busca una experiencia de lectura fluida, una estructura consistente y la adopción completa de **buenas prácticas** de documentación técnica.

---

## **Plan de Acción Detallado**

### 1. Revisar y Ajustar Formato de Títulos/Subtítulos

1. **Identificar Archivos Conflictivos**  
   - Filtrar los _warnings_ que indiquen problemas de subrayado o inconsistencia de encabezados.  
   - Localizar los archivos `.rst` exactos y las líneas donde ocurren los errores.  

2. **Corregir la Longitud de Subrayado**  
   - Asegurar que cada título tenga un subrayado con al menos la misma longitud de caracteres que el texto.  
   - Respetar la jerarquía de secciones (por ejemplo, `#` para títulos principales, `=` para subsecciones, `-` para subsubsecciones, etc.).  

3. **Recompilar y Verificar**  
   - Ejecutar `make html` tras cada ajuste para cerciorarse de que el _warning_ haya desaparecido.  

---

### 2. Incluir los Documentos Faltantes en la `toctree`

1. **Agregar Rutas en el `index.rst` Principal**  
   - Verificar que `docs/08_normativas_y_regulaciones/index.rst`, `docs/09_requisitos_legales_y_aduaneros/index.rst` y `docs/verificacion_documentacion.rst` aparezcan bajo la directiva `.. toctree::` en `source/index.rst` o en el índice de alguna otra carpeta si corresponde.  

2. **Revisar Sub-Índices**  
   - Asegurarse de que cada carpeta (`08_normativas_y_regulaciones`, `09_requisitos_legales_y_aduaneros`, etc.) tenga su propio `index.rst` con un `.. toctree::` que incluya todos los archivos de la carpeta.  

3. **Estructura Coherente**  
   - Mantener la numeración (00, 01, 02, …) y la lógica de la guía.  
   - Evitar duplicar secciones similares: si existe un `index.rst` para la carpeta `08_normativas_y_regulaciones`, no debería haber otra carpeta distinta con el mismo contenido.  

4. **Compilar y Verificar**  
   - Al añadir las rutas faltantes, recompilar para ver si los _warnings_ de “document not included in any toctree” desaparecen.  

---

### 3. Definir la Etiqueta `normativas_internacionales` o Eliminarla

1. **Localizar la Referencia**  
   - Buscar en todo el proyecto (`grep -r "normativas_internacionales"`) para encontrar dónde se hace esa referencia.  

2. **Decidir Acción**  
   - **Definir la etiqueta**: Si es un tema que se debe cubrir, crear la subsección correspondiente en el archivo apropiado, por ejemplo, `docs/08_normativas_y_regulaciones/normativas_internacionales.rst`, con una etiqueta `.. _normativas_internacionales:`.  
   - **Eliminar la Referencia**: Si no existe tal sección o no se requiere, eliminar o comentar la referencia para evitar el _warning_.  

3. **Verificación Final**  
   - Después de crear o eliminar la etiqueta, recompilar y confirmar que el _warning_ desaparezca.  

---

### 4. Revisar Sustituciones y Limpieza Final

1. **Verificar Unicidad de Sustituciones**  
   - Confirmar que `substitutions.rst` sea la fuente única de todas las definiciones (`product`, `origin_country`, etc.).  
   - Revisar si algún archivo `.rst` define nuevamente las mismas sustituciones y eliminarlas.  

2. **Eliminar Comentarios Obsoletos**  
   - Buscar comentarios (`# ...`) o notas redundantes que hagan referencia a sustituciones ya movidas o temas no vigentes.  
   - Mantener la documentación lo más limpia y clara posible.  

3. **Incluir `substitutions.rst`**  
   - Asegurarse de que cada archivo que use sustituciones tenga la línea `.. include:: /substitutions.rst` **o** bien que se incluya de forma global en el `conf.py` si así se prefiere.  

4. **Compilación Final**  
   - Ejecutar `make html` y confirmar que no queden _warnings_ de sustituciones duplicadas o sin definir.  

---

### 5. Validación Final con el Tema “Book”

1. **Inspección Visual**  
   - Navegar por el `build/html/index.html` y comprobar la usabilidad con el **sphinx-book-theme**.  
   - Verificar secciones colapsables, niveles de encabezado, navegación previa/siguiente, etc.  

2. **Comprobación de Diapositivas y/o Diagramas**  
   - Revisar que los diagramas Mermaid y las tablas se visualicen correctamente con el nuevo tema.  
   - Ajustar estilos de `custom.css` si algo se ve desalineado.  

3. **Recoger Retroalimentación**  
   - Solicitar la opinión de los colaboradores y/o usuarios finales sobre la facilidad de uso y lectura.  
   - Recopilar sugerencias de mejoras estéticas o estructurales.  

---

## **Cronograma y Responsables (Sugerido)**

- **Día 1-2**:  
  - Ajustar títulos/subtítulos y corregir la mayoría de los errores de formato.  
  - Incluir documentos faltantes en la `toctree`.  

- **Día 3**:  
  - Resolver la etiqueta indefinida `normativas_internacionales`.  
  - Revisar sustituciones para evitar duplicados.  

- **Día 4**:  
  - Realizar una compilación final y verificar que no queden _warnings_.  
  - Asegurar la correcta visualización con *sphinx-book-theme*.  

- **Día 5**:  
  - Validación con un grupo de revisores o stakeholders.  
  - Recopilación de retroalimentación y ajustes finales.  

---

## **Conclusión**

La **Iteración 15** del plan se enfoca en la **limpieza minuciosa** de los _warnings_ restantes, la **inclusión** de todos los archivos en la estructura (`toctree`) y la **definición/ajuste** de etiquetas y sustituciones. Con esto se busca:

1. **Compilación Libre de Errores**  
2. **Estructura Consistente** en todos los niveles de documentación.  
3. **Plena Adopción** del tema _“book”_ con una experiencia de lectura amigable y profesional.  

Siguiendo estos pasos, la documentación quedará en **condiciones óptimas**, alineada con las **mejores prácticas** de Sphinx y ofreciendo una **navegación** clara, completa y coherente.