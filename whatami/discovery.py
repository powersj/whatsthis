"""Launch the discovery of the system."""
import logging
import sys

from .modules.base import Module


def setup_logging(debug=False):
    """Set up logging to stdout."""
    log_level = logging.DEBUG if debug else logging.INFO
    log_format = '[%(asctime)s] %(levelname)8s: %(message)s'
    logging.basicConfig(stream=sys.stdout, format=log_format, level=log_level)


def launch(debug=False, json=False):
    """Discovery and execution of all modules."""
    setup_logging(debug)
    log = logging.getLogger('whatami')

    modules = {}
    for module in Module.__subclasses__():
        log.info('Loading module: %s', module.__name__)
        modules[module.__name__] = module()

    for _, module in modules.items():
        if json:
            print(module.to_json())
        else:
            print(module)
