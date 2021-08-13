#!/usr/bin/python3

#-- Use pprint module..

x=[[1,2,3,4],[11,22,33,44],[111,222,333,444]]
from pprint import pprint
pprint(x)

#-- Use printf style formatting..

x = 22/7
print('%22.11f' % x)

#-- Write some multivariate for loops..

for x,y in zip(range(5),range(3)):
  print('x',x,'y',y)

for x,y in enumerate(range(100,122,3)):
  print('x',x,'y',y)

for x,y,z in [[(1,11,111,1111,11111),22222,33333],(44444,55555,66666)]:
  print('x',x,'y',y,'z',z)

#-- What is screwed up about this, and why does it produce the following output?
#
#   x=42
#   y=7
#
#   for x in [0], y in [1]:
#     print('x',x,'y',y)
#   x [0] y 7
#   x False y 7
#
# ANS:
#   first of all, 'y' is not a parameter in this for loop, so it retains the value '7' throughout
#   x is taking on the value '[0]' in the first iteration
#   x is taking on the value of 'y in [1]' in the second iteration

#-- Compute diagonal sums with lambdas..

m=[
 [    5,    2,    3,    4,    1],
 [   10,   40,   30,   20,   50],
 [  100,  200,  300,  400,  500],
 [ 1001, 4000, 3000, 2000, 5000],
 [50000,20000,30000,40000,10000]
]

for reverse in [True,False]:
  func = reverse \
   and (lambda s: sum(s[len(s)-i-1][i] for i in range(len(s)))) \
   or (lambda s: sum(s[i][i] for i in range(len(s))))
  diagsum = func(m)
  print('reverse sum:',diagsum) if reverse else print('forward sum:',diagsum)

#-- Use a list comprehension to produce a list of lists..

m,n=5,4

o = [[[x**x for x in range(m)] for y in range(n)] for z in range(42,44)]
pprint(o,indent=2)

p = {k:v for k,v in zip(range(44,11,-3),o)}
pprint(p,indent=3)

#-- Use a ternery operator inside a list comprehension..
# e.g., x = [m**2 if m > 10 else m**4 for m in range(50)]

#-- Use a dictionary comprehension..

x={k:v for k,v in zip(range(12),[2,2,2,2,2,2,2,2,2,2,2,2,22])}
pprint(x)

j=[chr(j) for j in range(ord('c'),ord('m'),2)]
pprint(j)

k = {k:v for k,v in zip([chr(j) for j in range(ord('c'),ord('m'))],range(10007,200001,7))}
pprint(k,indent=3)

#-- Obtain user input to fill a list with integers (use split and strip)..

#ints = [int(vals.strip()) for vals in input('Enter some comma-separated integers:').split(',')]
#pprint(ints)

#-- Open a file, write to a file..
fn='/etc/hosts'
with open(fn) as f:
  for line in f:
    print(fn,', len:',len(line.strip(' 	\n')),'line:',line) if len(line.strip(' 	\n')) else True

#-- Develop a class..

#-- Use list unpacking to pass variable number of args..

#-- Use dictionary unpacking to combine two dictionaries..

#-- Use 'zip()' in an example..

#-- Use 'map()' in an example..

#-- Use 'any()' in an example..

#-- Use regular expressions..

#-- Convert this to a simpler expression using 'in'..
#
#       if socket.gethostname() == "bristle" or socket.gethostname() == "rete":
#         DEBUG = False
#       else:
#         DEBUG = True

#-- Write something using closures..

#-- Write something using decorators..

