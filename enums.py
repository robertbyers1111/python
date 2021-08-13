#!/usr/bin/python3

# We can use the following approach to create enum definitions..

class Shapes:
	Circle, Square, Triangle, Quadrangle = range(4)

print(Shapes.Circle)
print(Shapes.Square)
print(Shapes.Triangle)
print(Shapes.Quadrangle)

#1-> 0
#2-> 1
#3-> 2
#4-> 3

