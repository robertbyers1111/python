#!/usr/bin/python3
import random
import sys

#--------------------------

#-- NEED TO FIX THIS..

#zz for x,y in enumerated(['a','c','e','g','x','y'])
#zz input("zzz")

#--------------------------

#This will print
#
#[1]
#[1, 2]
#[1, 2, 3]

def f_a(a, L=[]):
    L.append(a)
    return L

print(f_a(1))
print(f_a(2))
print(f_a(3))

#--------------------------

# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:

def f_b(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f_b(1))
print(f_b(2))
print(f_b(3))

input("zzz");

#--------------------------

# KEYWORD ARGUMENTS

#accepts one required argument (voltage) and three optional arguments (state, action, and type). This function can be called in any of the following ways:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print()
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

input("zzz");

#--------------------------

# *arguments - an arbitrary number of (optional) arguments
# **keywords - an arbitrary number keyword=value pairs (must be last parameter)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

input("zzz");

#--------------------------

# SUPPLYING ARGS TO A FUNC USING * and **

args = [3, 6]
print('list(range(*args)): ', list(range(*args)))

# In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

def parrot2(voltage, state='a stiff', action='voom'):
    print()
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot2(**d)

input('zzz')

#--------------------------

#--(output too long)
#for x in sorted(sys.builtin_module_names):
#  print('   ',x)

#--------------------------

ints = set([1,1,2,3,3,3,4])
print(len(ints))

#--------------------------

for i in range(1,5):
  print(i)

#--------------------------

def myfunc():
  try:
    print('Monday')
  finally:
    print('Tuesday')

myfunc()

#--------------------------

print(list("hello"))

#--------------------------

print(int(-3/2))

#--------------------------

mylist = [10, 20, 30]
random.shuffle(mylist)
print(mylist)

#--------------------------

mylist=['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
print(mylist[:-1])

#--------------------------

print(random.seed(3))

#--------------------------

# *** Create a set with strings and perform search in set

objects = {"python", "coding", "tips", "for", "beginners"}

# Print set.
print(objects)
print(len(objects))

# Use of "in" keyword.
if "tips" in objects:
    print("These are the best Python coding tips.")

# Use of "not in" keyword.
if "Java tips" not in objects:
    print("These are the best Python coding tips not Java tips.")

#--------------------------
