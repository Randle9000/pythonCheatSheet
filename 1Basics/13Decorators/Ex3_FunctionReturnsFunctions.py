def f(x):
    def g(y):
        return y + x + 3
    return g

nf1 = f(3)
nf2 = f(5)

print(nf1(3))
print(nf2(111))

########################
print()

def polynomial_creator(a,b,c):
    def polynomial(x):
        return a*x**2 + b*x + c
    return polynomial

fp1 = polynomial_creator(1,2,3)
print(fp1(5))