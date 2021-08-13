#!/usr/bin/python

class Whatever:

    def __init__(self,value=7):
        self.color=value

    def show(self):
        print()
        print('color:',self.color)

if __name__ == '__main__':
    w1=Whatever()
    w1.show()
    w2=Whatever('blue')
    w2.show()

