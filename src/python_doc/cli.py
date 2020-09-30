# -*- coding: utf-8 -*-

import os
import sys
import importlib
import webbrowser
from urllib.parse import urljoin

from cliche import cli, main

from python_doc.__version__ import __version__


def validate_python_version(value):
    if value not in ["3.9", "3.8", "3.7", "3.6"]:
        raise ValueError("Unsupported Python version!")


def validate_module_name(value):
    if value is not None:
        module_spec = importlib.util.find_spec(value)
        if module_spec is None:
            raise ValueError(f"No module named {value}!")
    return value


def get_python_version():
    return ".".join([str(sys.version_info.major), str(sys.version_info.minor)])


@cli
def run(module_name: str = None, python_version: str = get_python_version(), web=False):
    """
    Open Python docs in the browser.

    :param module_name: Name of the module.
    :param python_version: Python version.
    :param web: Open page on docs.python.org.
    """
    validate_python_version(python_version)
    validate_module_name(module_name)
    if web:
        data_path = "https://docs.python.org/"
        joiner = urljoin
    else:
        cwd = os.path.dirname(__file__)
        data_path = os.path.join(cwd, "data")
        joiner = os.path.join

    if module_name is not None:
        webbrowser.open(joiner(data_path, f"{python_version}/library/{module_name}.html"), new=2)
    else:
        webbrowser.open(joiner(data_path, f"{python_version}/index.html"), new=2)
