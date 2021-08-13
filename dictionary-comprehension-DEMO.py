#!/usr/bin/python3

# Demo of a dictionary comprehension

d={i:chr(i) for i in range(ord('a'),ord('z')+1)}

for k,v in d.items():
  print(k,':',v)
