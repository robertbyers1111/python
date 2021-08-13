#msg1 = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
msg = """ \r abcd \n efgh wxyz \n\n 0123abcd  \naabcdd \r \n \r \n \r \n \r \n       4567\r\r\n"""

#------------------------------------------------------------------------------
# NOTES:
#
# 1. No args means split on whitespace (but it trims whitespace too)
#
# 2. The arg is one delimiter as a string, not a list of delimiter chars
#
# 3. To split and retain leading/trailing whitespace use re.split()
#
#------------------------------------------------------------------------------



print
print '--------- (see note 1)'

for line in msg.split('abcd'):

  print 'line:',line



print
print '--------- (see note 2)'

for line in msg.split():

  print 'line:',line



print
print '--------- (see note 3)'

import re

for line in re.split('\r|\n', msg):

  print 'line:', line

