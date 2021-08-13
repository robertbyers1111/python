#!/usr/bin/python

#----------------------------------------------------------------------------
# Use subprocess, per this comment fond on stackoverflow ...
#
#       Can't see why you'd use os.system even for
#       quick/dirty/one-time. subprocess seems so
#       much better.
#
#----------------------------------------------------------------------------

from subprocess import Popen, PIPE

cmd = "/sbin/ifconfig"

p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)

for line in p.stdout:
    print "line:  ", line.rstrip()

out, err = p.communicate()
