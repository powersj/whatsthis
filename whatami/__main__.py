"""Program entry point and arg parser."""
import argparse

from .discovery import launch

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()

    launch(args.debug, args.json)

if __name__ == '__main__':
    main()
