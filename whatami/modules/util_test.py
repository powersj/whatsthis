"""Test cases for util functions."""
import os

from .base import TestCase
from . import util


class TestCaseUtil(TestCase):
    """Util test case."""

    def test_readfile_nonexistent(self):
        """Test nonexistent file."""
        result = util.readfile('fakefile')
        self.assertEqual(result, '')

    def test_readfile(self):
        """Test reading a file."""
        data = 'test data'
        temp_path = util.write_tempfile(data)
        output = util.readfile(temp_path)
        os.unlink(temp_path)
        self.assertEqual(data, output)

    def test_kilobytes2human_none(self):
        """Test empty or zero value."""
        result = util.kilobytes2human(0)
        self.assertEqual(result, '0KB')

    def test_kilobytes2human_alphastr(self):
        """Test string with alphabet charchters."""
        result = util.kilobytes2human('34000KB')
        self.assertEqual(result, '34MB')

    def test_kilobytes2human_string(self):
        """Test string, rather than int."""
        result = util.kilobytes2human('10000')
        self.assertEqual(result, '10MB')

    def test_kilobytes2human_small(self):
        """Test value less than 1."""
        result = util.kilobytes2human(0.1)
        self.assertEqual(result, '<1KB')

    def test_kilobytes2human_kb(self):
        """Test single kilobyte."""
        result = util.kilobytes2human(1)
        self.assertEqual(result, '1KB')

    def test_kilobytes2human_mb(self):
        """Test single megabyte."""
        result = util.kilobytes2human(1000)
        self.assertEqual(result, '1MB')

    def test_kilobytes2human_gb(self):
        """Test single gigabyte."""
        result = util.kilobytes2human(1000000)
        self.assertEqual(result, '1GB')

    def test_kilobytes2human_tb(self):
        """Test single terabyte."""
        result = util.kilobytes2human(1000000000)
        self.assertEqual(result, '1TB')

    def test_kilobytes2human_pb(self):
        """Test single petabyte."""
        result = util.kilobytes2human(1000000000000)
        self.assertEqual(result, '1PB')
