import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100, endpoint=True)
y = np.sin(x ** 2) + np.cos(x)
f, (ax1, ax2) = plt.subplots(1, 2,
                             sharey=True)
derivative = 2 * x * np.cos(x**2) - np.sin(x)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.plot(x, derivative)

plt.show()