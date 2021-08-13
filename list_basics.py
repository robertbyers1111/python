#!/usr/bin/python

#   +----------------+
#---| Fun With Lists |---
#   +----------------+

# Assignment to slices is also possible, and this can even change the size of
# the list or clear it entirely:

a = range(1,12)
b = ['omg', 'wtf', 'abc', 'xyz']


# THESE ONLY WORK IN PYTHON2 (python3 gets "TypeError: 'range' object does not support item assignment")
#
#       # Replace some items:
#
#       a[0:2] = ['OMG', 'WTF']
#       print('a =',a)
#
#       # Remove some:
#
#       a[5:7] = []
#       print('a =',a)
#
#       # Insert some:
#
#       a[1:1] = ['bletch', 'xyzzy']
#       print('a =',a)
#
#       # Insert (a copy of) itself at the beginning
#
#       a[:0] = a
#       print('a =',a)
#
#       # Clear the list: replace all items with an empty list
#
#       a[:] = []
#       print('a =',a)

# The built-in function len() also applies to lists:

print()
len(a)
print('len(a) =',len(a))

# List of lists

print()
z = [a[0:3],b[0:3]]
for zz in z:
    print('zz:',zz)

# Does a list contain an item?

print()
a = ['abc','def','xyz']
for match in ['abc', '123']:
    if match in a:
        print('YES, {} is in {}'.format(match,a))
    else:
        print('NO, {} is NOT in {}'.format(match,a))

#!/usr/bin/python3

# The try statement has another optional clause which is intended to
# define clean-up actions that must be executed under all circumstances.
#
# A finally clause is always executed before leaving the try statement,
# whether an exception has occurred or not. When an exception has
# occurred in the try clause and has not been handled by an except
# clause (or it has occurred in an except or else clause), it is
# re-raised after the finally clause has been executed. The finally
# clause is also executed “on the way out” when any other clause of the
# try statement is left via a break, continue or return statement.

def test1():
    try:
        raise KeyboardInterrupt
    finally:
        print('Goodbye, world!')

def test2():
    try:
        print('returning 1')
        return 1
    finally:
        print('returning 2')
        return 2
test1()
test2()


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

