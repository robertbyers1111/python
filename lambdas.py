#!/usr/bin/python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FROM http://www.diveintopython.net/power_of_introspection/lambda_functions.html
#
# "lambda functions are a matter of style. Using them is never required;
# anywhere you could use them, you could define a separate normal
# function and use that instead. I use them in places where I want to
# encapsulate specific, non-reusable code without littering my code with
# a lot of little one-line functions."
#
# Here are the lambda functions in apihelper.py:
#
#   processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
#
# Notice that this uses the simple form of the and-or trick, which is
# okay, because a lambda function is always true in a boolean context.
# (That doesn't mean that a lambda function can't return a false value.
# The function is always true; its return value could be anything.)
#
# Also notice that you're using the split function with no arguments.
# You've already seen it used with one or two arguments, but without any
# arguments it splits on whitespace.
#
# Example 4.21. split With No Arguments
#
# >>> s = "this   is\na\ttest"  1
# >>> print s
# this   is
# a   test
# >>> print s.split()           2
# ['this', 'is', 'a', 'test']
# >>> print " ".join(s.split()) 3
# 'this is a test'
#
# 1  This is a multiline string, defined by escape characters instead of
# triple quotes. \n is a carriage return, and \t is a tab character.
#
# 2  split without any arguments splits on whitespace. So three spaces, a
# carriage return, and a tab character are all the same.
#
# 3  You can normalize whitespace by splitting a string with split and
# then rejoining it with join, using a single space as a delimiter. This
# is what the info function does to collapse multi-line doc strings into
# a single line.
#
# So what is the info function actually doing with these lambda
# functions, splits, and and-or tricks?
#
#    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
#
# processFunc is now a function, but which function it is depends on the
# value of the collapse variable. If collapse is true,
# processFunc(string) will collapse whitespace; otherwise,
# processFunc(string) will return its argument unchanged.
#
# To do this in a less robust language, like Visual Basic, you would
# probably create a function that took a string and a collapse argument
# and used an if statement to decide whether to collapse the whitespace
# or not, then returned the appropriate value. This would be inefficient,
# because the function would need to handle every possible case. Every
# time you called it, it would need to decide whether to collapse
# whitespace before it could give you what you wanted. In Python, you can
# take that decision logic out of the function and define a lambda
# function that is custom-tailored to give you exactly (and only) what
# you want. This is more efficient, more elegant, and less prone to those
# nasty oh-I-thought-those-arguments-were-reversed kinds of errors. 
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x = lambda z: z**2

print('\nx:',x(3))

s = "this   is\na\ttest"

print('\ns:',s)
print('\ns.split():',s.split())
print('\ns joined:'," ".join(s.split()))

collapse = True
processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)

t=processFunc(s)

print('\nt:',t)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Compute matrix diagonal sums using a lambda function..

m = [
 [10,20,30,4001],
 [100,200,30001,400],
 [1000,200001,3000,4000],
 [1000001,20000,30000,40000]
]

print('\n'+'~'*38+'\nSums of the diagonals of a matrix..\n')

for reverse in [False,True]:
  sumLambda = reverse and (lambda s: sum(s[len(s)-i-1][i] for i in range(len(s)))) or (lambda s: sum(s[i][i] for i in range(len(s))))
  diagonalsum = sumLambda(m)
  print('Reverse:',diagonalsum) if reverse else print('Forward:',diagonalsum)

