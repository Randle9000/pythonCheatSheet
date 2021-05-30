import numpy as np

i16 = np.dtype(np.int16)
a = np.linspace(1, 9, 7)
b = np.linspace(-5, -2, 7)
x = np.array([a, b])
print(x, '\n')
y = np.array([a, b], i16)
print(y)
