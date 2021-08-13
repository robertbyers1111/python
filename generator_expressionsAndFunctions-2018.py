#!/usr/bin/python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# My favorit article on generators: https://www.dataquest.io/blog/python-generators-tutorial/

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Use generator expressions or functions for large numbers of items.
#
# Use list comprehensions if you need the entire list at once.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# A generator expression is like a generator function without the function.

unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}

gen = (ord(c) for c in unique_characters)

gen
# <generator object <genexpr> at 0x00BADC10>

next(gen)
# 69

next(gen)
# 68

tuple(ord(c) for c in unique_characters)
# (69, 68, 77, 79, 78, 83, 82, 89)

# A generator expression is like an anonymous function that yields
# values. The expression itself looks like a list comprehension, but it’s
# wrapped in parentheses instead of square brackets.

# The generator expression returns… an iterator.

# Calling next(gen) returns the next value from the iterator.

# If you like, you can iterate through all the possible values and return
# a tuple, list, or set, by passing the generator expression to tuple(),
# list(), or set(). In these cases, you don’t need an extra set of
# parentheses — just pass the “bare” expression ord(c) for c in
# unique_characters to the tuple() function, and Python figures out that
# it’s a generator expression.

# Using a generator expression instead of a list comprehension can save
# both CPU and RAM. If you’re building an list just to throw it away
# (e.g. passing it to tuple() or set()), use a generator expression
# instead! 

# Here’s another way to accomplish the same thing, using a generator
# function:

def ord_map(a_string):
    for c in a_string:
        yield ord(c)

gen = ord_map(unique_characters)

# The generator expression is more compact but functionally equivalent. 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# FROM http://www.siafoo.net/article/52

# There is a downside to list comprehensions: the entire list has to be
# stored in memory at once. This isn't a problem for small lists like the
# ones in the above examples, or even of lists several orders of
# magnitude larger. But eventually this becomes pretty inefficient.

# Generator expressions are newish in Python 2.4, and possibly the least
# publicized Cool Thing About Python ever. As in, I just found out about
# them. Generator expressions do not load the whole list into memory at
# once, but instead create a 'generator object' so only one list element
# has to be loaded at any time.

# Of course, if you actually need to use the entire list for something,
# this doesn't really help much. But if you're just passing it off to
# something that takes any iterable object -- like a for loop -- you
# might as well use a generator function.

# Generator expressions have the same syntax as list comprehensions, but
# with parentheses around the outside instead of brackets:

# Since we're going for efficiency, I'm using a tuple instead of a list ;)

numbers = (1,2,3,4,5)

squares_under_10 = (number*number for number in numbers if number*number < 10)

# squares_under_10 is now a generator object, from which each successive
# value can be gotten by calling .next()

for square in squares_under_10:
    print(square)

# prints '1 4 9'

# This is ever so slightly more efficient than using a list
# comprehension.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Use generator expressions for large numbers of items.
#
# Use list comprehensions if you need the entire list at once.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# If neither of these is true, just do whatever you want. It's probably good
# practice to use generator expressions unless there's some reason not to,
# but you're not going to see any real difference in efficiency unless the
# list is very large.

# As a final note, generator expressions only need to be surrounded by
# one set of parentheses. So, if you're calling a function with only a
# generator expression, you only need one set of parentheses. This is
# valid Python: some_function(item for item in list).

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Generators are iterators, a kind of iterable you can only iterate over
# once. Generators do not store all the values in memory, they generate
# the values on the fly:

mygenerator = (x*x for x in range(3))

print('\nFirst time iterating via generator..')
for i in mygenerator:
  print(i)

# 0, 1, 4

print('\nSecond time iterating via generator..')
for i in mygenerator:
  print(i)

# <nothing prints!>

# It is just the same except you used () instead of []. BUT, you cannot
# perform for i in mygenerator a second time since generators can only be
# used once: they calculate 0, then forget about it and calculate 1, and
# end calculating 4, one by one.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# My favorit article on generators: https://www.dataquest.io/blog/python-generators-tutorial/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
