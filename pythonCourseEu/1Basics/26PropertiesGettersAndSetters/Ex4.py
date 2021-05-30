#Public instead of Private Attributes

# Let's summarize the usage of private and public attributes,
# getters and setters and properties:
# Let's assume that we are designing a new class and
# we pondering about an instance or class attribute "OurAtt",
# which we need for the design of our class.
# We have to observe the following issues:
#
#     Will the value of "OurAtt" be needed by the possible users of our class?
#     If not, we can or should make it a private attribute.
#     If it has to be accessed, we make it accessible as a public attribute
#     We will define it as a private attribute with the corresponding property, if and only if we have to do some checks or transformation of the data. (As an example, you can have a look again at our class P, where the attribute has to be in the interval between 0 and 1000, which is ensured by the property "x")
#     Alternatively, you could use a getter and a setter, but using a property is the Pythonic way to deal with it!
#
# Let's assume we have defined "OurAtt" as a public attribute.
# Our class has been successfully used by other users for quite a while.
# Now comes the point which frightens some traditional OOPistas out of the wits:
#  Imagine "OurAtt" has been used a an integer.
# Now, our class has to ensure
# that "OurAtt" has to be a value between 0 and 1000?
# Without property, this is really a horrible scenario!
# Due to properties it's easy: We create a property version of "OurAtt".


#1st Version
#
# class OurClass:
#
#     def __init__(self, a):
#         self.OurAtt = a
#
#
# x = OurClass(10)
# print(x.OurAtt)

# 2nd Version
class OurClass:

    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val


x = OurClass(10)
print(x.OurAtt)