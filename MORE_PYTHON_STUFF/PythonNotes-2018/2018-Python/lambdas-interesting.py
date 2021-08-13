#!/usr/bin/python3

# FROM: https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
#
# I got a list of dictionaries and want that to be sorted by a value of
# that dictionary.
#
# This
#
# [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
#
# sorted by name, should become
#
# [{'name':'Bart', 'age':10}, {'name':'Homer', 'age':39}]
#
#
# Answer..
#
# It may look cleaner using a key instead a cmp:
#
# newlist = sorted(list_to_be_sorted, key=lambda k: k['name']) 
#
# or as J.F.Sebastian and others suggested,
#
# from operator import itemgetter newlist = sorted(list_to_be_sorted,
# key=itemgetter('name')) 
#
# For completeness (as pointed out in comments by fitzgeraldsteele), add
# reverse=True to sort descending
#
# newlist = sorted(l, key=itemgetter('name'), reverse=True)


z = [
 {'name':'Homer', 'age':39}, 
 {'name':'Bart', 'age':10},
 {'name':'Cath', 'age':49},
 {'name':'Bob', 'age':57},
 {'name':'Leo', 'age':16},
 {'name':'Nate', 'age':14},
 {'name':'Tess', 'age':10},
]

print()
print('Sorted by first name..')

for r in sorted(z, key = lambda k: k['name']):
  print('%8s: %2d' % (r['name'],r['age']))

print()
print('Sorted by age..')

for r in sorted(z, key = lambda k: k['age']):
  print('%8s: %2d' % (r['name'],r['age']))

