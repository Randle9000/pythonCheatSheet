from sympy import Symbol, exp, sin, sqrt, diff, symbols
x, y = symbols('x,y')
a = diff(sin(x), x)
print(a)
b = diff(exp(sin(x)), x)
print(b)
c = diff((3*x**4),x,x,x)
print(c)
d = diff((3*x**4),x, 4)
print(d,'\n')



###
from sympy import integrate, evalf
a = integrate(x**2, x)
print('Integrates', '\n', a)
b = integrate(x**9, y)
print(b)
c = integrate(sin(x*2), (x, 0, 2))
print(c)
print(c.evalf())


