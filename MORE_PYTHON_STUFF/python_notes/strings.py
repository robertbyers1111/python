#!/usr/local/bin/python

# Not sure if this is necessary
import string

#   +---------+
#---| Strings |---
#   +---------+
#
#   They can be enclosed in single quotes ('...') or double quotes ("...") with
#   the same result. '\' can be used to escape quotes:
#
#   >>> 'spam eggs'  # single quotes
#   'spam eggs'
#
#   >>> 'doesn\'t'  # use \' to escape the single quote...
#   "doesn't"
#
#   >>> "doesn't"  # ...or use double quotes instead
#   "doesn't"
#
#   >>> '"Yes," he said.'
#   '"Yes," he said.'
#
#   >>> "\"Yes,\" he said."
#   '"Yes," he said.'
#
#   >>> '"Isn\'t," she said.'
#   '"Isn\'t," she said.'

print('spam eggs')
print('doesn\'t')
print("doesn't")
print('"Yes," he said.')
print("\"Yes,\" he said.")
print('"Isn\'t," she said.')

#   +--------+
#---| Length |---
#   +--------+

junk = 'this is a string of length: '
print(junk + str(len(junk))) # string length

#   +-------------------------------+
#---| Raw Strings (string literals) |
#   +-------------------------------+
#
# what is this?
#
# r'ab\n'
#
# .. it means the backslash is just a normal character.
#
# From docs.python.org ...
#
# When an 'r' or 'R' prefix is present, a character following a backslash
# is included in the string without change, and all backslashes are left
# in the string. For example, the string literal r"\n" consists of two
# characters: a backslash and a lowercase 'n'. String quotes can be
# escaped with a backslash, but the backslash remains in the string; for
# example, r"\"" is a valid string literal consisting of two characters: a
# backslash and a double quote; r"\" is not a valid string literal (even a
# raw string cannot end in an odd number of backslashes). Specifically, a
# raw string cannot end in a single backslash (since the backslash would
# escape the following quote character). Note also that a single backslash
# followed by a newline is interpreted as those two characters as part of
# the string, not as a line continuation.
#
# When an 'r' or 'R' prefix is used in conjunction with a 'u' or 'U'
# prefix, then the \uXXXX and \UXXXXXXXX escape sequences are processed
# while all other backslashes are left in the string. For example, the
# string literal ur"\u0062\n" consists of three Unicode characters: 'LATIN
# SMALL LETTER B', 'REVERSE SOLIDUS', and 'LATIN SMALL LETTER N'.
# Backslashes can be escaped with a preceding backslash; however, both
# remain in the string. As a result, \uXXXX escape sequences are only
# recognized when there are an odd number of backslashes.
#
#   print('C:\some\name')
#   C:\some
#   ame
#
#   print(r'C:\some\name')
#   C:\some\name
#
#   +---------------+
#---| Concatenation |---
#   +---------------+
#
#   Repeat 'un' 3 times, then append '-ium'
#
#   3*'un' + '-ium'
#   ununun-ium
#
#   'x'*10
#   xxxxxxxxxx

print('C:\some\name')
print(r'C:\some\name')
print(3*'un'+'-ium')
print('xY'*10)
print("xY"*10)

#   +---------------------+
#---| Auto-concatenation. |---
#   +---------------------+
#
# Two or more string literals (i.e. the ones enclosed between quotes) next to
# each other are automatically concatenated (!!!)
#
#   >>> 'Py' 'thon'
#   'Python'
#
# This only works with two literals, not with variables or expressions:
#
#   >>> prefix = 'Py'
#   >>> prefix 'thon'  # can't concatenate a variable and a string literal
#     ...
#   SyntaxError: invalid syntax
#
#   >>> ('un' * 3) 'ium'
#     ...
#   SyntaxError: invalid syntax
#
# If you want to concatenate variables or a variable and a literal, use +:
#
#   >>> prefix + 'thon'
#   'Python'
#
# This feature is particularly useful when you want to break long strings:
#
#   >>> text = ('Put several strings within parentheses '
#               'to have them joined together.')
#
#   >>> text
#   'Put several strings within parentheses to have them joined together.'

#   +------------------------------------+
#---| Loop through each line of a string |---
#   +------------------------------------+

theData = """
anvilIp_192_168_225_3:1486 radiumwater5_vm eth3:5ce_9 vharirian
anvilIp_192_168_225_4:1486 radiumwater5_vm eth3:5ce_10 vharirian
anvilIp_192_168_225_5:1486 radiumwater5_vm eth3:5ce_11 vharirian
"""

for line in theData.split('\n'):
   print('line: ', line)

#   +-------------------------+
#---| String Strip (trimming) |---
#   +-------------------------+

word = "	   abc   def	xyz	   "
print("XXX" + word + "XXX")
print("YYY" + word.strip() + "YYY")

#   +---------------+
#---| Triple Quotes |---
#   +---------------+

# strings can be surrounded in a pair of matching triple-quotes: """ or '''.
# End of lines do not need to be escaped when using triple-quotes, but they
# will be included in the string.

print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#   +-----------------------+
#---| Repeating a character |---
#   +-----------------------+


#   +-----------------------------------+
#---| String Indexes and Slice Notation |---
#   +-----------------------------------+

word = 'Leo,Nate'
print("word[0]: " + word[0])
print("word[1]: " + word[1])
print("word[2]: " + word[2])
print("word[0:3]: " + word[0:3])
print("word[0:4]: " + word[0:4])
print("word[:3]: " + word[:3])
print("word[4:]: " + word[4:])

# Indices may be negative numbers, to start counting from the right. For example:
#
# >>> word[-1]     # The last character
# 'A'
# >>> word[-2]     # The last-but-one character
# 'p'
# >>> word[-2:]    # The last two characters
# 'pA'
# >>> word[:-2]    # Everything except the last two characters
# 'Hel'
#
# But note that -0 is really the same as 0, so it does not count from the right!
#
# >>> word[-0]     # (since -0 equals 0)
# 'H'
#
# Out-of-range negative slice indices are truncated, but don't try this for single-element (non-slice) indices:
#
# >>> word[-100:]
# 'HelpA'
# >>> word[-10]    # error
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# IndexError: string index out of range
#
# The best way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:
#
#  +---+---+---+---+---+
#  | H | e | l | p | A |
#  +---+---+---+---+---+
#  0   1   2   3   4   5
# -5  -4  -3  -2  -1


