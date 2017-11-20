"""Util module."""
import re
import math
import tempfile


def firstmatch(string, regex, return_int=False):
    """Return first match or empty string."""
    matches = re.findall(string, regex)

    try:
        return int(matches[0]) if return_int else matches[0]
    except IndexError:
        if return_int:
            return 0
        return ''


def kilobytes2human(kilobytes):
    """Convert kilbytes to SI human (decimal) readable size."""
    if isinstance(kilobytes, str):
        try:
            kilobytes = int(kilobytes)
        except ValueError:
            kilobytes = int(''.join([i for i in kilobytes if i.isdigit()]))

    if not kilobytes:
        return '0KB'
    elif kilobytes < 1:
        return '<1KB'

    magnitudes = ['KB', 'MB', 'GB', 'TB', 'PB']
    order = int(math.floor(math.log(kilobytes, 1000)))
    power = math.pow(1000, order)
    size = round(kilobytes / power)

    return '%s%s' % (size, magnitudes[order])


def readfile(file_path):
    """Read a file in python, effectively `cat`."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return ''

    return content.strip()


def write_tempfile(data):
    """Write data to temporary file."""
    temp = tempfile.NamedTemporaryFile(delete=False, mode='w+t')
    temp.write(data)
    temp.close()

    return temp.name
