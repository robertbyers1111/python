#!/usr/bin/python

import os

#--------------------------------------------------------------------------------
#
# Quick takeaways ..
#
#	os.environ['HOME']
#
#	os.environ.get('LOGNAME')
#
#--------------------------------------------------------------------------------

# Note: using os.environ.get() will return `None` if a key
# is not present rather than raise a `KeyError`

print '   env( HOME ):', os.environ['HOME']

for var in [ 'LOGNAME', 'LUGNAME' ]:
  val = os.environ.get(var)
  if val:
    print '   env(',var,'):',val

