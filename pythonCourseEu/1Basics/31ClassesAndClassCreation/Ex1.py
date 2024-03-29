#In this chapter of our tutorial, # we will provide
# you with a deeper insight into the magic happening behind the scenes,
# when we are defining a class or creating an instance of a class.
#  You may ask yourself:
# "Do I really have to learn theses additional
# details on object oriented programming in Python?"
# Most probably not, or you belong to the few people who design classes at a
# very advanced level.

#First, we will concentrate on the relationship between type and class.
#  When you have defined classes so far, you may have asked yourself,
# what is happening "behind the lines".
# We have already seen, that applying "type" to an object returns the class
# of which the object is an instance of:

x = [4, 5, 9]
y = "Hello"
print(type(x), type(y))
print(type(type(x)), type(type(y)))

#A user-defined class (or the class "object") is an instance of the class "type".
#  So, we can see, that classes are created from type
# In Python3 there is no difference between "classes" and "types".
# They are in most cases used as synonyms.

#The fact that classes are instances of a class "type" allows us to program metaclasses. We can create classes, which inherit from the class "type". So, a metaclass is a subclass of the class "type".

#Instead of only one argument, type can be called with three parameters:

#type(classname, superclasses, attributes_dict)
#If type is called with three arguments, it will return a new type object. This provides us with a dynamic form of the class statement.

#    "classname" is a string defining the class name and becomes the name attribute;
#    "superclasses" is a list or tuple with the superclasses of our class. This list or tuple will become the bases attribute;
#    the attributes_dict is a dictionary, functioning as the namespace of our class. It contains the definitions for the class body and it becomes the dict attribute.
print()

class A:
    pass
x = A()
print(type(x))

print()
B = type("B", (), {})
y = B()
print(type(y))

#Generally speaking, this means, that we can define a class A with
#type(classname, superclasses, attributedict)

#When we call "type", the call method of type is called.
# The call method runs two other methods: new and init:

#type.__new__(typeclass, classname, superclasses, attributedict)
#type.__init__(cls, classname, superclasses, attributedict)

#The new method creates and returns the new class object,
# and after this the init method initializes the newly created object
print()

#robot
class Robot:
    counter = 0
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        return "Hi, I am " + self.name
def Rob_init(self, name):
    self.name = name

##robot2
Robot2 = type("Robot2",
              (),
              {"counter":0,
               "__init__": Rob_init,
               "sayHello": lambda self: "Hi, I am " + self.name})

x1 = Robot2("Marvin")
print(x1.name)
print(x1.sayHello())
y1 = Robot("Marvin")
print(y1.name)
print(y1.sayHello())
print(x1.__dict__)
print(y1.__dict__)