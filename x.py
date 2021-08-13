import os
import subprocess as sp

LOCKFILE = '/tmp/deleteme.now'
try:
  os.remove(LOCKFILE)
except OSError:
  pass

pid = 1

child = sp.Popen( \
 ['/bin/ps', \
  '--no-headers',
  '-opid',
  '-p%s' % pid],
 shell=False, \
 stdout=sp.PIPE, \
 stderr=sp.PIPE)

foundpid = ''

for line in child.stdout:
  foundpid = line.strip()

print 'foundpid:',foundpid

#for line in child.stderr:
#  print 'stderr:',line
#
#print 'sppid:',sppid

spio = child.communicate()[0]
sprc = child.returncode


