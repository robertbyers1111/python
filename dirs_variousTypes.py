#!/usr/bin/python3
import pdb

# A tool to nicely show the output of dir() for various python data types

def func(s):
  iterable='(iterable)' if '__iter__' in dir(s) else 'NOT iterable'
  print('\n===',s,type(s),iterable)
  for x in sorted(dir(s)):
    print('  ',x)

for x in [
 pdb,
 bytes,
 bool,
 chr,
 complex,
 dict,
 float,
 frozenset,
 int,
 list,
 set,
 str,
 tuple,
 zip,
]:
  func(x)

