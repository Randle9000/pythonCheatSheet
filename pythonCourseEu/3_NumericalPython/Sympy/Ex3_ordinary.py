#rownanie rozniczkowe

from sympy import Symbol, dsolve, Function, Derivative, Eq
y = Function("y")
x = Symbol('x')
y_ = Derivative(y(x), x)
print(dsolve(y_ + 5*y(x), y(x))) # y' + 5y  # result C1*exp(-5*x)


