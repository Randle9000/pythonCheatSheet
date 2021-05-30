def cities():
    yield ('London')
    yield ('Warsaw')
    yield ('Zagreb')
    yield ('Barcelona')
    yield ('Paris')
    yield ('Rome')

try:
    c = cities()
    while True:
        city = next(c)
        print(city, end='\n')
except StopIteration:
    pass

#instead of using StopIteration You can use None

print('\n second example with None \n')
c = cities()
while True:
    city = next(c, None)
    if city is None:
        break
    print(city, end='\n')
