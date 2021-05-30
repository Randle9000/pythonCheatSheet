def decorator_factory(message):
    print(message)

    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print("deco wants to tell you {0}".format(message))
            return func(*args, **kwargs)
        return wrapped_func
    return decorator


@decorator_factory("multiply")
def multiply(a, b):
    return a*b

print(multiply(3,5), '\n')

################## class
def deco_fact(*deco_args, **deco_kwargs):

    class Decorator(object):
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print(deco_args)
            return self.func(*args, **kwargs)
    return Decorator


@deco_fact("add")
def add(a, b):
    return a+b

print(add(5,6))