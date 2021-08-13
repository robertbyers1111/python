#!/usr/bin/python

#---------------------------------------------------------------------

# PROGRAMATICALLY SET AN ATTRIBUTE OF AN OBJECT (setattr())

#---------------------------------------------------------------------

# setattr and getattr are builtins but only defined for an object if explicitly defined
#
# __setattr__ and __getattr__ are also builtins, but never call them directly (python does it for you)

class Abc():

    # name of this method does not need to be setattr, it merely needs to call the setattr built-in
    def setattr(self, name, value):
        setattr(self, name, value)

    def show_setattrs(self):
        # setattr is a python builtin
        # self.setattr is this function
        # self.__setattr__ is a method-wrapper
        print()
        print(f"           setattr: {setattr}")
        print(f"      self.setattr: {self.setattr}")
        print(f"  self.__setattr__: {self.__setattr__}")
        print()

    def show(self):
        callables=[]
        keys = (name for name in dir(self) if not name.startswith('_'))
        for key in sorted(keys):
            value = getattr(self, key)
            if not callable(value):
                print(key,' = ',value)
            else:
                callables.append({key : value})

        print('\nCALLABLES..\n')
        for thing in callables:
            for k,v in thing.items():
                print(k,' = ',v)

#---------------------------------------------------------------------

dut1 = Abc()

dut1.setattr('bogus', 23)
dut1.setattr('hopscotch', 'wtf')
dut1.setattr('legume', 'worgge')
dut1.setattr('17', '34/2')
dut1.setattr('bagus', 23)
dut1.setattr('bogus', 23)
dut1.setattr('bogus', 24)
dut1.setattr('bogus', 23)
dut1.setattr('bogus', 23)
dut1.setattr('bogus', 24)
dut1.setattr('dut1', dut1)
dut1.setattr('dut1.show', dut1.show)

dut1.show_setattrs()
dut1.show()

