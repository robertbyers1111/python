#!/usr/bin/python

import inspect
import logging
from datetime import datetime


def whoami():
  return(inspect.stack()[1][3])

#   +--------------+
#---| Init logging |-----------------------------------------------------------
#   +--------------+

def initlogging():
  global logger
  logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s  %(funcName)-7.7s %(levelname)5.5s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
  logger = logging.getLogger(whoami())
  logger.setLevel(logging.DEBUG)


#   +-------------------------------------+
#---| Logging is accessible from anywhere |------------------------------------
#   +-------------------------------------+

def FUNC_A():
  logger.info('')
  logger.info('IN: '+whoami())
  logger.debug('Here is some useless nothingness from '+whoami())
  logger.debug('Here is some useless nothingness from '+whoami())
  logger.debug('Here is some useless nothingness from '+whoami())
  logger.debug('Here is some useless nothingness from '+whoami())


#   +-------------------------------------+
#---| Functions can have their own logger |------------------------------------
#   +-------------------------------------+

def FUNC_B():

  #-- Get my own logger

  localLog = logging.getLogger(whoami())
  localLog.setLevel(logging.INFO)

  #-- and use it..

  localLog.info('')
  localLog.info('IN: '+whoami())
  localLog.debug('Here is some useless nothingness from '+whoami())
  localLog.debug('Here is some useless nothingness from '+whoami())
  localLog.debug('Here is some useless nothingness from '+whoami())
  localLog.debug('Here is some useless nothingness from '+whoami())


#   +------+
#---| Main |-------------------------------------------------------------------
#   +------+

initlogging()
FUNC_A()
FUNC_B()

