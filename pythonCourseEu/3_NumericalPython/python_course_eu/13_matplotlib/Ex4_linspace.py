import numpy as np
import matplotlib.pyplot as plt

# evenly spaced list
X = np.linspace(-2 * np.pi, 2 * np.pi, 70, endpoint=True)


F1 = 3 * np.sin(X)
F2 = np.sin(2*X)
F3 = 0.3 * np.sin(X)

fig, ax = plt.subplots()

startx, endx = -2 * np.pi - 0.1, 2*np.pi + 0.1
starty, endy = -3.1, 3.1
ax.axis([startx, endx, starty, endy])

ax.plot(X, F1, X, F2, X, F3)
ax.plot(X, F1, 'ob', X, F2, 'xr', X, F3, 'xg')
plt.show()