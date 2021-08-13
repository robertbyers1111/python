
import re

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# filename = 'bogus.jpg'
#
# m = re.search('(\S+)\.(\S+)', filename)
#
# if m:
#   print(m.groups()[0])
#   print(m.groups()[1])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# pi = 3.14
# m = re.search('(\d+)\.(\d+)', str(pi))
# if m:
#     print(f"int: {m.groups()[0]}, frac: {m.groups()[1]}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

input = "pi: 3.14"
m = re.search('([a-zA-Z]+):\s*([\d.]+)', input)
if m:
    print(f"name: {m.groups()[0]}, int: {m.groups()[1]}")
