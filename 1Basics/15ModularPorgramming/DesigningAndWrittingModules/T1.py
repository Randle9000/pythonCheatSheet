from importlib import reload
import Fibonacci


print(Fibonacci.fib(16))

reload(Fibonacci)
print(Fibonacci.fib(16))

from Fibonacci import fib, ifib
print(ifib(23))

print(dir(Fibonacci))