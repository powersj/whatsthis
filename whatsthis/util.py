# This file is part of whatsthis. See LICENSE file for license information.
"""Program entry point and arg parser."""

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

    return out, err, process.returncode
