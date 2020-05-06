#We will demonstrate in our last example the usefulness of class methods
# in inheritance. We define a class "Pets" with a method "about".
# This class will be inherited in a subclass "Dogs" and "Cats".
# The method "about" will be inherited as well.
# We will define the method "about" as a "staticmethod" in our first implementation
#  to show the disadvantage of this approach:

class Pets:
    name = "pet animals"

    # @staticmethod
    # def about():
    #     print("This class is about {}!".format(Pets.name))

    @classmethod
    def about(cls):
        print("This class is about {}!".format(cls.name))

class Dogs(Pets):
    name = "'man's best friends' (Frederick II)"


class Cats(Pets):
    name = "cats"


p = Pets()
p.about()
d = Dogs()
d.about()
c = Cats()
c.about()