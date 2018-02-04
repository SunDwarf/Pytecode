#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pytecode documentation build configuration file, created by
# sphinx-quickstart on Sun Feb  4 01:49:35 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import sys

import sphinx_py3doc_enhanced_theme
from pkg_resources import DistributionNotFound, get_distribution

try:
    _release = get_distribution('pytecode')
except DistributionNotFound:
    version = "0.0.0"
    release = "0.0.0"
else:
    version = '.'.join(_release.version.split(".")[:3])
    release = _release.version

try:
    import pytecode
except ImportError:
    sys.path.insert(0, os.path.abspath("../.."))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx_autodoc_typehints',
]

# == Autodoc conf == #
autosummary_generate = True

autoclass_content = 'both'  # include both class docstring and __init__
autodoc_default_flags = [
    # Make sure that any autodoc declarations show the right members
    'members',
    'inherited-members',
    'private-members',
    'show-inheritance',
]
# make autodoc look less... bad
autodoc_member_order = "bysource"


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Pytecode'
copyright = '2018, Laura F. Dickinson'
author = 'Laura F. Dickinson'

# boilerplate
language = None
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------
html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {
    'bodyfont': '"Cabin",Arial,sans-serif',
    'codefont': "'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Monaco', "
                "'Courier New', monospace",
    'googlewebfonturl': 'https://fonts.googleapis.com/css?family=Cabin'
}


html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Pytecodedoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Pytecode.tex', 'Pytecode Documentation',
     'Laura F. Dickinson', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pytecode', 'Pytecode Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Pytecode', 'Pytecode Documentation',
     author, 'Pytecode', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/3.7/': None}
