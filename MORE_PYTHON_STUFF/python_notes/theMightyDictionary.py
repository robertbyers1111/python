#!/usr/bin/python3

# FROM http://pyvideo.org/pycon-us-2010/the-mighty-dictionary-55.html

for key in 'Monty', 3.14159, (2,6,4):
    print('%12s: %16X (0x%X)' % (key,hash(key), hash(key)%8) )

