"""Launch the discovery of the system."""
import json
import logging
import sys

from .modules.base import Module


def setup_logging(debug=False):
    """Set up logging to stdout."""
    log_level = logging.DEBUG if debug else logging.INFO
    log_format = '[%(asctime)s] %(levelname)8s: %(message)s'
    logging.basicConfig(stream=sys.stdout, format=log_format, level=log_level)


def launch(debug=False, json_output=False):
    """Discovery and execution of all modules."""
    setup_logging(debug)
    log = logging.getLogger('whatami')

    modules = {}
    for module in Module.__subclasses__():
        log.debug('Loading module: %s', module.__name__)
        modules[module.__name__] = module()

    if json_output:
        module_json = [module.to_json() for module in modules.values()]
        print(json.dumps(module_json, indent=2))
    else:
        for name, module in sorted(modules.items(), key=lambda x: x[1].order):
            print(name)
            print(module)
            print()
