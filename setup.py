#!/usr/bin/env python3
"""
Setup script for LlamaAnki.
This file is provided for backward compatibility with setuptools.
Projects should transition to using pyproject.toml.
"""

from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(    package_dir={"": "src"},
    packages=find_packages(where="src"),
) 