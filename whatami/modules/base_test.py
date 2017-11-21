"""Test cases for base classes."""
from .base import Module, TestCase


class TestCaseModule(TestCase):
    """Module bse test case."""

    def setUp(self):
        """Set up a module object for testing."""
        self.module = Module()

    def test_string(self):
        """Test string output."""
        self.assertEqual(str(self.module), '')
        self.assertEqual(repr(self.module), '')

    def test_json(self):
        """Test assert NotImplementedError."""
        with self.assertRaises(NotImplementedError):
            self.module.to_json()
