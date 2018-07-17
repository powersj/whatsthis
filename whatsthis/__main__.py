# This file is part of whatsthis. See LICENSE file for license information.
"""Program entry point and arg parser."""

import argparse
import json
import logging
import platform
import sys

from whatsthis.collect import Collect
from whatsthis.discovery import Discovery


def _setup_args():
    """TODO."""
    parser = argparse.ArgumentParser(prog='whatsthis')
    parser.add_argument(
        '--data-dir', help='use previously collected data in this directory'
    )
    parser.add_argument(
        '--debug', action='store_true', help='show debug logging'
    )
    parser.add_argument(
        '--json', action='store_true', help='output in JSON rather than text'
    )

    subparsers = parser.add_subparsers(title='Subcommands', dest='subcommand')
    subparsers.add_parser(
        'version', help='print version'
    )
    subparsers.add_parser(
        'features', help='list defined features'
    )
    collect = subparsers.add_parser(
        'collect', help='collect system data required data'
    )
    collect.add_argument(
        '--output-dir', default='', help='place collected data here'
    )

    return parser.parse_args()


def _setup_logging(debug=False):
    """Set up the root logger with format and level."""
    log = logging.getLogger()

    level = logging.DEBUG if debug else logging.INFO
    log.setLevel(level)

    console = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console.setFormatter(formatter)
    log.addHandler(console)


def _print_features():
    """Print available features."""
    import whatsthis
    print(json.dumps(whatsthis.__features__, indent=4, sort_keys=True))


def _print_version():
    """Print current version."""
    import whatsthis
    print(whatsthis.__version__)


def verify_platform_support():
    """Determine platform and kernel version support for sysfs."""
    if platform.system() != 'Linux':
        print('error: only linux platform supported')
        sys.exit(1)

    major, minor, _ = platform.python_version_tuple()
    if int(major) < 3 or int(minor) < 4:
        print('error: require at least python 3.4')
        sys.exit(1)

    major, minor, _ = platform.release().split('.')
    if int(major) < 3 and int(minor) < 6:
        print('error: no sysfs support')
        sys.exit(1)


def launch():
    """Run it all."""
    args = _setup_args()
    _setup_logging(args.debug)

    verify_platform_support()

    if not args.subcommand:
        Discovery(args.json, args.data_dir)
    elif args.subcommand == 'features':
        _print_features()
    elif args.subcommand == 'collect':
        Collect(args.output_dir)
    elif args.subcommand == 'version':
        _print_version()


if __name__ == '__main__':
    sys.exit(launch())
