from polynomials import polynomials
import numpy as np
import matplotlib.pyplot as plt


p = polynomials.Polynomial(-0.8, 2.3, 0.5, 1, 0.2)
p_der = p.derivative()

fig, ax = plt.subplots()
X = np.linspace(-2, 3, 50, endpoint=True)
F = p(X)
F_derivative = p_der(X)
ax.plot(X, F)
ax.plot(X, F_derivative)

ax.legend(['p', 'derivation of p'])

plt.show()
