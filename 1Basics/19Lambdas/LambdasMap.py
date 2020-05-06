#same as def sum(x,y):
#   return x + y

sum = lambda x, y : x + y
print(sum(3,4))

################
#the map func
#r = map(func, seq)


C = [39.2, 36.5, 37.3, 38, 37.8] # The first argument func is the name of a function and the second a sequence (e.g. a list) seq
F = list(map(lambda x: (float(9)/5)*x + 32, C)) # fahrenheit
print(F)
C = list(map(lambda x: (float(5)/9)*(x-32), F))
print(C)


###############
print()
from math import sin, cos, tan, pi

def map_functions(x, functions):
    """ map an iterable of functions on the the object x """
    res = []
    for func in functions:
        res.append(func(x))
    return res

family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))