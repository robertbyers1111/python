#!/usr/bin/python

# Demo of reading arbitrary name/value pairs into an object and then iterating through it 

import re

#-- This is the data to be processed

lines = """
  mode = standalone
  name = wabbit
  wancom0_ip = 10.196.145.49
  accessmode = telnet
  accessport = wancom0
  tsip = 10.196.144.55
  tsport = 2006
  port1_network = labnet1
  port1_slot = 0
  port1_port = 0
  port2_network = labnet2
  port2_slot = 0
  port2_port = 0
  port3_network = labnet3
  port3_slot = 0
  port3_port = 0
"""

#-- CLASS DEFINITION -------

class Dut():
  def __init__(self,id):
    self.id = id

  def show(self):
    keys = (name for name in dir(self) if not name.startswith('_'))
    for key in keys:
      value = getattr(self, key)
      if not callable(value):
        print '    ',key,'=',value


#-- MAIN -------------------

dut = Dut(1)

for line in re.split('\r|\n', lines):

  tuple = re.match("^\s*([^=]+)\s*=\s*(.+)$", line)

  if tuple:

      setattr(dut, tuple.group(1), tuple.group(2))

dut.show()
