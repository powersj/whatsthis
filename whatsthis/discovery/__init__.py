# This file is part of whatsthis. See LICENSE file for license information.
"""Discover the system information.

This can be based on the current system or via specific data
directories.
"""

from importlib import import_module
import logging

from whatsthis.discovery import probes


class Discovery:  # pylint: disable=R0903
    """Do the discovering."""

    def __init__(self, data_dir=None):
        """Initialize discovery."""
        self.data = {}
        logging.info('initializing probes')
        for module_name, class_name in probes.ENABLED.items():
            probe = self._import_probe(module_name, class_name)
            logging.info(probe.name)
            probe(data_dir)

    @staticmethod
    def _import_probe(module_name, class_name):
        """Use importlib to import a specific probe via a module's class."""
        module_object = import_module('whatsthis.probes.%s' % module_name)
        return getattr(module_object, class_name)
