#!/usr/bin/python

import re

line = "abc 300 xyz"
pattern = "^.*\s+(\d+)\s+.*$"
searched = re.search(pattern, line)

if searched:
  print
  print '     MATCHED PATTERN:', searched.re.pattern
  print '        COLUMN RANGE:', searched.start(),'-',searched.end()
  print '      MATCHED STRING:', searched.string
  print '   EXTRACTED INTEGER:', searched.group(1)

  value = searched.group(1)
  print
  print '               value:',value
  print '    type of value is:',type(value)

  ivalue = int(value)
  print
  print '              ivalue:',ivalue
  print '   type of ivalue is:',type(ivalue)

  fvalue = float(value)
  print
  print '              fvalue:',fvalue
  print '   type of fvalue is:',type(fvalue)

