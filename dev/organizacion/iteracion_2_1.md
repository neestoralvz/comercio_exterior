\# Plan de Acción para la Conversión de Archivos Markdown a
reStructuredText en macOS

Este plan detalla los pasos a seguir para la conversión de archivos
Markdown (.md) a reStructuredText (.rst) en un entorno macOS, dado que
**ya se ha tomado la decisión de realizar la migración**.

\## Pasos a Seguir

\### 1. Preparación

- **Respaldo:** Crear una copia de seguridad de todos los archivos
  Markdown. Se creara una rama de git llamada
  <span class="title-ref">backup-markdown</span> y se respaldara la
  informacion en esta rama.
- **Instalar Pandoc:** Instalar Pandoc si aún no está instalado. La
  forma más común en macOS es usando Homebrew.
  - **Instalación de Homebrew (si no lo tienes):**

    Abre una terminal y ejecuta el siguiente comando:

        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  - **Instalación de Pandoc:**

    Una vez que tengas Homebrew instalado, ejecuta el siguiente comando
    en la terminal:

        brew install pandoc

  - **Verificación:**

    Verifica que Pandoc esté accesible desde la línea de comandos
    ejecutando:

        pandoc --version

\### 2. Script de Conversión

- **Crear un Script de Conversión:** Se creara un script en Python para
  automatizar la conversión de todos los archivos en el directorio
  <span class="title-ref">docs_md</span>.

  Ejemplo de script en Python para convertir todos los archivos .md en
  la carpeta docs_md (y sus subcarpetas):

  `` `python import os import subprocess  def convert_md_to_rst(docs_md_path):     """     Convierte archivos Markdown a reStructuredText usando Pandoc.      Args:         docs_md_path: Ruta al directorio que contiene los archivos         Markdown.     """     for root, _, files in os.walk(docs_md_path):         for file in files:             if file.endswith(".md"):                 md_path = os.path.join(root, file)                 rst_path = os.path.splitext(md_path)[0] + ".rst"                 try:                     subprocess.run(                         ["pandoc", "-f", "markdown", "-t", "rst", md_path, "-o", rst_path],                         check=True,                     )                     print(f"Convertido: {md_path} a {rst_path}")                 except subprocess.CalledProcessError as e:                     print(f"Error al convertir {md_path}: {e}")   if __name__ == "__main__":     docs_md_directory = "source/docs_md"  # Ajusta la ruta si es necesario     convert_md_to_rst(docs_md_directory) ``\`

- **Explicación del Script:**

  - Importa los módulos <span class="title-ref">os</span> y
    <span class="title-ref">subprocess</span>.
  - Define la función <span class="title-ref">convert_md_to_rst</span>
    que recorre el directorio <span class="title-ref">docs_md</span> y
    sus subdirectorios.
  - Para cada archivo con extensión <span class="title-ref">.md</span>,
    llama a <span class="title-ref">pandoc</span> para convertirlo a
    <span class="title-ref">.rst</span>.
  - Imprime un mensaje indicando si la conversión fue exitosa o si hubo
    un error.

- **Guardar el Script:**

  - Guarda el script en un archivo llamado
    <span class="title-ref">convert_to_rst.py</span> en la raíz del
    proyecto (la misma carpeta donde esta el archivo
    <span class="title-ref">conf.py</span>).

- **Ejecutar el Script:**

  - Abre una terminal en la carpeta raíz del proyecto y ejecuta el
    script con el comando <span class="title-ref">python
    convert_to_rst.py</span>.

\### 3. Ajustes Manuales

- **Revisar los Archivos Convertidos:** Abrir los archivos
  <span class="title-ref">.rst</span> generados y verificar que la
  conversión se haya realizado correctamente.
- **Corregir Errores:** Es posible que Pandoc no pueda convertir
  perfectamente todos los elementos de Markdown a reStructuredText.
  Realizar ajustes manuales si es necesario, prestando especial atención
  a:
  - Encabezados
  - Listas
  - Tablas
  - Enlaces
  - Imágenes
  - Código en línea y bloques de código
- **Adaptar a la Sintaxis de reStructuredText:** Familiarizarse con la
  sintaxis de reStructuredText y realizar los cambios necesarios para
  que los archivos sean válidos.

\### 4. Actualizar `conf.py` e `index.rst`

- **Eliminar \`\`myst_parser\`\`:** Eliminar la extensión `myst_parser`
  del archivo `conf.py`.

- **Modificar \`\`source_suffix\`\`:** En `conf.py`, cambiar la
  configuración de `source_suffix` a:

  `` `python source_suffix = {     '.rst': 'restructuredtext', } ``\`

- **Ajustar \`\`index.rst\`\`:** Modificar las referencias a los
  archivos en `index.rst` para que apunten a los archivos
  <span class="title-ref">.rst</span> convertidos.

- **Actualizar rutas de archivos en la documentación:** Actualizar las
  rutas de los archivos <span class="title-ref">.rst</span> a lo largo
  de la documentación, incluyendo los archivos `index.rst` de cada
  subcarpeta.

\### 5. Compilar y Verificar

- **Compilar la Documentación:** Ejecutar `make html` en la carpeta raíz
  del proyecto para generar la documentación HTML.
- **Revisar el Resultado:** Abrir la documentación generada en un
  navegador y verificar que todo se visualice correctamente. Prestar
  atención a la estructura, el formato y la navegación.

\### 6. Eliminar archivos Markdown

- **Eliminar los archivos \`.md\` originales:** Una vez que la
  conversión se haya completado y verificado, eliminar los archivos
  <span class="title-ref">.md</span> originales del directorio
  <span class="title-ref">docs_md</span>. Esto se puede hacer
  manualmente o mediante un comando como el siguiente, con **cuidado**:

      find source/docs_md -name "*.md" -type f -delete

  *Nota: Este comando eliminará permanentemente los archivos Markdown.
  Asegúrate de tener una copia de seguridad o de que los cambios estén
  confirmados en un sistema de control de versiones como Git antes de
  ejecutarlo.*

\## Mantenimiento Futuro

- **Documentar la Decisión:** Documentar la decisión de cambiar a
  reStructuredText y las razones detrás de ella en un archivo `README` o
  en la propia documentación.
- **Capacitación:** Si el equipo no está familiarizado con
  reStructuredText, proporcionar una breve capacitación o recursos para
  facilitar la transición.
- **Guía de Estilo:** Crear una guía de estilo para reStructuredText que
  defina las convenciones que se utilizarán en la documentación.

Siguiendo este plan de acción, se podrá realizar una conversión
eficiente de Markdown a reStructuredText en macOS, aprovechando las
ventajas que ofrece este formato para la documentación con Sphinx.
