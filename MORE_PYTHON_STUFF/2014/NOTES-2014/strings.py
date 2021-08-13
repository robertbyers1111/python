#!/usr/bin/python

#   +-------------------------+
#---| String Strip (trimming) |---
#   +-------------------------+

word = "	   abc   def	xyz	   "
print "XXX" + word + "XXX"
print "YYY" + word.strip() + "YYY"

#   +---------------+
#---| Triple Quotes |---
#   +---------------+

# strings can be surrounded in a pair of matching triple-quotes: """ or '''.
# End of lines do not need to be escaped when using triple-quotes, but they
# will be included in the string.

print """
Usage: thingy [OPTIONS] 
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""

#   +-----------------------+
#---| Repeating a character |---
#   +-----------------------+

print '-'*80

#   +-----------------------------------+
#---| String Indexes and Slice Notation |---
#   +-----------------------------------+

word = 'Leo Nate'
print "word[0]: " + word[0]
print "word[1]: " + word[1]
print "word[2]: " + word[2]
print "word[0:3]: " + word[0:3]	# "slice notation" (but '0:3' prints chars 0,1,2 and NOT 3!)
print "word[:3]: " + word[:3]
print "word[4:]: " + word[4:]

##zz Indices may be negative numbers, to start counting from the right. For example:
##zz 
##zz >>> word[-1]     # The last character
##zz 'A'
##zz >>> word[-2]     # The last-but-one character
##zz 'p'
##zz >>> word[-2:]    # The last two characters
##zz 'pA'
##zz >>> word[:-2]    # Everything except the last two characters
##zz 'Hel'
##zz 
##zz But note that -0 is really the same as 0, so it does not count from the right!
##zz 
##zz >>> word[-0]     # (since -0 equals 0)
##zz 'H'
##zz 
##zz Out-of-range negative slice indices are truncated, but don't try this for single-element (non-slice) indices:
##zz 
##zz >>> word[-100:]
##zz 'HelpA'
##zz >>> word[-10]    # error
##zz Traceback (most recent call last):
##zz   File "<stdin>", line 1, in ?
##zz IndexError: string index out of range
##zz 
##zz The best way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:
##zz 
##zz  +---+---+---+---+---+ 
##zz  | H | e | l | p | A |
##zz  +---+---+---+---+---+ 
##zz  0   1   2   3   4   5 
##zz -5  -4  -3  -2  -1

