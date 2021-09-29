# __init__ is not responsible for the creating the instance it initializes the object, it mutates the instance of class
# and object exists before __init__ execution is ended,
# proof let's put breakpoint inside __init__ got ot watch in debugger
# and in 'watch' write :type(self) it exists as an object

class Foo:
    def __init__(self):
        self.x = 5
        self.y = 7


foo = Foo()


# the special method __new__  the __new__ is inherited from base class object for each class.
""" Allocation with __new__"""


class Foo:
    # object is usefull for object interning like static fields and it
    # so if we want to dynamically assign static field only once then it must be done in __new__
    # the purpose of __new__ is to allocate new object
    def __new__(cls, *args, **kwargs): # __new__ is a class methods it's a special type of static methods
        print("args=", repr(args))
        print("kwargs=", repr(kwargs))
        obj = super().__new__(cls) # so as the the purpose of __new__ is to allocate new object we nned to create one
        print("id(obj =", id(obj))
        return obj

    def __init__(self, x):
        self.x = x
        self.y = 7
        print("id(obj =", id(self))


foo = Foo(x=5)