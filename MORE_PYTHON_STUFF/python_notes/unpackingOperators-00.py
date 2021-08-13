#!/usr/bin/python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# [UNPACKING OPERATORS]
#
# https://www.python.org/dev/peps/pep-0448/
#
#     *  => iterable unpacking operator
#     ** => dictionary unpacking operator
#
# Note..
#     **keywords - an arbitrary number keyword=value pairs
#
# Example..
#     **{'blue':1, 'orange':3}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(*[1], *[2], 3)
#
# 1, 2, 3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
z = dict(**{'x': 1}, y=2, **{'z': 3})
#
# {'y': 2, 'x': 1, 'z': 3}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = {'blue':1, 'orange':3}
y = {'magenta':10}
z = dict(**x,**y)
#
# {'blue': 1, 'orange': 3, 'magenta': 10}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for k,v in dict(**x, **y).items():
  print('%10s: %2d' % (k,v))
#
#      blue:  1
#    orange:  3
#   magenta: 10

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# This func accepts an arbitrary number of args..

def afunc(*z):
  print('\nafunc()..')

  if 'DEF' in z:
    print('FOUND DEF!')

  for a in z:
    print('   a',a)

b=[11,22,33]
c=[111,222,333]

#pass one arg..

afunc('ABC')
    #   a ABC

#or two..
afunc('DEF',b)

    #   a DEF
    #   a [11, 22, 33]

#or three..
afunc('XYZ',b,c)

    #   a XYZ
    #   a [11, 22, 33]
    #   a [111, 222, 333]

#or use unpacking to combine 2nd and 3rd into a single list..
afunc('ZZZ',[*b,*c])

    #   a ZZZ
    #   a [11, 22, 33, 111, 222, 333]
