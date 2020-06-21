# This file is part of whatsthis. See LICENSE file for license information.
"""Read cpu cache data."""

from whatsthis.probes import Probe


class Cache(Probe):
    """TODO."""

    def __init__(self, cpu_index, path):
        """TODO.

        path: /sys/devices/system/node/node0/cpu3/cache/index0
        """
        super().__init__()
        self.size = self._sysfs_read("%s/size" % path)
        self.level = self._sysfs_read("%s/level" % path)
        self.type = self._parse_type(path)

    def _parse_type(self, path):
        """TODO.

        Data
        Instruction
        Unified
        Unified
        """
        raw_type = self._sysfs_read("%s/type" % path)
        if raw_type == "Unified":
            return ""
        elif raw_type == "Data":
            return "d"
        elif raw_type == "Instruction":
            return "i"

        return ""

    def __str__(self):
        """TODO."""
        return "L%s%s (%s)" % (self.level, self.type, self.size)
