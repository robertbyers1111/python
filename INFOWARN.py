#!/usr/bin/python

from datetime import datetime

#   +---------+
#---| MSGtool |-----------------------------------------------------------------
#   +---------+

def MSGtool(*args):
  msg = datetime.now().strftime('[%Y/%m/%d %H:%M:%S]')
  for arg in args:
    msg = msg+' '+str(arg)
  return msg

#   +------+
#---| DATA |--------------------------------------------------------------------
#   +------+

def DATA(*args):
  print MSGtool(*args)

#   +------+
#---| INFO |--------------------------------------------------------------------
#   +------+

def INFO(*args):
  msg = 'INFO '+MSGtool(*args)
  print msg

#   +------+
#---| WARN |--------------------------------------------------------------------
#   +------+

def WARN(*args):
  msg = 'WARN '+MSGtool(*args)
  print msg

#   +------+
#---| MAIN |--------------------------------------------------------------------
#   +------+

a = 15
b = 75
str1 = "(queried)"
str2 = "responded"
INFO(a,str1,b,str2)
