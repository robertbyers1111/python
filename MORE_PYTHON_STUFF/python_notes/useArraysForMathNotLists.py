#!/usr/bin/python3

# Arrays and lists are both used in Python to store data, but they don't
# serve exactly the same purposes. They both can be used to store any
# data type (real numbers, strings, etc), and they both can be indexed
# and iterated through, but the similarities between the two don't go
# much further. The main difference between a list and an array is the
# functions that you can perform to them. For example, you can divide an
# array by 3, and each number in the array will be divided by 3 and the
# result will be printed if you request it. If you try to divide a list
# by 3, Python will tell you that it can't be done, and an error will be
# thrown.

# Here's how it would work:

x = array([3, 6, 9, 12])
x/3.0
print(x)

# In the above example, your output would be:

# array([1, 2, 3, 4])

# If you tried to do the same with a list, it would very similar:

y = [3, 6, 9, 12]
y/3.0
print(y)

# It's almost exactly like the first example, except you wouldn't get a
# valid output because the code would throw an error.

# It does take an extra step to use arrays because they have to be
# declared while lists don't because they are part of Python's syntax, so
# lists are generally used more often between the two, which works fine
# most of the time. However, if you're going to perform arithmetic
# functions to your lists, you should really be using arrays instead.
# Additionally, arrays will store your data more compactly and
# efficiently, so if you're storing a large amount of data, you may
# consider using arrays as well.

