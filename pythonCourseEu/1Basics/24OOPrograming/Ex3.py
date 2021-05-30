def hi(obj):
    print("Hi, I am " + obj.name + "!")

class Robot:
    pass

x = Robot()
x.name = "Marvin"
hi(x)