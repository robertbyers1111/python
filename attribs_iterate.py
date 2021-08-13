#!/usr/bin/python


# BUMMER: THESE SOLUTIONS ONLY DISPLAY THE ATTRIBUTE NAMES, NOT VALUES


#---------------------------------------------------------------
def show(*args):
  print('\n')
  msg = ''
  for arg in args:
    msg += arg
  print('=====', msg)
  print

#---------------------------------------------------------------
# Assuming you have a class such as

class Cls(object):

   foo = 1
   bar = 'hello'

   def func(self):
     return 'call me'

obj = Cls()

#---------------------------------------------------------------
# Calling dir on the object gives you back all the attributes of that
# object, including python special attributes. Although some object
# attributes are callable, such as methods.

show('dir(obj)..')

print(dir(obj))

# ['__class__', '__delattr__', '__dict__', '__doc__', '__format__',
# '__getattribute__', '__hash__', '__init__', '__module__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bar',
# 'foo', 'func']

#---------------------------------------------------------------
show('filter out the special methods by using a list comprehension..')

print([a for a in dir(obj) if not a.startswith('__')])

# ['bar', 'foo', 'func']

#---------------------------------------------------------------
show( 'or if you prefer map/filters..')

print(filter(lambda a: not a.startswith('__'), dir(obj)))

# ['bar', 'foo', 'func']

#---------------------------------------------------------------
show( 'If you want to filter out the methods, you can use the builtin callable as a check..')

print([a for a in dir(obj) if not a.startswith('__') and not callable(getattr(obj,a))])

# ['bar', 'foo']

#---------------------------------------------------------------
show( 'You could also inspect the difference between your class and its parent using..')

print(set(dir(Cls)) - set(dir(object)))

# set(['__module__', 'bar', 'func', '__dict__', 'foo', '__weakref__'])

