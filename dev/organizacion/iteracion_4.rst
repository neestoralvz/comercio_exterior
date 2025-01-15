# Plan de Acción para la Documentación con Sphinx (Iteración 4) - Diagnóstico y Mejora

## Diagnóstico del Estado Actual

*   **Conversión a reStructuredText:** Completada.
*   **Estructura de Carpetas:**  Se ha renombrado `docs_md` a `docs`. La
    carpeta `dev` se ha movido a la raíz del proyecto y está excluida de
    la compilación.
*   **Archivos `index.rst`:** Se han creado archivos `index.rst` en cada
    subcarpeta de `docs`, mejorando la organización y navegación.
*   **Contenido:** Se han realizado mejoras iniciales en la estructura
    y navegación, aplicando parcialmente las mejores prácticas. Se
    observa la inclusión de referencias cruzadas y descripciones en los
    `toctree`.
*   **Configuración de Sphinx:** `conf.py` está configurado
    correctamente, con `dev` excluida.
*   **Referencias a Markdown:** Se han actualizado las referencias a los
    archivos `.md` dentro de `index.rst` para que apunten a los archivos `.rst`.
*   **Mejores Prácticas:** Se han empezado a aplicar, pero aún hay
    margen de mejora en cuanto a la redacción, la exhaustividad de la
    información y el uso de elementos que faciliten la comprensión
    como se describió en la iteración anterior.
*   **Diagramas:** Todavía no se han creado los diagramas.

## Plan de Acción Mejorado (Iteración 4)

### 1. Revisar y Ajustar `conf.py`

*   Asegurar que la configuración en `conf.py` sea óptima,
    específicamente:

    ```python
    # Ruta a la carpeta raíz de la documentación, relativa a donde está el archivo conf.py.
    # En este caso, al estar conf.py y docs en la misma carpeta, source_dir es '.'.
    source_dir = '.'

    # Patrones a excluir, relativos al directorio source_dir.
    # Se excluyen la carpeta de compilación, los archivos de respaldo y la carpeta dev.
    exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '../dev']
    ```
*   Verificar que el path sea correcto:
    ```python
    # Ajusta la ruta de búsqueda de Python para que Sphinx pueda encontrar módulos o extensiones personalizadas.
    sys.path.insert(0, os.path.abspath("."))
    ```

### 2. Completar la Implementación de Mejores Prácticas

*   **Aplicar las mejoras sugeridas en la iteración anterior a todas
    las secciones de la documentación.**
*   **Enfoque:** Consistencia, claridad, uso de referencias cruzadas
    y una estructura que facilite la navegación.
*   **Revisión exhaustiva:** Revisar cada archivo `index.rst` y cada
    archivo `.rst` de contenido para asegurar que se han aplicado
    correctamente las mejoras.

*   **Ejemplos:**
    *   **`source/index.rst`:**
        *   Describir el propósito de la documentación.
        *   Indicar los destinatarios.
        *   Detallar la estructura.
        *   Explicar cómo navegarla.
        *   Incluir una sección de *Generación de la Documentación*.

    *   **`source/docs/01_precios_y_pagos/index.rst`:**
        *   Describir el contenido de la sección.
        *   Incluir referencias a otras secciones relacionadas.
        *   Utilizar `:ref:` para enlazar a las subsecciones.

    *   **`source/docs/00_introduccion/index.rst`:**
        *   Describir el proceso general de exportación.
        *   Explicar cómo usar la documentación.
        *   Utilizar `:ref:` para enlazar a las secciones donde se
            detallan los pasos.

### 3. Análisis Profundo y Planificación de Contenido

*   **Lectura Detallada:**  Leer cada archivo `.rst` para comprender
    el flujo de información e identificar ambigüedades.
*   **Identificar Información Clave:**  Determinar la información
    crítica para el equipo de ventas.
*   **Reunión con el Equipo de Ventas:**
    *   Validar la estructura actual y el contenido.
    *   Identificar las preguntas más frecuentes y las áreas que
        generan más dudas.
*   **Planificación de Contenido:**
    *   Definir las mejoras a realizar en cada archivo `.rst`, con
        base en el análisis y el feedback del equipo.
    *   Establecer un cronograma para completar la información
        faltante y mejorar la existente.

### 4.  Completar y Mejorar la Información con Enfoque Pragmático

*   **`overview.rst`:**
    *   Completar la información sobre la concentración del ácido
        sulfúrico y el código HS.
    *   Asegurar que la introducción sea clara, concisa y
        proporcione una visión general completa del proceso de
        exportación.
*   **`precios.rst`:**
    *   Completar los valores faltantes en la fórmula de cálculo de
        precios.
    *   Añadir ejemplos concretos del cálculo de precios para
        diferentes escenarios.
    *   Clarificar cualquier ambigüedad en la redacción.
*   **`terminos_de_pago.rst`:**
    *   Revisar la claridad y precisión de las descripciones de cada
        tipo de pago.
    *   Asegurar que las condiciones y plazos sean consistentes con
        las políticas de la empresa.
*   **`mexico.rst` y `guatemala.rst`:**
    *   Verificar la vigencia de las normativas mencionadas.
    *   Actualizar los enlaces a las fuentes oficiales, si es
        necesario.
    *   Considerar la inclusión de un resumen ejecutivo de las
        normativas más relevantes para el equipo de ventas.
*   **`incoterms_seleccionados.rst`:**
    *   Confirmar que los Incoterms seleccionados sean los más
        adecuados para la exportación de ácido sulfúrico a Guatemala.
    *   Añadir una justificación clara de la elección de cada
        Incoterm.
*   **`agentes_aduanales_contactos.rst`:**
    *   Verificar la vigencia de la información de contacto.
    *   Añadir una breve descripción de los servicios que ofrece cada
        agente aduanal.
*   **`documentacion_exportacion.rst` y `documentacion_importacion.rst`:**
    *   Crear un checklist o una tabla que resuma los documentos
        requeridos para la exportación e importación.
    *   Especificar claramente los requisitos de formato y contenido
        para cada documento.
*   **`permisos_especiales.rst`:**
    *   Detallar el proceso para obtener cada permiso especial.
    *   Incluir información sobre los tiempos de tramitación y los
        costos asociados.
*   **`planificacion_transporte.rst`:**
    *   Definir las rutas de transporte más comunes.
    *   Añadir información sobre los tiempos de tránsito y los costos
        estimados.
    *   Considerar la inclusión de un mapa de ruta.
*   **`exportacion_mexico.rst` e `importacion_guatemala.rst`:**
    *   Describir el proceso de exportación e importación paso a paso,
        utilizando un lenguaje claro y conciso.
    *   Incluir diagramas de flujo para visualizar mejor el proceso.
*   **`plan_gestion_riesgos.rst`:**
    *   Identificar los riesgos específicos asociados a la exportación
        de ácido sulfúrico a Guatemala.
    *   Desarrollar un plan de mitigación para cada riesgo
        identificado.
*   **`directorio.rst`:**
    *   Verificar la vigencia de la información de contacto.
    *   Organizar el directorio de forma lógica, por ejemplo, por
        departamento o función.

### 5. Crear Diagramas (Cuando Aporten Valor)

*   **Valor Práctico:**  Crear diagramas solo si aportan un valor
    claro para la comprensión del proceso de ventas o de exportación.
*   **Herramientas:** Utilizar `sphinx.ext.graphviz` o
    `sphinx_mermaid`.
*   **Tipos de Diagramas (Ejemplos):**
    *   **Flujo del Proceso de Ventas:** Simplificado y enfocado en
        los pasos clave.
    *   **Flujo del Proceso de Exportación:** Con los pasos críticos
        para la exportación a Guatemala.

### 6. Compilar y Revisar

*   **Compilar la Documentación:** Ejecutar `make html` para generar
    la documentación HTML.
*   **Revisar el Resultado:**  Verificar estructura, información,
    diagramas, navegación y enlaces.

### 7. Mantenimiento y Mejora Continua

*   **Establecer un Proceso de Revisión:** Definir la frecuencia de
    revisión y actualización de la documentación.
*   **Recopilar Feedback:** Implementar un mecanismo para que el
    equipo de ventas pueda proporcionar feedback y sugerencias de
    mejora.
*   **Actualizar Regularmente:** Mantener la documentación actualizada
    con la información más reciente sobre regulaciones, procesos y
    mejores prácticas.

## Próximos Pasos

1.  Revisar y ajustar el archivo `conf.py`.
2.  Implementar las mejores prácticas de organización y navegación
    en todas las secciones.
3.  Realizar el análisis profundo de la documentación y la reunión
    con el equipo de ventas.
4.  Definir el plan detallado para completar y mejorar la
    información.

Este plan de acción mejorado, junto con los pasos ya ejecutados,
proporciona una base sólida para desarrollar una documentación
pragmática y de alta calidad para el equipo de ventas.