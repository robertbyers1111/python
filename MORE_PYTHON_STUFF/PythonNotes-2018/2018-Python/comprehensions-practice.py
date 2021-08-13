#!/usr/bin/python3

# List comprehension demo..

mylist = [i for i in range(6)]
for i in mylist:
  print('i=',i)

# Dictionary comprehension demo..

d = {i:chr(i) for i in range(ord('a'),ord('z')+1)}

for k,v in d.items():
  print(k,':',v)
