# Plan de Acción para la Documentación con Sphinx (Iteración 6) - Diagnóstico y Mejora

## Diagnóstico del Estado Actual

*   **Conversión a reStructuredText:** Completada.
*   **Estructura de Carpetas:** Se ha renombrado `docs_md` a `docs`. La
    carpeta `dev` está en la raíz del proyecto y excluida de la
    compilación.
*   **Archivos `index.rst`:** Se han creado `index.rst` en cada
    subcarpeta, con mejoras sustanciales en estructura y navegación. Se
    han aplicado buenas prácticas de redacción y organización.
*   **Contenido:**
    *   Se ha comenzado la aplicación de plantillas en varias
        secciones:
        *   `01_precios_y_pagos/index.rst`
        *   `01_precios_y_pagos/precios.rst`
        *   `01_precios_y_pagos/terminos_de_pago.rst`
        *   `02_normativas_y_regulaciones/index.rst`
        *   `02_normativas_y_regulaciones/mexico.rst`
        *   `02_normativas_y_regulaciones/guatemala.rst`
        *   `04_requisitos_legales_y_aduaneros/index.rst`
        *   `05_transporte_y_logistica/index.rst`
        *   `05_transporte_y_logistica/planificacion_transporte.rst`
    *   Se ha mejorado el contenido de estas secciones, aplicando
        metadatos, referencias cruzadas, notas, advertencias y otros
        elementos.
    *   Aún queda trabajo por hacer en el resto de las secciones.
*   **Configuración de Sphinx:** `conf.py` está configurado
    correctamente y se han añadido opciones avanzadas, incluyendo
    variables globales.
*   **Referencias a Markdown:** Actualizadas.
*   **Mejores Prácticas:** Se ha avanzado significativamente en la
    aplicación de mejores prácticas en cuanto a estructura,
    organización, redacción y uso de elementos de reStructuredText.
*   **Diagramas:** Todavía no se han creado.
*   **Plantillas:** Se han creado y aplicado parcialmente las
    plantillas.
*   **Estilos:** Se ha añadido un archivo `custom.css` con mejoras
    sustanciales en la apariencia.
*   **JavaScript:** Se ha añadido un archivo `custom.js` para mejorar
    la experiencia del usuario.

## Plan de Acción Mejorado (Iteración 6)

### 1. Completar la Aplicación de Plantillas

*   **Objetivo:** Asegurar una estructura y formato consistentes en
    toda la documentación.
*   **Acción:** Aplicar las plantillas `section_template.rst` y
    `subsection_template.rst` a todos los archivos `.rst` restantes
    en la carpeta `docs`.
*   **Beneficio:** Facilita la creación de nuevo contenido, mejora la
    legibilidad y el mantenimiento.

### 2.  Completar y Mejorar la Información (Enfoque Pragmático)

*   **Acciones:**
    *   **`overview.rst`:** Completar información sobre concentración
        y código HS. Revisar introducción.
    *   **`precios.rst`:** Completar valores faltantes, añadir
        ejemplos.
    *   **`terminos_de_pago.rst`:** Revisar descripciones y
        condiciones.
    *   **`mexico.rst` y `guatemala.rst`:** Verificar vigencia de
        normativas, actualizar enlaces y resumir puntos clave.
    *   **`incoterms_seleccionados.rst`:** Confirmar adecuación y
        justificar elección.
    *   **`agentes_aduanales_contactos.rst`:** Verificar información
        de contacto y describir servicios.
    *   **`documentacion_exportacion.rst` y `documentacion_importacion.rst`:**
        Crear checklist o tabla y especificar requisitos.
    *   **`permisos_especiales.rst`:** Detallar proceso, tiempos y
        costos.
    *   **`planificacion_transporte.rst`:**  Ya se ha trabajado en
        esta sección, pero se puede mejorar aún más (ver siguiente
        punto).
    *   **`exportacion_mexico.rst` e `importacion_guatemala.rst`:**
        Describir proceso paso a paso.
    *   **`plan_gestion_riesgos.rst`:** Identificar riesgos y
        desarrollar plan de mitigación.
    *   **`directorio.rst`:** Verificar información y organizar por
        departamento o función.

### 3.  Desarrollar Subsecciones Pendientes de Transporte y Logística

*   **Objetivo:** Completar la información sobre transporte y
    logística.
*   **Acciones:**
    *   Crear y completar las subsecciones:
        *   `requisitos_seguridad.rst`
        *   `documentacion_transporte.rst`
    *   Utilizar la plantilla de subsección para mantener la
        consistencia.

### 4.  Desarrollar la Sección de Formalidades de Frontera

*   **Objetivo:**  Detallar los procedimientos en frontera.
*   **Acciones:**
    *   Completar las subsecciones:
        *   `exportacion_mexico.rst`
        *   `importacion_guatemala.rst`
    *   Utilizar la plantilla de subsección.
    *   Incluir información sobre inspecciones, documentación,
        tiempos de proceso y coordinación entre autoridades.

### 5.  Desarrollar la Sección de Gestión de Riesgos

*   **Objetivo:**  Identificar y mitigar riesgos.
*   **Acciones:**
    *   Completar la subsección `plan_gestion_riesgos.rst`.
    *   Utilizar la plantilla de subsección.
    *   Incluir información sobre riesgos operativos, de transporte,
        aduaneros, regulatorios, comerciales, financieros y
        ambientales.
    *   Desarrollar medidas de mitigación para cada tipo de riesgo.

### 6. Crear Diagramas

*   **Objetivo:** Mejorar la comprensión de procesos complejos.
*   **Acciones:**
    *   Crear un diagrama de flujo del proceso de exportación.
    *   Crear un diagrama de flujo del proceso de ventas.
*   **Herramientas:** Utilizar `sphinx.ext.graphviz` o
    `sphinx_mermaid`.

### 7. Revisar y Ajustar `conf.py` e `index.rst`

*   **Objetivo:** Asegurar una configuración óptima y una correcta
    estructura.
*   **Acciones:**
    *   Revisar que `conf.py` refleje todos los cambios realizados.
    *   Verificar que `index.rst` tenga una introducción clara, una
        `toctree` completa y que todas las secciones estén
        correctamente enlazadas.

### 8. Compilar y Revisar

*   **Objetivo:** Verificar la correcta generación y visualización
    de la documentación.
*   **Acciones:**
    *   Ejecutar `make html` para compilar la documentación.
    *   Revisar la documentación generada en un navegador,
        verificando la estructura, el formato, la información, los
        diagramas, la navegación y los enlaces.

### 9. Mantenimiento y Mejora Continua

*   **Objetivo:** Asegurar que la documentación se mantenga
    actualizada y siga siendo un recurso útil.
*   **Acciones:**
    *   Establecer un proceso de revisión periódica.
    *   Habilitar un canal para que el equipo de ventas pueda
        proporcionar feedback.
    *   Actualizar la documentación.

## Próximos Pasos

1.  Continuar aplicando las plantillas a todas las secciones y
    subsecciones.
2.  Completar la información faltante en los archivos `.rst`,
    siguiendo el plan detallado en el punto 2 de esta iteración.
3.  Desarrollar las secciones pendientes de transporte y logística,
    formalidades de frontera y gestión de riesgos.
4.  Crear los diagramas de flujo.

Este plan de acción, en su sexta iteración, se enfoca en completar la
aplicación de plantillas, desarrollar las secciones pendientes y
finalizar la documentación con un enfoque pragmático. Los siguientes
pasos están claramente definidos para avanzar hacia una documentación
completa y de alta calidad.