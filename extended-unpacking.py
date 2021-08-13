#!/usr/bin/python3

# Neat trick using a list comprehension inside a lambda..

dbg = lambda *w: [print(x,'=',eval(x)) for x in w]

a, *b, c = [1, 2, 3, 4, 5]
dbg('a')
dbg('b','c')
coolprint = dbg
coolprint('a')
coolprint('b','c')
coolprint('a','b','c')
coolprint('c','b','b','a','b','c')


# a = 1
# b = [2, 3, 4]
# c = 5

