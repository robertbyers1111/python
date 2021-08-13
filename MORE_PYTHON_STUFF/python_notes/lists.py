#!/usr/bin/python

#   +----------------+
#---| Fun With Lists |---
#   +----------------+

# Assignment to slices is also possible, and this can even change the size of
# the list or clear it entirely:

a = range(1,12)
b = ['omg', 'wtf', 'abc', 'xyz']


# THESE DO NOT WORK, they result in "TypeError: 'range' object does not support item assignment"
#
#       # Replace some items:
#
#       a[0:2] = ['OMG', 'WTF']
#       print('a =',a)
#
#       # Remove some:
#
#       a[5:7] = []
#       print('a =',a)
#
#       # Insert some:
#
#       a[1:1] = ['bletch', 'xyzzy']
#       print('a =',a)
#
#       # Insert (a copy of) itself at the beginning
#
#       a[:0] = a
#       print('a =',a)
#
#       # Clear the list: replace all items with an empty list
#
#       a[:] = []
#       print('a =',a)

# The built-in function len() also applies to lists:

print()
len(a)
print('len(a) =',len(a))

# List of lists

print()
z = [a[0:3],b[0:3]]
for zz in z:
    print('zz:',zz)

# Does a list contain an item?

print()
a = ['abc','def','xyz']
for match in ['abc', '123']:
    if match in a:
        print('YES, {} is in {}'.format(match,a))
    else:
        print('NO, {} is NOT in {}'.format(match,a))

