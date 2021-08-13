#!/usr/bin/python3
# Four ways to reverse string/list.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reverse the list itself.

testList = [1, 3, 5]
testList.reverse()
print(testList)

#-> [5, 3, 1]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reverse while iterating in a loop.

for element in reversed([1,3,5]):
  print(element)

#1-> 5
#2-> 3
#3-> 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reverse a string in line.

print("Test Python"[::-1])

# This gives the output as ”nohtyP tseT”

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reverse a list using slicing.

print([1, 3, 5][::-1])

# The above command will give the output as [5, 3, 1].

