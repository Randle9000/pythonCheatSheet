class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class MyClass(Singleton):
    i = 1

a = MyClass()
b = MyClass()
print(a.i)
print(b.i)
a.i = 3
print(a.i)
print(b.i)