#!/usr/bin/python

import datetime
import os
import re
import shutil
import sys

from datetime import datetime
from os import path
from subprocess import Popen, PIPE

#-------------------------------------------------------------------------------
#
# DO NOT USE readline() !!!
#
#-------------------------------------------------------------------------------
#
#    FROM http://stupidpythonideas.blogspot.com/2013/06/readlines-considered-silly.html
#
# Never call readlines() on a file
#
# Calling readlines() makes your code slower, less explicit, less
# concise, for absolutely no benefit.
#
# There are hundreds of questions on places like StackOverflow about
# the readlines method, and in every case, the answer is the same.
#
#    "My code is takes forever before it even gets started, but it's
#    pretty fast once it gets going."
#
# That's because you're calling readlines.
#
#    "My code seems to be worse than linear on the size of the input,
#    even though it's just a simple loop."
#
# That's because you're calling readlines.
#
#     "My code can't handle giant files because it runs out of
#     memory."
#
# That's because you're calling readlines.
#
#     "My second call to readlines returns nothing."
#
# That's not directly because you're calling readlines; it's because
# you're trying to read from a file whose read pointer is at the end.
# But the reason it's not obvious why this can't work is that you're
# using readlines.
#
# In fact, even if you don't have any of these problems, you should
# not use readlines, because it never gives you any advantage.
#
# What's wrong with readlines()?
#
# The whole point of readlines() is that it reads the entire file into
# memory at once and parses it into a list.
#
# So, you can't do anything else until it's read and parsed the whole
# file. This is why your program takes a while to start: reading files
# is slow. If you let Python and your OS interleave the "waiting for
# the disk" part with the "running your code" part, it will get
# started almost immediately, and often go a lot faster overall.
#
# And meanwhile, you're using up memory to store the whole list at
# once. In fact, you need enough memory to hold the original data, the
# strings built out of it, the list built out of those strings, and
# various bits of temporary storage. (Although the temporary storage
# goes away once readlines is done, the giant list of strings
# doesn't.) That's why you run out of memory.
#
# Also, all that memory allocation takes time. If you only use a bit
# of memory at a time, Python can keep reusing it over and over; if
# you use a bunch of memory at the same time, Python has to find room
# for all of it, causing it to call malloc more often. You're also
# making Python fight with your OS's disk cache. And if it you
# allocate too much, you can cause your system to start swapping.
# That's why your time seems superlinear. It's actually linear,
# except for a few cliffs that you fall off along the way: needing
# to malloc, needing to swap, etc. And those transitions completely
# swamp everything else and make it hard (and pointless) to measure
# the linear part.
#
# It can get even worse if you're calling readlines() on a file-like
# object that has to do some processing. For example, if you call it
# on the result of a gzip.open, it has to read and decompress the
# entire file, which means even more startup delay, even more
# temporary memory wasted, and even more opportunity for interleaving
# lost.
#
# So what should I use?
#
# 99% of the time, the answer is to just use the file itself. As the
# documentation says:
#
#     Note that it's already possible to iterate on file objects
#     using for line in file:... without calling file.readlines().
#
# The reason you're calling readlines is to get an iterable full of
# lines, right? A file is already an iterable full of lines. And it's
# a smart iterable, reading lines as you need them, with some clever
# buffering under the covers.
#
# This following two blocks of code do almost the same thing:
#
#     with open('foo.txt') as f:
#         for line in f.readlines():
#             dostuff(line)
#
#     with open('foo.txt') as f:
#         for line in f:
#            dostuff(line)
#
# Both of them call dostuff on each line in foo.txt. The only
# difference is that the first one reads all of foo.txt into memory
# before starting to loop, while the second one just reads a buffer at
# a time, automatically, while looping.
#
# What if I actually need a list rather than just some arbitrary
# iterable?
#
# Make a list out of it:
#
#     with open('foo.txt') as f:
#         lines = list(f)
#
# This has exactly the same effect as calling f.readlines(), but it
# makes it explicit that you wanted a list, in exactly the same way
# you make that explicit anywhere else (e.g., calling an itertools
# function, or Python 3.x's map or filter).
#
# Remember..
#
#-------------------------------------------------------------------------------
#
# DO NOT USE readline() !!!
#
#-------------------------------------------------------------------------------

fn1 = 'junk.junk'
fn2 = 'bogus.bogus'
fn3 = 'wtf.wtf'

try:
    filename = sys.argv[1]
except:
    filename = '/etc/hosts/'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# basename and extension

matches = re.search('(\S+)(\.\S+)', filename)

if matches:
    print(f"basename: {matches.groups()[0]}")
    print(f"extension: {matches.groups()[1]}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# exists

if path.exists(filename):

    print(f"{filename} exists")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# filetype

if path.isfile(filename):

    print(f"{filename} is a regular file")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# datetimes

created =  datetime.fromtimestamp(path.getctime(filename)).strftime('%Y-%m%d-%H:%M:%S')
modified = datetime.fromtimestamp(path.getmtime(filename)).strftime('%Y-%m%d-%H:%M:%S')
accessed = datetime.fromtimestamp(path.getatime(filename)).strftime('%Y-%m%d-%H:%M:%S')

print(f"Created:  {created}")
print(f"Modified: {modified}")
print(f"Accessed: {accessed}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# create empty

f = open(fn1,'w')
f.close()
print(f"{fn1} should now exist")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# rename (os.rename)

os.rename(fn1, fn2)
print(f"{fn1} renamed to {fn2}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# copy

shutil.copy2(fn2, fn3)
print(f"{fn2} copied to {fn3}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# rename (shutil.move)

shutil.move(fn3, fn1)
print(f"{fn3} renamed to {fn1}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reading

with open(fn1) as f:
    for line in f:
        print(f"line: {line}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Writing

fh = open(fn1, 'w')
fh.write('42')
fh.close()

