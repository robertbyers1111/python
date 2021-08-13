#!/usr/bin/python

import os
import signal
import sys
import time
from datetime import datetime

signal_lookup = {
 1: 'SIGHUP',
 2: 'SIGINT',
 3: 'SIGQUIT',
 4: 'SIGILL',
 5: 'SIGTRAP',
 6: 'SIGABRT',
 7: 'SIGBUS',
 8: 'SIGFPE',
 9: 'SIGKILL',
 10: 'SIGUSR1',
 11: 'SIGSEGV',
 12: 'SIGUSR2',
 13: 'SIGPIPE',
 14: 'SIGALRM',
 15: 'SIGTERM',
 16: 'SIGSTKFLT',
 17: 'SIGCHLD',
 18: 'SIGCONT',
 19: 'SIGSTOP',
 20: 'SIGTSTP',
 21: 'SIGTTIN',
 22: 'SIGTTOU',
 23: 'SIGURG',
 24: 'SIGXCPU',
 25: 'SIGXFSZ',
 26: 'SIGVTALRM',
 27: 'SIGPROF',
 28: 'SIGWINCH',
 29: 'SIGIO',
 30: 'SIGPWR',
 31: 'SIGSYS',
 34: 'SIGRTMIN',
 35: 'SIGRTMIN+1',
 36: 'SIGRTMIN+2',
 37: 'SIGRTMIN+3',
 38: 'SIGRTMIN+4',
 39: 'SIGRTMIN+5',
 40: 'SIGRTMIN+6',
 41: 'SIGRTMIN+7',
 42: 'SIGRTMIN+8',
 43: 'SIGRTMIN+9',
 44: 'SIGRTMIN+10',
 45: 'SIGRTMIN+11',
 46: 'SIGRTMIN+12',
 47: 'SIGRTMIN+13',
 48: 'SIGRTMIN+14',
 49: 'SIGRTMIN+15',
 50: 'SIGRTMAX-14',
 51: 'SIGRTMAX-13',
 52: 'SIGRTMAX-12',
 53: 'SIGRTMAX-11',
 54: 'SIGRTMAX-10',
 55: 'SIGRTMAX-9',
 56: 'SIGRTMAX-8',
 57: 'SIGRTMAX-7',
 58: 'SIGRTMAX-6',
 59: 'SIGRTMAX-5',
 60: 'SIGRTMAX-4',
 61: 'SIGRTMAX-3',
 62: 'SIGRTMAX-2',
 63: 'SIGRTMAX-1',
 64: 'SIGRTMAX'
}

#   +--------------+
#---| sighand_USR1 |------------------------------------------------------------
#   +--------------+

def sighand_USR1(signal, frame):

  mypid = os.getpid()
  signame = signal_lookup[signal]

  print
  print 'ATTENTION:'
  print 'pid %d has received signal %d (%s)'%(mypid,signal,signame)
  print 'continuing..'
  print

#   +--------------+
#---| sighand_USR2 |------------------------------------------------------------
#   +--------------+

def sighand_USR2(signal, frame):

  mypid = os.getpid()
  signame = signal_lookup[signal]

  print
  print 'NOTE:'
  print 'pid %d has received signal %d (%s)'%(mypid,signal,signame)
  print 'continuing..'
  print

#   +------+
#---| MAIN |--------------------------------------------------------------------
#   +------+

signal.signal(signal.SIGUSR1, sighand_USR1)
signal.signal(signal.SIGUSR2, sighand_USR2)

print
mypid = os.getpid()

pausesecs = 5

while True:
  print datetime.now().strftime('%Y/%m/%d %H:%M:%S'),'  pid',mypid,'  pausing',pausesecs,'seconds..'
  time.sleep(5)

