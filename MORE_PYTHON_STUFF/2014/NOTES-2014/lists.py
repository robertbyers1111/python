#!/usr/bin/python

#   +----------------+
#---| Fun With Lists |---
#   +----------------+

# Assignment to slices is also possible, and this can even change the size of
# the list or clear it entirely:

##zz >>> # Replace some items:
##zz ... a[0:2] = [1, 12]
##zz >>> a
##zz [1, 12, 123, 1234]
##zz >>> # Remove some:
##zz ... a[0:2] = []
##zz >>> a
##zz [123, 1234]
##zz >>> # Insert some:
##zz ... a[1:1] = ['bletch', 'xyzzy']
##zz >>> a
##zz [123, 'bletch', 'xyzzy', 1234]
##zz >>> # Insert (a copy of) itself at the beginning
##zz >>> a[:0] = a
##zz >>> a
##zz [123, 'bletch', 'xyzzy', 1234, 123, 'bletch', 'xyzzy', 1234]
##zz >>> # Clear the list: replace all items with an empty list
##zz >>> a[:] = []
##zz >>> a
##zz []
##zz 
##zz The built-in function len() also applies to lists:
##zz 
##zz >>> len(a)
##zz 8

