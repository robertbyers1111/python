#!/usr/bin/python

#-- Color Codes

colorcodes = {
  'red' : 3,
  'blue' : 4,
  'green' : 5
}

#-- Reverse lookup for color codes

colornames = dict((v, k) for k, v in colorcodes.items())

#-- dispaly color codes

print
for x in sorted(colorcodes.keys()):
  print 'colorcodes[%s]: %s' % (x, colorcodes[x])

#-- dispaly color names

print
for x in sorted(colornames.keys()):
  print 'colornames[%s]: %s' % (x, colornames[x])

