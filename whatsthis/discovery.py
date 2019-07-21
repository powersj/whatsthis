# This file is part of whatsthis. See LICENSE file for license information.
"""Discover the system information.

This can be based on the current system or via specific data
directories.
"""


class Discovery:  # pylint: disable=R0903
    """Do the discovering."""

    def __init__(self, json=False, data_dir=None):
        """Initialize discovery."""
        self.json = json
        self.data_dir = data_dir
