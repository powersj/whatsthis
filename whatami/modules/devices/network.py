"""Network module."""
import logging
import os

from .. import base
from .. import util


class Network(base.Module):
    """Network class."""

    def __init__(self):
        """Initialization."""
        super(Network, self).__init__()

        self.adapters = []

    def __str__(self):
        """Return each adapter's information."""
        string = ''
        for adapter in self.adapters:
            string = '%s\n%s' % (string, adapter)
        return string

    def discovery(self):
        """Utilize the information in /sys/class/net.

        Walks those devices, with the exception of the 'lo' device.
        """
        self.log.debug('Discovering network...')
        for device in os.listdir('/sys/class/net/'):
            if 'lo' in device:
                continue
            self.adapters.append(NetworkDevice(device))


class NetworkDevice(object):
    """NetworkDevice class."""

    def __init__(self, device):
        """Initialization."""
        super(NetworkDevice, self).__init__()
        self.log = logging.getLogger(name=__name__)
        self.name = device
        self.sys_path = '/sys/class/net/%s' % device
        self.mac = None
        self.mtu = None
        self.type = None

    def __str__(self):
        """Return basic information about a network deivce."""
        return '[%s] %s mtu %s %s' % (self.name, self.type, self.mtu,
                                      self.mac)

    def discovery(self):
        """Go through the device files in /sys/class/net/device."""
        self.mac = util.readfile('%s/address' % self.sys_path)
        self.mtu = util.readfile('%s/mtu' % self.sys_path)

        if os.path.exists('%s/device' % self.sys_path):
            self.type = 'physical'
        elif os.path.exists('%s/bridge' % self.sys_path):
            self.type = 'bridge'
        else:
            self.type = 'unknown'
