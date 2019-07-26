# This file is part of whatsthis. See LICENSE file for license information.
"""Program entry point and arg parser."""

import argparse
import json
import logging
import platform
import sys

from whatsthis import __features__, __version__
from whatsthis.collect import Collect
from whatsthis.discovery import Discovery


def _setup_args():
    """TODO."""
    parser = argparse.ArgumentParser(prog='whatsthis')
    parser.add_argument(
        '--data-dir',
        help='use previously collected data from specified directory'
    )
    parser.add_argument(
        '--debug', action='store_true', help='enable debug logging'
    )
    parser.add_argument(
        '--json', action='store_true', help='enable output in JSON'
    )

    subparsers = parser.add_subparsers(title='Subcommands', dest='subcommand')
    collect = subparsers.add_parser(
        'collect', help='collect required system data'
    )
    collect.add_argument(
        '--output-dir', default='',
        help='place collected data here instead of `pwd`'
    )
    subparsers.add_parser(
        'features', help='return parseable list of feature flags'
    )
    subparsers.add_parser(
        'version', help='return version of application'
    )

    return parser.parse_args()


def _setup_logging(debug=False):
    """Set up the root logger with format and level."""
    log = logging.getLogger()

    if debug:
        level = logging.DEBUG
        formatter = logging.Formatter('%(asctime)s - %(message)s')
    else:
        level = logging.INFO
        formatter = logging.Formatter('%(message)s')

    console = logging.StreamHandler()
    console.setFormatter(formatter)
    log.setLevel(level)
    log.addHandler(console)


def _verify_platform_support():
    """Determine platform and kernel version support for sysfs."""
    if platform.system() != 'Linux':
        print('error: only linux platform supported')
        sys.exit(1)

    major, minor, _ = platform.release().split('.')
    if int(major) < 3 and int(minor) < 6:
        print('error: at least kernel 3.6 for sysfs support required')
        sys.exit(1)

    major, minor, _ = platform.python_version_tuple()
    if int(major) < 3 or int(minor) < 5:
        print('error: at least python 3.5 required')
        sys.exit(1)


def launch():
    """Run it all."""
    args = _setup_args()
    _setup_logging(args.debug)
    _verify_platform_support()

    if not args.subcommand:
        Discovery(args.json, args.data_dir)
    elif args.subcommand == 'collect':
        Collect(args.output_dir)
    elif args.subcommand == 'features':
        print(json.dumps(__features__, indent=4, sort_keys=True))
    elif args.subcommand == 'version':
        print(__version__)


if __name__ == '__main__':
    sys.exit(launch())
