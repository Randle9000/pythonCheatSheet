

"""In many cases we don't know what the result may look like before you plot it. It could be for example, 
that the legend will overshadow an important part of the lines. If you don't know what the data may look like, 
it may be best to use 'best' as the argument for loc. Matplotlib will automatically try to find the best possible location for the legend:
"""
from polynomials.polynomials import Polynomial
import numpy as np
import matplotlib.pyplot as plt

p = Polynomial(2, -1, -5, -6)
p_der = p.derivative()
print(p_der)

fig, ax = plt.subplots()
X = np.linspace(-2, 3, 50, endpoint=True)
F = p(X)
F_derivative = p_der(X)
ax.plot(X, F, label="$" + str(p) + "$")
ax.plot(X, F_derivative, label="$" + str(p_der) + "$")

ax.legend(loc='best')
plt.show()
