#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

from os.path import dirname

model_dir = dirname(__file__)
# Compatibility with the main modules
comp_min = '1.0.0'
comp_max = '2.0.0'

__version__ = '1.0.0'

__all__ = [__version__, 'comp_min', 'comp_max', 'model_dir']
