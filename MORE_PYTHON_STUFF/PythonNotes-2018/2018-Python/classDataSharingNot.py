#!/usr/bin/python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Question.. Why are x, y and z all the same???
#
# class a:
#    list = []
#
# x = a()
# y = a()
# z = a()
#
# x.list.append(1)
# y.list.append(2)
# x.list.append(3)
# y.list.append(4)
#
# print(x.list) # prints [1, 3]
# print(y.list) # prints [2, 4]
# print(z.list)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Comments..
#
# Please, do not use list as an attribute name. list is a buil-in
# function to construct a new list. You should write name classes with
# capital letter.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# My solution..

class B:
  def __init__(self,*x):
    self.l=[*x]

  def append(self,*x):
    self.l.append(*x)

  def show(self):
    for x in self.l:
      print('item:',x)

xx=B([11])
#yy=B()
xx.append([1,2,3])
xx.show()
#yy.show()
