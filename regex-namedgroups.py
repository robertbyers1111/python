#!/usr/bin/python

#------------------------------------------------------
#-- Demo of parsing and iterating through named groups
#------------------------------------------------------

import re

line = '10.196.147.153  <-> 10.196.2.5  3  1985  5  8858  8  9056  2.236117618  0.0006'

#(fyi: this doesn't have to be in a compiled pattern, could be in the call to re.match())

pattern = re.compile("^\
(?P<srcip>\d+\.\d+\.\d+\.\d+)\s+<->\s+\
(?P<dstip>\d+\.\d+\.\d+\.\d+)\s+\
(?P<rxframes>\d+)\s+\
(?P<rxbytes>\d+)\s+\
(?P<txframes>\d+)\s+\
(?P<txbytes>\d+)\s+\
(?P<totframes>\d+)\s+\
(?P<totbytes>\d+)\s+\
(?P<relstart>\S+)\s+\
(?P<duration>\S+)\s*$")

def checkit():
  parsed = re.match(pattern, line)

  if parsed:

    print
    for key in parsed.groupdict().keys():
      print '%15s: %s' % (key, parsed.group(key))

checkit()
