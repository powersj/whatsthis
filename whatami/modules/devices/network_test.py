"""Test cases for network module.."""
from unittest.mock import patch

from .network import Network, NetworkDevice
from ..base import TestCase


class TestCaseNetwork(TestCase):
    """Network test case."""

    def setUp(self):
        """Set up a network object for testing."""
        self.network = Network()

    @patch('whatami.modules.devices.network.Network._list_devices')
    def test_empty_network(self, mock_list_devices):
        """Test when empty output from meminfo."""
        mock_list_devices.return_value = []
        self.network.discovery()

        assert self.network.adapters == []

    @patch('whatami.modules.devices.network.Network._list_devices')
    def test_local_network(self, mock_list_devices):
        """Test when empty output from meminfo."""
        mock_list_devices.return_value = ['lo']
        self.network.discovery()

        assert self.network.adapters == []

    @patch('os.listdir')
    def test_list_devices_empty(self, mock_listdir):
        """Test listing devices."""
        mock_listdir.return_value = []
        self.network.discovery()
        assert self.network.adapters == []
        assert str(self.network) == ''

    def test_adapters(self):
        """Test adapters."""
        self.network.discovery()
        assert self.network.adapters
        assert str(self.network) != ''


class TestCaseNetworkDevice(TestCase):
    """Network Device test case."""

    def setUp(self):
        """Set up a network device object for testing."""
        self.device = NetworkDevice('')

    @staticmethod
    def test_lo():
        """Test using lo interface."""
        device = NetworkDevice('lo')
        device.discovery()
        assert device.name == 'lo'

    def test_networkdevice_empty(self):
        """Testing emtpy device."""
        assert self.device.name == ''
        assert str(self.device) == '[] None mtu None None'

    @patch('os.path.exists')
    def test_get_type_physical(self, mock_path):
        """Test physical type device."""
        mock_path.return_value = True
        assert self.device._get_type() == 'physical'  # pylint: disable=W0212

    @patch('os.path.exists')
    def test_get_type_bridge(self, mock_path):
        """Test bridge type device."""
        mock_path.side_effect = [False, True]
        assert self.device._get_type() == 'bridge'  # pylint: disable=W0212

    @patch('os.path.exists')
    def test_get_type_empty(self, mock_path):
        """Test unknown type device."""
        mock_path.side_effect = [False, False]
        assert self.device._get_type() == 'unknown'  # pylint: disable=W0212
