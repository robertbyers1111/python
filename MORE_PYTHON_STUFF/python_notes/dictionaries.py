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
  9:'to the 9th power',
  99:'to the 99th power',
  256:'to the 256th power',
  512:'to the 512th power',
  1024:'to the 1024th power',
  10240:'to the 10240th power'
}


# Check if a key/value exists

mydict{}

if "checkme" in mydict:
    mydict["checkme"] += 1
else:
    mydict["checkme"] = 1

# dict comprehensions..

n=10240
expon=10240
b = {x: x**expon for x in range(1,n+1)}

# looping through dictionaries with 'items()'..

print()
print('first',n, 'integers', expons[expon])

for items in b.items():
  print(items)

print()
print('first',n, 'integers', expons[expon])

for k,v in b.items():
  print("{:5d}**{} = {}".format(k,expon,v))

