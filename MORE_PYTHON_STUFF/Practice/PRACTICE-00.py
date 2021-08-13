#!/usr/bin/python3

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#-- Use a lambda to print a list

# ANSWER:

prfunc = lambda lst: print(*lst,sep='\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#-- Memorize which are iterable, which are immutable..

#-------------+--------------+---------------+
#             |   Iterable   |   Immutable   |
#-------------+--------------+---------------+
# bool        |              |               |
# chr         |              |               |
# dictionary  |              |               |
# frozenset   |              |               |
# int         |              |               |
# list        |              |               |
# set         |              |               |
# str         |              |               |
# tuple       |              |               |
# zip         |              |               |
#-------------+--------------+---------------+

# ANSWER:

#-------------+--------------+---------------+
#             |   Iterable   |   Immutable   |
#-------------+--------------+---------------+
# bool        |     n        |     yes       |
# chr         |     n        |     yes       |
# dictionary  |     yes      |      n        |
# frozenset   |     yes      |     yes       |
# int         |     n        |     yes       |
# list        |     yes      |      n        |
# set         |     yes      |      n        |
# str         |     yes      |     yes       |
# tuple       |     yes      |     yes       |
# zip         |     yes      |     yes?      |
#-------------+--------------+---------------+

#-- Memorize the methods for the following data types..

# higher priority..
#   set (17)
#   dict (11)
#   list (11)
#   frozenset (8)
#   tuple (2)
#
# lower priority..
#   int (8)
#   str (44)
#   zip
#   bool
#   bytes
#   chr

# ANSWER:
#
# dict (11)
#   clear, copy, get, update
#   items, keys, values, fromkeys,
#   pop, popitems, setdefault
#
# frozenset (8)
#   copy, union, intersection,
#   difference, symmetric_difference,
#   isdisjoint, issuperset, issubset,
#
# int (8)
#   real, imag, numerator, denominator,
#   conjugate, to_bytes, from_bytes, bit_length
#
# list (11)
#   append, clear, copy, extend, insert, pop, remove,
#   count, index, reverse, sort
#
# set (17)
#   add, clear, copy, discard, pop, remove,
#   isdisjoint, issuperset, issubset,
#   union, intersection,
#   difference, symmetric_difference,
#   update, intersection_update, difference_update, symmetric_difference_update,
#
# tuple (2)
#   count,index
#
# lower priority..
#   str
#   zip
#   bool
#   bytes
#   chr

# === <class 'bool'> <class 'type'> NOT iterable
#    bit_length
#    conjugate
#    denominator
#    from_bytes
#    imag
#    numerator
#    real
#    to_bytes
#
# === <class 'bytes'> <class 'type'> (iterable)
#    capitalize
#    center
#    count
#    decode
#    endswith
#    expandtabs
#    find
#    fromhex
#    hex
#    index
#    isalnum
#    isalpha
#    isdigit
#    islower
#    isspace
#    istitle
#    isupper
#    join
#    ljust
#    lower
#    lstrip
#    maketrans
#    partition
#    replace
#    rfind
#    rindex
#    rjust
#    rpartition
#    rsplit
#    rstrip
#    split
#    splitlines
#    startswith
#    strip
#    swapcase
#    title
#    translate
#    upper
#    zfill
# 
# === <built-in function chr> <class 'builtin_function_or_method'> NOT iterable
# 
# === <class 'dict'> <class 'type'> (iterable)
#    clear
#    copy
#    fromkeys
#    get
#    items
#    keys
#    pop
#    popitem
#    setdefault
#    update
#    values
# 
# === <class 'frozenset'> <class 'type'> (iterable)
#    copy
#    difference
#    intersection
#    isdisjoint
#    issubset
#    issuperset
#    symmetric_difference
#    union
# 
# === <class 'int'> <class 'type'> NOT iterable
#    bit_length
#    conjugate
#    denominator
#    from_bytes
#    imag
#    numerator
#    real
#    to_bytes
# 
# === <class 'list'> <class 'type'> (iterable)
#    copy
#    clear
#    append
#    extend
#    insert
#    remove
#    pop
#    reverse
#    sort
#    count
#    index
# 
# === <class 'set'> <class 'type'> (iterable)
#    add
#    clear
#    copy
#    difference
#    difference_update
#    discard
#    intersection
#    intersection_update
#    isdisjoint
#    issubset
#    issuperset
#    pop
#    remove
#    symmetric_difference
#    symmetric_difference_update
#    union
#    update
# 
# === <class 'str'> <class 'type'> (iterable)
#    capitalize
#    casefold
#    center
#    count
#    encode
#    endswith
#    expandtabs
#    find
#    format
#    format_map
#    index
#    isalnum
#    isalpha
#    isdecimal
#    isdigit
#    isidentifier
#    islower
#    isnumeric
#    isprintable
#    isspace
#    istitle
#    isupper
#    join
#    ljust
#    lower
#    lstrip
#    maketrans
#    partition
#    replace
#    rfind
#    rindex
#    rjust
#    rpartition
#    rsplit
#    rstrip
#    split
#    splitlines
#    startswith
#    strip
#    swapcase
#    title
#    translate
#    upper
#    zfill
# 
# === <class 'tuple'> <class 'type'> (iterable)
#    count
#    index
# 
# === <class 'zip'> <class 'type'> (iterable)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#FROM: http://www.techbeamers.com/python-interview-questions-programmers/

#-- What is the output of the following?..

def extendList(val, list=[]):
    list.append(val)
    return(list)

list1 = extendList(10)
print()
print("list1 = %s" % list1)

list2 = extendList(123,[])
print()
print("list1 = %s" % list1)
print("list2 = %s" % list2)

list3 = extendList('a')
print()
print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)

# ANSWER:
#
#   list1 = [10, 'a']
#   list2 = [123]
#   list3 = [10, 'a']
#
# Note: The evaluation of default arg expressions occurs at the time of
# function definition, not during its invocation.
#
# Follow-up: How to get the following output?
#
#    list1 = [10]
#    list2 = [123]
#    list3 = ['a']
#
# ANSWER:
#
# def extendList2(val, list=None):
#   list = [] if list is None else list
#   list.append(val)
#   return(list)

#-- Change to the user's home directory..

# ANSWER:

import os
print()
print('       current dir:',os.getcwd())
os.chdir(os.path.expanduser('~'))
print('   new current dir:',os.getcwd())

#-- What are the most common built-in types available in Python?

# ANSWER:
#
# Here is the list of most commonly used built-in types that Python
# supports:
#
#    Immutable built-in types of Python
#        Numbers
#        Strings
#        Tuples
#
#    Mutable built-in types of Python
#        List
#        Sets
#        Dictionaries

#-- COMPARE: List vs Tuple?..

# ANSWER:
#
# Lists are mutable, tuples are immutable.
# Tuples can be hashed (using it as a key for dictionaries).

#--COMPARE:  List vs Set?..

# ANSWER:
#
# 1. Sets can't contain duplicates
#
# 2. Sets are unordered
#
# 3. In order to find an element in a set, a hash lookup is used (which
#    is why sets are unordered). This makes __contains__ ('in' operator)
#    more efficient for sets than lists.
#
# 4. Sets can only contain hashable items (see #3). If you try:
#    set(([1],[2])) you'll get a TypeError.
#
# In practical applications, lists are very nice to sort and have order
# while sets are nice to use when you don't want duplicates and don't
# care about order.
#
# Also note that if you don't care about order, etc, you can use..
#
#      new_set = myset.intersection(mylist)
#
# to get the intersection between a set and a list.

#--COMPARE:  Tuple vs Set?..

#--COMPARE: def vs lambda
#
# ANSWER:
#
# 1. def can hold multiple expressions; lambda is a uni-expression function.
#
# 2. def generates a function and assigns a name to it. lambda forms a
#    function and returns the function itself.
#
# 3. def can have a return statement, lambda cannot.
#
# 4. lambdas can be used inside a list and dictionary.

#-- Use re to check if a string is an email address..

import re
lines = [
 '<abcd efgh>bob.byers1111@gmail.com<defghi>',
 '<abcd efgh> bob.byers1111#@gmail.com defghi',
 '<abcd efgh> bob.byers1111@gmail_user.com defghi',
 '<abcd efgh> bob.byers1111@gmail-user.com defghi',
 '<abcd efgh> bob.byers1111@gmail-user.com',
]

# ANSWER:

print()
for line in lines:
  status = 'YES!' if re.search('[0-9a-zA-Z\._-]+@[a-zA-Z0-9\.-]+\W', line) else 'no..'
  print(status,line)

#-- What is the output?..

list = ['a', 'b', 'c', 'd', 'e']
print()
print (list[10:])

# ANSWER:

# []

# (there won’t be an IndexError)

# You should know that trying to fetch a member from the list using an
# index that exceeds the member count (for example, attempting to access
# list[10] as given in the question) would yield an IndexError. By the
# way, retrieving only a slice at an opening index that surpasses the no.
# of items in the list won’t result in an IndexError. It will just return
# an empty list.

#-- Ternary operator..

# ANSWER:

x, y = 35, 75
print(x if x < y else y)

#-- How to use the debugger?..

# ANSWER..
#
# % python -m pdb scriptname.py
#
#            Add breakpoint: b
#          Resume execution: c
#    Step by step debugging: s
#         Move to next line: n
#          List source code: l
#       Print an expression: p

#-- Convert a list into a string, a tuple..

# ANSWER:

l = ['a','b','c','d','a']
print()
print('list:',l)

s = ''.join(l)
print('string:',s)

t = tuple(l)
print('tuple:',t)

s = set(l)
print('set:',s)

d = dict(enumerate(l))
print('dict:',d)

#-- Count occurences of 'a'..

# ANSWER:

print('l.count(a):',l.count('a'))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#-- Use a lambda to print a list

# ANSWER:

prfunc = lambda lst: print(*lst,sep='\n')

#-- What is the output?

a1=b'abAB'
a2=r'abAB'

print('\nb..')
prfunc(a1)

print('\nr..')
prfunc(a2)

#-- Use pprint module with some of its options..

x=[[1,2,3,4],[(1,11,111,1111),22,33,44],[111,('a','oranges',222),{'a':333,'bb':444},555]]

#-- Use printf style formatting..

x = 22/7

#-- Write some multivariate for loops..

#-- append to a list with two different techniques..

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

#-- Iterate through an arbitrary object..

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-- FROM eInfochips interview 2018-0416..

#-- What are fixtures..

#-- How to handle missing import modules?..

#-- What are the primary features of a Python testing framework?

#-- How to do parallel testing?

#-- How to register a shutdown function?

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
