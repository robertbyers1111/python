#!/usr/bin/python3

import re

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# ① Now, each match rule is its own function which returns the
# results of calling the re.search() function.
#
# ② Each apply rule is also its own function which calls the
# re.sub() function to apply the appropriate pluralization rule.
#
# ③ Instead of having one function (plural()) with multiple rules, you
# have the rules data structure, which is a sequence of pairs of
# functions.
#
# ④ Since the rules have been broken out into a separate data
# structure, the new plural() function can be reduced to a few lines of
# code. Using a for loop, you can pull out the match and apply rules two
# at a time (one match, one apply) from the rules structure. On the first
# iteration of the for loop, matches_rule will get match_sxz, and
# apply_rule will get apply_sxz. On the second iteration (assuming you
# get that far), matches_rule will be assigned match_h, and apply_rule
# will be assigned apply_h. The function is guaranteed to return
# something eventually, because the final match rule (match_default)
# simply returns True, meaning the corresponding apply rule
# (apply_default) will always be applied.
#
# The “rules” variable is a sequence of pairs of functions.
#
# The reason this technique works is that everything in Python is an
# object, including functions. The rules data structure contains
# functions — not names of functions, but actual function objects. When
# they get assigned in the for loop, then matches_rule and apply_rule are
# actual functions that you can call. On the first iteration of the for
# loop, this is equivalent to calling matches_sxz(noun), and if it
# returns a match, calling apply_sxz(noun). 
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def match_f(noun):
    return re.search('f$', noun)

def apply_f(noun):
    return re.sub('f$', 'ves', noun)

def match_sxz(noun):
    return re.search('[sxz]$', noun)

def apply_sxz(noun):
    return re.sub('$', 'es', noun)

def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)

def apply_h(noun):
    return re.sub('$', 'es', noun)

def match_y(noun):
    return re.search('[^aeiou]y$', noun)

def apply_y(noun):
    return re.sub('y$', 'ies', noun)

def match_default(noun):
    return True

def apply_default(noun):
    return noun + 's'

rules = ((match_sxz, apply_sxz),
         (match_f, apply_f),
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default)
         )

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

#   +---------+
#---| M A I N |----------------------------------------------------------------
#   +---------+

words = ('bogy', 'batch', 'bass', 'pillow', 'leaf', 'beef', 'mice', 'moose')

for word in words:
  pword = plural(word)
  print('%10s => %s' % (word,pword) )

