#!/usr/bin/env python3
""" Setup.py """

import os
import sys

from setuptools import find_packages, setup

sys.path.append(os.path.abspath("src"))
# pylint: disable=wrong-import-position

setup(
    name="gemeindeverzeichnis",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    scripts=["src/manage.py"],
    author="Integreat App Project",
    author_email="info@integreat-app.de",
    description="Gemeindeverzeichnis",
    license="Apache2.0",
    keywords="Gemeindeverzeichnis",
    url="http://github.com/Integreat/gemeindeverzeichnis-django",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
    ],
)
