#!/usr/bin/python3

# .join() operates on strings only

# It joins the string with itself using the chars from arg
#
# if there are multiple chars in the arg, the string is repeated once
# for each arg, joining them with each successive char from the arg

nothing=''.join('')
print(nothing)

oneA=''.join('A')
print(oneA)

twoB=''.join('BB')
print(twoB)

twoBanotherWay='B'*2
print(twoBanotherWay)

d='_ZZZ_'

e=d.join('.,:!@#$%^&*')
print(e)

f='FIVE'.join(' '*6)
print(f)
