# This file is part of whatsthis. See LICENSE file for license information.
"""Collects the necessary data from a system and produces a tarball.

This sub-command is invoked via:

    whatsthis collect

That command would produce a tarball called
"HOSTNAME-YYYYMMDD-HHMMSS.tar.gz" in the current directory.

The output folder can be changed to a new location using the
`--output-dir` option:

    whatsthis collect --output-dir /tmp

The file would still be called the same, but be placed in the
specified directory.
"""

import datetime
import logging
import os
import platform
import shutil
import tempfile

from whatsthis.collect import proc, sys
from whatsthis.file import copy, dd, exists, tar
from whatsthis.subp import execute


class Collect:
    """Collect /proc and /sys from a system."""

    def __init__(self, output_dir=''):
        """Initialize the collect class.

        Args:
            output_dir: directory to place output in (default: current dir)
        """
        self.tmp_dir = tempfile.mkdtemp(prefix='whatsthis-')

        logging.info('starting collection')
        logging.debug('tempdir: %s', self.tmp_dir)
        self.gather_proc()
        self.gather_sys()

        tar_filename = '%s-%s.tar.gz' % (
            platform.node(),
            datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        )
        tar(self.tmp_dir, os.path.join(output_dir, tar_filename))

        shutil.rmtree(self.tmp_dir)

    def gather_proc(self):
        """Collect specific files from /proc."""
        logging.info('/proc')

        for file_path in proc.FILES:
            if not exists(file_path):
                continue
            copy(file_path, os.path.join(self.tmp_dir, file_path[1:]))

    def gather_sys(self):
        """Collect all of /sys.

        Requires the use of -noleaf due to the odd behavior of sysfs.
        Cannot assume it acts like any other filesystem.
        """
        logging.info('/sys')

        for sys_path in sys.FILES:
            result = execute([
                'find', sys_path, '-noleaf', '-type', 'f', '-perm', '/444'
            ])

            for file_path in sorted(result.split('\n')):
                if 'autosuspend_delay_ms' in file_path:
                    continue
                if 'thermal_zone' in file_path:
                    continue

                dd(file_path, os.path.join(self.tmp_dir, file_path[1:]))
