import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-2 * np.pi, 2 * np.pi, 100)
F1 = np.sin(X)
F2 = 3 * np.sin(X)
fig, ax = plt.subplots()

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.set_xticklabels([r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$',
                    r'$-\frac{\pi}{2}$', 0, r'$\frac{\pi}{2}$', 
                    r'$+\pi$', r'$\frac{3\pi}{2}$', r'$+2\pi$'])
ax.plot(X, F1, X, F2)

plt.show()