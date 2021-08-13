#!/usr/bin/python3

import re
a='abcdefg'

#-- MOST BASIC..

if re.search('bcd','abcdefg'):
  print('bcd found')

#-- Slightly less basic..

for searchstr in ['bc','zz']:
  print(searchstr,'found') if re.search(searchstr,a) else print(searchstr,'NOT found')

