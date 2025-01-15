# **Plan de Verificación de Documentación – Instrucciones (Iteración Actualizada)**

A continuación se presenta la **versión actualizada** del plan, incorporando la **revisión de listas y sublistas** en archivos RST, tras la detección de que no se reflejan en la salida HTML generada por Sphinx. Este plan mantiene el enfoque de **diagnosticar**, **corregir** y **cerrar** todos los temas relacionados con la verificación y el buen formateo de la documentación.

---

## 1. Generar un reporte general de los archivos

1. **Listar todos los archivos `.rst`** del proyecto, tanto en `source/` como en `dev/organizacion/hallazgos/`.  
2. **Resumir el contenido** de cada archivo, indicando secciones principales y fecha de última modificación.  
3. **Detectar** archivos o rutas que no estén enlazados en ninguna `toctree`.

---

## 2. Elaborar un diagnóstico de hallazgos y pendientes

1. **Comparar** el estado de cada archivo (marcas `[X]`, `[?]`, `[✓]`) con el contenido real.  
2. **Identificar** incongruencias, referencias rotas, fechas inconsistentes o secciones vacías.  
3. **Registrar** un listado final de pendientes a resolver.

---

## 3. Revisar y corregir documentos con fechas futuras en el historial de cambios

1. **Localizar** archivos que muestren fechas en el historial mayores a la fecha real o versión deseada.  
2. **Sustituir** por fechas correctas o, si la intención es reflejar una actualización futura, **documentarlo claramente**.  
3. **Actualizar** el `CHANGELOG` o la sección de historial en el mismo archivo.

---

## 4. Atender errores de formato RST y referencias cruzadas

1. **Examinar** los archivos marcados con `[X]` para detectar sintaxis de tablas, listas o enlaces mal formateados.  
2. **Corregir** la sintaxis de acuerdo con las buenas prácticas de RST y Sphinx (tablas delimitadas, enlaces `:ref:`, etc.).  
3. **Verificar** que todas las etiquetas referenciadas (`.. _etiqueta:`) existan y que no haya _warnings_ por enlaces indefinidos.

---

## 5. Verificar la información técnica en documentos marcados con `[?]`

1. **Extraer** apartados técnicos (normativas, convenios, datos de producto) para validarlos con los equipos especialistas.  
2. **Consolidar** la retroalimentación e incorporarla en los documentos.  
3. **Marcar** como `[✓]` en caso de confirmación, o mantener `[?]` si se requiere más investigación.

---

## 6. Consolidar los hallazgos en los archivos de `dev/organizacion/hallazgos/`

1. **Registrar** en cada archivo de hallazgos (`.rst`) las correcciones o investigaciones pendientes.  
2. **Mantener** el historial de revisiones con fecha y descripción breve de lo corregido o investigado.  
3. **Asignar** responsable y estado final a cada hallazgo.

---

## 7. Compilar y cerrar la verificación

1. **Ejecutar** `make html` para generar la documentación en HTML.  
2. **Asegurar** que no aparezcan _warnings_ o errores en la compilación.  
3. **Confirmar** el estado definitivo de cada archivo (preferentemente `[✓]` o con notas claras para un seguimiento futuro).

---

## 8. Asegurar el mantenimiento continuo

1. **Programar** revisiones periódicas (cada trimestre) para prevenir desactualizaciones.  
2. **Utilizar** un sistema de control de versiones (Git) con mensajes de confirmación claros.  
3. **Habilitar** notificaciones o alertas cuando se acerque la fecha de revisión o se detecten cambios relevantes.

---

## 9. **Verificar la visualización de listas y sublistas** en los archivos RST

*(Este paso se incorpora como resultado de la detección de problemas en la salida HTML.)*

1. **Analizar la sintaxis**:  
   - Revisar la **indentación** en listas anidadas; en RST se requiere que cada nivel de sublista esté correctamente sangrado.  
   - Asegurar que las **marcas** de lista (`-`, `*`, o `1.`) estén seguidas por un espacio y que la línea siguiente tenga la sangría adecuada.  
   - Verificar que, si hay texto explicativo debajo de un ítem de lista, exista una **línea en blanco** o la **identación** correcta según el estilo RST.  
2. **Corroborar estilos**:  
   - Revisar `custom.css` u hojas de estilo que puedan **anular** la apariencia de las listas.  
   - Confirmar que no existan reglas CSS que oculten marcadores de lista (por ejemplo, `list-style: none;`).  
3. **Hacer pruebas**:  
   - En algún archivo de prueba, colocar una lista y sublista con indentación RST recomendada, por ejemplo:
     ```rst
     - Item de primer nivel
       - Subitem
         - Sub-subitem
     ```  
   - Compilar y observar si la jerarquía se refleja en la vista HTML.  
4. **Corregir** en caso de que los archivos productivos tengan listas definidas con un estilo o indentación incompatible (por ejemplo, usando tabulaciones en lugar de espacios).  
5. **Verificar** nuevamente con `make html` y asegurarse de que las listas se muestren de forma esperada.

---

## **Estado Actual del Plan**

- Tras revisar la estructura (`source/` y `dev/organizacion/hallazgos/`), se tiene **un amplio conjunto** de archivos `.rst`.  
- Se detectó que muchas listas y sublistas **no** se muestran adecuadamente en la versión HTML, lo cual indica posibles **problemas de indentación** o **reglas CSS**.  
- Se incorpora una **nueva sección (Paso 9)** para atender específicamente la visualización de listas y sublistas.  
- El resto de los pasos (1 a 8) siguen enfocados en corregir fechas, referencias cruzadas, verificación técnica y consolidación de hallazgos.

---

### **Conclusión**

Con esta **iteración**, el plan integra la **verificación y corrección** de las listas y sublistas en los archivos RST, garantizando que el contenido se muestre de manera clara y estructurada en la documentación generada por Sphinx. Al seguir estos pasos, se obtendrá una documentación **coherente, sin errores** de formato y con una **navegación** y **visualización** óptimas para los usuarios finales.