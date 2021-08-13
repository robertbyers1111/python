#!/usr/bin/python3

#-- Use pprint module with some of its options..

from pprint import pprint
x=[[1,2,3,4],[(1,11,111,1111),22,33,44],[111,('a','oranges',222),{'a':333,'bb':444},555]]
pprint(x,indent=1,width=10)

#-- Use printf style formatting..

x = 22/7
print('\npi=%27.11f=pi'%x)

#-- Write some multivariate for loops..

print()
for x,y in enumerate(range(10,0,-1)):
  print('x:',x,'y:',y)

print()
for x,y in [[1,2],[3,4],[55,66]]:
  print('x:',x,'y:',y)

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

print()
for reverse in [True,False]:
  sumfunc = reverse and (lambda s: sum(s[len(s)-i-1][i] for i in range(len(s)))) or (lambda s: sum(s[i][i] for i in range(len(s))))
  print('reverse',end=' ') if reverse else print('forward',end=' ')
  print('diag sum:',sumfunc(m))

#-- Use a list comprehension to produce a list of lists..

m,n=8,9

print()
l = [[x**y for x in range(m)] for y in range(n)]
pprint(l,indent=2,width=55)

#-- Use a ternery operator inside a list comprehension..
print()
l = [x**3 if x%2 else (-x)**3 for x in range(15)]
print(l)

# e.g., x = [m**2 if m > 10 else m**4 for m in range(50)]

#-- Use a dictionary comprehension..

print()
d = {i:(i**3 if i%2 else (-i)**3) for i in range(15)}
for k,v in d.items():
  print(k,':',v)

#-- Use a dictionary comprehension with keys 'c', 'd', 'e',... and values are lists of lists from above..

print()
d = {x:x*2 if x%2 else (-x)*2 for x in range(ord('c'),ord('z'),1)}
for k,v in d.items():
  print(k,':',v)


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

d = {z:z**z if z%2 else z for z in range(8)}
print()
for k,v in d.items():
  print(k,':',v)

#-- Merge two dictionaries (with duplicate keys)

a={'a':75,'x':99,'b':101,'f':42,'c':(12,3)}
b={'a':750,'f':420}
d={**a,**b}
print()
for k in sorted(d.keys()):
  print(k,':',d[k])

#-- Iterate through a dictionary in key-sorted order..

#-- Obtain several lines from stdin to fill a list with integers Use split and strip. Use prompt string inside the func call (rather than a separate call to print())..

#-- Open a file, write to a file..

fin='/etc/hosts'
fon='/tmp/wtf.txt'
fo = open(fon,'w')
with open(fin) as f:
  for line in f:
    print('   line:',line,end='')
    fo.write('xxx'+line)
fo.close()
f.close()
with open(fon) as f:
  for line in f:
    print('   line:',line,end='')

#-- Develop a class..

class Wtf:

  def __init__(self,a=42):
    self.aa=a

  def doit(self,n=15):
    self.b = {z:z**3 if z%2 else (-z)**3 for z in range(n)}

  def show(self):
    print()
    print('aa:',self.aa)
    for k in sorted(self.b.keys()):
      print('  ',k,':',self.b[k])

x=Wtf()
y=Wtf(1)
x.doit(14)
y.doit()
x.show()
y.show()

#-- Use list unpacking to pass variable number of args..

def showwtf(*args):
  for x in args:
    print('x:',x)

aaa=42
bbbb={'a':42,'bb':420,'zzzz':42000,'ccc':4200}
showwtf('a',aaa,bbbb)

#-- Use dictionary unpacking to combine two dictionaries..

a={'a':42,'bb':420,'zzzz':42000,'ccc':4200}
bb={'aa':42,'bbb':420,'zzzzz':42000,'cccd':4200}
ccc={42:42,'bb':420,43:42000,'cccx':4200}

def showdicts(x,*args,**kwargs):
  print()
  print('x:',x)

  for a in args:
    print('a:',a)

  for k,v in kwargs.items():
    print(k,':',v)

showdicts(a,bb,ccc,y=72)

#-- Use 'zip()' in an example..
a=[(1,22),(333,4444)]
b=[(10,220),(3330,44440)]
print()
for x in (a,b):
  print('   ',x)
print()
for x in zip(a,b):
  print('   ',x)

#-- Use 'map()' in an example..

print()
c=map(a,b)
print(c)
for x in []:
  print('   map:',x)

#-- Use 'any()' in an example..

#-- Use regular expressions..
import re
print('FOUND!') if re.search('bcd','abcde') else print('not found')

#-- Convert this to a simpler expression using 'in'..
#
#       if socket.gethostname() == "bristle" or socket.gethostname() == "rete":
#         DEBUG = False
#       else:
#         DEBUG = True

import socket
DEBUG= True if socket.gethostname() in ['RmbInspiro2018','bristle','rete'] else False
print('DEBUG:',DEBUG)

#-- Write something using closures..

#-- Write something using decorators..

print()
print('Decorator demo..')

def dohtmlbody(func,*args):
  def wrapper(*args):
    print('<html><body>',end='')
    func(*args)
    print('</body></html>')
  return(wrapper)

def dobold(func,*args):
  def wrapper(*args):
    print('<b>')
    func(*args)
    print('</b>',end='')
  return(wrapper)

@dohtmlbody
@dobold
def showit(*args):
  for i,msg in enumerate(args):
    print(i,':',msg,'<br>')

showit('abc','def','xyz','123')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-- FROM eInfochips interview 2018-0416..

#-- What are fixtures..

#-- How to handle missing import modules?..

#-- What are the primary features of a Python testing framework?

#-- How to do parallel testing?

#-- How to register a shutdown function?

import atexit
def thatsall():
  print()
  print('Thats all, folks!')

atexit.register(thatsall)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
