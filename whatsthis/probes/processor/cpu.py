# This file is part of whatsthis. See LICENSE file for license information.
"""Read cpu data."""

from whatsthis.probes.processor.cache import Cache
from whatsthis.probes import Probe


class CPU(Probe):
    """TODO."""

    def __init__(self, node_index, path):
        """TODO."""
        super().__init__()

        self.index = self._get_index(path, "cpu")
        self.path = path
        self.topology = {
            "node": node_index,
            "socket": self._sysfs_read("%s/topology/physical_package_id" % self.path),
            "core": self._sysfs_read("%s/topology/core_id" % self.path),
            "thread": self._sysfs_read("%s/topology/thread_siblings_list" % self.path)
            .split(",")
            .index(self.index),
        }

        cache_glob = "%s/cache/index*[0-9]" % self.path
        self.cache = [
            Cache(self.index, path) for path in sorted(self._sysfs_search(cache_glob))
        ]

    def __lt__(self, other):
        """TODO."""
        return int(self.index) < int(other.index)

    def __str__(self):
        """TODO."""
        cache = ""
        for level in self.cache:
            cache += " %s" % level

        return "cpu %s: %s/%s/%s%s" % (
            self.index,
            self.topology["socket"],
            self.topology["core"],
            self.topology["thread"],
            cache,
        )
