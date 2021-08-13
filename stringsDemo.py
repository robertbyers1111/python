#!/usr/bin/python3

s = 'Guido'

#-- Does a string contain something???

if 'uid' in s:
  print('yes,',s,'contains uid')

#-- Point many variables to successive characters (cool!)

a,b,c,d,e = s

for z in ['a','b','c','d','e']:
  print(z,':',eval(z))

