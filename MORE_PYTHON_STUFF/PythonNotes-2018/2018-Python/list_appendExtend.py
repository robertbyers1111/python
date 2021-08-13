#!/usr/bin/python3

def show(*args):
  print('\nyour list..')
  for x in args:
    print('   x:',x)

l=[22]
l.append(['a',42])
show(l)

l=[22]
l.extend(['a',42])
show(l)


