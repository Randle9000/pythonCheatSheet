#Abstract classes are classes that contain one or more abstract methods.
# An abstract method is a method that is declared,
#  but contains no implementation.
# Abstract classes may not be instantiated,
# and require subclasses to provide implementations for the abstract methods.
#  Subclasses of an abstract class in Python are not required to implement
# abstract methods of the parent class.

#Let's look at the following example:

class AbstractClass:
    def do_something(self):
        pass


class B(AbstractClass):
    pass


a = AbstractClass()
b = B()
#
# If we start this program, we see that this is not an abstract class, because:
#
#     we can instantiate an instance from
#     we are not required to implement do_something in the class defintition of B
#
# Our example implemented a case of simple inheritance which has nothing to do
# with an abstract class. In fact, Python on its own doesn't provide
# abstract classes. Yet, Python comes with a module which provides the
# infrastructure for defining Abstract Base Classes (ABCs).
# This module is called - for obvious reasons - abc.
#
# The following Python code uses the abc module and defines an abstract base class:

from abc import ABC, abstractmethod


class AbstractClassExample(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass

class DoAdd42(AbstractClassExample):
    pass

x = DoAdd42(4)