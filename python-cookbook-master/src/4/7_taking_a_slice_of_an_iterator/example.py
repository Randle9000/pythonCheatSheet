def count(n):
    while True:
        yield n
        n += 2

c = count(0)
# c[10:20] #TypeError: 'generator' object is not subscriptable

import itertools
for x in itertools.islice(c, 10, 20):
    print(x)