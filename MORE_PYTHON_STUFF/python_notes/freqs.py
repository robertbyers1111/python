#!/usr/bin/python3

# Find the most frequent value in a list.

test = [1,2,3,4,2,2,3,1,4,4,4]
print(max(set(test), key=test.count))

#-> 4

