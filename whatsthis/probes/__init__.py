# This file is part of whatsthis. See LICENSE file for license information.
"""Initialize probes."""

import glob
import os
import platform

from whatsthis.subp import execute


class Probe:
    """Base probe class."""

    name = 'Unknown'

    def __init__(self, data_dir=None):
        """Initialize probe."""
        self.data_dir = data_dir
        # x86_64, aarch64, ppc64le, s390x
        self.arch = platform.machine()

    @staticmethod
    def _get_index(path, pattern):
        """TODO."""
        return os.path.basename(path).replace(pattern, '')

    @staticmethod
    def _human_units(value):
        """TODO."""
        if value.endswith('kB'):
            value = str(int(int(value.rstrip('kB')) / 1000 / 1000)) + 'GB'
        return value

    @staticmethod
    def _sysfs_search(pattern):
        """Search for matches in sysfs."""
        return glob.glob(pattern)

    @staticmethod
    def _sysfs_read(path):
        """Read file from sysfs."""
        return execute(['cat', path])
