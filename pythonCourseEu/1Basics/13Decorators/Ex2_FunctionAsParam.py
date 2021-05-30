def g():
    print("Hi it's me g funcion!! Nice to meet You!!")

def f(func):
    print("Hi i am f function, i can invoke the function which you passed me!")
    print("Now i call the 'func'")
    func()

f(g)

##############
print()

import math


def foo(func, *x):
    for i in x:
        print(func, func(i))

foo(math.sin, 1, 2, 3.14)
foo(math.cos, 0, 1, 2, math.pi)