#!/usr/bin/python3

# Form a unified list without using any loops.

import itertools
test = [[-1, -2], [30, 40], [25, 35]]
print(list(itertools.chain.from_iterable(test)))

#-> [-1, -2, 30, 40, 25, 35]

# If you have an input list with nested lists or tuples as elements, then
# use the below trick. However, the limitation here is that it’s using a
# for Loop.

def unifylist(l_input, l_target):
    for it in l_input:
        if isinstance(it, list):
            unifylist(it, l_target)
        elif isinstance(it, tuple):
            unifylist(list(it), l_target)
        else:
            l_target.append(it)
    return l_target

test =  [[-1, -2], [1,2,3, [4,(5,[6,7])]], (30, 40), [25, 35]]

print(unifylist(test,[]))

#Output => [-1, -2, 1, 2, 3, 4, 5, 6, 7, 30, 40, 25, 35]

# Another simpler method to unify the list containing lists and tuples is
# by using the Python’s <more_itertools> package. It doesn’t require
# looping. Just do a <pip install more_itertools>, if not already have
# it.

import more_itertools

test = [[-1, -2], [1, 2, 3, [4, (5, [6, 7])]], (30, 40), [25, 35]]

print(list(more_itertools.collapse(test)))

#Output=> [-1, -2, 1, 2, 3, 4, 5, 6, 7, 30, 40, 25, 35]
