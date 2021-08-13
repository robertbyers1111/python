#!/usr/bin/python3

# Return multiple values from functions.

# Not many programming languages support this feature. However, functions
# in Python do return multiple values.

# Please refer the below example to see it working.

# function returning multiple values.
def x():
	return 1, 2, 3, 4

# Calling the above function.
a, b, c, d = x()

print(a, b, c, d)

#-> 1 2 3 4
