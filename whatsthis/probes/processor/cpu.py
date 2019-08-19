# This file is part of whatsthis. See LICENSE file for license information.
"""Read cpu data."""

from whatsthis.probes import Probe


class CPU(Probe):
    """TODO."""

    def __init__(self, node_index, path):
        """TODO."""
        super().__init__()

        self.node_index = node_index
        self.index = self._get_index(path, 'cpu')
        self.path = path

    def __lt__(self, other):
        """TODO."""
        return self.index < other.index

    @property
    def core_id(self):
        """TODO."""
        return self._sysfs_read('%s/topology/core_id' % self.path)
