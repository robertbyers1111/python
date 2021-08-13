#!/usr/bin/python3

# Adding the '=[]' makes the variable static and local !!!

def foo(var,values=[]):
  values.append(var)
  print(values)
  return values

foo(11)
foo(22)
foo(33)
vox = foo(44)
print(vox)

