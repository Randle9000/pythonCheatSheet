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

test = map(ord, 'Mati Klys')
# maps are lazy (it's called lazy evaluation) it means that it does nto produce any result if it is not needed
print(test)
print(list(test))
# map is iterable object, so we must iterate over it to produce result - next()

result = map(Trace()(ord), "Mati_K")
print(result)
print(list(result))
# map (f(x,y,z), [xs], [ys], [zs]) # <- that how to pass parameters to funcs

# five approaches to create list of stirngs
a = [str(i) for i in range(5)]
b = list(map(str, range(5)))
c = list(str(i) for i in range(5))