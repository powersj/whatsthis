"""Storage module.

Meant for storage devices discovered under /sys/block and are
not virtual devices.
"""
import os

from tabulate import tabulate

from .. import base
from .. import util


class Storage(base.Module):
    """Block Storage class."""

    def __init__(self):
        """Initialization."""
        super(Storage, self).__init__()
        self.devices = self._get_devices()

    def __str__(self):
        """Return each storage device found."""
        if not self.devices:
            return 'No storage devices found'

        table = []
        for device in self.devices:
            table.append(str(device).split(' '))
        return tabulate(table)

    def _get_devices(self):
        """Utilize inforamtion in /sys/block.

        Ignores any virtual block devices.
        """
        devices = []
        virtual_devices = self._list_virtual_devices()
        for device in self._list_devices():
            if device in virtual_devices:
                continue
            devices.append(BlockDevice(device))

        return devices

    @staticmethod
    def _list_virtual_devices():
        """List all devices."""
        return os.listdir('/sys/devices/virtual/block')

    @staticmethod
    def _list_devices():
        """List all devices."""
        return os.listdir('/sys/block')

    def to_json(self):
        """Return dictionary like item for JSON output."""
        devices = {}
        for device in self.devices:
            devices[device.name] = device.to_json()

        return {
            "storage": devices
        }


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
        return '%s %s' % (self.name, self.size)

    def _size_from_sectors(self):
        """Read size from /sys/block and convert to human size.

        Linux always considers sectors to be 512 bytes long independently
        of the devices real block size.
        """
        sectors = util.readfile('%s/size' % self.sys_path)

        if not sectors:
            kilobytes = 0
        else:
            kilobytes = int(sectors) / 2

        return util.kilobytes2human(kilobytes)

    def to_json(self):
        """Return dictionary like item for JSON output."""
        return {
            "size": self.size
        }
