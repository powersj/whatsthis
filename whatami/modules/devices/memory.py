"""Memory module."""
from .. import base
from .. import util


class Memory(base.Module):
    """Memory class."""

    def __init__(self):
        """Initialization."""
        super(Memory, self).__init__()

        self.system_total = None
        self.swap_total = None

    def __str__(self):
        """Return system memory count."""
        return '%s system memory' % (self.system_total)

    def discovery(self):
        """Utilize the information in /proc/meminfo.

        For now capture the system and swap totals.
        """
        self.log.debug('Discovering memory...')

        meminfo = util.readfile('/proc/meminfo')
        self.system_total = util.firstmatch(r'MemTotal:\s*(.*) kB',
                                            meminfo, True)
        self.swap_total = util.firstmatch(r'SwapTotal:\s*(.*) kB',
                                          meminfo, True)
