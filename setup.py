#!/usr/bin/env python3
"""TODO."""
import os
from setuptools import setup

NAME = 'whatami'
PWD = os.path.abspath(os.path.dirname(__name__))
METADATA_FILE = os.path.join(PWD, NAME, '__version__.py')

METADATA = {}
with open(METADATA_FILE, 'r') as file:
    exec(file.read(), METADATA)

setup(
    name=NAME,
    version=METADATA['__version__'],
    description=METADATA['__description__'],
    author=METADATA['__author__'],
    author_email=METADATA['__author_email__'],
    url=METADATA['__url__'],
    license=METADATA['__license__'],
    packages=[NAME],
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
