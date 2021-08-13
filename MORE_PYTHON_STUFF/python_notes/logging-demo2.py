#!/usr/bin/python

# FURTHER READING:
#
# https://docs.python.org/3.5/library/logging.html
# https://docs.python.org/3.5/howto/logging-cookbook.html

import inspect
import logging
from datetime import datetime


def whoami():
  return(inspect.stack()[1][3])


def FUNC_A():
  logger = logging.getLogger(whoami())
  logger.setLevel(logging.DEBUG)
  logger.info('IN: '+whoami())
  logger.debug('Here is some useless nothingness from '+whoami())


def FUNC_Z():
  logger = logging.getLogger(whoami())
  logger.setLevel(logging.INFO)
  logger.info('IN: '+whoami())
  logger.debug('Here is some useless nothingness from '+whoami())


#-- Initialize logging..

logging.basicConfig(filename='example.log', level=logging.DEBUG, filemode='w', format='[%(asctime)s  %(module)-15.15s %(funcName)-7.7s %(name)7.7s %(levelname)5.5s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

FUNC_A()
FUNC_Z()

