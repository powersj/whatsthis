"""Util module."""
import re
import math


def firstmatch(string, regex, return_int=False):
    """Return first match or empty string."""
    matches = re.findall(string, regex)

    try:
        return int(matches[0]) if return_int else matches[0]
    except IndexError:
        if return_int:
            return -1
        return ''


def kilobytes2human(kilobytes):
    """Convert kilbytes to human (decimal) readable size."""
    if not kilobytes:
        return '0KB'
    elif kilobytes == 0:
        return '0KB'

    if isinstance(kilobytes, str):
        kilobytes = int(kilobytes)

    magnitudes = ['KB', 'MB', 'GB', 'TB', 'PB']
    order = int(math.floor(math.log(kilobytes, 1024)))
    power = math.pow(1000, order)
    size = round(kilobytes / power, 2)

    return "%s%s" % (size, magnitudes[order])


def readfile(file_path):
    """Read a file in python, effectively `cat`."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except TypeError:
        return ''

    return content.strip()
