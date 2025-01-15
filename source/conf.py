# conf.py

import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------
# Ajusta la ruta de búsqueda de Python para que Sphinx pueda encontrar módulos o extensiones personalizadas.
sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------
project = "Documentación de Comercio Exterior"
author = "Equipo de Comercio Exterior"
release = "1.0.0"
version = ".".join(release.split(".")[:2])  # Versión corta (X.Y)
copyright = f"{datetime.now().year}, {author}"

# -- General configuration ---------------------------------------------------
# Ruta a la carpeta raíz de la documentación
source_dir = '.'
master_doc = 'index'  # Documento principal
templates_path = ['_templates']  # Carpeta para plantillas personalizadas
today_fmt = '%d de %B de %Y'  # Formato de fecha en español

extensions = [
    # Extensiones básicas de Sphinx
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",  # Para referencias entre documentaciones
    "sphinx.ext.autosectionlabel",  # Para referencias automáticas a secciones
    "sphinx.ext.todo",  # Para marcar tareas pendientes
    "sphinx.ext.ifconfig",  # Para contenido condicional
    "sphinx.ext.extlinks",  # Para enlaces externos abreviados
    "sphinx.ext.githubpages",  # Para publicación en GitHub Pages
    "sphinx.ext.imgmath",  # Para fórmulas matemáticas
    "sphinx.ext.graphviz",  # Para diagramas
    "sphinxcontrib.mermaid",  # Para diagramas mermaid
]

# Configuración para autosectionlabel
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# Configuración para todo
todo_include_todos = True
todo_link_only = False
todo_emit_warnings = True

# Configuración de formatos de archivo soportados
source_suffix = {
    '.rst': 'restructuredtext',
}

# Tema y opciones
html_theme = "sphinx_book_theme"
html_theme_options = {
    # Repository
    "repository_url": "",
    "use_repository_button": False,
    "use_issues_button": False,
    "use_edit_page_button": False,
    
    # Navigation
    "toc_title": "En esta página",
    "show_toc_level": 3,
    "show_nav_level": 2,
    
    # Appearance
    "logo": {
        "image_light": "_static/logo.png",
        "image_dark": "_static/logo.png",
    },
    "home_page_in_toc": True,
    "announcement": "",
    
    # Extra features
    "use_download_button": True,
    "use_fullscreen_button": True,
}

# Configuración HTML adicional
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']
html_favicon = '_static/favicon.ico'
html_title = f"{project} v{release}"
html_short_title = project
html_logo = '_static/logo.png'  # Logo de la documentación

# Configuración de salida PDF (si se usa sphinx-latex)
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    'figure_align': 'htbp',
    'babel': '\\usepackage[spanish]{babel}',
}

# Patrones a excluir
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '../dev',  # Excluye la carpeta dev
    '**/.git',
    '**/.gitignore',
    '**/__pycache__',
    '**/.pytest_cache',
    '**/README.md',  # Excluir READMEs
]

# Idioma y localización
language = 'es'
locale_dirs = ['locale/']
gettext_compact = False
gettext_additional_targets = ['literal-block', 'image']

# Otras configuraciones
html_show_sourcelink = False  # No mostrar enlaces al código fuente
html_show_sphinx = False     # No mostrar el footer de Sphinx
html_copy_source = False     # No copiar archivos fuente RST
html_show_copyright = True   # Mostrar el copyright
html_last_updated_fmt = '%d de %B de %Y'  # Formato de última actualización

# Configuración de búsqueda
html_search_language = 'es'
html_search_options = {
    'type': 'default',
    'dict': None  # Usar diccionario de español predeterminado
}

# Configuración de enlaces externos frecuentes
extlinks = {
    'issue': ('https://github.com/tuorganizacion/proyecto/issues/%s', '#'),
    'pr': ('https://github.com/tuorganizacion/proyecto/pull/%s', 'PR #'),
    'commit': ('https://github.com/tuorganizacion/proyecto/commit/%s', ''),
}

# Configuración de intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# Configuración de graphviz
graphviz_output_format = 'svg'

# Configuración de imgmath
imgmath_image_format = 'svg'
imgmath_font_size = 14

# Archivo de sustituciones
rst_prolog = """
.. include:: /substitutions.rst
"""

# Función para agregar rutas personalizadas
def setup(app):
    # Agregar archivos estáticos personalizados
    app.add_css_file('custom.css')
    app.add_js_file('custom.js')
