# This file is part of whatsthis. See LICENSE file for license information.
"""Test file.py."""

import os
from tempfile import TemporaryDirectory

from whatsthis import file


def test_copy():
    """Test copying a file."""
    with TemporaryDirectory(prefix="whatsthis-test-copy") as tmp_dir:
        new = os.path.join(tmp_dir, "test")
        prime = os.path.join(tmp_dir, "prime")
        os.mknod(new)
        assert file.copy(new, prime)
        assert file.exists(prime)


def test_copy_fail():
    """Test fail copying a file."""
    with TemporaryDirectory(prefix="whatsthis-test-copy") as tmp_dir:
        prime = os.path.join(tmp_dir, "prime")
        assert not file.copy("fakefile", prime)
        assert not file.exists(prime)


def test_dd():
    """Test dd a file."""
    with TemporaryDirectory(prefix="whatsthis-test-dd") as tmp_dir:
        new = os.path.join(tmp_dir, "test")
        prime = os.path.join(tmp_dir, "prime")
        os.mknod(new)
        assert file.dd(new, prime)
        assert file.exists(prime)


def test_dd_fail():
    """Test fail dd a file."""
    with TemporaryDirectory(prefix="whatsthis-test-dd") as tmp_dir:
        prime = os.path.join(tmp_dir, "prime")
        assert not file.dd("fakefile", prime)
        assert not file.exists(prime)


def test_exists_fake_file():
    """Remove fake file."""
    file.exists("fake_file")


def test_remove_fake_file():
    """Remove fake file."""
    file.remove("fake_file")


def test_mkdir():
    """Make a directory."""
    with TemporaryDirectory(prefix="whatsthis-test-mkdir") as tmp_dir:
        file.mkdir(os.path.join(tmp_dir, "mkdir"))


def test_tar():
    """Test tar directory."""
    with TemporaryDirectory(prefix="whatsthis-test-mkdir") as tmp_dir:
        new = os.path.join(tmp_dir, "test")
        subdir = os.path.join(new, "subtest")
        tar = os.path.join(tmp_dir, "new.tar.gz")
        file.mkdir(new)
        file.mkdir(subdir)
        file.tar(new, tar)
        assert file.exists(tar)
