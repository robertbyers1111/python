#!/usr/bin/python3

# We can set breakpoints in our Python script with the help of the <pdb>
# module. Please follow the below example.

import pdb

# We can specify <pdb.set_trace()> anywhere in the script and set a
# breakpoint there. It’s extremely convenient.

x=42
y=7
pdb.set_trace()

x,y=y,x
pdb.set_trace()
