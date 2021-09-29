"""
Class definiton:
when we create the class then:
1) Metaclass creates namespace dictionary
2) Runtime populates namespace from class block
3) Metaclass allocates class object
4) We've got the new class
"""
# eg

"""
name = Widget 
metaclass = type
bases = () # other than implicit Object (class does not have any parent class)
kwargs = {}
namespace = metaclass.__prepare__(name, bases, **kwargs)  -- create new namespace object which behaves like dict.
Widget = metaclass.__new__(metaclass, name, bases, namespace, **kwargs) -- to allocate class object
metaclass.__init__(Widget, name, bases, namespace, **kwargs) -- to initialize class object
"""

class TracingMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs): # mcs refers to the metaclass itself.
        print("TracingMeta.__prepare__(name, bases, **kwargs")
        print(" mcs = ", mcs)
        print(" name = ", name)
        print(" bases = ", bases)
        print(" kwargs = ", kwargs)
        namespace = super().__prepare__(name, bases) # delegates to the base type class method
        print("<-- namespace = ", namespace)
        print()
        return namespace

    def __new__(mcs, name, bases, namespace, **kwargs): # the purpose is to allocate the new class object (classes are objects!)
        print("TracingMeta__new__(mcs, name, bases, namespace, **kwargs")
        print(" mcs = ", mcs)
        print(" name = ", name)
        print(" bases = ", bases)
        print(" namespace = ", namespace)
        print(" kwargs = ", kwargs)
        cls = super().__new__(mcs, name, bases, namespace) # we forward mcs ,name bases, namespace
        print("<-- cls = ", cls)
        print()
        return cls # we return here the class object (not object of the class) classes are object and we return that object!

    # the __init__ give us opportunity to modify the dcitionary of class attributes,
    # which includes methods, before the class is instantied
    def __init__(cls, name, bases, namespace, **kwargs): # the purpose of __init__ is to configure the newly created class object!
        print("TracingMeta.__init__(cls, name, bases, namespace, **kwargs")
        print(" cls = ", cls)
        print(" name = ", name)
        print(" bases = ", bases)
        print(" namespace = ", namespace)
        print(" kwargs = ", kwargs)
        super().__init__(name, bases, namespace)
        print()

    def metamethod(cls): # metamethod are rarely used
        print("TracingMeta.metamethod(cls)")
        print("cls =", cls)
        print()


class Widget(metaclass=TracingMeta):
    pass

# now we can:
Widget.metamethod()
# but we cannot:

w = Widget()
try:
    w.metamethod()
except AttributeError as e:
    print("You cannot do that")