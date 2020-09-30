# -*- coding: utf-8 -*-

import os
import sys
import importlib
import webbrowser
from urllib.parse import urljoin

import click

from .__version__ import __version__


def validate_python_version(ctx, param, value):
    py_versions = ["3.9", "3.8", "3.7", "3.6"]

    if value not in py_versions:
        raise click.BadParameter("Unsupported Python version!")

    return value


def validate_module_name(ctx, param, value):
    if value is not None:
        module_spec = importlib.util.find_spec(value)
        if module_spec is None:
            raise click.BadParameter(f"No module named {value}!")

    return value


def get_python_version():
    return ".".join([str(sys.version_info.major), str(sys.version_info.minor)])


@click.command("python-doc")
@click.version_option(version=__version__)
@click.option("-m", "--module-name", default=None, callback=validate_module_name, help='Name of the module.')
@click.option(
    "-py", "--python-version", default=get_python_version(), callback=validate_python_version, help='Python version.'
)
@click.option("-w", "--web", is_flag=True, default=False, help='Open page on docs.python.org.')
@click.pass_context
def cli(*args, **kwargs):
    """Open Python docs in the browser."""
    module_name = kwargs["module_name"]
    python_version = kwargs["python_version"]
    web = kwargs["web"]

    if web:
        data_path = "https://docs.python.org/"
        joiner = urljoin
    else:
        cwd = os.path.dirname(__file__)
        data_path = os.path.join(cwd, "data")
        joiner = os.path.join

    if module_name is not None:
        webbrowser.open(
            joiner(data_path, f"{python_version}/library/{module_name}.html"), new=2
        )
    else:
        webbrowser.open(joiner(data_path, f"{python_version}/index.html"), new=2)
