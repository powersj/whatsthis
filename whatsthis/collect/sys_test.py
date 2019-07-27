# This file is part of whatsthis. See LICENSE file for license information.
"""Test sys.py."""

from whatsthis.collect.sys import FILES


def test_sys_files():
    """Verify sys has files list."""
    assert FILES
    assert isinstance(FILES, list)
