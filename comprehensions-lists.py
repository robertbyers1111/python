#!/usr/bin/python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# python.org 5.1.3. List Comprehensions

# List comprehensions provide a concise way to create lists. Common
# applications are to make new lists where each element is the result of some
# operations applied to each member of another sequence or iterable, or to
# create a subsequence of those elements that satisfy a certain condition.

# For example, assume we want to create a list of squares, like:

squares = []
for x in range(10):
    squares.append(x**2)

print('squares:  ', squares)

# Note that this creates (or overwrites) a variable named x that still exists
# after the loop completes. We can calculate the list of squares without any
# side effects using:

squares2 = list(map(lambda x: x**2, range(10)))
print('squares2: ',squares2)

# or, equivalently:

squares3 = [x**2 for x in range(10)]
print('squares3: ',squares3)

# ..which is more concise and readable.

# A list comprehension consists of brackets containing an expression followed
# by a for clause, then zero or more for or if clauses. The result will be a
# new list resulting from evaluating the expression in the context of the for
# and if clauses which follow it. For example, this listcomp combines the
# elements of two lists if they are not equal:

print('x,y if x!=y:', [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FROM http://www.siafoo.net/article/52

# Map and Filter at Once

# Now we get to the true power of list comprehensions. If I haven't yet
# convinced you that map and filter are generally a waste of your time,
# hopefully this will.

# Say I want to map and filter a list at the same time. In other words,
# I'd like to see the square of each element in the list where said
# element is under 4. Once more, the Python neophyte way:

numbers = [1,2,3,4,5]
squares = []
for number in numbers:
    if number < 4:
        squares.append(number*number)

# squares is now [1,4,9]

# The code is starting to expand in the horizontal direction now! Alas,
# what could we possibly do to simplify the code? We could try using map
# and filter, but I don't have a good feeling about this...

numbers = [1,2,3,4,5]
squares = map(lambda x: x*x, filter(lambda x: x < 4, numbers))

# squares is now [1,4,9]

# While map and filter were ugly before, now they're just unreadable.
# Obviously this isn't a good idea. Once more, list comprehensions save
# the day:

numbers = [1,2,3,4,5]
squares = [number*number for number in numbers if number < 4]

# square is now [1,4,9]

# This is a bit longer than the earlier list comprehension examples, but
# in my opinion still very readable. It's definitely better than a for
# loop or using map and filter.

# As you can see, a list comprehension filters then maps. If you
# absoulutely need to map then filter, things can get more complicated.
# You might even have to use nested list comprehensions, the map and
# filter commands, or a regular old for loop, depending on what is
# cleanest. That discussion, though, is outside the scope of this
# article.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# From last part of python.org 5.1.3 on list comprehensions..

vec = [-4, -2, 0, 2, 4]

# Create a new list with the values doubled
[x*2 for x in vec]

     # => [-8, -4, 0, 4, 8]

# Filter the list to exclude negative numbers
[x for x in vec if x >= 0]

     # =>  [0, 2, 4]

# Apply a function to all the elements
[abs(x) for x in vec]

     # => [4, 2, 0, 2, 4]

# Call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

     # => ['banana', 'loganberry', 'passion fruit']

# Create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]

     # => [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Note: the tuple must be parenthesized, otherwise an error is raised
#
# [x, x**2 for x in range(6)]
# File "<stdin>", line 1, in ?
#   [x, x**2 for x in range(6)]
#                ^
# SyntaxError: invalid syntax

# Flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]

[num for elem in vec for num in elem]

     # => [1, 2, 3, 4, 5, 6, 7, 8, 9]

