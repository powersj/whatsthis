# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.distro import Distro


class Sysfs(Distro):
    """TODO."""

    @property
    def nodes(self):
        """TODO."""
        return []

    @property
    def node(self, index, attribute):
        """TODO."""
        pass

    @property
    def cpu(self, index, attribute):
        """TODO."""
        pass

    @property
    def cpu_cache(self, index, attribute):
        """TODO."""
        pass
