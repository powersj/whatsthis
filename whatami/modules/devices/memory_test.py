"""Test cases for memory module."""
from unittest.mock import patch

from .memory import Memory
from ..base import TestCase


class TestCaseMemory(TestCase):
    """Memory test case."""

    def setUp(self):
        """Set up a memory object for testing."""
        self.memory = Memory()

    @patch('whatami.modules.util.readfile')
    def test_empty_meminfo(self, mock_readfile):
        """Test when empty output from meminfo."""
        mock_readfile.return_value = ''
        self.memory.discovery()

        assert self.memory.system_total == -1
        assert self.memory.swap_total == -1

    @patch('whatami.modules.util.readfile')
    def test_positive(self, mock_readfile):
        """Test typical output from Linux system."""
        mock_readfile.return_value = """
        MemTotal:       16380220 kB
        SwapTotal:       2097148 kB
        """
        self.memory.discovery()

        assert self.memory.system_total == 16380220
        assert self.memory.swap_total == 2097148
        assert str(self.memory) == '16380220 system memory'
