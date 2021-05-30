import numpy as np
## creates ones and zeros
x = np.linspace(2, 5, 7)
a = np.ones([2, 7])
b = np.zeros([2, 6])
c = np.ones_like(x)
d = np.zeros_like(x)
e = np.empty([4, 4])

## identity
f = np.identity(5)
print(f, '\n')

## eye
g = np.eye(3, 5, 0)
print(g, '\n')
h = np.eye(4, 5, 1)
print(h)

