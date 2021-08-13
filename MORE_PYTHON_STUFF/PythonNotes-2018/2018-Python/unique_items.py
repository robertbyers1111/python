#!/usr/bin/python3

# Interesting method of keeping only the unique items in a list or string
#
# ①  Given a list of several strings, the set() function will return a
#    set of unique strings from the list. This makes sense if you think
#    of it like a for loop. Take the first item from the list, put it in
#    the set.  Second. Third. Fourth. Fifth — wait, that’s in the set
#    already, so it only gets listed once, because Python sets don’t
#    allow duplicates.  Sixth. Seventh — again, a duplicate, so it only
#    gets listed once. The end result? All the unique items in the
#    original list, without any duplicates. The original list doesn’t
#    even need to be sorted first.
#
# ②  The same technique works with strings, since a string is just a
#    sequence of characters.
#
# ③  Given a list of strings, ''.join(a_list) concatenates all the
#    strings together into one.
#
# ④  So, given a list of strings, this line of code returns all the
#    unique characters across all the strings, with no duplicates.
#
# The alphametics solver uses this technique to build a set of all the
# unique characters in the puzzle.

words = ['baseball', 'basketball', 'hockey', 'football', 'soccer', 'lacrosse', 'tennis', 'swimming', 'skiing']

unique_characters = set(''.join(words))

print('unique_characters:',unique_characters)

