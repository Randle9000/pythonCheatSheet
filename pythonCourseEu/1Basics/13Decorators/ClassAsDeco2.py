class decorator2:
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()


@decorator2
def foo():
    print("inside foo()")


foo()