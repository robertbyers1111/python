#!/usr/bin/python3

# Iterate through a list of dictionaries, sorted by a field from the dictionaries

response = [
 {'a':1, 'b':2222, 'LastModified':1320, 'c':33},
 {'a':11, 'LastModified':1229, 'b':222, 'c':3},
 {'LastModified':1400,'a':111, 'b':2, 'c':3333},
 {'a':1111, 'b':22, 'LastModified':180, 'c':333}
]

response = sorted(response, key=lambda k: k['LastModified']) 

for x in response:
  print('x',x)
