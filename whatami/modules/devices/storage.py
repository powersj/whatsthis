"""Storage module.

Meant for storage devices discovered under /sys/block and are
not virtual devices.
"""
import os

from .. import base
from .. import util


class Storage(base.Module):
    """Block Storage class."""

    def __init__(self):
        """Initialization."""
        super(Storage, self).__init__()

        self.devices = []

    def __str__(self):
        """Return each storage device found."""
        msg = ''
        for device in self.devices:
            msg = '%s\n%s' % (msg, device)
        return msg

    def discovery(self):
        """Utilize inforamtion in /sys/block.

        Ignores any virtual block devices.
        """
        self.log.debug('Discovering storage...')

        virtual_devices = os.listdir('/sys/devices/virtual/block')
        for device in os.listdir('/sys/block'):
            if device in virtual_devices:
                continue
            self.devices.append(BlockDevice(device))


class BlockDevice(object):
    """Disk Storage class."""

    def __init__(self, name):
        """Initialization."""
        super(BlockDevice, self).__init__()
        self.name = name
        self.sys_path = '/sys/block/%s' % self.name
        self.size = self._size_from_sectors()

    def __str__(self):
        """Return each block device and size."""
        return '[%s] %s' % (self.name, self.size)

    def _size_from_sectors(self):
        """Read size from /sys/block and convert to human size.

        Linux always considers sectors to be 512 bytes long independently
        of the devices real block size.
        """
        sectors = util.readfile('%s/size' % self.sys_path)
        kilobytes = int(sectors) / 2
        return util.kilobytes2human(kilobytes)


class Partition(object):
    """Partition class."""

    def __init__(self, name):
        """Initialization."""
        super(Partition, self).__init__()

        self.name = name
        self.size = None
        self.filesystem = None
        self.flags = None

    def __str__(self):
        """Return each partition with size."""
        return '[%s] %s' % (self.name, self.size)

    def discovery(self):
        """TODO."""
        pass
