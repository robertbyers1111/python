#!/usr/bin/python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# *** M U S T  K N O W ***
#
# import/from mnemonic: 'frimport'
#
# what uses []?       lists, array indexes
# what uses {}?       sets, dictionaries
# what uses ()?       tuples
#
# write a tuple
# write a dictionary
# write a set
# write a list
#
# write a slice (mnemonic: fruntil = from:until)
#
# print out the items of a list with index numbers
#
# diff between tuple and list?
# what is a set?
# what are python dictionaries? (ans: sort of a hash table or associative array)
#
# what are iter() and next()?
# write code that uses iter() and next()
#
# write a multivariate for loop
#
# use these functions..
#   join()
#   split()
#   map()
#
# compute the sums of columns, rows, and diags of an nxn matrix (hint: use zip() and sum())
#
# format using "fmstr % (args)" ex.: '%d %7.2f mph' % (car, speed)
#
# format using format() method for a string (the string is the format
# specifier, the args are the vars to be formatted)
#
# what will set() do to a list? a string?
#
# what is advantage of using 'with' for reading a file?
# write code to read a file using 'with'
#
# write a list, dictionary and set comprehension
#
# write code using 'try', and 'except', and 'finally'
#
# write code to catch divide by zero exceptions
#
# write a class demo
#
# how does repr() work? Use it with zfill() and ljust()
#
# use keyword arguments to call a function
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# [UNPACKING OPERATORS]
#
# https://www.python.org/dev/peps/pep-0448/
#
# Know these (from misc.py)..
#
#     * iterable unpacking
#     ** dictionary unpacking
#
# syntax..
#
#     *arguments - an arbitrary number of (optional) arguments
#     **keywords - an arbitrary number keyword=value pairs (must be last parameter)
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# print the last three elements of a 10 element list
#
# Use 'in' and 'not in' with a set (can use with a list and/or dictionary?)
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def whatis(x):
  print('   ',type(x))
  print('   ',x)

#frimport
from datetime import datetime

#list
whatis(['abc',1,2.3,4,'xyz'])
#
#set (automatically filters out duplicates)
whatis({'a','b','c','b','b','b','b','b','b','d'})
#
#dict
whatis({1:'ab', 7:'def', 9:'xyz'})
#
#tuple: a comma-separated sequence of values (customary to enclose in parens)
whatis((1,'ab',77,'defef','syz'))

#tuple oddity..
whatis(5,) #hmm how to pass it as a tuple???
a=5,
whatis(a)

#slice of a list..
a = ['abc', 123, 'def', ('h',7), 789, {'andover':5, 'chelmsford':2}, 'xyz']

print()
print('list..')
for item in a:
  print('  ',item)

print()
print('elements 2, 3 and 4..')
print(a[2:5])

#enumerated list..
print()
print('enumerated list..')
for k,v in enumerate(a):
  print()
  print('item',k)
  whatis(v)

#dictionary..
x={'abc':5, 'bb':'def', 'mhs':1979, '':0}
print()
print('keys of x:',x.keys())

