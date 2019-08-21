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

    def __str__(self):
        """TODO."""
        return 'cpu %s: %s/%s/%s' % (
            self.index, self.socket_index, self.core_index, self.thread_index
        )

    @property
    def socket_index(self):
        """TODO."""
        return self._sysfs_read('%s/topology/physical_package_id' % self.path)

    @property
    def core_index(self):
        """TODO."""
        return self._sysfs_read('%s/topology/core_id' % self.path)

    @property
    def thread_index(self):
        """TODO."""
        siblings = self._sysfs_read(
            '%s/topology/thread_siblings_list' % self.path
        )
        return siblings.split(',').index(self.index)
