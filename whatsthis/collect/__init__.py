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

from whatsthis.file import copy, dd, exists, tar
from whatsthis.subp import execute

COMMANDS = {
    "lsblk": "lsblk",
    "ip a": "ip_a",
    "lscpu": "lscpu",
    "lshw -short": "lshw",
    "lshw -json": "lshw.json",
    "lsipc": "lsipc",
    "lsmem": "lsmem",
    "lspci": "lspci",
    "lspci -vv": "lspci_vv",
    "blkid -o export": "blkid"
}

PROC_FILES = [
    "/proc/buddyinfo",
    "/proc/cmdline",
    "/proc/cpuinfo",
    "/proc/crypto",
    "/proc/devices",
    "/proc/diskstats",
    "/proc/interrupts",
    "/proc/iomem",
    "/proc/mdstat",
    "/proc/meminfo",
    "/proc/misc",
    "/proc/modules",
    "/proc/mounts",
    "/proc/net/vlan",
    "/proc/net/bonding",
    "/proc/partitions",
    "/proc/sched_debug",
    "/proc/schedstat",
    "/proc/scsi/scsi",
    "/proc/scsi/sg/device_strs",
    "/proc/stat",
    "/proc/swaps",
    "/proc/version",
    "/proc/zoneinfo",
]

SYS_FILES = [
    "/sys",
]


class Collect:
    """Collect /proc and /sys from a system."""

    def __init__(self, output_dir=""):
        """Initialize the collect class.

        Args:
            output_dir: directory to place output in (default: current dir)
        """
        self.tmp_dir = tempfile.mkdtemp(prefix="whatsthis-")

        logging.info("starting collection")
        logging.debug("tempdir: %s", self.tmp_dir)

        self.proc()
        self.sys()

        os.makedirs(os.path.join(self.tmp_dir, 'cmd'))
        for command, filename in COMMANDS.items():
            print("running: %s" % command)
            result = execute(command)

            output_file = os.path.join(self.tmp_dir, 'cmd', filename)
            with open(output_file, "w") as file_out:
                file_out.write(result.stdout)

        tar_filename = "%s-%s.tar.gz" % (
            platform.node(),
            datetime.datetime.now().strftime("%Y%m%d-%H%M%S"),
        )
        tar(self.tmp_dir, os.path.join(output_dir, tar_filename))

    def __del__(self):
        """On delete clean up."""
        shutil.rmtree(self.tmp_dir)

    def proc(self):
        """Collect specific files from /proc."""
        logging.info("/proc")

        for file_path in PROC_FILES:
            if not exists(file_path):
                continue
            copy(file_path, os.path.join(self.tmp_dir, file_path[1:]))

    def sys(self):
        """Collect all of /sys.

        Requires the use of -noleaf due to the odd behavior of sysfs.
        Cannot assume it acts like any other filesystem.
        """
        logging.info("/sys")

        for sys_path in SYS_FILES:
            result = execute(
                ["find", sys_path, "-noleaf", "-type", "f", "-perm", "/444"]
            )

            for file_path in sorted(result.split("\n")):
                if 'autosuspend_delay_ms' in file_path:
                    continue
                if 'kernel/slab' in file_path:
                    continue
                if 'firmware/efi' in file_path:
                    continue
                if 'sys/module' in file_path:
                    continue
                if 'thermal/thermal_zone' in file_path:
                    continue
                if 'firmware/acpi' in file_path:
                    continue
                if 'devices/virtual/thermal' in file_path:
                    continue
                if 'sys/devices/platform' in file_path:
                    continue

                file_stat = os.stat(file_path)
                if oct(file_stat.st_mode)[-1:] == 0:
                    continue

                dd(file_path, os.path.join(self.tmp_dir, file_path[1:]))
