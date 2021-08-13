#!/usr/bin/python

import re

line = "abc 300 xyz"
pattern = "^.*\s+(\d+)\s+.*$"
searched = re.search(pattern, line)

if searched:
  print('\n')
  print('     MATCHED PATTERN:', searched.re.pattern)
  print('        COLUMN RANGE:', searched.start(),'-',searched.end())
  print('      MATCHED STRING:', searched.string)
  print('   EXTRACTED INTEGER:', searched.group(1))

  value = searched.group(1)
  print('\n')
  print('               value:',value)
  print('    type of value is:',type(value))

  ivalue = int(value)
  print('\n')
  print('              ivalue:',ivalue)
  print('   type of ivalue is:',type(ivalue))

  fvalue = float(value)
  print('\n')
  print('              fvalue:',fvalue)
  print('   type of fvalue is:',type(fvalue))

#-- Check object's type using an 'if' statement

a = {'b':2, 'c':3}

if (type(a) is dict):
    print('\n OK: a is a dict')
else:
    print('\n Uh oh. a is NOT a dict')

