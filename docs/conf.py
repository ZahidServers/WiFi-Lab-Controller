# -- WiFi-Lab-Controller Documentation Configuration ----------------

import os
import sys
import datetime

# Add project root so autodoc can import modules
sys.path.insert(0, os.path.abspath(".."))

# --- Project information -----------------------------------------------------

project = "WiFi Lab Controller"
author = "Mohammed Zahid Wadiwale"
year = datetime.datetime.now().year
copyright = f"{year}, {author}"
try:
    from wifilab import __version__ as release
except Exception:
    release = "1.2.0"

# --- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = []

# --- HTML output -------------------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_theme_options = {
    "collapse_navigation": False,
    "style_external_links": True,
}

html_logo = None
html_favicon = None

# Make headings like ReadTheDocs style
napoleon_google_docstring = True
napoleon_numpy_docstring = True

# Allow markdown (.md)
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
