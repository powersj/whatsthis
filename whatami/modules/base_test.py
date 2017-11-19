"""Test cases for base classes."""
from .base import Module, TestCase


class TestCaseUtil(TestCase):
    """Util test case."""
    def setUp(self):
        """Set up a module object for testing."""
        self.module = Module()

    def test_string(self):
        """Test string output."""
        assert '' == str(self.module)
        assert '' == repr(self.module)

    def test_discovery(self):
        """Test discovery method."""
        with self.assertRaises(NotImplementedError):
            self.module.discovery()
