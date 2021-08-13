#!/usr/local/bin/python

#-- OLDER -----------------------

favs = ('maichy', 'dana', 'mika')

print
for x in favs:
  print 'Name:', x.rjust(10)

print
for x in favs:
  print '%-10s %-10s' % ('Name:', x)

#-- NEWER ------------------------

targets = 41
alive = 40
pctdead = 3
descr = 'mgmt network'


msg = '%3d queried %3d responded (%2d%% down) %12s'  %  (targets, alive, pctdead, descr)


print
print msg

