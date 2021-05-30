from timeit import default_timer as timer
import time

def f(x):
    time.sleep(0.01)
    return x**2
t1 = timer()
a = [f(x) for x in range(100) if (f(x) > 10)] # it invoke f(x) two time instead You can write:
t2 = timer()



t3 = timer()
b = [v for v in (f(x) for x in range(100)) if v > 10]
t4 = timer()

print("a", t2 - t1)
print("b", t4 -t3)
print(a,"\n",b)

# however for the better readability the best option is to create the more abstract method

def process_square_funct(iterable):
    for x in iterable:
        yield f(x)

t1 = timer()
c = [x for x in process_square_funct(range(100)) if x > 10]
t2 = timer()
print(t2-t1)
print(c)