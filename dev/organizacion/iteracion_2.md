\# Plan para la Documentación con Sphinx

Dado que vamos a utilizar Sphinx, aquí te presento un plan sobre cómo
deberías llevar la documentación, aprovechando las capacidades de Sphinx
y la estructura de archivos que ya tienes.

\## Estructura de la Documentación con Sphinx

Sphinx organiza la documentación en una estructura jerárquica,
utilizando archivos `.rst` (reStructuredText) o `.md` (Markdown, con la
extensión `myst_parser`). Ya tienes una buena base con la estructura
actual, pero aquí te sugiero cómo adaptarla y mejorarla.

\### 1. Mantener la Estructura de Carpetas

La estructura de carpetas que tienes es lógica y está bien organizada.
Mantenla como base:

    source
    ├── conf.py
    ├── index.rst
    └── docs_md
        ├── 00_introduccion
        │   └── overview.md
        ├── 01_precios_y_pagos
        │   ├── precios.md
        │   └── terminos_de_pago.md
        ├── 02_normativas_y_regulaciones
        │   ├── guatemala.md
        │   └── mexico.md
        ├── 03_incoterms
        │   └── incoterms_seleccionados.md
        ├── 04_requisitos_legales_y_aduaneros
        │   ├── agentes_aduanales_contactos.md
        │   ├── documentacion_exportacion.md
        │   ├── documentacion_importacion.md
        │   └── permisos_especiales.md
        ├── 05_transporte_y_logistica
        │   └── planificacion_transporte.md
        ├── 06_formalidades_frontera
        │   ├── exportacion_mexico.md
        │   └── importacion_guatemala.md
        ├── 07_gestion_riesgos
        │   └── plan_gestion_riesgos.md
        └── 08_contactos_y_soporte
            └── directorio.md

\### 2. Convertir Archivos Markdown a reStructuredText (Opcional)

Aunque Sphinx puede manejar Markdown con `myst_parser`, considera
convertir los archivos `.md` a `.rst` para aprovechar al máximo las
capacidades de Sphinx. reStructuredText ofrece mayor flexibilidad y
control sobre la estructura y el formato.

Si decides mantenerlos en Markdown, esta bien, es una cuestion de
preferencia.

\#### Herramientas para Conversión:

- **Pandoc:** Una herramienta de línea de comandos que puede convertir
  entre varios formatos, incluido Markdown a reStructuredText.
- **MyST-Parser:** Si prefieres mantener los archivos en Markdown,
  asegúrate de que `myst_parser` esté correctamente configurado en
  `conf.py`.

\### 3. `conf.py`

Tu archivo `conf.py` está bien configurado. Solo asegúrate de:

- **Habilitar la Extensión Correcta:** Si decides usar reStructuredText,
  no es necesario `myst_parser`. Para Markdown, asegúrate de que esté
  incluido en `extensions`.
- **Rutas de Documentos:** Verifica que la ruta a los archivos sea
  correcta.
- **Tema:** `sphinx_rtd_theme` es una buena elección, aunque si se
  quiere experimentar mas adelante se pueden probar `furo` o
  `pydata_sphinx_theme`.

\### 4. `index.rst` (Archivo Principal)

Tu `index.rst` es correcto. Este archivo sirve como la página principal
de tu documentación. La directiva `toctree` define la estructura de la
documentación. Asegúrate de que todas las secciones y subsecciones estén
incluidas.

Ejemplo de estructura:

    .. Documentación de Comercio Exterior documentation master file

    =========================================
     Documentación de Comercio Exterior
    =========================================

    Bienvenido(a) a la documentación de comercio exterior. En esta guía encontrarás
    información y procedimientos para la exportación de ácido sulfúrico desde México
    hacia Guatemala, así como requisitos, normativas y mejores prácticas.

    .. toctree::
       :maxdepth: 2
       :caption: Contenido:

       docs_md/00_introduccion/overview
       docs_md/01_precios_y_pagos/index
       docs_md/02_normativas_y_regulaciones/index
       docs_md/03_incoterms/index
       docs_md/04_requisitos_legales_y_aduaneros/index
       docs_md/05_transporte_y_logistica/index
       docs_md/06_formalidades_frontera/index
       docs_md/07_gestion_riesgos/index
       docs_md/08_contactos_y_soporte/index

    Indices y Tablas
    =================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`

Se han creado archivos `index.rst` en cada subcarpeta principal de la
documentacion para organizar mejor el contenido.

Ejemplo del contenido de `source/docs_md/01_precios_y_pagos/index.rst`:

    .. _precios_y_pagos:

    ==================
    Precios y Pagos
    ==================

    .. toctree::
       :maxdepth: 1

       precios
       terminos_de_pago

\### 5. Archivos `.rst` o `.md` Individuales

Cada archivo dentro de `docs_md` debe tener un encabezado claro y, si es
necesario, subsecciones.

Ejemplo de un archivo `.rst`:

    .. _precios:

    ========
    Precios
    ========

    Cálculo de Precios
    ===================

    Aquí va la descripción del cálculo de precios, fórmulas, etc.

    .. nota::
       Los valores específicos y la formula deben ser completados.

    .. advertencia::
       Los precios pueden variar, consultar fuentes oficiales.

Ejemplo de un archivo `.md`:

    # Precios

    ## Cálculo de Precios

    Aquí va la descripción del cálculo de precios, fórmulas, etc.

    > **Nota**
    > Los valores específicos y la formula deben ser completados.

    > **Advertencia**
    > Los precios pueden variar, consultar fuentes oficiales.

\### 6. Incluir Diagramas

Una de las ventajas de Sphinx es la posibilidad de incluir diagramas.

- **Graphviz:** Puedes usar la extensión `sphinx.ext.graphviz` para
  crear diagramas con el lenguaje DOT.

  Ejemplo en un archivo `.rst`:

      .. graphviz::

         digraph {
           a -> b;
           b -> c;
           c -> a;
         }

- **Mermaid:** Puedes utilizar la extensión `sphinx_mermaid` para crear
  diagramas utilizando la sintaxis de Mermaid.

  Ejemplo en un archivo `.rst` o `.md`:

      .. mermaid::

         graph TD;
            A-->B;
            B-->C;
            C-->A;

      # Diagramas

      Aquí se puede incluir una descripción del diagrama.

      ```mermaid
      graph TD;
         A-->B;
         B-->C;
         C-->A;
      ```

  *Nota: Para usar la extensión \`\`sphinx_mermaid\`\`, primero debes
  instalarla. Normalmente, esto se puede hacer usando pip:*

      pip install sphinx-mermaid

  *Luego, debes añadir la extensión a tu archivo \`\`conf.py\`\`:*

      # conf.py
      extensions = [
          # ... otras extensiones ...
          'sphinx_mermaid',
      ]

\### 7. Compilación de la Documentación

Para generar la documentación en formato HTML, ejecuta el siguiente
comando en la carpeta raíz del proyecto:

    make html

Esto creará la documentación HTML en la carpeta `_build/html`.

\## Consideraciones sobre la Documentación como Proceso de Ventas de
Exportaciones

La documentación debe servir como una guía completa para el proceso de
ventas. Considera incluir:

- **Flujo del Proceso de Ventas:** Un diagrama que ilustre el proceso de
  ventas paso a paso, desde la prospección hasta el cierre y la
  postventa.
- **Preguntas Frecuentes (FAQ):** Una sección con preguntas frecuentes
  de los clientes y sus respuestas.
- **Guías de Resolución de Problemas:** Para ayudar al equipo de ventas
  a manejar objeciones y problemas comunes.

\## Diagramas Necesarios

Basándome en la información que has proporcionado, los siguientes
diagramas podrían ser útiles:

- **Diagrama de Flujo del Proceso de Exportación:** Para ilustrar el
  proceso completo, desde la recepción del pedido hasta la entrega del
  producto en Guatemala.
- **Diagrama de Flujo del Proceso de Ventas:** Para visualizar el ciclo
  de ventas, incluyendo la prospección, la presentación, la negociación,
  el cierre y el seguimiento.
- **Diagrama de la Cadena de Suministro:** Para mostrar a los
  stakeholders y los pasos involucrados en la cadena de suministro del
  ácido sulfúrico.
- **Mapa de Ruta Logística:** Un mapa que muestre las rutas de
  transporte desde México hasta Guatemala, incluyendo aduanas y puntos
  de control.

\## Plan de Acción a Corto Plazo

1.  **Decidir entre Markdown y reStructuredText:** Evalúa la complejidad
    de la documentación y decide si convertir los archivos a
    reStructuredText o mantenerlos en Markdown.
2.  **Revisar y Completar la Información Existente:** Completa la
    información faltante en los archivos `.md` o `.rst`
    (concentraciones, códigos HS, valores en `precios.md`, etc.).
3.  **Crear Diagramas:** Define qué diagramas son más importantes y
    empieza a crearlos usando Graphviz o Mermaid, en caso de haber
    elegido mantener la documentacion en Markdown, instala y configura
    la extension `sphinx_mermaid`.
4.  **Revisar \`\`index.rst\`\` y \`\`conf.py\`\`:** Asegúrate de que
    estén correctamente configurados y reflejen la estructura deseada.
5.  **Compilar y Revisar:** Genera la documentación en HTML y revisa el
    resultado.

Continuaremos trabajando en la documentación para que sea una
herramienta útil y completa para tu equipo de ventas.

\## Proximos Pasos

Con la informacion que me has compartido, ahora puedo proceder a generar
el contenido de cada archivo de la documentacion.
