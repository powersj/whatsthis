# This file is part of whatsthis. See LICENSE file for license information.
"""Test __main__.py."""

import logging
from unittest import mock

import pytest

from whatsthis.__main__ import _setup_logging, _verify_platform_support


def test_logging_info():
    """Verify logging level is info."""
    _setup_logging()
    level = logging.getLevelName(logging.root.level)
    assert level == "INFO"


def test_logging_debug():
    """Verify logging level is debug."""
    _setup_logging(debug=True)
    level = logging.getLevelName(logging.root.level)
    assert level == "DEBUG"


@mock.patch("sys.platform")
def test_platform_empty(mock_system):
    """Verify we are on linux platform."""
    mock_system.return_value = ""
    with pytest.raises(SystemExit):
        _verify_platform_support()


@mock.patch("sys.platform")
def test_platform_windows(mock_system):
    """Verify we are on linux platform."""
    mock_system.return_value = "win32"
    with pytest.raises(SystemExit):
        _verify_platform_support()


@mock.patch("sys.platform")
def test_platform_cygwin(mock_system):
    """Verify we are on linux platform."""
    mock_system.return_value = "cygwin"
    with pytest.raises(SystemExit):
        _verify_platform_support()


@mock.patch("sys.platform")
def test_platform_darwin(mock_system):
    """Verify we are on linux platform."""
    mock_system.return_value = "darwin"
    with pytest.raises(SystemExit):
        _verify_platform_support()


@mock.patch("platform.release")
def test_wrong_kernel_2_6(mock_release):
    """Verify we using version greater than 2."""
    mock_release.return_value = "2.6.0"
    with pytest.raises(SystemExit):
        _verify_platform_support()


@mock.patch("platform.release")
def test_wrong_kernel_3(mock_release):
    """Verify we using version greater than 3.5."""
    mock_release.return_value = "3.5.0"
    with pytest.raises(SystemExit):
        _verify_platform_support()


@mock.patch("platform.python_version_tuple")
def test_wrong_python_2_7(mock_python):
    """Verify we using version greater than 2."""
    mock_python.return_value = ("2", "7", "0")
    with pytest.raises(SystemExit):
        _verify_platform_support()


@mock.patch("platform.python_version_tuple")
def test_wrong_python_3_4(mock_python):
    """Verify we using version greater than 3.4."""
    mock_python.return_value = ("3", "4", "0")
    with pytest.raises(SystemExit):
        _verify_platform_support()
