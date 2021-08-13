#!/usr/bin/python3

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a
# single line. Suppose the following input is supplied to the program:
#
# 8
#
# Then, the output should be:
#
# 40320

def computeFactorials(arr):
  soln={}
  for number in arr:
    factorial=1
    for i in range(2,number+1):
      factorial *= i
    soln[number] = factorial
  return(soln)

factorials = computeFactorials( [ 11, 1, 18, 3, 7, 4, 14, 8, 6, 5, 12, 9, 10, 13, 15, 16, 17 ] )

for i in sorted(factorials.keys()):
  print(i,factorials[i])
