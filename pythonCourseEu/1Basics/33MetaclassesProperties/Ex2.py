#Creating Singletons using Metaclasses

#The singleton pattern is a design pattern that restricts the instantiation
# of a class to one object. It is used in cases where exactly
# one object is needed. The conceptcan be generalized to restrict the
# instantiation to a certain or fixed number of objects.
# The term stems from mathematics, where a singleton,
#  - also called a unit set -, is used for sets with exactly one element.

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    pass


class RegularClass():
    pass


x = SingletonClass()
y = SingletonClass()
print(x == y)
x = RegularClass()
y = RegularClass()
print(x == y)

# Alternative
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class SingletonClass(Singleton):
    pass


class RegularClass():
    pass


x = SingletonClass()
y = SingletonClass()
print(x == y)
x = RegularClass()
y = RegularClass()
print(x == y)