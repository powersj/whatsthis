# This file is part of whatsthis. See LICENSE file for license information.
"""Subp module."""

import logging
import subprocess


def execute(args, data=None, env=None, shell=False):
    """Subprocess wrapper.

    Args:
        args: command to run
        data: data to pass
        env: optional env to use
        shell: optional shell to use

    Returns:
        Tuple of stdout, stderr, return code

    """
    args = args.split(' ') if isinstance(args, str) else args

    logging.debug('running %s', args)
    process = subprocess.Popen(
        args,
        env=env,
        shell=shell,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    (out, err) = process.communicate(data)
    out = '' if not out else out.rstrip().decode("utf-8")
    err = '' if not err else err.rstrip().decode("utf-8")

    return Result(out, err, process.returncode)


class Result(str):  # pylint: disable=too-many-ancestors
    """Result Class."""

    def __init__(self, stdout, stderr='', return_code=-1):
        """Initialize class."""
        super().__init__()

        self.stdout = stdout
        self.stderr = stderr
        self.return_code = return_code

    def __new__(cls, stdout, stderr, return_code):
        """Create new class."""
        obj = str.__new__(cls, stdout)
        obj.stderr = stderr
        obj.return_code = return_code
        return obj

    def __bool__(self):
        """Boolean behavior."""
        return self.ok

    @property
    def failed(self):
        """Return opposite of ok: true if failure."""
        return not self.ok

    @property
    def ok(self):  # pylint: disable=invalid-name
        """Return boolean from return_code."""
        return not bool(self.return_code)
