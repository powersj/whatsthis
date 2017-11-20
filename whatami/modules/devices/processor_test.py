"""Test cases for processor module.."""
from unittest.mock import patch

from .processor import Processor
from ..base import TestCase


class TestCaseProcessor(TestCase):
    """Processor test case."""

    def setUp(self):
        """Set up a processor object for testing."""
        self.processor = Processor()

    @patch('whatami.modules.util.readfile')
    def test_empty_cpuinfo(self, mock_readfile):
        """Test when empty output from cpuinfo."""
        mock_readfile.return_value = ''
        self.processor.discovery()

        assert self.processor.cpus == 0
        assert self.processor.model == ''

    @patch('whatami.modules.util.readfile')
    def test_positive(self, mock_readfile):
        """Test typical output from Linux system."""
        mock_readfile.return_value = """
        model name  : Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz
        processor   : 0
        processor   : 1
        processor   : 2
        """
        self.processor.discovery()

        test_count = 3
        test_model = 'Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz'
        print(self.processor)
        assert self.processor.cpus == test_count
        assert self.processor.model == test_model
        self.assertIn('Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz',
                      str(self.processor))
