import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
ax.scatter(3, 7, s=42)
ax.scatter(1, 4, s=172)

X = np.random.randint(0, 100, (20,))
Y = np.random.randint(0, 100, (20,))
fig, ax = plt.subplots()
ax.scatter(X, Y, s=42)
plt.show()