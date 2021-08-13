#!/usr/bin/python3

#-- Use pprint module with some of its options..

x=[[1,2,3,4],[(1,11,111,1111),22,33,44],[111,('a','oranges',222),{'a':333,'bb':444},555]]

from pprint import pprint
pprint(x,indent=3,depth=2,width=11)

#-- Use printf style formatting..

x = 22/7
print('%9.4f'%x)

#-- Write some multivariate for loops..

for x,y,z in zip([1,2,3],[11,22,33],[111,222,333]):
  print('x',x,'y',y,'z',z)

for x,y,z in [1,2,3],[11,22,33],[111,222,333]:
  print('x',x,'y',y,'z',z)

#-- What is screwed up about this, and why does it produce the following output?
#
#   x,y=42,7
#   for x in [0], y in [1]:
#     print('x',x,'y',y)
#   x [0] y 7
#   x False y 7
#
#ANS: y is not a loop parameter. 'y in [1]' is the value x takes for the last iteration

#-- Compute diagonal sums with lambdas..


m=[
 [    5,    2,    3,    4,    1],
 [   10,   40,   30,   20,   50],
 [  100,  200,  300,  400,  500],
 [ 1001, 4000, 3000, 2000, 5000],
 [50000,20000,30000,40000,10000]
]

for reverse in [True,False]:
  func = reverse and (lambda s: sum(s[len(s)-i-1][i] for i in range(len(s)))) or \
  (lambda s: sum(s[i][i] for i in range(len(s))))
  diagsum=func(m)
  print('reverse',end=' ') if reverse else print('forward',end=' ')
  print('diag sum:',diagsum)

#-- Use a list comprehension to produce a list of lists..

m,n=8,9

o=[[x**2 for x in range(m)] for y in range(n)]
pprint(o,indent=4)

#-- Use a ternery operator inside a list comprehension..

l = [z**z if z%2 else z for z in range(5)]
pprint(l,width=22)

d = {z:z**z if z%2 else z:z for z in range(6)}
pprint(d,width=22)
# e.g., x = [m**2 if m > 10 else m**4 for m in range(50)]

#-- Use a dictionary comprehension..

#-- Use a dictionary comprehension with keys 'c', 'd', 'e',... and values are lists of lists from above..

#-- Iterate through a dictionary in key-sorted order..

#-- Obtain several lines from stdin to fill a list with integers Use split and strip. Use prompt string inside the func call (rather than a separate call to print())..

#-- Open a file, write to a file..

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

