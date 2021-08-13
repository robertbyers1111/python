#!/usr/bin/python

#----------------------------------------------------------------
#
# Trimming whitespace from strings: use 'strip()' method
#
# Also, use lstrip() and rstrip() for left and right strip
#
#----------------------------------------------------------------

from subprocess import Popen, PIPE
cmd = "/sbin/ifconfig"
p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)

for line in p.stdout:
    print "line:  ", line.rstrip()

out, err = p.communicate()
