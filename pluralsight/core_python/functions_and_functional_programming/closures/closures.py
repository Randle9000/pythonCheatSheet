#  Python implements closures with special attribute name __closure__
#  closures remembers the object from the enclosing scope that are mandatory to function work properly.
#  they are recorded (keep alive even if the enclosed scope is gone) in attribute name called __closure__

def enclosing():
    x = 'closed over'
    def loc_func():
        print(x)
    return loc_func

en = enclosing()
en()
a = en.__closure__[0].cell_contents
print(en.__closure__[0].cell_contents)


#  it's usefull for fruncion factories (function which return functions)
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


raise_to_square = raise_to(2)
raise_to_cube = raise_to(3)

print(raise_to_square.__closure__[0].cell_contents)
print(raise_to_cube.__closure__[0].cell_contents)

# simpel exampel of use with nonlocal

import time

def make_time():
    last_called = None
    def elapsed():
        nonlocal last_called # binds to last_called of make_time
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        return result
    return elapsed

t = make_time()
print(t())
print(t())
print(t())
print(t())