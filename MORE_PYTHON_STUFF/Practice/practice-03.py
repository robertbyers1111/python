#!/usr/bin/python3

#-- Use pprint module..

x=[[1,2,3,4],[11,22,33,44],[111,222,333,444]]

#-- Use printf style formatting..

x = 22/7

print('%9.6f' % x)

#-- Write some multivariate for loops..

#-- What is screwed up about this, and why does it produce the following output?
#
#   x=42
#   y=7
#
#   for x in [0], y in [1]:
#     print('x',x,'y',y)
#   x [0] y 7
#   x False y 7

x=[42,41,40,39]
y=['a','b','c','d']

for i,j in zip(x,y):
  print('i:',i,'j:',j)

#-- Compute diagonal sums with lambdas..

m=[
 [    5,    2,    3,    4,    1],
 [   10,   40,   30,   20,   50],
 [  100,  200,  300,  400,  500],
 [ 1001, 4000, 3000, 2000, 5000],
 [50000,20000,30000,40000,10000]
]

func=(lambda s: [s[i][len(s)-1] for i in range(len(s))])
#unc=(lambda s: sum(s[len(s)-i-1][i] for i in range(len(s))))
z=func(m)
print('xxx',z)

for reverse in [True,False]:
  func = reverse and (lambda s: sum(s[len(s)-i-1][i] for i in range(len(s)))) or (lambda s: sum(s[i][i] for i in range(len(s))))
  diagsum=func(m)
  print('reverse:',diagsum) if reverse else print('forward:',diagsum)

for reverse in [True,False]:
  func = reverse and (lambda s: sum(s[len(s)-i-1][i] for i in range(len(s)))) or (lambda s: sum(s[i][i] for i in range(len(s))))
  diagsum = func(m)
  print('reverse',diagsum) if reverse else print('forward',diagsum)

#for reverse in [True,False]:
#   func = reverse and (lambda s: sum(s[len(s)-i-1][i] for i in range(len(s)))) or (lambda s: sum(s[i][i] for i in range(len(s))))
#   diagsum = func(m)
#   print('reverse sum is',diagsum) if reverse else print('forward sum is:',diagsum)
#


print('len:',len(m))

#-- Use a list comprehension to produce a list of lists..

m=8
n=9

o = [[y**2 for y in range(n)] for x in range(m)]
for z in o:
  print('z:',z)

#-- Use a ternery operator inside a list comprehension..

x = [m*m if m % 2 else m for m in range(10)]
#x = [m**2 if m > 10 else m**4 for m in range(50)]

for z in x:
  print('z:',z)
# e.g., x = [m**2 if m > 10 else m**4 for m in range(50)]

#-- Use a dictionary comprehension..

#-- Obtain user input to fill a list with integers (use split and strip)..

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

