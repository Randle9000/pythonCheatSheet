# instead of manipulating on the object values via __dict__, use builtin function like
# setattr, getattr, delattr, hasattr.

class Foo:
    def __init__(self):
        self.x = 5
        self._x = 6
        _x = 7

foo = Foo()

print(foo.__dict__)
print(dir(foo))
# --------------------------


class Vector:
    def __init__(self, **cords):
        private_coord = {"_" + k : v for k, v in cords.items()}
        self.__dict__.update(private_coord)

    def __getattr__(self, name):
        private_name = "_" + name
        if private_name not in self.__dict__:
            raise AttributeError(f'{self.__class__} object does not have attribute {name}')
        return getattr(self, private_name)

    def __delattr__(self, item):
        raise AttributeError(f"it's not allowed to delete attribute {item}")

    def __setattr__(self, name, value):
        raise AttributeError(f"can't set attribute {name}")


v = Vector(a=1, b=2)
print(v.__dict__)
print(dir(v))

# to fix this we need to add __getattr__ method to Vector, __getattr__ does not replace
# the standard approach to get attribute, it is invoked only when first approach does not work.
try:
    print(v.a)
    # it invokes __getattr__ and the 'a' is passed as a parameter,
    # then we glue '_' to it (check implementation) and we get that attribute

except AttributeError as e:
    print(e.args)

# but here we can still assign v.a but not even assign but create
try:
    v.a = 5
except AttributeError as e:
    print(e.args)

try:
    v.x
except AttributeError as e:
    print(e.args)

try:
    del v.x
except AttributeError as e:
    print(e.args)