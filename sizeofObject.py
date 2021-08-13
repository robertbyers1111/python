#!/usr/bin/python3

import sys
x=1
print(sys.getsizeof(x))
#-> 28

y = ['.'*10000000]
print(sys.getsizeof(y))

#-> 72

#(lazy list?)

