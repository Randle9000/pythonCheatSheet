# examples
from functools import reduce
a = filter(lambda x: x%2 == 0, range(10))
b = map(lambda x: 2*x, range(10))
c = reduce(lambda x,y: x+y, range(10))
print(next(a), next(a), next(a))
print(next(b), next(b), next(a))
print(c)

# list comprehension
#Filter
a1 = [x for x in range(10) if x%2 == 0]
print(a1)
# map
b1 = [2*x for x in range(10)]
print(b1)