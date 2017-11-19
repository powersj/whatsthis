"""Test cases for storage module.."""
from unittest.mock import patch

from .storage import Storage, BlockDevice
from ..base import TestCase


class TestCaseStorage(TestCase):
    """Storage test case."""

    def setUp(self):
        """Set up a storage object for testing."""
        self.storage = Storage()

    def test_storage(self):
        """Test storage."""
        self.storage.discovery()
        assert self.storage.devices
        assert str(self.storage) != ''

    @patch('whatami.modules.devices.storage.Storage._list_devices')
    def test_no_storage(self, mock_devices):
        """Test no storage."""
        mock_devices.return_value = []
        self.storage.discovery()
        assert not self.storage.devices
        assert str(self.storage) == ''


class TestCaseBlockDevice(TestCase):
    """Block Device test case."""

    def setUp(self):
        """Set up a block device object for testing."""
        self.device = BlockDevice('')

    @patch('whatami.modules.util.readfile')
    def test_size_from_sectors(self, mock_readfile):
        """Test converting size from sectors."""
        mock_readfile.return_value = '1953525168'
        size = self.device._size_from_sectors()  # pylint: disable=W0212
        print(size)
        assert size == "976.76GB"
