# OLD APPROACH (Javas approach)
# class P:
#
#     def __init__(self,x):
#         self.__x = x
#
#     def get_x(self):
#         return self.__x
#
#     def set_x(self, x):
#         self.__x = x
#
# p1 = P(42)
# p2 = P(4711)
# p1.set_x(p1.get_x()+p2.get_x())

#"p1.set_x(p1.get_x()+p2.get_x())"? It's ugly, isn't it?
# It's a lot easier to write an expression like the following,
#  if we had a public attribute x:
#Let's rewrite the class P in a Pythonic way. No getter, no setter and instead of the private attribute "self.__x" we use a public one:

class P:

    def __init__(self,x):
        self.x = x

p1 = P(42)
p2 = P(4711)
p1.x = p1.x + p2.x
print(p1.x)