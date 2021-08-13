#!/usr/bin/python3

import sys

#   +----------------------+
#---| Catch all exceptions |---
#   +----------------------+

try:
    a = 0/0
except:
    e = sys.exc_info()[0]
    print('Caught run-time error: %s' % e)

#   +------------------------------+
#---| Catch a particular exception |---
#   +------------------------------+

try:
    a = 0/0
except ZeroDivisionError as e:
    print('Caught run-time error: %s' % e)

