#!/usr/bin/python3

import atexit

def abc():
  print('Whoa!')

atexit.register(abc)

print('a')
print('b')
