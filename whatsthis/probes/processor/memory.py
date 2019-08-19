# This file is part of whatsthis. See LICENSE file for license information.
"""Read memory data."""

from whatsthis.probes import Probe


class Memory(Probe):
    """TODO."""

    def __init__(self, node_index, path):
        """TODO."""
        super().__init__()

        self.node_index = node_index
        self.path = path
        self.meminfo = self._sysfs_read(self.path).split('\n')

    @property
    def total(self):
        """TODO."""
        return self._search_meminfo('MemTotal')

    def _search_meminfo(self, key):
        """TODO."""
        for row in self.meminfo:
            if key in row:
                # '16180508kB'
                return ''.join(row.split(' ')[-2:])

        return '0kB'
