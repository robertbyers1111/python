#!/usr/bin/python3

def showzip(c):
  for i in c:
    print(i)

a=[1,2,3]
b=[11,22,33]
c=zip(a,b)
showzip(c)

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[11,22,33],[44,55,66],[77,88,99]]
c=zip(a,b)
showzip(c)

