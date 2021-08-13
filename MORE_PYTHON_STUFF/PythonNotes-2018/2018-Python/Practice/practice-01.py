#!/usr/bin/python3

#-- Use pprint module..
from pprint import pprint
pprint([[1,2,3,4],[11,22,33,44],[111,222,333,444]], width=20)

#-- Use printf style formatting..
pi=22/7
print('pi is approximately: %9.6f' % pi)

#-- Write some multivariate for loops..

for x,y in [[1,2],[11,22]]:
  print('x:',x,'y:',y)

#-- Compute diagonal sums with lambdas..

m=[
 [    5,    2,    3,    4,    1],
 [   10,   40,   30,   20,   50],
 [  100,  200,  300,  400,  500],
 [ 1001, 4000, 3000, 2000, 5000],
 [50000,20000,30000,40000,10000]
]

for reverse in [True,False]:
  func = reverse and (lambda s: sum(s[len(s)-i-1][i] for i in range(len(s)))) or (lambda s: sum(s[i][i] for i in range(len(s))))
  diagsum = func(m)
  print('reverse diag sum:',diagsum) if reverse else print('forward diag sum:',diagsum)

#-- Use a list comprehension..

m=8
n=10
x = [[i**j for j in range(1,m+1)] for i in range(1,n+1)]
pprint(x,width=62)

#-- Use a dictionary comprehension..

d = {i:i**2 for i in range(n+1)}
pprint(d,width=10)

#-- Obtain user input (use split and strip)..

#ints = [int(d.strip()) for d in input().split(',')]
#print('You entered:',ints)

#-- Open a file, write to a file..

fn='/etc/hosts'
with open(fn) as f:
  for line in f:
    print(fn+':',line,end='') if len(line.strip()) else True

#-- Develop a class..

class Big():
  def __init__(self,n=15):
    self.n = n
    self.l = [i for i in range(n)]
  def reverseme(self):
    self.l = [i for i in range(len(self.l)-1,-1,-1)]
  def show(self):
    pprint(self.l,width=999)

x = Big()
x.show()
x.reverseme()
x.show()

y = Big(25)
y.show()
y.reverseme()
y.show()

#-- Use list unpacking to pass variable number of args..

def afunc(*z):
  print('\nafunc()..')
  for a in z:
    print('   a',a)

b=[11,22,33]
c=[111,222,333]

afunc('ABC')

afunc('DEF',b)

afunc('XYZ',b,c)

afunc('ZZZ',[*b,*c])

#-- Use dictionary unpacking to combine two dictionaries..

d1={'x':1, 'y':33}
d2={'a':11, 'b':202, 'c':7}
d3 = dict(**d1, **d2)

#-- Use 'zip()' and '*' to pack then unpack..

e1 = [1,2,3]
e2 = [11,22,33]
e3 = zip(e1,e2)
print('e3',*e3)

#-- Use regular expressions..
import re

#-- Convert this to a simpler expression using 'in'..
#
#       if socket.gethostname() == "bristle" or socket.gethostname() == "rete":
#         DEBUG = False
#       else:
#         DEBUG = True

f1='bristle'
f2='BRUSTLE'

for f12 in [f1,f2]:
  if f12 in ['bristle', 'rete']:
    print(f12,'ok')
  else:
    print(f12,'NOT OK')

#-- Write something using closures..

#-- Write something using decorators..

