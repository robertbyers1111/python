#!/usr/bin/python

import logging
from datetime import datetime

class Abc():
  def __init__(self,who):
    logging.debug('')
    logging.debug('Creating new instance of class Abc')
    self.when = datetime.now()
    self.who = who

class Xyz():
  def __init__(self,who):
    logging.debug('')
    logging.debug('Creating new instance of class Xyz')
    self.when = datetime.now()
    self.who = who


#-- Start logging subsystem ------------------------------------

logging.basicConfig(filename='example.log', level=logging.DEBUG, filemode='w', format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


#-- Display numeric log levels for each textual level ----------

lognumDEBUG     = getattr(logging, 'DEBUG')
lognumINFO      = getattr(logging, 'INFO')
lognumWARNING   = getattr(logging, 'WARNING')
lognumERROR     = getattr(logging, 'ERROR')
lognumCRITICAL  = getattr(logging, 'CRITICAL')

logging.info('')
logging.info( '   Debug log level number is %d' % lognumDEBUG )
logging.info( '    Info log level number is %d' % lognumINFO )
logging.info( ' Warning log level number is %d' % lognumWARNING )
logging.info( '   Error log level number is %d' % lognumERROR )
logging.info( 'Critical log level number is %d' % lognumCRITICAL )


#-- Show logging methods ---------------------------------------

logging.info('')
logging.info('=== logging methods..')

keys = (name for name in dir(logging) if not name.startswith('_'))

for key in sorted(keys):
  value = getattr(logging, key)
  if callable(value):
    logging.info('%18s : %s' % (key, value))


#-- Show logging attributes ------------------------------------

logging.info('')
logging.info('=== logging attributes..')

keys = (name for name in dir(logging) if not name.startswith('_'))

for key in sorted(keys):
  value = getattr(logging, key)
  if not callable(value):
    logging.info('%18s = %s' % (key, value))


#-- Show Logger methods ----------------------------------------

logging.info('')
logging.info('=== logging.Logger methods..')

keys = (name for name in dir(logging.Logger) if not name.startswith('_'))

for key in sorted(keys):
  value = getattr(logging.Logger, key)
  if callable(value):
    logging.info('%18s : %s' % (key, value))


#-- Show Logger attributes -------------------------------------

logging.info('')
logging.info('=== logging.Logger attributes..')

keys = (name for name in dir(logging.Logger) if not name.startswith('_'))

for key in sorted(keys):
  value = getattr(logging.Logger, key)
  if not callable(value):
    logging.info('%18s = %s' % (key, value))


#-- Test logging from within class methods ---------------------

abc = Abc('abc')
xyz = Xyz('xyz')

