#!/usr/bin/python3

def safeDivide(x,y):
  try:
    a = x/y
  except:
    a = 0
  finally:
    return a

print(safeDivide(10,0))

# Can also specify a particular exception..

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as errmsg:
    print('I am handling a run-time error:', errmsg)

