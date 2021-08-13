#!/usr/bin/python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# To verify multiple values, we can do in the following manner.

if m in [1,3,5,7]:
  print('yes')

# instead of:

if m==1 or m==3 or m==5 or m==7:
  print('blah')

# Alternatively, we can use ‘{1,3,5,7}’ instead of ‘[1,3,5,7]’ for ‘in’
# operator because ‘set’ can access each element by O(1).

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Basic if-then-else..

a = 10
b = 11
c = 99

if a > b:
  print('a gt b')
elif a < b:
  print('a lt b')
else:
  print('a == b')

if a > b \
or b > c \
or c < a:
  print('WTF')
else:
  print('OK')

