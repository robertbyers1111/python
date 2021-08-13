#!/usr/local/python3

def scope_test():

    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"

    #(should not affect this scope's spam)
    do_local()
    print("After local assignment:", spam)

    #(should modify this scope's spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)

    #(should not affect this scope's spam)
    do_global()
    print("After global assignment:", spam)

#should reflect the global assignment called earlier in do_global()
scope_test()
print("In global scope:", spam)

# RESULTS..
# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam
