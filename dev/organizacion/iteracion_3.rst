# Plan de Acción para la Documentación con Sphinx (Iteración 3) - Enfoque Pragmático

Esta iteración del plan se enfoca en mantener la documentación **pragmática, organizada y fácil de navegar**, siguiendo las mejores prácticas de la industria.

## Principios Rectores

*   **Pragmatismo:** La documentación debe ser una herramienta útil que resuelva problemas reales del equipo de ventas. Se priorizará la información esencial y se evitará la complejidad innecesaria.
*   **Claridad:** El lenguaje debe ser claro, conciso y sin ambigüedades. La estructura debe ser lógica e intuitiva.
*   **Facilidad de Navegación:** La información debe ser fácil de encontrar y acceder. Se utilizarán elementos de navegación como índices, tablas de contenido y enlaces internos.
*   **Consistencia:** Se mantendrá un estilo y formato consistente en toda la documentación.
*   **Actualización:** La documentación debe ser un recurso vivo que se actualice y mejore continuamente.

## Plan de Acción Mejorado (Enfoque Pragmático)

### 1. Renombrar `docs_md` a `docs` y Actualizar Configuraciones

*   **Acción:** Renombrar la carpeta `docs_md` a `docs`.
*   **Actualizar `index.rst`:** Modificar las referencias a `docs_md` para que apunten a `docs`.
*   **Actualizar `conf.py`:**
    *   Ajustar las rutas en `conf.py` para que reflejen el cambio de nombre.
    *   Asegurar que la carpeta `dev` esté excluida del proceso de compilación (ya configurado en la iteración anterior).

### 2. Crear Archivos `index.rst` para Cada Subcarpeta

*   Crear un archivo `index.rst` en cada subcarpeta de `docs`.
*   Utilizar la directiva `toctree` para listar el contenido de cada sección.
*   Añadir una breve descripción del contenido de cada archivo listado en el `toctree`.

Ejemplo para `docs/01_precios_y_pagos/index.rst`:

```rst
.. _precios_y_pagos:

==================
Precios y Pagos
==================

Esta sección cubre todo lo relacionado con precios, cotizaciones y términos de pago para la exportación de ácido sulfúrico a Guatemala.

.. toctree::
   :maxdepth: 1

   precios.rst - Información detallada sobre el cálculo de precios, incluyendo costos directos e indirectos.
   terminos_de_pago.rst - Descripción de los términos de pago disponibles, incluyendo anticipos, cartas de crédito y transferencias bancarias.
```

### 3.  Mejores Prácticas para la Organización y Navegación

*   **Jerarquía Clara:** Mantener una jerarquía de carpetas y archivos lógica y consistente, con no más de 3 o 4 niveles de profundidad para facilitar la navegación.
*   **Convención de Nombres:** Utilizar nombres de archivos descriptivos y en minúsculas, separados por guiones bajos (por ejemplo, `calculo_de_precios.rst`).
*   **Secciones Bien Definidas:** Cada archivo `.rst` debe tener un propósito claro y estar enfocado en un tema específico.
*   **Introducciones Claras:** Cada sección y subsección debe tener una breve introducción que explique su contenido y propósito.
*   **Enlaces Internos:** Utilizar enlaces internos (referencias) para conectar información relacionada entre diferentes archivos y secciones.
*   **Índice General:** El archivo `index.rst` principal debe servir como un índice general de toda la documentación, con una `toctree` que incluya todas las secciones principales.
*   **Búsqueda:** Aprovechar la funcionalidad de búsqueda integrada de Sphinx para permitir a los usuarios encontrar rápidamente la información que necesitan.

### 4. Análisis Profundo de la Documentación Existente y Planificación

*   **Lectura Detallada y Comprensión:**  Leer cada archivo `.rst` para entender el flujo de información, el propósito de cada sección y las relaciones entre los archivos.
*   **Esquema Pragmático:** Crear un esquema que refleje una estructura simplificada y enfocada en las necesidades del equipo de ventas, priorizando la información más utilizada.
*   **Identificación de Información Clave:** Identificar la información esencial para el proceso de venta y exportación.
*   **Reunión con el Equipo de Ventas:**
    *   Presentar el esquema propuesto y recabar feedback.
    *   Identificar las preguntas más frecuentes del equipo y de los clientes.
    *   Determinar qué información es la más consultada o la que genera más dudas.
*   **Ajuste del Esquema:** Refinar el esquema en función del feedback del equipo de ventas.

### 5. Completar y Mejorar la Información con Enfoque Pragmático

*   **Priorizar Información Esencial:**  Enfocarse en completar y mejorar la información crítica para el proceso de ventas.
*   **Lenguaje Claro y Directo:** Redactar la información de forma clara, concisa y directa, evitando tecnicismos innecesarios.
*   **Ejemplos Prácticos:** Incluir ejemplos concretos y casos de uso para ilustrar los conceptos clave.
*   **Checklists y Tablas:** Utilizar checklists y tablas para resumir información y facilitar su consulta.
*   **Eliminar Información Redundante u Obsoleta:**  Eliminar cualquier información que no sea relevante para el equipo de ventas o que esté desactualizada.

*   **Acciones por archivo:** Se detallaran las acciones específicas para cada archivo después del análisis y la reunión con el equipo de ventas.

### 6. Crear Diagramas (Cuando Aporten Valor)

*   **Valor Práctico:**  Crear diagramas solo si aportan un valor claro para la comprensión del proceso de ventas o de exportación.
*   **Herramientas:** Utilizar `sphinx.ext.graphviz` o `sphinx_mermaid`.
*   **Tipos de Diagramas (Ejemplos):**
    *   **Flujo del Proceso de Ventas:**  Simplificado y enfocado en los pasos clave.
    *   **Flujo del Proceso de Exportación:**  Con los pasos críticos para la exportación a Guatemala.

### 7.  `conf.py` y `index.rst`

*   **Revisar `conf.py`:** Reflejar los cambios realizados.
*   **Optimizar `index.rst`:**
    *   Introducción clara y concisa al propósito de la documentación.
    *   `toctree` bien organizada.
    *   Enlaces a las secciones más importantes.

### 8. Compilar, Revisar y Validar

*   **Compilar:** Generar la documentación HTML (`make html`).
*   **Revisar:**  Verificar estructura, información, diagramas, navegación y enlaces.
*   **Validar con el Equipo de Ventas:** Obtener feedback del equipo de ventas sobre la usabilidad y utilidad de la documentación.

### 9. Mantenimiento y Mejora Continua

*   **Establecer un Proceso de Revisión:** Definir la frecuencia de revisión y actualización de la documentación.
*   **Recopilar Feedback:** Implementar un mecanismo para que el equipo de ventas pueda proporcionar feedback y sugerencias de mejora.
*   **Actualizar Regularmente:** Mantener la documentación actualizada con la información más reciente sobre regulaciones, procesos y mejores prácticas.

## Próximos Pasos

1.  Renombrar `docs_md` a `docs` y actualizar `conf.py` e `index.rst`.
2.  Crear los archivos `index.rst` para cada subcarpeta, con descripciones claras en la `toctree`.
3.  Realizar el análisis profundo de la documentación y la reunión con el equipo de ventas.
4.  Definir el plan detallado para completar y mejorar la información con un enfoque pragmático.
5.  Implementar las mejoras y crear los diagramas que sean necesarios.

Este plan mejorado pone el foco en la utilidad práctica de la documentación, siguiendo las mejores prácticas de organización y navegación, y asegurando que la información sea un recurso valioso para el equipo de ventas.