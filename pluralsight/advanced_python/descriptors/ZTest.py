class Foo:

    def __get__(self, instance, owner):
        print("aa")
        return instance

    def __set__(self, instance, value):
        return value


class Bar:
    def __init__(self, mass):
        self.mass = mass

    mass = Foo()


b = Bar(5)
print(b.mass)
