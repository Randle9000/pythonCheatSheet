from polynomials.polynomials import Polynomial

import numpy as np
import matplotlib.pyplot as plt

p = Polynomial(1, 0, -12, 0)
p_der = p.derivative()

fig, ax = plt.subplots()
X = np.arange(-5, 5, 0.1)
F = p(X)

F_derivative = p_der(X)
ax.grid()

maximum = (-2, p(-2))
minimum = (2, p(2))
ax.annotate("local maximum", maximum)
ax.annotate("local minimum", minimum)

ax.plot(X, F, label="p")
ax.plot(X, F_derivative, label="derivation of p")

ax.legend(loc='best')
plt.show()