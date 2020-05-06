#WSo far we used functions as decorators. Before we can define a decorator as a class, we have to introduce the __call__ method of classes. We mentioned alreaedy that a decorator is simply a callable object that takes a function as an input parameter. A function is a callable object, but what lots of Python programmers don't know. We can define classes as callable objects as well. The __call__ method is called, if the instance is called "like a function", i.e. using brackets.

class Fibonacci:
    def __init__(self):
        self.cache = {}
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]

fib = Fibonacci()

for i in range(15):
    print(fib(i), end=", ")