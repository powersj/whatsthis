"""Test cases for processor module.."""
from unittest.mock import patch

from .processor import Processor
from ..base import TestCase


class TestCaseProcessor(TestCase):
    """Processor test case."""

    @patch('whatami.modules.util.readfile')
    def test_empty_cpuinfo(self, mock_readfile):
        """Test when empty output from cpuinfo."""
        mock_readfile.return_value = ''
        processor = Processor()
        expected_json = {'processor': {'qty': 0, 'model': ''}}
        self.assertEqual(processor.cpus, 0)
        self.assertEqual(processor.model, '')
        self.assertEqual(processor.to_json(), expected_json)

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
        test_model = 'Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz'
        self.assertEqual(processor.cpus, 3)
        self.assertEqual(processor.model, test_model)
        self.assertIn(test_model, str(processor))
