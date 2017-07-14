#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 11:43:35 2017
# https://stackoverflow.com/questions/2737966/how-to-change-the-stdin-encoding-on-python
"""


# Hopefully both output UTF-8

import sys

print(sys.stdout.encoding)
print('\n')
print(sys.stdin.encoding)

