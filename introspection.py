#!/usr/bin/python

#------------------------------
# INTROSPECTION
#
# Useful tools..
#
#     type()
#     dir()
#------------------------------

from datetime import datetime
from datetime import timedelta
from time import sleep

epoch_seconds = 0
epoch = datetime.utcfromtimestamp(epoch_seconds)

t0 = datetime.now()
sleep(0.12345)
t1 = datetime.now()
elapsed = t1 - t0
wtf = dir(elapsed)

print
print '     object epoch is of type:',type(epoch)
print '   object elapsed is of type:',type(elapsed)
print
print "   object elapsed has these attributes..."
print

for wtfwtf in wtf:
  print '                    ',wtfwtf

print

