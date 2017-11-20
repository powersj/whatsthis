"""Processor module."""
from tabulate import tabulate

from .. import base
from .. import util


class Processor(base.Module):
    """Processor class."""

    def __init__(self):
        """Initialization."""
        super(Processor, self).__init__()

        self.cpus = None
        self.model = None
        self.threads_per_core = None
        self.cores_per_socket = None
        self.sockets = None
        self.vendor = None
        self.flags = None

    def __str__(self):
        """Return string with the nubmer and type of processors."""
        table = [
            [self.cpus, self.model]
        ]
        return tabulate(table)

    def discovery(self):
        """Utilize information from /proc/cpuinfo."""
        self.log.debug('Discovering processors...')

        cpuinfo = util.readfile('/proc/cpuinfo')
        self.cpus = cpuinfo.count('processor')
        self.model = util.firstmatch(r'model name.*\s: (.+?)\n', cpuinfo)
