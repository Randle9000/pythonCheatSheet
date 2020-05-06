#A staticmethod is a method that knows nothing about the class or instance
#  it was called on. It just gets the arguments that were passed,
#  no implicit first argument. It is basically useless in Python
# -- you can just use a module function instead of a staticmethod.

# classmethod, on the other hand, is a method that
# gets passed the class it was called on, or the class of the instance
# it was called on, as first argument. This is useful
# when you want the method to be a factory for the class:
# since it gets the actual class it was called on as first argument,
# you can always instantiate the right class, even when subclasses are involved

#Static Methods

class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def RobotInstances():
        return Robot.__counter


if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())
    print(y.RobotInstances())

########class method
#Static methods shouldn't be confused with class methods.
#  Like static methods class methods are not bound to instances,
# but unlike static methods class methods are bound to a class.
#  The first parameter of a class method is a reference to a class

#The use cases of class methods:
#    the are used in the definition of the so-called
# factory methods, which we will not cover here.

#    They are often used, where we have static methods,
#  which have to call other static methods. To do this, we would have to hard code the class name, if we had to use static methods. This is a problem, if we are in a use case, where we have inherited classes.

class RobotV2:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @classmethod
    def RobotInstances(cls):
        return cls, RobotV2.__counter


if __name__ == "__main__":
    print(RobotV2.RobotInstances())
    x = RobotV2()
    print(x.RobotInstances())
    y = RobotV2()
    print(x.RobotInstances())
    print(RobotV2.RobotInstances())