# conf.py

project = "Documentación de Comercio Exterior"
author = "Equipo de Comercio Exterior"
release = "1.0.0"

extensions = [
    # Extensión para admitir MyST (Markdown), en caso de seguir con .md
    "myst_parser",
    # Extensiones comunes de Sphinx
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',  # Solo si usas MyST
}

# Tema
html_theme = "sphinx_rtd_theme"

# Otras configuraciones
html_theme_options = {
    "canonical_url": "",
    "analytics_id": "",
    "logo_only": False,
}

# Paths
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
