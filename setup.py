#!/usr/bin/env python3
"""Python packaging configuration."""
import os
from setuptools import setup

NAME = 'whatami'
PWD = os.path.abspath(os.path.dirname(__name__))

METADATA_FILE = os.path.join(PWD, NAME, '__init__.py')
METADATA = {}
with open(METADATA_FILE, 'r') as init_file:
    exec(init_file.read(), METADATA)

REQUIREMENTS_FILE = os.path.join(PWD, 'requirements.txt')
REQUIREMENTS = []
with open(REQUIREMENTS_FILE, 'r') as req_file:
    REQUIREMENTS = req_file.read().splitlines()

setup(
    name=NAME,
    version=METADATA['__version__'],
    description=METADATA['__description__'],
    author=METADATA['__author__'],
    author_email=METADATA['__author_email__'],
    url=METADATA['__url__'],
    license=METADATA['__license__'],
    packages=[NAME],
    install_requires=REQUIREMENTS,
    zip_safe=True,
    entry_points={
        'console_scripts': ['%s=%s' % (NAME, NAME)]
    },
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: System :: Hardware',
        'Topic :: System :: Operating System Kernels :: Linux',
        'Topic :: Utilities',
    )
)
