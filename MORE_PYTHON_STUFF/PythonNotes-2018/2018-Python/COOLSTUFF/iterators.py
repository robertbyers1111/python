#!/usr/bin/python3

# iter() and next() are how Python loops through arbitrary objects
# See 9.9. Iterators from https://docs.python.org/3.4/tutorial/classes.html

s='abcdefghijklm'

it=iter(s)
print(it)

while True:
  try:
    print(next(it))
  except:
    break

