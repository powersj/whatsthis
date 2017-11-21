"""Test cases for memory module."""
from unittest.mock import patch

from .memory import Memory
from ..base import TestCase


class TestCaseMemory(TestCase):
    """Memory test case."""

    @patch('whatami.modules.util.readfile')
    def test_empty_meminfo(self, mock_readfile):
        """Test when empty output from meminfo."""
        mock_readfile.return_value = ''
        memory = Memory()
        self.assertEqual(memory.system_total, '0KB')
        self.assertEqual(memory.swap_total, '0KB')
        self.assertIn('0KB', str(memory))

    @patch('whatami.modules.util.readfile')
    def test_positive(self, mock_readfile):
        """Test typical output from Linux system."""
        mock_readfile.return_value = """
        MemTotal:       16380220 kB
        SwapTotal:       2097148 kB
        """
        memory = Memory()
        self.assertEqual(memory.system_total, '16GB')
        self.assertEqual(memory.swap_total, '2GB')
        self.assertIn('16GB', str(memory))
