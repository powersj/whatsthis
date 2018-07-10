# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.instance import Instance


class Discovery:
    """TODO."""

    def __init__(self, json=False, data_dir=None):
        """TODO."""
        self.json = json
        self.data_dir = data_dir
        self.instance = Instance()
