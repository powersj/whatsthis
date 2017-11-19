"""Test cases for util functions."""
import os

from .base import TestCase
from . import util


class TestCaseUtil(TestCase):
    """Util test case."""

    @staticmethod
    def test_readfile_nonexistent():
        """Test nonexistent file."""
        result = util.readfile('/tmp/fakefile')
        assert result == ''

    @staticmethod
    def test_readfile():
        """Test reading a file."""
        data = 'test data'
        temp_path = util.write_tempfile(data)
        output = util.readfile(temp_path)
        os.unlink(temp_path)

        assert data == output

    @staticmethod
    def test_kilobytes2human_none():
        """Test empty or zero value."""
        result = util.kilobytes2human(0)
        assert result == '0KB'

    @staticmethod
    def test_kilobytes2human_alphastr():
        """Test string with alphabet charchters."""
        result = util.kilobytes2human('34000KB')
        print(result)
        assert result == '34.0MB'

    @staticmethod
    def test_kilobytes2human_string():
        """Test string, rather than int."""
        result = util.kilobytes2human('10000')
        assert result == '10.0MB'

    @staticmethod
    def test_kilobytes2human_small():
        """Test value less than 1."""
        result = util.kilobytes2human(0.1)
        print(result)
        assert result == '<1KB'

    @staticmethod
    def test_kilobytes2human_kb():
        """Test single kilobyte."""
        result = util.kilobytes2human(1)
        assert result == '1.0KB'

    @staticmethod
    def test_kilobytes2human_mb():
        """Test single megabyte."""
        result = util.kilobytes2human(1000)
        assert result == '1.0MB'

    @staticmethod
    def test_kilobytes2human_gb():
        """Test single gigabyte."""
        result = util.kilobytes2human(1000000)
        assert result == '1.0GB'

    @staticmethod
    def test_kilobytes2human_tb():
        """Test single terabyte."""
        result = util.kilobytes2human(1000000000)
        assert result == '1.0TB'

    @staticmethod
    def test_kilobytes2human_pb():
        """Test single petabyte."""
        result = util.kilobytes2human(1000000000000)
        assert result == '1.0PB'
