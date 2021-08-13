#!/usr/bin/python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DO NOT NAME THIS FILE 'math.py'
#
# It gets called when you import datetime (!!!) and perhaps others as well
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

denom = 100

a = 153
adot = 153.

b = a / denom
bdot = adot / denom

print("%d / %d = %d" % (a,denom,b))
print("%0.1f / %d = %0.2f" % (adot,denom,bdot))

#- Floor division discards the fractional part

floor = 17 // 3        #(result is 5)
print("17 // 3 = %d" % floor)

