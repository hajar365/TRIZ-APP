# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TRIZ-APP'
copyright = '2025, hajar el hadri and jouak bouthayna'
author = 'hajar el hadri and jouak bouthayna '
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath('../'))

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_rtd_theme',  # Add this for Read the Docs theme
]

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'  # Use the Read the Docs theme

# -- Other options -----------------------------------------------------------

# This is needed for Read the Docs to render the documentation correctly
html_static_path = ['_static']
