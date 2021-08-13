#!/usr/bin/python3

class ParentClass:
  var1 = "var1 - from ParentClass"
  var2 = "var2 - from ParentClass"

  def show(self):
    print('in parent',self.var1)
    print('in parent',self.var2)

class ChildClass(ParentClass):
  var2 = "var2 - from Child"
  var3 = "var3 - from Child"
  pass

  def show(self):
    print('child',self.var2)
    print('child',self.var3)

c = ChildClass()
c.show()
print(c.var1)
print(c.var2)
print(c.var3)
