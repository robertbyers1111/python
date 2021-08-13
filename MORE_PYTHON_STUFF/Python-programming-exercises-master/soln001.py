#!/usr/bin/python3

# Write a program which will find all such numbers which are divisible
# by 7 but are not a multiple of 5, between 2000 and 3200 (both
# included). The numbers obtained should be printed in a comma-separated
# sequence on a single line.

min=2000
max=3200

soln=[]
for i in range(min,max+1):
  if i % 7 == 0:
    if i % 5 != 0:
      soln.append(i)

comma=''
for i in soln:
  print(comma,i,end='')
  comma=','

