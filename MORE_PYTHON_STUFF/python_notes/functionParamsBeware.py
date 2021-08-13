#!/usr/bin/python3

# One thing to keep in mind is that default values are evaluated when the
# function is compiled, which is an important distinction if the value is
# mutable. The behaviour below is probably not what was intended:

def foo(val, arr=[]):
    arr.append(val)
    return arr

# When using the function:

print(foo(1))
print(foo(2))
# [1]
# [1, 2]

# This happens because the default value (an empty list) was evaluated
# once, when the function was compiled, then re-used on every call to the
# function. To get an empty list on every call, the code needs to be
# written like this:

def foo(val, arr=None):
    if arr is None:
        arr = []
    arr.append(val)

    return arr

# When using the function, we get:

print(foo(1))
print(foo(2))
# [1]
# [2]
