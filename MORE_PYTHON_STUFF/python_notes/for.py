#!/usr/bin/python


networks = {
 'abc' : 'ABCD',
 'def' : 'DEFG',
 'xyz' : 'XYZ0'
}


#-------------------------------------------------------------------------------

for name, value in sorted(networks.items()):

  print
  print '     name:',name
  print '    value:',value
  print


#-------------------------------------------------------------------------------
# USING 'if not' on the same line as 'for'

import re

lines = """{dut:4500 dut1, abc, def, abc, xyz}"""

for line in re.split('\r|\n',lines):

  omg = re.search('abc', line)

  omgdir = sorted(dir(omg))

  for wtf in (wtf for wtf in omgdir if not wtf.startswith('__')):

    print '   ',getattr(omg,wtf)

