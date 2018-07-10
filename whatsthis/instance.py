# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.distro.command import Command
from whatsthis.distro.proc import Proc
from whatsthis.distro.sysfs import Sysfs


class Instance:
    """TODO."""

    def __init__(self):
        """TODO."""
        self.cmd = Command()
        self.proc = Proc()
        self.sysfs = Sysfs()

    @property
    def arch(self):
        """TODO."""
        pass

    @property
    def books(self):
        """TODO."""
        pass

    @property
    def cores(self):
        """TODO."""
        pass

    @property
    def drawers(self):
        """TODO."""
        pass

    @property
    def memory(self):
        """TODO."""
        pass

    @property
    def sockets(self):
        """TODO."""
        pass

    @property
    def threads(self):
        """TODO."""
        pass
