# This file is part of whatsthis. See LICENSE file for license information.
"""File module."""

import logging
import os
import tarfile

from whatsthis.subp import execute


def copy(src, dst):
    """Use cp to properly copy a file from /proc."""
    logging.debug('copying %s to %s', src, dst)

    mkdir(os.path.dirname(dst))
    result = execute([
        'cp', '--recursive', '--no-dereference',
        '--preserve=mode,timestamps', '--dereference',
        src, dst
    ])

    if result.failed:
        logging.warning('failed to copy %s to %s', src, dst)
        return False

    return True


def dd(src, dst):  # pylint: disable=invalid-name
    """Use dd to copy a file.

    There are times where dd fails due to a list of reasons. This
    tries to catch the usual list.
    """
    logging.debug('dd %s to %s', src, dst)

    mkdir(os.path.dirname(dst))
    result = execute([
        'dd', 'status=noxfer', 'iflag=nonblock',
        'if=%s' % src,
        'of=%s' % dst
    ])

    if result.failed:
        logging.warning('failed to dd %s to %s', src, dst)
        return False

    return True


def exists(src):
    """Boolean if file exists."""
    return os.path.exists(src)


def remove(src):
    """Attempt to remove a file, do nothing if it fails."""
    logging.debug('removing %s', src)

    try:
        os.remove(src)
    except FileNotFoundError:
        pass


def mkdir(dirname):
    """Use to make multiple directories at once."""
    logging.debug('creating %s', dirname)

    if not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)


def tar(src, dst):
    """Tar up the collected directories.

    This produces a tarball with only the subdirectories that were
    produces in the temporary directory.
    """
    logging.debug('compressing data in %s', src)

    with tarfile.open(dst, "w:gz") as archive:
        for subdir in [f for f in os.walk(src)][0][1]:
            archive.add(os.path.join(src, subdir), arcname=subdir)

    logging.info('wrote %s', dst)
