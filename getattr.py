#!/usr/bin/python

# USE 'getattr' to iterate through the attributes of an object

import re

lines = """{dut:4500 dut1, abc, def, abc, xyz}"""
for line in re.split('\r|\n',lines):
  omg = re.search('abc', line)
  for wtf in (wtf for wtf in sorted(dir(omg)) if not wtf.startswith('__')):
    print '   ',getattr(omg,wtf)

