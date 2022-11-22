# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import joyrl
import sphinx_rtd_theme

project = 'JoyRL'
copyright = '2022, johnjim0816'
author = 'johnjim0816'
release = joyrl.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    # 'sphinx.ext.imgmath',
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinxcontrib.bibtex",
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = ['.rst']
master_doc = 'index'

autodoc_default_options = {
    "special-members":
    ", ".join(
        [
            "__len__",
            "__call__",
            "__getitem__",
            "__setitem__",
            # "__getattr__",
            # "__setattr__",
        ]
    )
}

autodoc_member_order = "bysource"
bibtex_bibfiles = ['refs.bib']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ["_static"]

def setup(app):
    app.add_js_file("https://cdn.jsdelivr.net/npm/vega@5.20.2")
    app.add_js_file("https://cdn.jsdelivr.net/npm/vega-lite@5.1.0")
    app.add_js_file("https://cdn.jsdelivr.net/npm/vega-embed@6.17.0")

    # app.add_js_file("js/copybutton.js")
    app.add_js_file("js/benchmark.js")
    app.add_css_file("css/style.css")
