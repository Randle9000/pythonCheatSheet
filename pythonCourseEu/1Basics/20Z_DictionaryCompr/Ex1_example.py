#simple example
a = {x: x*2 for x in (1,2,3)}
b = dict((x, x*3) for x in range(1,4))
print(a)
print(b)

