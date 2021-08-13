#!/usr/bin/python

import inspect

def whoami():
  return(inspect.stack()[1][3])

def whocalledme():
  return(inspect.stack()[2][3])

def whoarewe():
  print
  msgprefix = '         I am:'
  for wtf in inspect.stack():
    if wtf[3] != 'whoarewe':
      print msgprefix,wtf[3]
      msgprefix = '    called by:'

def abcd():
  whoarewe()
  efgh()

def efgh():
  whoarewe()
  xyz()

def xyz():
  whoarewe()

abcd()

