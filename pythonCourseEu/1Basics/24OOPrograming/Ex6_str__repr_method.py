#We will have a short break in our treatise on data abstraction for a quick side-trip.
# We want to introduce two important magic methods "__str__" and "__repr__", which we will need in future examples.
# In the course of this tutorial, we have already encountered the __str__ method.
# We had seen that we can depict various data as string by using the str function, which uses "magically" the internal
#  __str__ method of the corresponding data type. __repr__is similar. It also produces a string representation.

class A:
    def __repr__(self):
        return "42"


a = A()
print(repr(a))
print(str(a))


print()
class B:
    def __str__(self):
        return "42"

b = B()
print(repr(b))
print(str(b))
