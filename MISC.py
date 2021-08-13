#!/usr/local/bin/python

#   +--------------+
#---| VARIABLE "_" |---
#   +--------------+

# In interactive mode, the last printed expression is assigned to the variable _.
# This means that when you are using Python as a desk calculator, it is somewhat
# easier to continue calculations, for example:

##zz >>> tax = 12.5 / 100
##zz >>> price = 100.50
##zz >>> price * tax
##zz 12.5625
##zz >>> price + _
##zz 113.0625
##zz >>> round(_, 2)
##zz 113.06
##zz >>>

#   +---------------------+
#---| Multiple Assignment |---
#   +---------------------+

a, b = 0, 1
while b < 10:
      print b
      a, b = b, a+b

