#!/usr/bin/python

import sys

def whatever():
  myname = sys._getframe().f_code.co_name
  print myname

whatever()
