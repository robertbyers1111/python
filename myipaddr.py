#!/usr/bin/python

import re
from subprocess import Popen, PIPE

#   +---------------------+
#---| anvil_IPs directory |---
#   +---------------------+

print '\nSearching anvil_IPs directory..'

me = 'bbyers'
numFoundForMe = 0

patternIPv4 = '^.*anvilIp_\
(?P<ipoct1>\d+)_(?P<ipoct2>\d+)_(?P<ipoct3>\d+)_(?P<ipoct4>\d+)\s*:\s*\
(?P<pid>\d+)\s*\
(?P<host>\S+)\s*\
(?P<interface>\S+)\s*\
(?P<username>\S+)\s*\
'

cmd = "/bin/egrep . /home/qa/anvil_IPs/sqa/anvilIp_*"
p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
for line in p.stdout:
  for match in re.finditer(patternIPv4,line):
    if match:
      dict = match.groupdict()
      ipAddr = dict['ipoct1'] + '.' + dict['ipoct2'] + '.' + dict['ipoct3'] + '.' + dict['ipoct4']
      pid = dict['pid']
      host = dict['host']
      interface = dict['interface']
      username = dict['username']
      if username == me:
        numFoundForMe = numFoundForMe + 1
        print '\n',line.rstrip()
        print '   IP Addr:',ipAddr
        print '   pid:',pid
        print '   host:',host
        print '   interface:',interface
        print '   username:',username

if numFoundForMe:
  print '\nFound',numFoundForMe,'interfaces for',me,'\n'
else:
  print '\nNo interfaces found for',me,'\n'

out, err = p.communicate()

