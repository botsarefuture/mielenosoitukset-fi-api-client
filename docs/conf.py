# Configuration file for the Sphinx documentation builder.

import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------

project = 'Demonstration API Client'
author = 'Verso Vuorenmaa'
copyright = f'{datetime.now().year}, {author}'
release = '1.0.0'
version = release

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Automatic API documentation
    'sphinx.ext.napoleon',  # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',  # Add links to the source code
    'sphinx.ext.autosummary',  # Auto-generate summary tables
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # You can use 'sphinx_rtd_theme' for a ReadTheDocs theme
html_static_path = ['_static']
html_logo = '_static/logo.png'  # Optional: Add a logo if you have one
html_favicon = '_static/favicon.ico'  # Optional: Add a favicon if you have one

# -- Options for autodoc -----------------------------------------------------

autodoc_member_order = 'bysource'

# -- Options for Napoleon ----------------------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True
