#!/usr/bin/python

#---------------------------------------------------------------------

# PROGRAMATICALLY SET AN ATTRIBUTE OF AN OBJECT (setattr())

#---------------------------------------------------------------------

class Abc():

  def __init__(self):
    pass


  def setattr(self, name, value):

    setattr(self, name, value)


  def show(self):
    keys = (name for name in dir(self) if not name.startswith('_'))
    for key in sorted(keys):
      value = getattr(self, key)
      if not callable(value):
        print '    ',key,'=',value

#---------------------------------------------------------------------

dut1 = Abc()
dut1.setattr('bogus', 23)
dut1.setattr('hopscotch', 'wtf')
dut1.setattr('17', '34/2')
dut1.setattr('bagus', 23)
dut1.setattr('bogus', 23)
dut1.setattr('bogus', 24)
dut1.show()

