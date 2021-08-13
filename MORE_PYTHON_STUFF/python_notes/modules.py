#!/usr/bin/python

import sys
from modulesmodules import exponentialize

expons = {
  1:'identity',
  2:'squared',
  3:'cubed', 
  4:'to the 4th power',
  5:'to the 5th power',
  6:'to the 6th power',
  7:'to the 7th power',
  8:'to the 8th power',
  9:'to the 9th power',
 10:'to the 10th power'
}

for i in range(1,4):
    for j in range(3,4):

      print()
      print('first',i, 'integers', expons[i])

      for k,v in exponentialize(i,j).items():
        print('     x:',k,'x**',i,'=',v)

