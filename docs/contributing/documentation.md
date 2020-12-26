# Documentation

The documentation is built with [MkDocs](https://www.mkdocs.org/) and the
[Material for MkDocs theme](https://squidfunk.github.io/mkdocs-material/) and
is written in Markdown.

## Building

To build the documentation site, first setup a Python virtual environment and
install the mkdocs-material package, which will pull in all other dependencies:

```shell
virtualenv .venv
. .venv/bin/activate
pip install mkdocs-material
```

To build the docs, use the makefile target:

```shell
make docs
```

Launch a web server to pull up the docs and then point a browser at
[http://0.0.0.0:8000/](http://0.0.0.0:8000/) to view the site:

```shell
python3 -m http.server --directory site/
```
