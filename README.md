# whatsthis

[![Build Status](https://travis-ci.org/powersj/whatsthis.svg?branch=master)](https://travis-ci.org/powersj/whatsthis)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5ae8804cd8044e5a8853d989886647b1)](https://www.codacy.com/app/mrpowersj/whatsthis?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=powersj/whatsthis&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/powersj/whatsthis/branch/master/graph/badge.svg)](https://codecov.io/gh/powersj/whatsthis)

Am I in a cloud, on a container, or just plain metal? This is a Python
3 based CLI app to determine what a system is. Started after wanting to
explore /proc and /sys and to better understand what type of system
I may be on at any given time.

## Install

Install directly from [PyPI](https://pypi.org/project/whatsthis/):

```shell
pip3 install whatsthis
```

Project's requirements.txt file can include whatsthis as a dependency. Check out the [pip documentation](https://pip.readthedocs.io/en/1.1/requirements.html) for instructions on how to include a particular version or git hash.

Install from latest master:

```shell
git clone https://github.com/powersj/whatsthis
cd whatsthis
python3 setup.py install
```

## Usage

Example usage and subcommands:

```shell
whatsthis
whatsthis collect
whatsthis features
```

See `whatsthis -h` for more information.

## Bugs & Contact

File bugs on GitHub at the [whatsthis project](https://github.com/powersj/whatsthis/issues/new).
