#!/usr/bin/python

favs = ('maichy', 'dana', 'mika')

for x in favs:
  print 'Name:', x.rjust(10)

for x in favs:
  print '%-10s %-10s' % ('Name:', x)
