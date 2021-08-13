#!/usr/bin/python3

# FROM https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks

# I have a list of arbitrary length, and I need to split it up into equal
# size chunks and operate on it. There are some obvious ways to do this,
# like keeping a counter and two lists, and when the second list fills
# up, add it to the first list and empty the second list for the next
# round of data, but this is potentially extremely expensive.
#
# I was wondering if anyone had a good solution to this for lists of any
# length, e.g. using generators.
#
# I was looking for something useful in itertools but I couldn't find
# anything obviously useful. Might've missed it, though.
#
# Here's a generator that yields the chunks you want:

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

# Also you can simply use list comprehension instead of writing a
# function. Python 3:
#
# [l[i:i + n] for i in range(0, len(l), n)]

import pprint
pprint.pprint(list(chunks(range(10, 75), 10)))

# [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
#  [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
#  [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
#  [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
#  [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
#  [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
#  [70, 71, 72, 73, 74]]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# FROM https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

# yield is a keyword that is used like return, except the function will
# return a generator.

def createGenerator():
   mylist = range(3)
   for i in mylist:
       yield i*i

mygenerator = createGenerator() # create a generator

print(mygenerator) # mygenerator is an object!
# <generator object createGenerator at 0xb7555c34>

for i in mygenerator:
    print(i)

# 0
# 1
# 4

# Here it's a useless example, but it's handy when you know your function
# will return a huge set of values that you will only need to read once.

# To master yield, you must understand that when you call the function,
# the code you have written in the function body does not run. The
# function only returns the generator object, this is a bit tricky :-)

# Then, your code will be run each time the for uses the generator.

# Now the hard part:

# The first time the for calls the generator object created from your
# function, it will run the code in your function from the beginning
# until it hits yield, then it'll return the first value of the loop.
# Then, each other call will run the loop you have written in the
# function one more time, and return the next value, until there is no
# value to return.

# The generator is considered empty once the function runs but does not
# hit yield anymore. It can be because the loop had come to an end, or
# because you do not satisfy an "if/else" anymore.

# Your code explained

# Generator:

# Here you create the method of the node object that will return the generator

def _get_child_candidates(self, distance, min_dist, max_dist):

    # Here is the code that will be called each time you use the generator object:

    # If there is still a child of the node object on its left
    # AND if distance is ok, return the next child
    if self._leftchild and distance - max_dist < self._median:
        yield self._leftchild

    # If there is still a child of the node object on its right
    # AND if distance is ok, return the next child
    if self._rightchild and distance + max_dist >= self._median:
        yield self._rightchild

    # If the function arrives here, the generator will be considered empty
    # there is no more than two values: the left and the right children

# Caller:

# Create an empty list and a list with the current object reference
result, candidates = list(), [self]

# Loop on candidates (they contain only one element at the beginning)
while candidates:

    # Get the last candidate and remove it from the list
    node = candidates.pop()

    # Get the distance between obj and the candidate
    distance = node._get_dist(obj)

    # If distance is ok, then you can fill the result
    if distance <= max_dist and distance >= min_dist:
        result.extend(node._values)

    # Add the children of the candidate in the candidates list
    # so the loop will keep running until it will have looked
    # at all the children of the children of the children, etc. of the candidate
    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))

#(return result here)

# This code contains several smart parts:

# The loop iterates on a list but the list expands while the loop is
# being iterated :-) It's a concise way to go through all these nested
# data even if it's a bit dangerous since you can end up with an infinite
# loop. In this case,

# candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))

# exhausts all the values of the generator, but while keeps creating new
# generator objects which will produce different values from the previous
# ones since it's not applied on the same node.

# The extend() method is a list object method that expects an iterable
# and adds its values to the list.

# Usually we pass a list to it:

a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

# [1, 2, 3, 4]

# But in your code it gets a generator, which is good because:

# You don't need to read the values twice.

# You may have a lot of children and you don't want them all stored in
# memory.

# And it works because Python does not care if the argument of a method
# is a list or not. Python expects iterables so it will work with
# strings, lists, tuples and generators! This is called duck typing and
# is one of the reason why Python is so cool. But this is another story,
# for another question...

# You can stop here, or read a little bit to see an advanced use of a
# generator:

# Controlling a generator exhaustion

class Bank(): # let's create a bank, building ATMs
   crisis = False
   def create_atm(self):
       while not self.crisis:
           yield "$100"
hsbc = Bank() # when everything's ok the ATM gives you as much as you want
corner_street_atm = hsbc.create_atm()
print(corner_street_atm.next())
# $100
print(corner_street_atm.next())
# $100
print([corner_street_atm.next() for cash in range(5)])
# ['$100', '$100', '$100', '$100', '$100']
hsbc.crisis = True # crisis is coming, no more money!
print(corner_street_atm.next())
# <type 'exceptions.StopIteration'>
wall_street_atm = hsbc.create_atm() # it's even true for new ATMs
print(wall_street_atm.next())
# <type 'exceptions.StopIteration'>
hsbc.crisis = False # trouble is, even post-crisis the ATM remains empty
print(corner_street_atm.next())
# <type 'exceptions.StopIteration'>
brand_new_atm = hsbc.create_atm() # build a new one to get back in business
for cash in brand_new_atm:
   print(cash)
# $100
# $100
# $100
# $100
# $100
# $100
# $100
# $100
# $100

# Note: For Python3 useprint(corner_street_atm.__next__()) or
# print(next(corner_street_atm))

# It can be useful for various things like controlling access to a
# resource.

# Itertools, your best friend

# The itertools module contains special functions to manipulate
# iterables. Ever wish to duplicate a generator? Chain two generators?
# Group values in a nested list with a one liner? Map / Zip without
# creating another list?

# Then just import itertools.

# An example? Let's see the possible orders of arrival for a 4 horse
# race:

horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)
# <itertools.permutations object at 0xb754f1dc>
print(list(itertools.permutations(horses)))
# [(1, 2, 3, 4),
#  (1, 2, 4, 3),
#  (1, 3, 2, 4),
#  (1, 3, 4, 2),
#  (1, 4, 2, 3),
#  (1, 4, 3, 2),
#  (2, 1, 3, 4),
#  (2, 1, 4, 3),
#  (2, 3, 1, 4),
#  (2, 3, 4, 1),
#  (2, 4, 1, 3),
#  (2, 4, 3, 1),
#  (3, 1, 2, 4),
#  (3, 1, 4, 2),
#  (3, 2, 1, 4),
#  (3, 2, 4, 1),
#  (3, 4, 1, 2),
#  (3, 4, 2, 1),
#  (4, 1, 2, 3),
#  (4, 1, 3, 2),
#  (4, 2, 1, 3),
#  (4, 2, 3, 1),
#  (4, 3, 1, 2),
#  (4, 3, 2, 1)]

# Understanding the inner mechanisms of iteration

# Iteration is a process implying iterables (implementing the __iter__()
# method) and iterators (implementing the __next__() method). Iterables
# are any objects you can get an iterator from. Iterators are objects
# that let you iterate on iterables.

