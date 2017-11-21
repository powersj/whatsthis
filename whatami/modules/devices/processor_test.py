"""Test cases for processor module.."""
from unittest.mock import patch

from .processor import Processor
from ..base import TestCase


class TestCaseProcessor(TestCase):
    """Processor test case."""

    @patch('whatami.modules.util.readfile')
    @staticmethod
    def test_empty_cpuinfo(mock_readfile):
        """Test when empty output from cpuinfo."""
        mock_readfile.return_value = ''
        processor = Processor()

        assert processor.cpus == 0
        assert processor.model == ''

    @patch('whatami.modules.util.readfile')
    def test_positive(self, mock_readfile):
        """Test typical output from Linux system."""
        mock_readfile.return_value = """
        model name  : Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz
        processor   : 0
        processor   : 1
        processor   : 2
        """
        processor = Processor()

        test_count = 3
        test_model = 'Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz'
        assert processor.cpus == test_count
        assert processor.model == test_model
        self.assertIn('Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz',
                      str(processor))
