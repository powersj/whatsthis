"""Base module for base classes.

Module base class to be used by all modules.

TestCase base class to be used by all tests.
"""
import logging
import unittest


class Module(object):
    """Module base class."""

    def __init__(self):
        """Set up logging for each."""
        self.log = logging.getLogger(name=self.__class__.__name__)
        self.order = 100000

    def __str__(self):
        """By default return an empty string."""
        return ''

    def __repr__(self):
        """By default return whatever __str__ has instead of useless object."""
        return self.__str__()

    def to_json(self):
        """Return dictionary like item for JSON output."""
        raise NotImplementedError


class TestCase(unittest.TestCase):
    """TestCase base class."""

    def shortDescription(self):
        """Override the use of the docstring by the unittest class.

        This will result in output the following format:
        method_name (test_class)
        """
        return None
