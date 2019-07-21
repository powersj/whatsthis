# This file is part of whatsthis. See LICENSE file for license information.
"""Test __init__.py."""


def test_version():
    """Verify version returns and in correct format."""
    from whatsthis import __version__

    assert __version__
    assert isinstance(__version__, str)
    assert '.' in __version__


def test_features():
    """Verify features is a valid JSON string."""
    from whatsthis import __features__

    assert __features__
    assert isinstance(__features__, dict)
    assert 'subcommands' in __features__
