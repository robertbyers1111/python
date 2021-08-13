#!/usr/local/bin/python

import pickle

# Rather than have users be constantly writing and debugging code to save
# complicated data types, Python provides a standard module called pickle. This
# is an amazing module that can take almost any Python object (even some forms
# of Python code!), and convert it to a string representation; this process is
# called pickling. Reconstructing the object from the string representation is
# called unpickling. Between pickling and unpickling, the string representing
# the object may have been stored in a file or data, or sent over a network
# connection to some distant machine.

# If you have an object x, and a file object f that's been opened for writing,
# the simplest way to pickle the object takes only one line of code:

a = ('ABC', 'DEF')
b = ('123', '456')
c = (a,b)
f = open('/tmp/pickleDemo.tmp', 'w')
pickle.dump(c, f)
f.close()

