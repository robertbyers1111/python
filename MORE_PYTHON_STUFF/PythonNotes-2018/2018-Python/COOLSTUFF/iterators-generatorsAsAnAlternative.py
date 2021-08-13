#!/usr/bin/python3

# From https://docs.python.org/3.4/tutorial/classes.html

# 9.10. Generators

# Generators are a simple and powerful tool for creating iterators. They
# are written like regular functions but use the yield statement
# whenever they want to return data. Each time next() is called on it,
# the generator resumes where it left off (it remembers all the data
# values and which statement was last executed). An example shows that
# generators can be trivially easy to create:

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

# Anything that can be done with generators can also be done with
# class-based iterators as described in the previous section. What makes
# generators so compact is that the __iter__() and __next__() methods
# are created automatically.

# Another key feature is that the local variables and execution state
# are automatically saved between calls. This made the function easier
# to write and much more clear than an approach using instance variables
# like self.index and self.data.

# In addition to automatic method creation and saving program state,
# when generators terminate, they automatically raise StopIteration. In
# combination, these features make it easy to create iterators with no
# more effort than writing a regular function.

# 9.11. Generator Expressions

# Some simple generators can be coded succinctly as expressions using a
# syntax similar to list comprehensions but with parentheses instead of
# brackets. These expressions are designed for situations where the
# generator is used right away by an enclosing function. Generator
# expressions are more compact but less versatile than full generator
# definitions and tend to be more memory friendly than equivalent list
# comprehensions.

# Examples:

sum(i*i for i in range(10))                 # sum of squares
# 285

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product
# 260

from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

unique_words = set(word  for line in page  for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
# ['f', 'l', 'o', 'g']

