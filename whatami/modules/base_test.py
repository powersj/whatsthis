"""Test cases for base classes."""
from .base import Module, TestCase


class TestCaseModule(TestCase):
    """Module bse test case."""

    def setUp(self):
        """Set up a module object for testing."""
        self.module = Module()

    def test_string(self):
        """Test string output."""
        assert str(self.module) == ''
        assert repr(self.module) == ''
