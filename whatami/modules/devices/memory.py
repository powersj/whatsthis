"""Memory module."""
from tabulate import tabulate

from .. import base
from .. import util


class Memory(base.Module):
    """Memory class."""

    def __init__(self):
        """Initialization."""
        super(Memory, self).__init__()
        self.system_total = self._get_memory_total()
        self.swap_total = self._get_swap_total()

    def __str__(self):
        """Return system memory count."""
        table = []
        table.append(['System', self.system_total])
        table.append(['Swap', self.swap_total])
        return tabulate(table)

    @staticmethod
    def _get_memory_total():
        """Report total memory value."""
        meminfo = util.readfile('/proc/meminfo')
        memory = util.firstmatch(r'MemTotal:\s*(.*) kB', meminfo, True)
        return util.kilobytes2human(memory)

    @staticmethod
    def _get_swap_total():
        """Report total swap value."""
        meminfo = util.readfile('/proc/meminfo')
        swap = util.firstmatch(r'SwapTotal:\s*(.*) kB', meminfo, True)
        return util.kilobytes2human(swap)
