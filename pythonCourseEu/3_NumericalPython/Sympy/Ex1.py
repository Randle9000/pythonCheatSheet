from sympy import Symbol, symbols, Rational
from sympy.stats import std

def splitter(additional_information=''):
    print('\n\n####### {0} #########\n'.format(additional_information))

x = Symbol('x')
print(type(x))
y = Symbol('y')
a = 2*x - y + x - y
print(a, '\n') # 3*x - 2*y
a_result = a.subs(x, 10)
print(a_result, '\n')


x, y, z = symbols('x, y, z')
b = 3*x - 2*y + 4*z + 4*z
print(b, '\n')
b_result = b.subs({x: 10, y: 15, z: 11})
print(b_result)

### Numeric types
splitter('Numeric types')
a_r = Rational(33, 22)
b_r = Rational(1,7)
print(a_r)
print(a_r * b_r)
print(a_r.evalf())

##
from sympy import *

x, y, h  = symbols('x y h')
gfg_exp = x/(2*sqrt(h*x))

print("Before Integration : {}".format(gfg_exp))

# Use sympy.integrate() method
intr = integrate(gfg_exp, (x, 0, h))

print("After Integration : {}".format(intr))