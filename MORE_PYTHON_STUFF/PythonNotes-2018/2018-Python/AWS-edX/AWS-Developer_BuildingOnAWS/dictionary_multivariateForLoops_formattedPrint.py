#!/usr/bin/python3

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-- Demo of many things..
#--
#--   dictionary
#--   for with multiple variables
#--   loop through individual dictionary items
#--   loop using sorted list of dictionary keys
#--   print formatting with %
#--   merging two dictionaries with '**'
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x = {'a':3,'b':5,'c':9}
y = {'a':2,'c':4,'d':8}
z = {**x,**y}

for k,v in z.items():
  print('%s: %s' % (k,v) )

for k in sorted(z.keys()):
  print('%s: %s' % (k, z[k]) )
