#We have the same classification again in object-oriented programming:
#    Private attributes should only be used by the owner, i.e. inside of the class definition itself.
#    Protected (restricted) Attributes may be used, but at your own risk. Essentially, this means that they should only be used under certain conditions.
#    Public Attributes can and should be freely used.

#
#Naming	Type	Meaning
#name 	Public
#	These attributes can be freely used inside or outside of a class definition.
#_name 	Protected
#	Protected attributes should not be used outside of the class definition, unless inside of a subclass definition.
#__name 	Private
#	This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, except inside of the class definition itself.

class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
x = A()
print(x.pub)
x.pub = x.pub + " and my value can be changed"
print(x.pub)
print(x._prot)
print(x.__priv)

print()
#
# class A():
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def GetX(self):
#         return self.__x
#
#     def GetY(self):
#         return self.__y
#
#     def SetX(self, x):
#         self.__x = x
#
#     def SetY(self, y):
#         self.__y = y

print()


class Robot:
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year

    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_build_year(self, by):
        self.__build_year = by

    def get_build_year(self):
        return self.__build_year

    def __repr__(self):
        return "Robot('" + self.__name + "', " + str(self.__build_year) + ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " + str(self.__build_year)


if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")