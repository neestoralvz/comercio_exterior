# **Plan de Verificación de Documentación – Instrucciones (Iteración Actualizada)**

## **Estado Actual**

1. Se cuenta con un archivo principal, `verificacion_documentacion.md` (mencionado en la conversación), que **resume** los resultados de la primera verificación.  
2. Existen **checklists** de hallazgos en la carpeta `dev/organizacion/hallazgos/`, que contienen anotaciones específicas sobre secciones y documentos con problemas o pendientes de revisión.  
3. Se ha detectado un **problema** en la visualización de **listas y sublistas** dentro de los archivos RST, que no se muestran adecuadamente en la salida HTML de Sphinx.  
4. Se dispone de **contexto previo** sobre cambios realizados en la documentación y la estructura del proyecto (`source/` y `dev/`). Este historial debe ser considerado para evitar retrabajos o verificaciones duplicadas.  

Con base en lo anterior, se requiere **una nueva verificación** que integre las listas de chequeo (`verificacion_documentacion.md`, hallazgos) y se aplique la corrección del formateo de listas.

---

## **1. Revisar y Actualizar la Lista de Verificación (verificacion_documentacion.md)**

1. **Objetivo**: Contar con un punto de partida confiable que describa las secciones, el estado de cada documento y los hallazgos pendientes.  
2. **Acciones**:  
   - Analizar el contenido de `verificacion_documentacion.md` para conocer el **estatus** de cada archivo (marcas `[X]`, `[?]`, `[✓]` u otras).  
   - Incorporar cualquier **cambio reciente** (por ejemplo, correcciones ya aplicadas, documentos nuevos, etc.).  
   - Validar que la lista sea **actual** y refleje la situación real de la documentación.

---

## **2. Revisar los Checklists en `dev/organizacion/hallazgos/`**

1. **Objetivo**: Aprovechar los registros de hallazgos detallados en cada archivo RST de hallazgos.  
2. **Acciones**:  
   - Identificar los **documentos** que presentan problemas de formato, enlaces rotos o fechas inadecuadas.  
   - Marcar en cada checklist si se ha resuelto el hallazgo o si continúa pendiente.  
   - Integrar la información con la lista principal de verificación (`verificacion_documentacion.md`).

---

## **3. Verificar y Corregir la Visualización de Listas y Sublistas**

1. **Objetivo**: Asegurar que todas las listas (bullets, enumeradas, definiciones) se muestren correctamente en HTML.  
2. **Acciones**:  
   - **Inspeccionar** la indentación de cada lista en los archivos RST, revisando:  
     - Uso de espacios en lugar de tabulaciones.  
     - Añadir líneas en blanco cuando sea necesario (especialmente en listas anidadas).  
   - **Comprobar** si en el `custom.css` u otras hojas de estilo se aplica algún `list-style: none;` u otra regla que oculte marcadores.  
   - **Crear** (o mantener) un archivo de prueba, por ejemplo `test_lists.rst`, para garantizar que se visualizan correctamente diversos niveles de anidación y tipos de listas.  
   - **Ejecutar** `make html` y **validar** la salida, asegurándose de que las listas aparezcan tal como se definieron.

---

## **4. Revalidar Fechas e Historial de Cambios**

1. **Objetivo**: Alinear las fechas y notas de versiones con la realidad o el calendario oficial.  
2. **Acciones**:  
   - Buscar en los archivos RST aquellos con **fechas futuras** o no coherentes en el historial (por ejemplo, “2024-01-20” cuando estamos en 2025).  
   - Decidir si se corrige la fecha para reflejar la última revisión o si se justifica como una próxima revisión planificada.  
   - Documentar la corrección en el historial local (o `CHANGELOG`, si existe).

---

## **5. Integrar la Información Técnica de Documentos Marcados con `[?]`**

1. **Objetivo**: Validar y/o completar el contenido que requiera confirmación de equipos especializados (Legal, Financiero, Técnico, etc.).  
2. **Acciones**:  
   - Revisar el contenido de documentos con `[?]` en la lista de verificación.  
   - Contactar a los responsables o consultar fuentes oficiales para confirmar datos (normas, especificaciones técnicas, convenios, etc.).  
   - Actualizar la documentación y marcar como `[✓]` cuando se confirme la información.

---

## **6. Consolidar los Hallazgos en sus Respectivos Archivos**

1. **Objetivo**: Mantener un historial transparente de los problemas detectados y sus resoluciones.  
2. **Acciones**:  
   - Documentar las correcciones realizadas, incluyendo la fecha, el archivo modificado y la descripción de la acción (por ejemplo, “Se corrigió indentación en la sublista de `uso_guia.rst`”).  
   - Si un hallazgo requiere más análisis, mantener la marca `[?]` e incluir detalles del porqué en el archivo de hallazgos.  
   - Asegurarse de que, al final de este proceso, cada hallazgo esté **asociado** a una acción concreta (resuelto o pendiente con responsables asignados).

---

## **7. Generar una Nueva Verificación Integrada**

1. **Objetivo**: Confirmar que los cambios en listas, fechas y contenidos se hayan aplicado correctamente.  
2. **Acciones**:  
   - Ejecutar nuevamente el proceso de verificación descrito en `verificacion_documentacion.md`, ajustado con las correcciones.  
   - Compilar con Sphinx (`make html`) y **revisar** que no aparezcan _warnings_ relevantes.  
   - Comprobar que la visualización de listas sea correcta en todos los documentos.

---

## **8. Mantenimiento Continuo**

1. **Objetivo**: Evitar que surjan nuevas incongruencias en la documentación.  
2. **Acciones**:  
   - **Programar** revisiones trimestrales o semestrales de la documentación, según las necesidades del proyecto.  
   - Mantener un **control de versiones** con mensajes claros de confirmación cada vez que se edite un archivo.  
   - **Emplear notificaciones** (por ejemplo, issues en un repositorio) para alertar sobre secciones críticas o próximas revisiones de fechas importantes.

---

## **Conclusión y Próximos Pasos**

1. **Adoptar** este plan como la guía para la **nueva verificación**, combinando la información de `verificacion_documentacion.md`, los **checklists** de hallazgos y el **historial** de cambios realizados.  
2. **Prestar especial atención** a la corrección de listas y sublistas, asegurando que la indentación y el estilo RST cumplan las normas, así como verificando que no existan reglas CSS que oculten marcadores.  
3. **Cerrar la verificación** con un reporte actualizado, reflejando el estado final de cada archivo y las acciones tomadas para asegurar la **calidad** y **consistencia** de la documentación.