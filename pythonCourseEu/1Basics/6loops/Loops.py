n = 20
s = 0
c = 1

while c < n:

    c = c + 1

    if c == 10:
        continue
    print(c)

    if c == 25: # change c to 25 and you will se what happens
        print(c)
        break

else:
    print('koniec')
print(c)

