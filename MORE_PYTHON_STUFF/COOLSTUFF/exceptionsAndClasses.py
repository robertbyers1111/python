#!/usr/bin/python3

# From "9.8. Exceptions Are Classes Too", https://docs.python.org/3.4/tutorial/classes.html
#
# This is interesting and worth studying further

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Full text of the section 9.8..
#
# User-defined exceptions are identified by classes as well. Using this
# mechanism it is possible to create extensible hierarchies of exceptions.
#
# There are two new valid (semantic) forms for the raise statement:
#
# raise Class
#
# raise Instance
#
# In the first form, Class must be an instance of type or of a class
# derived from it. The first form is a shorthand for:
#
# raise Class()
#
# A class in an except clause is compatible with an exception if it is
# the same class or a base class thereof (but not the other way around —
# an except clause listing a derived class is not compatible with a base
# class). For example, the following code will print B, C, D in that
# order:
#
# class B(Exception):
#     pass
# class C(B):
#     pass
# class D(C):
#     pass
#
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")
#
# Note that if the except clauses were reversed (with except B first),
# it would have printed B, B, B — the first matching except clause is
# triggered.
#
# When an error message is printed for an unhandled exception, the
# exception’s class name is printed, then a colon and a space, and
# finally the instance converted to a string using the built-in function
# str().

