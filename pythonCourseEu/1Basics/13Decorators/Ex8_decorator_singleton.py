def singleton(cls):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper


@singleton
class SomeSingletonClass:
    x = 2

    def __init__(self):
        print("created")


@singleton
class SomeSingletonClass2:
    x = 5

    def __init__(self):
        print("created")


s1 = SomeSingletonClass()
s2 = SomeSingletonClass()

s1.x = 3
print(s1.x)
print(s2.x)

s3 = SomeSingletonClass2()
s4 = SomeSingletonClass2()
print(s3.x, s4.x)