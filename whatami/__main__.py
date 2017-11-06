"""Program entry point and arg parser."""
import argparse

from whatami.discovery import launch

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('--debug', action='store_true')
    ARGS = PARSER.parse_args()

    launch(ARGS.debug)
