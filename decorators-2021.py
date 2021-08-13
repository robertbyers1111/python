#!/usr/bin/python3

def TheDecorator(func):
    def TheInnerFunc():
        print("Inside wrapper")
        func()
        print("That's all for now")
    return TheInnerFunc
 
@TheDecorator
def myFunc():
   print("Inside myFunc !!!!!!!!!!!")

myFunc()

