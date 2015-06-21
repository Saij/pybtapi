#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
import pybtapi

setup(
    name                    = "pybtapi",
    version                 = pybtapi.__version__,
    author                  = "Christoph Friedrich",
    tests_require           = [],
    install_requires        = ["pybluez"],
    scripts                 = [],
    author_email            = "christoph@christophfriedrich.de",
    description             = "A simple Bluetooth API interface",
    packages                = find_packages(),
    include_package_data    = True,
    platforms               = "any",
)
