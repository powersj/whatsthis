"""Test cases for network module.."""
from unittest.mock import patch

from .network import Network, NetworkDevice
from ..base import TestCase


class TestCaseNetwork(TestCase):
    """Network test case."""

    @patch('whatami.modules.devices.network.Network._get_adapters')
    def test_empty_network(self, mock_list_devices):
        """Test when no adapters."""
        mock_list_devices.return_value = []
        network = Network()
        self.assertEqual(network.adapters, [])

    @patch('whatami.modules.devices.network.Network._list_devices')
    def test_local_network(self, mock_list_devices):
        """Test when only local adapter."""
        mock_list_devices.return_value = ['lo']
        network = Network()
        self.assertEqual(network.adapters, [])

    @patch('os.listdir')
    def test_list_devices_empty(self, mock_listdir):
        """Test listing devices."""
        mock_listdir.return_value = []
        network = Network()
        self.assertEqual(network.adapters, [])
        self.assertIn('No network adapters found', str(network))

    def test_adapters(self):
        """Test adapters."""
        network = Network()
        self.assertIsNotNone(network.adapters)
        self.assertNotIn('No network adapters found', str(network))


class TestCaseNetworkDevice(TestCase):
    """Network Device test case."""

    def test_lo(self):
        """Test using lo interface."""
        device = NetworkDevice('lo')
        self.assertEqual(device.name, 'lo')

    def test_networkdevice_empty(self):
        """Testing emtpy device."""
        device = NetworkDevice('')
        self.assertEqual(device.name, '')
        self.assertIn('unknown', str(device))

    @patch('os.path.exists')
    def test_get_type_physical(self, mock_path):
        """Test physical type device."""
        mock_path.return_value = True
        device = NetworkDevice('')
        self.assertIn('physical', device.type)

    @patch('os.path.exists')
    def test_get_type_bridge(self, mock_path):
        """Test bridge type device."""
        mock_path.side_effect = [False, True]
        device = NetworkDevice('')
        self.assertIn('bridge', device.type)

    @patch('os.path.exists')
    def test_get_type_empty(self, mock_path):
        """Test unknown type device."""
        mock_path.side_effect = [False, False]
        device = NetworkDevice('')
        self.assertIn('unknown', device.type)
