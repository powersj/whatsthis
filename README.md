# whatami

[![Build Status](https://travis-ci.org/powersj/whatami.svg?branch=master)](https://travis-ci.org/powersj/whatami)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/826bc65137244c0faae0f5daab3682dd)](https://www.codacy.com/app/mrpowersj/whatami?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=powersj/whatami&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/powersj/whatami/branch/master/graph/badge.svg)](https://codecov.io/gh/powersj/whatami)

Am I in a cloud, on a container, or just plain metal? This is a Python 3 based CLI app to determine what a system is.

This started as a project to play and learn more about /proc and /sys on a Linux system as well as Python 3.

## Prereqs
These can either be obtained via apt:

```
$ apt update
$ apt install python3-tabulate
```

Or if you prefer to use pip3 point it at the requirements.txt file:

```
$ pip3 install --user tabulate
```

## How to Run

```
python3 -m whatami
```

The output can be altered with the `--josn` or `--csv` flags.
