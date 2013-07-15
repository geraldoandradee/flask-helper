#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import (print_function, unicode_literals)
"""
Flask-Helper
============

Flask-Helper is a command line utility to boost start flask projects.


"""
__author__ = 'Geraldo Andrade <geraldo@geraldoandrade.com>'

import argparse

parser = argparse.ArgumentParser(description='Create files for boost flask development process.')

# let's create all arguments to process
parser.add_argument('--newapp', default='micro', help='Creates a complete Flask App according with argument')
parser.add_argument('--database', help='Creates an app with database support.', default=None)
parser.add_argument('--cache', help='Creates an app with cache support.', default=None)
parser.add_argument('--debugtoolbar', help='Creates an app with cache support.', default=None)
parser.add_argument('--form', help='Creates an app with form support.', default=None)
parser.add_argument('--test', help='Creates an app with testing support.')


# lets do the trick ...


