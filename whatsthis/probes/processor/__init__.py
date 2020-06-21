# This file is part of whatsthis. See LICENSE file for license information.
"""CPU probe."""

import logging

from whatsthis.probes import Probe
from whatsthis.probes.processor.node import Node


class Processor(Probe):
    """Launch processor class."""

    name = "processor"
    data = {}

    def __init__(self, data_dir):
        """Initialize processor probe."""
        super().__init__(data_dir)

        for node in self.nodes:
            logging.info("node: %s", node.index)
            logging.info("\tmemory: %s", self._human_units(node.memory.total))
            for cpu in sorted(node.cpus):
                logging.info("\t%s", cpu)

    @property
    def nodes(self):
        """Find all system nodes."""
        node_glob = "/sys/devices/system/node/node*"
        return [Node(path) for path in self._sysfs_search(node_glob)]
