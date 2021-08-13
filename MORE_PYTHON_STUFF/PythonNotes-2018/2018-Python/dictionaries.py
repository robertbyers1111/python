#!/usr/bin/python

# dictionaries in python

a = {'aa':25, 'bb':33, 'cc':-17, 'dd':0}
print(a)

# Note a.keys() returns type 'dict_keys'
# .. to get a list, use 'list(a.keys())

print(type(a))
print(type(a.keys()))
print(type(list(a.keys())))

expons = {
  2:'squared',
  3:'cubed', 
  4:'to the 4th power',
  5:'to the 5th power',
  6:'to the 6th power',
  7:'to the 7th power',
  8:'to the 8th power',
  9:'to the 9th power'
}

# dict comprehensions..

n=10
expon=9
b = {x: x**expon for x in range(1,n+1)}

# looping through dictionaries with 'items()'..

print()
print('first',n, 'integers', expons[expon])

for items in b.items():
  print(items)

print()
print('first',n, 'integers', expons[expon])

for k,v in b.items():
  print('x:',k,'x**3:',v)

