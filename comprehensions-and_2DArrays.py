
From: http://www.i-programmer.info/programming/python/3942-arrays-in-python.html

#   +----------------+
#---| Comprehensions |---
#   +----------------+

A comprehension is roughly speaking just an expression that specifies a
sequence of values - think of it as a compact for loop. In Python a
comprehension can be used to generate a list.

This means that we can use a comprehension to initialize a list so that
it has a predefined size. The simplest form of a list comprehension is

[expression for variable in list]

For example, to create the list equivalent of a ten-element array you
could write:

myList=[0 for i in range(10)]

Following this you have a ten-element list and you can write

myList[i]=something

without any worries - as long as i<10.

You can also use the for variable in the expression. For example:

myList=[i for i in range(10)]

sets myList to [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] and

myList=[i*i for i in range(10)]

sets myList to [0, 1, 4, 9, 16, 25, 36, 49, 64, 81].

The idea is that if you want to treat a list as an array then
initializing it in this way can be thought of as the Python equivalent
of dimensioning the array.

#   +----------------+
#---| Two dimensions |---
#   +----------------+

It has to be said that one-dimensional arrays are fairly easy - it is
when we reach two or more dimensions that mistakes are easy to make. For
a programmer moving to Python the problem is that there are no explicit
provisions for multidimensional arrays. As a list can contain any type
of data there is no need to create a special two-dimensional data
structure. All you have to do is store lists within lists - after all
what is a two-dimensional array but a one-dimensional array of rows.

In Python a 2x2 array is [[1,2],[3,4]] with the list [1,2] representing
the first row and the list [3,4] representing the second row. You can
use slicing to index the array in the usual way. For example, if

myArray=[[1,2],[3,4]]

then

myArray[0]

is the list [1,2] and

myArray[0][1]

is [1,2][1], i.e. 2.

As long as you build your arrays as nested lists in the way described
then you can use slicing in the same way as you would array indexing.

That is:

myArray[i][j]

is the i,jth element of the array.

For example, to do something with each element in myArray you might
write:

for i in range(len(myArray)):
 for j in range(len(myArray[i])):
  print myArray[i][j]

Where len(myArray) us used to get the number of rows and
len(myArray[i])) to get the number of elements in a row. Notice that
there is no need for all of the rows to have the same number of
elements, but if you are using a list as an array this is an assumption
you need to enforce.

Notice that in the two-dimensional case the non-indexed for loop can
also prove useful, but you cannot avoid a nested loop:

for row in myArray:
 for e in row:
  print e

You can also use the index method to recover the i,j type index of an
element, but you have to be careful how you do it. For example, to print
the row and column index of the element:

for row in myArray:
 for e in row:
  print myArray.index(row),row.index(e)

Finally, we have the problem of initializing the array so that

myArray[i][j]=value

doesn't generate an error. In other words, what is the two-dimensional
equivalent of the dimension statement using comprehensions?

The answer is that we need to use a nested comprehension to create the
list. For example, to create a 3x3 matrix we could use:

myArray=[[0 for j in range(3)] for i in range(3)]

To understand this comprehension you need to see that the inner
comprehension is just:

[0 for j in range(3)]

which creates a row, and then the outer comprehension just creates a
list of rows.

As before, you can use the index variables in the expression. For
example:

myArray=[[i*j for j in range(3)] for i in range(3)]

In general, if you want to work with an m by n array use:

myArray=[[0 for j in range(n)] for i in range(m)]

and everything should work as you would expect.

#   +-------------------------+
#---| Advanced comprehensions |---
#   +-------------------------+

In Python there are lots of clever ways of doing things that you
generally wouldn't dream of in a lesser language. For example, a
comprehension can be used to generate a list based on other lists. It is
generally easy to get hold of the rows of a matrix:

for row in myArray:
  do something with row

but getting at the columns as lists is much more difficult. However,
with the help of a comprehension it is easy to get column j as a list:

col=[row[j] for row in myArray]

Using the same idea, if you want a transpose a matrix then usually you
need to write two explicit for loops but to do the job in Python you can
simply write:

myArray= [[row[i] for row in myArray] 
          for i in range(len(myArray))]

Python has lots of, usually functional, ways of working with arrays that
aren't encountered in other languages. This should be enough to get you
started on using lists as arrays and in more creative ways.

