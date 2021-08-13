#!/usr/bin/python

import turtle

def wth(x,y,z):
  w = x+y%(z+1)
  return w

wn = turtle.Screen()
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("Hello, Tess!")      # Set the window title

tess = turtle.Turtle()
tess.pensize(3)               # Tell tess to set her pen width
tess.speed(10)

for i in range(100):
  for c in ['blue', 'red', 'green', 'purple', 'black', 'yellow', 'pink', 'white']:
    tess.color(c)
    tess.forward(350)
    tess.right(140)
    tess.forward(350)
    tess.right(4.5)
    #u = wth(0,3,i%10)
    #tess.right(u)

wn.mainloop()
