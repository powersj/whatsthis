"""Test cases for util functions."""
import os

from .base import TestCase
from . import util


class TestCaseUtil(TestCase):
    """Util test case."""

    def test_readfile_nonexistent(self):
        """Test nonexistent file."""
        output = util.readfile('/tmp/fakefile')
        assert '' == output

    def test_readfile(self):
        """Test reading a file."""
        data = 'test data'
        temp_path = util.write_tempfile(data)
        output = util.readfile(temp_path)
        os.unlink(temp_path)

        assert data == output

    def test_kilobytes2human_none(self):
        """Test empty or zero value."""
        result = util.kilobytes2human(0)
        assert '0KB' == result

    def test_kilobytes2human_string_invalid(self):
        """Test string with alphabet charchters."""
        result = util.kilobytes2human('34000KB')
        print(result)
        assert '34.0MB' == result

    def test_kilobytes2human_string(self):
        """Test string, rather than int."""
        result = util.kilobytes2human('10000')
        assert '10.0MB' == result

    def test_kilobytes2human_small(self):
        """Test value less than 1."""
        result = util.kilobytes2human(0.1)
        print(result)
        assert '<1KB' == result

    def test_kilobytes2human_kb(self):
        """Test single kilobyte."""
        result = util.kilobytes2human(1)
        assert '1.0KB' == result

    def test_kilobytes2human_mb(self):
        """Test single megabyte."""
        result = util.kilobytes2human(1000)
        assert '1.0MB' == result

    def test_kilobytes2human_gb(self):
        """Test single gigabyte."""
        result = util.kilobytes2human(1000000)
        assert '1.0GB' == result

    def test_kilobytes2human_tb(self):
        """Test single terabyte."""
        result = util.kilobytes2human(1000000000)
        assert '1.0TB' == result

    def test_kilobytes2human_pb(self):
        """Test single petabyte."""
        result = util.kilobytes2human(1000000000000)
        assert '1.0PB' == result
