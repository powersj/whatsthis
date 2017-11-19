"""Test cases for network module.."""
from unittest.mock import patch

from .network import Network
from ..base import TestCase


class TestCaseNetwork(TestCase):
    """Network test case."""

    def setUp(self):
        """Set up a network object for testing."""
        self.network = Network()

    @patch('os.listdir')
    def test_empty_network(self, mock_readfile):
        """Test when empty output from meminfo."""
        mock_readfile.return_value = []
        self.network.discovery()

        assert self.network.adapters == []
