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
import tarfile
import tempfile

from whatsthis.util import execute

PROC_FILES = [
    '/proc/buddyinfo',
    '/proc/cmdline',
    '/proc/cpuinfo',
    '/proc/crypto',
    '/proc/devices',
    '/proc/diskstats',
    '/proc/interrupts',
    '/proc/iomem',
    '/proc/mdstat',
    '/proc/meminfo',
    '/proc/misc',
    '/proc/modules',
    '/proc/mounts',
    '/proc/net/vlan',
    '/proc/net/bonding',
    '/proc/partitions',
    '/proc/sched_debug',
    '/proc/schedstat',
    '/proc/scsi/scsi',
    '/proc/scsi/sg/device_strs',
    '/proc/stat',
    '/proc/swaps',
    '/proc/version',
    '/proc/zoneinfo'
]


class Collect:
    """Collect /proc and /sys from a system."""

    def __init__(self, output_dir=''):
        """Initialize the collect class.

        Args:
            output_dir: directory to place output in (default: current dir)
        """
        self._log = logging.getLogger(__name__)
        self.tmp_dir = tempfile.mkdtemp(prefix='whatsthis-')
        self._log.debug('tempdir: %s', self.tmp_dir)

        self.collect()
        self.tar_output(output_dir)
        shutil.rmtree(self.tmp_dir)

    def collect(self):
        """Collect data."""
        self._log.info('starting collection')
        self.gather_proc()
        self.gather_sys()

    def gather_proc(self):
        """Collect specific files from /proc."""
        self._log.info('/proc')

        for file_path in PROC_FILES:
            self._copy_file(file_path)

    def gather_sys(self):
        """Collect all of /sys.

        Requires the use of -noleaf due to the odd behavior of sysfs.
        Cannot assume it acts like any other filesystem.
        """
        self._log.info('/sys')

        out, _, _ = execute([
            'find', '/sys', '-noleaf', '-type', 'f', '-perm', '/444'
        ])

        for file_path in sorted(out.split('\n')):
            if file_path.startswith('/sys/kernel') or 'cgroup' in file_path:
                continue

            self._dd_file(file_path)

    def tar_output(self, output_dir):
        """Tar up the collected directories.

        This produces a tarball with only the subdirectories that were
        produces in the temporary directory.
        """
        self._log.info('compressing data')
        tar_filename = '%s-%s.tar.gz' % (
            platform.node(),
            datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        )
        tar_path = os.path.join(output_dir, tar_filename)

        with tarfile.open(tar_path, "w:gz") as tar:
            for subdir in [f for f in os.walk(self.tmp_dir)][0][1]:
                tar.add(os.path.join(self.tmp_dir, subdir), arcname=subdir)

        self._log.info('wrote %s', tar_path)

    def _copy_file(self, file_path):
        """Use cp to properly copy a file from /proc."""
        self._log.debug(file_path)
        self._make_parent_dir(file_path)

        _, err, return_code = execute([
            'cp', '--recursive', '--no-dereference',
            '--preserve=mode,timestamps', '--dereference', '--parents',
            file_path, self.tmp_dir
        ])

        if return_code != 0:
            if 'No such file or directory' not in err:
                self._log.warning('failed to copy %s', file_path)
                return False

        return True

    def _dd_file(self, file_path):
        """Use dd to copy a file.

        There are times where dd fails due to a list of reasons. This
        tries to catch the usual list.
        """
        self._log.debug(file_path)
        self._make_parent_dir(file_path)
        filename = os.path.join(self.tmp_dir, file_path[1:])

        _, err, return_code = execute([
            'dd', 'status=noxfer', 'iflag=nonblock',
            'if=%s' % file_path,
            'of=%s' % filename
        ])

        if return_code != 0:
            if 'Input/output error\n0+0 records in\n0+0 records out' in err:
                self._remove_file(filename)
            elif 'Permission denied' in err:
                self._remove_file(filename)
            elif 'No data available' in err:
                self._remove_file(filename)
            elif 'Operation not supported' in err:
                self._remove_file(filename)
            elif 'Invalid argument' in err:
                self._remove_file(filename)
            elif 'No such device' in err:
                self._remove_file(filename)
            elif 'Operation not permitted' in err:
                self._remove_file(filename)
            else:
                self._log.warning('failed to dd %s', file_path)
                print(err)
                return False

        return True

    def _make_parent_dir(self, file_path):
        """Use to make multiple directories at once."""
        parent_dir = os.path.dirname(
            os.path.join(self.tmp_dir, file_path[1:])
        )
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)

    @staticmethod
    def _remove_file(filename):
        """Attempt to remove a file, do nothing if it fails."""
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass
