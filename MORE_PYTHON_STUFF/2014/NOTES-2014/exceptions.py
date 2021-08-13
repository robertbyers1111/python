#!/usr/bin/python
import sys

#-- Read an integer from user

while True:
  try:
    x = int(raw_input("Please enter a number: "))
    break
  except ValueError:
    print "Oops!  That was no valid number.  Try again..."

print 'You entered:', x

#-- Open a file from command line

print '\nYou entered', len(sys.argv[1:]), 'command line arguments'
for arg in sys.argv[1:]:
  try:
    print 'Attempting to open', arg
    f = open(arg, 'r')
  except IOError:
    print 'cannot open', arg
  else:
    print arg, 'has', len(f.readlines()), 'lines'
    f.close()

