fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)
print()
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)


###############################
print()
#reducing:
from functools import reduce

f = lambda a,b: a if (a > b) else b

reduce(f, [47,11,42,102,13])

print()
#######################
from functools import reduce
reduce(lambda x, y: x+y, range(1,101))