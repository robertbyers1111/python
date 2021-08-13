#!/usr/bin/python

#   +---------------------------------------+
#---| Open a file, read all of it, close it |---
#   +---------------------------------------+

fname = '/etc/hosts'
f = open(fname, 'r')
print '\nSuccessfully opened %s (%s)' % (fname,f)
print f.read()
f.close()

#   +-----------------------------------------------+
#---| Open a file, read first three lines, close it |---
#   +-----------------------------------------------+

fname = '/etc/hosts'
f = open(fname, 'r')
print '\nSuccessfully opened %s (%s)' % (fname,f)
print 'LINE:', f.readline(),
print 'LINE:', f.readline(),
print 'LINE:', f.readline(),
f.close()

#   +---------------------------------------+
#---| Open a file, read all lines, close it |---
#   +---------------------------------------+

fname = '/etc/hosts'
f = open(fname, 'r')
print '\nSuccessfully opened %s (%s)' % (fname,f)
for line in f.readlines():
  print 'LINE:', line,
f.close()

#   +------------------------------------------------------+
#---| FAV: Open a file, read lines one at a time, close it |---
#   +------------------------------------------------------+

fname = '/etc/hosts'
f = open(fname, 'r')
print '\nSuccessfully opened %s (%s)' % (fname,f)
for line in f:
  print 'LINE:', line,
f.close()

