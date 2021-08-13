
''' +---------+
#---| super() |----------------------------------------------------------------
    +---------+

#   +--------------------+
#---| From stackexchange |---
#   +--------------------+

The purpose of super is to handle inheritance diamonds. If the class inheritance structure uses only
single-inheritance, then using super() will result in the same calls as explicit calls to the "parent" class.

Consider this inheritance diamond:
'''

class A(object):
    def __init__(self):
        print('Running A.__init__')
        super(A,self).__init__()

class B(A):
    def __init__(self):
        print('Running B.__init__')
        super(B,self).__init__()

class C(A):
    def __init__(self):
        print('Running C.__init__')
        super(C,self).__init__()

class D(B,C):
    def __init__(self):
        print('Running D.__init__')
        super(D,self).__init__()

foo = D()

'''
which prints

Running D.__init__
Running B.__init__
Running C.__init__
Running A.__init__

while if we change B to B2 and use explicit calls to the parent __init__:

'''
class B2(A):
    def __init__(self):
        print('Running B.__init__')
        A.__init__(self)

class D2(B2,C):
    def __init__(self):
        print('Running D.__init__')
        super(D2,self).__init__()

bar = D2()

'''
then the chain of init calls becomes

Running D.__init__
Running B.__init__
Running A.__init__

So the call to C.__init__ is skipped entirely.

There is no one preferred option.

If you can guarantee that you do not want to support multiple inheritance then explicit parent calls are
simpler and clearer.

If you wish to support multiple inheritance now or in the future, then you need to use super(). But understand
that there are some pitfalls involved with using super, but with proper use these pitfalls can be avoided.
'''

''' +---------+
#---| super() |----------------------------------------------------------------
    +---------+

#   +---------------------+
#---| From realpython.com |---
#   +---------------------+

As in other object-oriented languages, super() allows you to call methods of the superclass in your subclass.
The primary use case of this is to extend the functionality of the inherited method.

Note: super() alone won’t make the method calls for you: you have to call the method on the proxy object itself.

Note: super() can also take two parameters: the first is the subclass, and the second parameter is an object
that is an instance of that subclass.

However: the parameterless call to super() is recommended and sufficient for most use cases, and needing to
change the search hierarchy regularly could be indicative of a larger design issue.

In the example below, you will create a class Cube that inherits from Square and extends the functionality
of .area() (inherited from the Rectangle class through Square) to calculate the surface area and volume of a
Cube instance:
'''

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

'''
Now that you’ve built the classes, let’s look at the surface area and volume of a cube with a side length of 3:

# >>> cube = Cube(3)
# >>> cube.surface_area()
# 54
# >>> cube.volume()
# 27

Caution: Note that in our example above, super() alone won’t make the method calls for you: you have to call
the method on the proxy object itself.

Here you have implemented two methods for the Cube class: .surface_area() and .volume(). Both of these
calculations rely on calculating the area of a single face, so rather than reimplementing the area
calculation, you use super() to extend the area calculation.

Also notice that the Cube class definition does not have an .__init__(). Because Cube inherits from Square
and .__init__() doesn’t really do anything differently for Cube than it already does for Square, you can
skip defining it, and the .__init__() of the superclass (Square) will be called automatically.

super() returns a delegate object to a parent class, so you call the method you want directly on it:

    super().area().

Not only does this save us from having to rewrite the area calculations, but it also allows us to change the
internal .area() logic in a single location. This is especially in handy when you have a number of
subclasses inheriting from one superclass.

A super() Deep Dive

Before heading into multiple inheritance, let’s take a quick detour into the mechanics of super().

While the examples above (and below) call super() without any parameters, super() can also take two
parameters: the first is the subclass, and the second parameter is an object that is an instance of that
subclass.

First, let’s see two examples showing what manipulating the first variable can do, using the classes already
shown:
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

'''
In Python 3, the super(Square, self) call is equivalent to the parameterless super() call. The first
parameter refers to the subclass Square, while the second parameter refers to a Square object which, in this
case, is self. You can call super() with other classes as well:
'''

class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length

'''
In this example, you are setting Square as the subclass argument to super(), instead of Cube. This causes
super() to start searching for a matching method (in this case, .area()) at one level above Square in the
instance hierarchy, in this case Rectangle.

In this specific example, the behavior doesn’t change. But imagine that Square also implemented an .area()
function that you wanted to make sure Cube did not use. Calling super() in this way allows you to do that.

Caution: While we are doing a lot of fiddling with the parameters to super() in order to explore how it
works under the hood, I’d caution against doing this regularly.

The parameterless call to super() is recommended and sufficient for most use cases, and needing to change
the search hierarchy regularly could be indicative of a larger design issue.

What about the second parameter? Remember, this is an object that is an instance of the class used as the
first parameter. For an example, isinstance(Cube, Square) must return True.

By including an instantiated object, super() returns a bound method: a method that is bound to the object,
which gives the method the object’s context such as any instance attributes. If this parameter is not
included, the method returned is just a function, unassociated with an object’s context.

For more information about bound methods, unbound methods, and functions, read the Python documentation on
its descriptor system.

Note: Technically, super() doesn’t return a method. It returns a proxy object. This is an object that
delegates calls to the correct class methods without making an additional object in order to do so.
'''

