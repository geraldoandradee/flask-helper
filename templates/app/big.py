#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import (print_function, unicode_literals)
import os

"""
%s
================

This is a file template from https://github.com/quein/flask-helper.

"""

__author__ = 'Geraldo Andrade'


from flask import Flask
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

app = Flask(__name__) # main app
app.template_folder = os.path.join(os.path.dirname(__file__), 'templates') # set template de dir
app.static_folder = ''
app.secret_key = ''





if __name__ =='__main__':
    app.run()