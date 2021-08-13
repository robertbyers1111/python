#!/usr/bin/python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Define a class which has at least two methods:
#
# getString: to get a string from console input
#
# printString: to print the string in upper case.
#
# Also please include simple test function to test the class methods.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Dut():

  def __init__(self,str):
    self.str = str

  def getString(self):
    self.str = input()
    return(self.str)

  def printString(self):
    print(self.str.upper())

dut = Dut('abcd')
dut.getString()
dut.printString()
