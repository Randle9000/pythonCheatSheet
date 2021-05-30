lx = [1,2,3,4]
ly = [0,9,8,3,4,5,6]

for x, y in zip(lx, ly):
    print(x,y)

from itertools import zip_longest

for x,y in zip_longest(lx, ly, fillvalue='c'):
    print(x,y)