#!/usr/bin/python

#-------------------------------------------------------------------------------
#
# Use 'Popen()' to spawn a subprocess
#
#-------------------------------------------------------------------------------

import subprocess as sp

child = sp.Popen(['/bin/ps', '-ubbyers', '-opid,tty,cmd'], shell=False, stdout=sp.PIPE, stderr=sp.PIPE)

print 'pid:',child.pid

#-- NOTE: Can only loop through stdout ONCE (!!!)
#-- Hence, we build a buffer that can be accessed later.

outbuf = ''
for line in child.stdout:
  outbuf += line

streamdata = child.communicate()[0]
rc = child.returncode

#-- NOTE: Cannot access stdout and stderr once communicate() has been called (!!!)
#-- Hence, we access outbuf, which was previously built while consuming stdout

for line in outbuf.split('\n'):
  print 'new:',line

