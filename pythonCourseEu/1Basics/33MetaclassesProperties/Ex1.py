#A metaclass is a class whose instances are classes.
# Like an "ordinary" class defines the behavior of the instances of the class,
#  a metaclass defines the behavior of classes and their instances.

#Metaclasses are not supported by every object oriented programming language.
# Those programming language,
#  which support metaclasses, considerably vary in way the implement them.
# Python is supporting them.

#Some programmers see metaclasses in Python as "solutions waiting or
# looking for a problem".

#There are numerous use cases for metaclasses. Just to name a few:

 #    logging and profiling
 #    interface checking
 #    registering classes at creation time
 #    automatically adding new methods
 #    automatic property creation
 #    proxies
 #    automatic resource locking/synchronization

 #Principially, metaclasses are defined like any other Python class,
# but they are classes that inherit from "type".
# Another difference is, that a metaclass is called automatically,
#  when the class statement using a metaclass ends. In other words:
# If no "metaclass" keyword is passed after the base classes
# (there may be no base classes either) of the class header, type()
#  (i.e. __call__ of type) will be called.
# If a metaclass keyword is used on the other hand,
#  the class assigned to it will be called instead of type.

#Now we create a very simple metaclass.
# It's good for nothing, except that it will print the content of
#  its arguments in the __new__ method and returns the results of
#  the type.__new__ call:

class LittleMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)

class S:
    pass

class A(S, metaclass=LittleMeta):
    pass

a = A()

#We can see LittleMeta.__new__ has been called and not type.__new__.

#Resuming our thread from the last chapter:
#  We define a metaclass
# "EssentialAnswers" which is capable of automatically including our
# augment_answer method:

x = input("Do you need the answer? (y/n): ")
if x.lower() == "y":
    required = True
else:
    required = False


def the_answer(self, *args):
    return 42


class EssentialAnswers(type):
    def __init__(cls, clsname, superclasses, attributedict):
        if required:
            cls.the_answer = the_answer


class Philosopher1(metaclass=EssentialAnswers):
    pass


class Philosopher2(metaclass=EssentialAnswers):
    pass


class Philosopher3(metaclass=EssentialAnswers):
    pass


plato = Philosopher1()
print(plato.the_answer())
kant = Philosopher2()
# let's see what Kant has to say :-)
print(kant.the_answer())

