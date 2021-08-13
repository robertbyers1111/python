#!/usr/bin/python3

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #
    # Write your code here.
    #

    numAHits = 0
    for d in apples:
        #print()
        #print('  a:',a)
        #print('  d:',d)
        #print('  s:',s)
        #print('a+d:',a+d)
        #print('  t:',t)
        if (a+d >= s and a+d <= t):
            numAHits +=1

    numOHits = 0
    for d in oranges:
        #print()
        #print('  b:',b)
        #print('  d:',d)
        #print('  s:',s)
        #print('b+d:',b+d)
        #print('  t:',t)
        if (b+d >= s and b+d <= t):
            numOHits +=1

    print(numAHits,numOHits)

if __name__ == '__main__':

    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    #s,t = 5,20
    #a,b = 8,17
    #m,n = 6,6
    #apple = [-5,-2,1,12,-3,5]
    #orange = [35,-5,22,-27,9,-3]

    #s,t = 7, 11
    #a,b = 5, 15
    #m,n = 3, 2
    #apple = [-2, 2, 1]
    #orange = [5, -6]

    countApplesAndOranges(s, t, a, b, apple, orange)

