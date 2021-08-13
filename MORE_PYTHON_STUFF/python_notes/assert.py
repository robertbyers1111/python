#!/usr/bin/python3

unique_characters = 'abcdefghijklmnop'

assert len(unique_characters) <= 10, 'Too many letters'

# …is equivalent to this:

if len(unique_characters) > 10:
    raise AssertionError('Too many letters')

