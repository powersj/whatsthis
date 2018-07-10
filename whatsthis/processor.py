# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.instance import Instance


class Processor(Instance):
    """TODO."""

    def __init__(self, index):
        """TODO."""
        super().__init__()
        self.index = index

    @property
    def cpu(self):
        """TODO."""
        return self.sysfs.node(self.index, 'cpulist')

    @property
    def memory(self):
        """TODO."""
        return self.sysfs.node(self.index, 'meminfo')

    @property
    def numa_distance(self):
        """TODO."""
        return self.sysfs.node(self.index, 'distance')

    @property
    def cache(self):
        """TODO."""
        cache = {}
        for level in self.sysfs.cpu(self.index, 'cache'):
            self.sysfs.cpu_cache(self.index, level, 'type')
            self.sysfs.cpu_cache(self.index, level, 'size')
            self.sysfs.cpu_cache(self.index, level, 'level')

        return cache

    @property
    def cores(self):
        """TODO."""
        return self.sysfs.cpu(self.index, 'toplogy/cores')

    @property
    def flags(self):
        """TODO."""
        return self.proc.cpuinfo

    @property
    def ghz_max(self):
        """TODO."""
        return self.sysfs.cpu(self.index, 'cpufreq/cpuinfo_max_freq')

    @property
    def ghz_min(self):
        """TODO."""
        return self.sysfs.cpu(self.index, 'cpufreq/cpuinfo_min_freq')

    @property
    def model(self):
        """TODO."""
        return self.proc.cpuinfo

    @property
    def threads(self):
        """TODO."""
        return self.sysfs.cpu(self.index, 'toplogy/threads')

    def _scan_cpus(self):
        """TODO."""
        nodes = []
        for index in self.sysfs.nodes:
            nodes.append(index)

        return nodes


class CPU(Processor):
    """TODO."""
