"""Test cases for storage module.."""
from unittest.mock import patch

from .storage import Storage, BlockDevice
from ..base import TestCase


class TestCaseStorage(TestCase):
    """Storage test case."""

    def test_storage(self):
        """Test storage."""
        storage = Storage()
        self.assertIsNotNone(storage.devices)
        self.assertNotIn(str(storage), 'No storage devices found')

    @patch('whatami.modules.devices.storage.Storage._list_devices')
    def test_no_storage(self, mock_devices):
        """Test no storage."""
        mock_devices.return_value = []
        storage = Storage()
        expected_json = {'storage': {}}
        self.assertEqual(storage.devices, [])
        self.assertIn(str(storage), 'No storage devices found')
        self.assertEqual(storage.to_json(), expected_json)


class TestCaseBlockDevice(TestCase):
    """Block Device test case."""

    @patch('whatami.modules.util.readfile')
    def test_size_from_sectors(self, mock_readfile):
        """Test converting size from sectors."""
        mock_readfile.return_value = '1953525168'
        device = BlockDevice('')
        self.assertEqual(device.size, "977GB")

    @patch('whatami.modules.util.readfile')
    def test_size_from_sectors_empty(self, mock_readfile):
        """Test converting size from sectors."""
        mock_readfile.return_value = ''
        device = BlockDevice('')
        self.assertEqual(device.size, "0KB")
