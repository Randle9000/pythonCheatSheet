

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-2 * np.pi, 4 * np.pi, 1400, endpoint=True)
F1 = np.sin(X**2)
F2 = X * np.sin(X)

fig, ax = plt.subplots()

# making the top and right spine invisible:
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# moving bottom spine up to y=0 position:
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
# moving left spine to the right to position x == 0:
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

ax.set_xticks( [-6.28, -3.14, 3.14, 6.28])
ax.set_yticks([-3, -1, 0, +1, 3])
ax.plot(X, F1)
ax.plot(X, F2)

plt.show()

