# python-library-template
A simple template for packaging custom python libraries

## About

This is a deliberately barebones template project for building custom python libraries. There are many roads up this particular mountain and this is one of them. Consider carefully if this approach is suitable for your needs.

The `example_module` directory contains code to build a library of the same name, using the Poetry package manager, configured via `pyproject.toml`. The chosen python version for this example is 3.9.

Ensure both python and poetry are installed.

## Building

1. Change to the module directory and create (and activate) a python virtual environment for isolation

```sh
cd example_library
python -m venv .venv
source .venv/bin/activate 
```

1. Build the project via poetry

```sh
poetry install && poetry build
```

1. This will output build libraries to `/dist`. To try them out, pip install them into your virtual environment

```sh
pip install dist/example_library-0.1.0-py3-none-any.whl
```

1. Finally test it using the `example_usage.py` script provided

```sh
cd ..
python example_usage.py
```