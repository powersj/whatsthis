# This file is part of whatsthis. See LICENSE file for license information.
"""Read node data."""

from whatsthis.probes import Probe
from whatsthis.probes.processor.cpu import CPU
from whatsthis.probes.processor.memory import Memory


class Node(Probe):
    """TODO."""

    def __init__(self, path):
        """TODO."""
        super().__init__()

        self.index = self._get_index(path, 'node')
        self.path = path

    @property
    def cpus(self):
        """TODO."""
        cpu_glob = '%s/cpu*[0-9]' % self.path
        return [CPU(self.index, path) for path in self._sysfs_search(cpu_glob)]

    @property
    def memory(self):
        """TODO."""
        path = '%s/meminfo' % self.path
        return Memory(self.index, path)
