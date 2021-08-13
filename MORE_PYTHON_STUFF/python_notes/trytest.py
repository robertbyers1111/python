#!/usr/bin/python3
def test():
 try:
  print('returning 1')
  return 1
 finally:
  print('returning 2')
  return 2
test()

print(list("hello"))

mylist=['abc','cde','abcde','efg']
print(max(mylist))

mylist=['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
print(mylist[:-1])

mylist=['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
print(mylist[int(-1/2)])

import random

for i in range(10):
  mylist = [10, 20, 30, 44]
  ret = random.shuffle(mylist)
  print(ret,mylist)

print(random.seed(3))

l=[11,22,33,44,22,44,666,11,22,22]
t=tuple(l)
s=set(l)

l.extend([[444],5])

print('len(l):',len(l),'l:',l)
print('len(t):',len(t),'t:',t)
print('len(s):',len(s),'s:',s)

