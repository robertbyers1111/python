#!/usr/bin/python

import sys, os

def isRunning(pid):
  f = os.popen("ps -p"+str(pid)+" --no-header -opid", "r")
  psResult = f.read().strip()
  if psResult != '':
    return 1
  else:
    return 0

def showIsRunning(pid):
  if isRunning(pid):
    print 'process',pid,'is running'
  else:
    print 'process',pid,'is NOT running'

showIsRunning(1)
showIsRunning(1234)

