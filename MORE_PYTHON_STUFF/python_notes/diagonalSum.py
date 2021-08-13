#!/usr/bin/python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# FROM https://stackoverflow.com/questions/15979937/trying-to-get-a-diagonal-sum
#
# Different ways to compute a diagonal sum
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Assuming that the matrix is square, this is a standard solution using a loop:
#
# def diagonalsum(m):
#   count = 0
#   for i in xrange(0, len(m)):
#     count += m[i][i]
#   return count
#
# ... Which can be written in a more concise way, by using generator expressions and the sum function:
#
# def diagonalsum(m):
#     return sum(m[i][i] for i in xrange(len(m)))
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Use numpy.trace: http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.trace.html. It returns the sum along diagonals of the array.
#
# import numpy as np
#
# M = np.array([[2,3,1],[1,1,1],[5,6,4]])
#
# print(M.trace())
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# To get the diagonal elements you take the first in the first row, the second in the second row ... the nth in the nth row.
#
# def diagonalsum(x):
#     a = randomlists(x)
#     return sum(row[i] for i, row in enumerate(a))
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The not so concise alternative that uses a normal for loop reads
#
# def diagonalsum(x):
#     a = randomlists(x)
#     result=0
#     for i, row in enumerate(a):
#         result += row[i]
#     return result
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def diagonalsum(m,*oargs):
  if 'reverse' in oargs:
    return sum(m[len(m)-i-1][i] for i in range(len(m)))
  else:
    return sum(m[i][i] for i in range(len(m)))

m = [
 [10,20,30,4001],
 [100,200,30001,400],
 [1000,200001,3000,4000],
 [1000001,20000,30000,40000]
]

#-- Using a function..

print('\nUsing a function..\n')
diagsumForward = diagonalsum(m)
diagsumReverse = diagonalsum(m,'reverse')
print('Forward:',diagsumForward)
print('Reverse:',diagsumReverse)

#-- Using a lambda..

print('\nUsing a lambda..\n')
for reverse in [False,True]:
  sumLambda = reverse and (lambda s: sum(s[len(s)-i-1][i] for i in range(len(m)))) or (lambda s: sum(s[i][i] for i in range(len(m))))
  newdiagonal = sumLambda(m)
  print('Reverse:',newdiagonal) if reverse else print('Forward:',newdiagonal)

