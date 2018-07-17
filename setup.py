#!/usr/bin/env python3
"""Python packaging configuration."""

import os
from setuptools import find_packages, setup

import whatsthis

PWD = os.path.abspath(os.path.dirname(__name__))
REQUIREMENTS_FILE = os.path.join(PWD, 'requirements.txt')
REQUIREMENTS = []
with open(REQUIREMENTS_FILE, 'r') as req_file:
    REQUIREMENTS = req_file.read().splitlines()

README_FILE = os.path.join(PWD, 'README.md')
with open(README_FILE, 'r') as readme:
    README_TEXT = readme.read()

setup(
    name='whatsthis',
    version=whatsthis.__version__,
    description=('Am I in a cloud, on a container, or just plain metal?'),
    long_description=README_TEXT,
    long_description_content_type='text/markdown',
    author='Joshua Powers',
    url='https://github.com/powersj/whatsthis',
    license='GNU General Public License v3 (GPLv3)',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['whatsthis=whatsthis.__main__:launch']
    },
    python_requires='>=3.4',
    install_requires=REQUIREMENTS,
    zip_safe=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
