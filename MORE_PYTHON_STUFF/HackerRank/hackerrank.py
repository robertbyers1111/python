#!/usr/bin/python3
import os
import sys
import math

#   +------+
#---| Loop |------------------------------------------------------------
#   +------+

#zz print('\n***\nA vs B..')

def solve(a0, a1, a2, b0, b1, b2):
    #
    # Write your code here.
    #
    ascore=0
    bscore=0
    for x,y in [(a0,b0),(a1,b1),(a2,b2)]:
        print('x,y:',x,y)
        if (x>y):
            ascore+=1
            print('a wins, current scores are:',ascore,bscore)
        elif (y>x):
            bscore+=1
            print('b wins, current scores are:',ascore,bscore)
    return(ascore,bscore)

#zz res=solve(5,6,7,3,6,10)
#zz print(res)

#   +-------------+
#---| aVeryBigSum |-----------------------------------------------------
#   +-------------+

#zz print('\n***\nBig sum..')

def aVeryBigSum(n, ar):
    sum=0
    for x in ar:
      sum+=x
    return(sum)

#zz bigsum=aVeryBigSum(5, [1000000001, 1000000002, 1000000003, 1000000004, 1000000005])
#zz print(bigsum)

#   +---------------+
#---| diagonal diff |---------------------------------------------------
#   +---------------+

#zz print('\n***\nDiagonal Diffs..')

def diagonalDifference(a):
    fwd=0
    bwd=len(a)-1
    print('len:',bwd)
    diag0=0
    diag1=0
    for x in a:
        y=x[fwd]
        z=x[bwd]
        print('x:',x,'x[%d]: %d, x[%d]: %d'%(fwd,x[fwd],bwd,x[bwd]))
        fwd+=1
        bwd-=1
        diag0+=y
        diag1+=z
    print('diag0:',diag0)
    print('diag1:',diag1)
    return(abs(diag0-diag1))

# Interactive mode only (not in pide)..
#
#    n = int(input())
#    a = []
#    for _ in range(n):
#        a.append(list(map(int, input().rstrip().split())))
#    diff = diagonalDifference(a)
#    print('diff:',diff)

# Pide mode..

#zz b=[[31, 51, 91], [21, 81, 41], [71, 2221, 31]]
#zz diff = diagonalDifference(b)
#zz print('diff:',diff)

#   +-----------+
#---| plusMinus |-------------------------------------------------------
#   +-----------+

#zz print('\n***\nPlusMinus..')

def plusMinus(arr):
    #
    # Write your code here.
    #
    pos=0.0
    neg=0.0
    zer=0.0
    for x in arr:
        if (x<0.0):
            neg+=1
        elif (x>0.0):
            pos+=1
        else:
            zer+=1
    size=len(arr)
    if (size>0):
        pctpos = pos/size
        pctzer = zer/size
        pctneg = neg/size
    else:
        pctpos = 0
        pctzer = 0
        pctneg = 0

    print('%7.4f'%pctneg)
    print('%7.4f'%pctzer)
    print('%7.4f'%pctpos)

#zz plusMinus([-1,3,-5,5,9,11])

#   +-----------+
#---| Staircase |--------------------------------------------------------------
#   +-----------+

#zz print('\n***\nStaircase..')

def staircase(n):
    print()
    print('Staircase',n)
    for i in range(1,n+1):
        j=n-i
        buf = ' '*j + '#'*i
        print(buf)

#zz staircase(-1)
#zz staircase(0)
#zz staircase(1)
#zz staircase(7)

#   +------------+
#---| miniMaxSum |-------------------------------------------------------------
#   +------------+

#zz print('\n***\nminiMaxSum..')

def miniMaxSum(arr):
    minsum=0xFFFFFFFF
    maxsum=0

    grandtotal=0
    for i in arr:
      grandtotal += i
    #print('sum of all:',grandtotal)

    for i in arr:
      foursum = grandtotal - i
      if (foursum < minsum):
        minsum = foursum
      if (foursum > maxsum):
        maxsum = foursum
      #print('i:',i,'foursum:',foursum,'min:',minsum,'max:',maxsum)

    return(minsum,maxsum)

#zz mins,maxs = miniMaxSum([11,325,2,17,42,10000001])
#zz print(mins,maxs)

#   +---------------------+
#---| birthdayCakeCandles |----------------------------------------------------
#   +---------------------+

#zz print('\n***\birthdayCakeCandles..')

def birthdayCakeCandles(n, ar):

    canblow=0

    max=0
    for i in ar:
        if (i>max):
            max=i

    for i in ar:
        if (i==max):
            canblow+=1

    return(canblow)

#zz canblow = birthdayCakeCandles(5,[3,2,1,3])
#zz print('can blow out',canblow,'candles')
#zz canblow = birthdayCakeCandles(5,[3,2,1,3,3,0,1,1,1,1,1,1,0,2,3])
#zz print('can blow out',canblow,'candles')

#   +----------------+
#---| timeConversion |---------------------------------------------------------
#   +----------------+

#zz print('\n***\ntimeConversion..')

import re

def timeConversion(s):

    amhrs = {
     '00':'00',
     '01':'01',
     '02':'02',
     '03':'03',
     '04':'04',
     '05':'05',
     '06':'06',
     '07':'07',
     '08':'08',
     '09':'09',
     '10':'10',
     '11':'11',
     '12':'00'
    }

    pmhrs = {
     '00':'12',
     '01':'13',
     '02':'14',
     '03':'15',
     '04':'16',
     '05':'17',
     '06':'18',
     '07':'19',
     '08':'20',
     '09':'21',
     '10':'22',
     '11':'23',
     '12':'12'
    }

    x = re.split(':|M', s)
    hr,mn,secAP = x[0:3]
    sec = secAP[0:2]
    if (secAP[2] == 'P'):
      newhr = pmhrs[hr]
    else:
      newhr = amhrs[hr]
    converted = newhr+':'+mn+':'+sec
    print('s:',s,'converted:',converted)
    return(converted)

#zz timeConverted = timeConversion('00:00:00AM')
#zz timeConverted = timeConversion('00:00:00PM')
#zz timeConverted = timeConversion('12:00:00AM')
#zz timeConverted = timeConversion('12:00:00PM')
#zz timeConverted = timeConversion('07:05:45PM')

#   +-----------------+
#---| gradingStudents |--------------------------------------------------------
#   +-----------------+

#zz print('\n***\ngradingStudents..')

def gradingStudents(grades):
    newgrades=[]
    for grade in grades:
        newgrade = grade
        if(grade > 37):
            modval = grade % 5
            if (modval == 3):
                newgrade += 2
            elif (modval == 4):
                newgrade += 1
        newgrades.append(newgrade)
    return(newgrades)

#zz newgrades = gradingStudents([79,72,73,66,40,0,100,39,35,24])
#zz print('newgrades:',newgrades)

