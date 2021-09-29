l = [(x, y) for x in range(5) for y in range(4)]
print(l) # cartesian product of x,y

# multiple if_clause

values = [x/(x - y) for x in range(100) if x > 50 for y in range(100) if x - y != 0]
print(values)

# corresponds to
values = []
for x in range(100):
    if x > 50:
        for y in range(100):
            if x-y != 0:
                values.append(x / (x - y))

# nested comprehension:

vals = [[y * 3 for y in range(x)] for x in range(10)]
print(vals)
