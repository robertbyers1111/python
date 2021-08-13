#!/usr/bin/python3
from pprint import pprint

#-- Use pprint module with some of its options..

x=[[1,2,3,4],[(1,11,111,1111),22,33,44],[111,('a','oranges',222),{'a':333,'bb':444},555]]
pprint(x,indent=2,width=44,depth=3)

#-- Use printf style formatting..

x = 22/7

print('%12.4f' % (x))

#-- Write some multivariate for loops..

for x,y in [(1,2),(11,22)]:
  print('x',x,'y',y)

for x,y in zip(range(5),range(100,105)):
  print('x',x,'y',y)

#-- What is screwed up about this, and why does it produce the following output?
#
#   x,y=42,7
#   for x in [0], y in [1]:
#     print('x',x,'y',y)
#   x [0] y 7
#   x False y 7

#-- Compute diagonal sums with lambdas..


m=[
 [    5,    2,    3,    4,    1],
 [   10,   40,   30,   20,   50],
 [  100,  200,  300,  400,  500],
 [ 1001, 4000, 3000, 2000, 5000],
 [50000,20000,30000,40000,10000]
]

for reverse in [True, False]:
  func = reverse and (lambda s: sum(s[len(s)-i-1][i] for i in range(len(s)))) or (lambda s: sum(s[i][i] for i in range(len(s)))) 
  diagsum = func(m)
  print('reverse ',end='') if reverse else print('forward ',end='')
  print('diag sum:',diagsum)

#-- Use a list comprehension to produce a list of lists..

m,n=8,9

l1=[[i**i for i in range(m)] for j in range(n)]
pprint(l1,width=44)

#-- Use a ternery operator inside a list comprehension..
d1 = {k:(k**2 if k%2 else -k*1000) for k in range(10)}
pprint(d1,indent=2,width=20)
# e.g., x = [m**2 if m > 10 else m**4 for m in range(50)]

#-- Use a dictionary comprehension..
d2 = {k:(k**k if k%2 else -10000*k) for k in range(11)}
pprint(d2,indent=2,width=20)

#-- Use a dictionary comprehension with keys 'c', 'd', 'e',... and values are lists of lists from above..

d3 = {chr(k):k*1000 for k in range(ord('a'),ord('m')+1)}
pprint(d3,indent=2,width=20)

#-- What is the solution to this dictionary comprehension issue?..

#   I'm practicing some python syntax exercises and I decided to write a
#   dictionary comprehension based on a similarly designed list
#   comprehension. But while the later is OK, the former results in a
#   syntax error.
#
#   This is my list comprehension..
#
#   >>> l = [z**z if z%2 else z for z in range(5)]
#   [0, 1, 2, 27, 4]
#
#   and this is my dictionary comprehension..
#
#   >>> d = {z:z**z if z%2 else z:z for z in range(5)}
#
#       SyntaxError: invalid syntax
#
#   is there a way to write a dictionary comprehension that is similar in
#   design to my list comprehension?

d4 = {z:(z**z if z%2 else z) for z in range(5)}
pprint(d4,indent=2,width=20)

#-- Iterate through a dictionary in key-sorted order..
for k in sorted(d3.keys()):
  print('k:',k,'v:',d3[k])

#-- Obtain several lines from stdin to fill a list with integers Use split and strip. Use prompt string inside the func call (rather than a separate call to print())..

with open('/etc/hosts') as f:
  for line in f.read().split('\n'):
    print('line:',line)

#-- Open a file, write to a file..

with open('/tmp/wtf.wtf','w') as f:
  print('type(f):',type(f))
  print('dir(_io.TextIOWrapper):',dir('_io.TextIOWrapper'))
  f.write('abc')

#-- Develop a class..

class Wtf():
  def __init__(self):
    self.bobo = 42
  def add(self,bop=7):
    self.bop=bop
  def show(self):
    print()
    print('   bobo:',self.bobo)
    print('    bop:',self.bop)

x = Wtf()
x.add()
x.show()
x.add(6)
x.show()

#-- Use list unpacking to pass variable number of args..

def wtf(*argus,**argus2):

  print()
  print('zzz')

  for arg in argus:
    print('   arg:',arg)

  for k,v in argus2:
    print('   k:',k,'v:',v)

wtf(1)
wtf(1,(11,22),[111,222,333])
wtf(10,(110,220),[1110,2220,3330], {'bay':[1,2,3,{'a':7,'b':8},'e']})

#-- Use dictionary unpacking to combine two dictionaries..

a={'a':42,'bb':{0:100,1:101,'z':107},'b':47}
b={1:44,-0.3:44}
c={**a,**{**b}}
pprint(c,indent=2,width=8)
d={**a,**b}
pprint(d,indent=2,width=8)

#-- Use 'zip()' in an example..

a=[1,2,3]
b=[11,22,33,44]
c=zip(a,b)
print()
for d in c:
  print('d:',d)

a=[1,2,3]
b=[11,22,33,44]
c=a+b
print()
for d in c:
  print('d:',d)

a={1:11,2:22}
b={3:333,4:444}
c=zip(a,b)
print()
for d in c:
  k,v=d
  print('k:',k,'v:',v)

a={'a':42,'bb':{0:100,1:101,'z':107},'b':47}
b={1:44,-0.3:44}
e=zip(a,b)
print()
for f in e:
  print('f:',f)

#-- Use 'map()' in an example..

#-- Use 'any()' in an example..

#-- Use regular expressions..

#-- Convert this to a simpler expression using 'in'..
#
#       if socket.gethostname() == "bristle" or socket.gethostname() == "rete":
#         DEBUG = False
#       else:
#         DEBUG = True

import socket
DEBUG = (True if socket.gethostname() in ['xmbInspiro2018','bristle','rete'] else False)
print('DEBUG:',DEBUG)
print(socket.gethostname())

#-- Write something using closures..

#-- Write something using decorators..

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-- FROM eInfochips interview 2018-0416..

#-- What are fixtures..

#-- How to handle missing import modules?..

#-- What are the primary features of a Python testing framework?

#-- How to do parallel testing?

#-- How to register a shutdown function?

def exitfunc():
  print('\nThat\'s all, folks!')
import atexit
atexit.register(exitfunc)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

