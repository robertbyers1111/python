#!/usr/bin/python

#---------------------------------------------------------
#-- Define a function within a function. Then you can
#-- make a function of a new name. In this example, the
#-- new functions are sqr(), cub() and quad()
#---------------------------------------------------------

def make_pow(n):
    def fixed_exponent_pow(x):
        return pow(x, n)
    return fixed_exponent_pow

sqr = make_pow(2)
print (sqr(10))

cub = make_pow(3)
print (cub(10))

quad = make_pow(4)
print (quad(2))
print (quad(quad(2)))
print (quad(quad(quad(2))))

