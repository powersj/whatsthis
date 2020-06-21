#!/usr/bin/env python3
"""Python packaging configuration."""

import os
from setuptools import find_packages, setup

from whatsthis import __author__, __title__, __version__

PWD = os.path.abspath(os.path.dirname(__title__))
REQUIREMENTS_FILE = os.path.join(PWD, "requirements.txt")
REQUIREMENTS = []
with open(REQUIREMENTS_FILE, "r") as req_file:
    REQUIREMENTS = req_file.read().splitlines()

README_FILE = os.path.join(PWD, "README.md")
with open(README_FILE, "r") as readme:
    README_TEXT = readme.read()

setup(
    name=__title__,
    version=__version__,
    description=("Am I in a cloud, on a container, or just plain metal?"),
    long_description=README_TEXT,
    long_description_content_type="text/markdown",
    author=__author__,
    url="https://github.com/powersj/%s" % __title__,
    license="GNU General Public License v3 (GPLv3)",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["%s=%s.__main__:launch" % (__title__, __title__)]
    },
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
    zip_safe=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
