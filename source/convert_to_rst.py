import os
import subprocess

def convert_md_to_rst(docs_md_path):
    """
    Convierte archivos Markdown a reStructuredText usando Pandoc.

    Args:
        docs_md_path: Ruta al directorio que contiene los archivos Markdown.
    """
    for root, _, files in os.walk(docs_md_path):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                rst_path = os.path.splitext(md_path)[0] + ".rst"
                try:
                    subprocess.run(
                        ["pandoc", "-f", "markdown", "-t", "rst", md_path, "-o", rst_path],
                        check=True,
                    )
                    print(f"Convertido: {md_path} a {rst_path}")
                except subprocess.CalledProcessError as e:
                    print(f"Error al convertir {md_path}: {e}")


if __name__ == "__main__":
    docs_md_directory = "docs_md"  # Ajusta la ruta si es necesario
    convert_md_to_rst(docs_md_directory) 