# This file is part of whatsthis. See LICENSE file for license information.
"""Test proc.py."""

from whatsthis.collect.proc import FILES


def test_proc_files():
    """Verify proc has files list."""
    assert FILES
    assert isinstance(FILES, list)
