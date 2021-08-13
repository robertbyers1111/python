#!/usr/bin/python

# KEY: use split() method otherwise it iterates on individual characters not lines

import string

theData = """
anvilIp_192_168_225_3:1486 radiumwater5_vm eth3:5ce_9 vharirian
anvilIp_192_168_225_4:1486 radiumwater5_vm eth3:5ce_10 vharirian
anvilIp_192_168_225_5:1486 radiumwater5_vm eth3:5ce_11 vharirian
"""

for line in theData.split('\n'):
   print 'line: ', line

