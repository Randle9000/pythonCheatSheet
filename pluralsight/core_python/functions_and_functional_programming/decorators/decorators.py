# decorats enhance nad existing function a non-intrusive and mainatainable way

# decorators take a callable argument and return a callable

# eg:
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap


def polish_city():
    return "Wrocław"

print(polish_city())



@escape_unicode
def polish_city():
    return "Wrocław"

print(polish_city())


# classes are callable so we can use class as decorator but only when __call__ is implemented
class CallCount: # it useful to control the count of
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f( *args, **kwargs)


# hello = CallCount(hello)
#    ==  # that's why we can call hello.count
# and here byc call hello("Mark") we really call the CallCount(hello).__call("Mark")
@CallCount
def hello(name):
    print('Hello, {}!'.format(name))


hello("Mark")
hello("Mark")
print(hello.count) # line 38-39 explanation


# class used as decorator are very usefull if we wanto to cotnrol sth. like:

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap


tracer = Trace()

# rotate_list = tracer(rotate_list) # it call __call__(self, f) and returns  wrap but we still have access to Trace object by trace
# rotate_list(l)
# =========
@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


l = [1, 2, 3]
print(l := rotate_list(l))
print(l := rotate_list(l))
print(l := rotate_list(l))
print(l := rotate_list(l))

tracer.enabled = False

print(l := rotate_list(l))
print(l := rotate_list(l))

# we can use as many decorators as we want and we can mix them class, instances of classes or the def, it does not matter
# use wraps when using decoration to not lose the infomration about py-docss