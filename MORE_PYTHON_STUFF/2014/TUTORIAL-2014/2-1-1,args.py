#!/usr/bin/python
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

