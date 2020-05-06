def gen():
    yield 1
    yield 2
    raise StopIteration(42)

g = gen()
print(next(g))
print(next(g))
print(next(g))