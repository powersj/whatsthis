"""Network module."""
import logging
import os

from tabulate import tabulate

from .. import base
from .. import util


class Network(base.Module):
    """Network class."""

    def __init__(self):
        """Initialization."""
        super(Network, self).__init__()
        self.log.debug('Discovering network...')
        self.adapters = self._get_adapters()

    def __str__(self):
        """Return each adapter's information."""
        if not self.adapters:
            return 'No network adapters found'

        table = []
        for adapter in self.adapters:
            table.append(str(adapter).split(' '))
        return tabulate(table)

    def _get_adapters(self):
        """Get all adapters from /sys/class/net."""
        adapters = []
        for device in self._list_devices():
            if 'lo' in device:
                continue
            adapters.append(NetworkDevice(device))

        return adapters

    @staticmethod
    def _list_devices():
        """List all network devices."""
        return os.listdir('/sys/class/net/')


class NetworkDevice(object):
    """NetworkDevice class."""

    def __init__(self, device):
        """Initialization."""
        super(NetworkDevice, self).__init__()
        self.log = logging.getLogger(name=__name__)
        self.name = device
        self.sys_path = '/sys/class/net/%s' % device
        self.mac = self._get_mac()
        self.mtu = self._get_mtu()
        self.type = self._get_type()

    def __str__(self):
        """Return basic information about a network deivce."""
        return '%s %s %s %s' % (self.name, self.type, self.mtu, self.mac)

    def _get_mac(self):
        """Return MAC Address of interface."""
        return util.readfile('%s/address' % self.sys_path)

    def _get_mtu(self):
        """Return MTU of interface."""
        return util.readfile('%s/mtu' % self.sys_path)

    def _get_type(self):
        """Return type of interface."""
        if os.path.exists('%s/device' % self.sys_path):
            return 'physical'
        elif os.path.exists('%s/bridge' % self.sys_path):
            return 'bridge'

        return 'unknown'
