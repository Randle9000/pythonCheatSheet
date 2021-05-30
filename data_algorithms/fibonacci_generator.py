def fib_gen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = a+b, a


def fib_func(n):
    a,b = 0,1
    for i in range(n-1):
        a, b = a+b, a
    return a


print(list(fib_gen(10)))
print(fib_func(10))