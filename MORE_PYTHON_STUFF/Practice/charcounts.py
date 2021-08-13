#!/usr/bin/python3

str = input('input a string: ')
print('your string is:',str)
print('   its type is:', type(str))

freqs = {}
for chr in str:
  try:
    freqs[chr] += 1
  except KeyError:
    freqs[chr] = 1

for key in sorted(freqs.keys()):
  print('Character: ', key, ' frequency: ', freqs[key])
