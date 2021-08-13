#!/usr/bin/python

from datetime import datetime

#   +----------------+
#---| BASIC FUNCTION |----------------------------------------------------------
#   +----------------+

def myfunc1(val):
  print
  print '=== IN: myfunc1'
  print
  print '    val:',val,type(val)
  return('whatev3r')

#   +--------------------+
#---| VARIABLE ARG COUNT |------------------------------------------------------
#   +--------------------+

def myfunc2(*args):

  NOW = datetime.now().strftime('[%Y/%m/%d %H:%M:%S]')

  print
  print '=== IN: myfunc2()'
  print
  print '   I was called with',len(args),'arguments..'

  msg = NOW

  for arg in args:
    print '     ',arg,'	',type(arg)
    msg = msg+' '+str(arg)

  print
  print msg

#   +------+
#---| MAIN |--------------------------------------------------------------------
#   +------+

myfunc1('xyz')
myfunc2('abc',237,'def xyz',7.50)
