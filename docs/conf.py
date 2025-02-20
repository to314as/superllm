"""
Sphinx configuration for SuperLLM documentation.
"""

import os
import sys
from datetime import datetime

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = 'SuperLLM'
copyright = f'{datetime.now().year}, SuperLLM Contributors'
author = 'SuperLLM Contributors'

# Import the package to get the version
import superllm
version = superllm.__version__
release = version

# General configuration
extensions = [
    'sphinx.ext.autodoc',  # Automatically generate API documentation
    'sphinx.ext.napoleon',  # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',  # Add links to highlighted source code
    'sphinx.ext.githubpages',  # Generate .nojekyll file for GitHub Pages
    'sphinx_autodoc_typehints',  # Better type hint support
    'myst_parser',  # Markdown support
]

# Add any paths that contain templates here, relative to this directory
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document
master_doc = 'index'

# Theme configuration
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'titles_only': False,
}

# Add any paths that contain custom static files (such as style sheets)
html_static_path = ['_static']

# These paths are either relative to html_static_path or fully qualified paths
html_css_files = [
    'custom.css',
]

# AutoDoc configuration
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None

# Type hints settings
set_type_checking_flag = True
typehints_fully_qualified = False
always_document_param_types = True 