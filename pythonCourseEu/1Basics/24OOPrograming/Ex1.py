#In fact, everything is a class in Python.
x = 42
print(type(x))


#---------------------------------


class Robot:
    pass

if __name__ == "__main__":
    x = Robot()
    y = Robot()
    y2 = y
    print(y == y2)
    print(y == x)