"""Network module."""
import os

from tabulate import tabulate

from .. import base
from .. import util


class Network(base.Module):
    """Network class."""

    def __init__(self):
        """Initialization."""
        super(Network, self).__init__()
        self.order = 300
        self.devices = self._get_devices()

    def __str__(self):
        """Return each device's information."""
        if not self.devices:
            return 'No network devices found'

        table = []
        headers = ['name', 'type', 'mtu', 'mac']
        for adapter in self.devices:
            table.append(str(adapter).split(' '))
        return tabulate(table, headers=headers)

    def _get_devices(self):
        """Get all devices from /sys/class/net."""
        devices = []
        for device in self._list_devices():
            if 'lo' in device:
                continue
            devices.append(NetworkDevice(device))

        return devices

    @staticmethod
    def _list_devices():
        """List all network devices."""
        return os.listdir('/sys/class/net/')

    def to_json(self):
        """Return dictionary like item for JSON output."""
        devices = {}
        for device in self.devices:
            devices[device.name] = device.to_json()

        return {
            "network": devices
        }


class NetworkDevice(object):
    """NetworkDevice class."""

    def __init__(self, device):
        """Initialization."""
        super(NetworkDevice, self).__init__()
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

    def to_json(self):
        """Return dictionary like item for JSON output."""
        return {
            "mac": self.mac,
            "mtu": self.mtu,
            "type": self.type
        }
