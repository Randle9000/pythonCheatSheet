def f():
    x  = 42
    print(x)
    def g():
        global x
        x = 43
        print('insider g, x =', x)
    print("before g x = " ,x)
    print('calling g() ')
    g()
    print('x after g()', x) #

f()
print('x main ',x)
