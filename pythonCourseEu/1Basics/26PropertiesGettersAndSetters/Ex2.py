# OLD LIKE JAVA APRROACH
# class P:
#
#     def __init__(self,x):
#         self.set_x(x)
#
#     def get_x(self):
#         return self.__x
#
#     def set_x(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x

#MORE Pythonic way
#Our new class means breaking the interface.
# The attribute x is not available anymore.
# That's why in Java e.g.
# people are recommended to use only private attributes with getters and setters,
#  so that they can change the implementation without
# having to change the interface.

#But Python offers a solution to this problem.
# The solution is called properties!
class P:

    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


p1 = P(1001)
print(p1.x)
p1.x = -12
print(p1.x)


# Alternative syntax
# x = property(__get_x, __set_x) !!!!!!
#EXAMPLE

# class P:
#
#     def __init__(self,x):
#         self.__set_x(x)
#
#     def __get_x(self):
#         return self.__x
#
#     def __set_x(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
#
#     x = property(__get_x, __set_x) ## This is the most crucial PART  !