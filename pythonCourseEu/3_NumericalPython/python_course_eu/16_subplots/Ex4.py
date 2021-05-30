import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-2*np.pi, 2*np.pi, 100, endpoint=True)
y = np.sin(x ** 2) + np.cos(x)

fig, ax = plt.subplots(1, subplot_kw=dict(polar=True))
ax.plot(x, np.sin(x) , "--g")
ax.plot(x, np.cos(x) , "--b")

plt.show()