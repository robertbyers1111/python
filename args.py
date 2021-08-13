#!/usr/bin/python

import os
import sys

#   +---------------+
#---| Counting args |---
#   +---------------+

numargs = len(sys.argv[1:])
endargs = numargs + 1

print '\nYou entered', numargs, 'command line arguments'

for i in range(1,endargs):
  print "arg[" + str(i) + "]: " + sys.argv[i]

#   +-----------------------+
#---| Don't bother counting |---
#   +-----------------------+

for arg in sys.argv[1:]:
  print 'ARG:', arg

#   +---------------+
#---| Usage example |---
#   +---------------+

if len(sys.argv[1:]) != 1:
  print '\nUSAGE:',os.path.basename(__file__),'file\n'
  sys.exit(-1)

