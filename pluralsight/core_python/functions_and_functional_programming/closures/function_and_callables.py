"""
__call__ is a special functions which allows object to become the callables just like functions
"""

# example of callable class
import random


class Zoo:
    def __call__(self):
        return f"There is {random.randrange(1000, 2000)} in the zoo"


# now the object of Zoo class can be called directly:
zoo_wro = Zoo()
print(zoo_wro())
print(callable(Zoo))


class SimpleClass:
    pass


print(callable(SimpleClass))


# Classes are callable:
def sequence_class(immutable):
    return tuple if immutable else list
    # if immutable:
    #     cls = tuple
    # else:
    #     cls = list
    # return cls


seq = sequence_class(immutable=True)
t = seq("Wroclaw") # here means that classes are callable we can get class from sequence_class function and then create it.
print(t, type(t))


# to check if the object is callable:
def is_even(num):
    return num % 2 == 0


print(callable(is_even))
is_odd = lambda num: num % 2 == 1
print(callable(is_odd))
print(callable("swinki trzy"))



