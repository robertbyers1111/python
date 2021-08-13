#!/usr/bin/python3

#-- Use pprint module with some of its options..

x=[[1,2,3,4],[(1,11,111,1111),22,33,44],[111,('a','oranges',222),{'a':333,'bb':444},555]]

#-- Use printf style formatting..

x = 22/7

#-- Write some multivariate for loops..

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

#-- Use a list comprehension to produce a list of lists..

m,n=8,9

#-- Use a ternery operator inside a list comprehension..
# e.g., x = [m**2 if m > 10 else m**4 for m in range(50)]

#-- Use a dictionary comprehension..

#-- Use a dictionary comprehension with keys 'c', 'd', 'e',... and values are lists of lists from above..

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

#-- Iterate through a dictionary in key-sorted order..

#-- Merge two dictionaries (with duplicate keys)

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

def htmlize(func,*args):
  def wrapper(*args):
    print('<html><body>')
    func(*args)
    print('</body></html>')
  return(wrapper)

@htmlize
def show(*args):
  for x in args:
    print(x,end='<br>\n')

show('abc','def','xyz')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-- FROM eInfochips interview 2018-0416..

#-- What are fixtures..

#-- How to handle missing import modules?..

#-- What are the primary features of a Python testing framework?

#-- How to do parallel testing?

#-- How to register a shutdown function?

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
