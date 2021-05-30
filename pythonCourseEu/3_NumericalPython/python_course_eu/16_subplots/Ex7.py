import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2*np.pi, 100, endpoint=True)
x_2 = np.linspace(0, 1*np.pi, 100, endpoint=True)
y = np.sin(x ** 2) + np.cos(x)

derivative = 2 * x * np.cos(x**2) - np.sin(x)

fig, axes = plt.subplots(2, 2)
axes[0, 0].plot(x, y)
axes[0, 1].plot(x, y)
axes[1, 0].plot(x, np.cos(x_2) * np.sin(x_2**2))
axes[1, 1].plot(x, derivative, "g--")

plt.show()