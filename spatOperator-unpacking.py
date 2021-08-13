#!/usr/bin/python3

#19. Unpack function arguments using splat operator.

# The splat operator offers an artistic way to unpack arguments lists.
# Please refer the below example for clarity.

def test(x, y, z):
	print(x, y, z)

testDict = {'x': 1, 'y': 2, 'z': 3} 
testList = [10, 20, 30]

test(*testDict)
test(**testDict)
test(*testList)

#1-> x y z
#2-> 1 2 3
#3-> 10 20 30

