import numpy as np

a = [[[1, 1],[1, 1]], [[1, 1],[1, 1]], [[1, 1],[1, 1]]]
b = [[[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1]]]
a_r = np.array(a)
b_r = np.array(b)
print("a shape", a_r.shape, '\n', 'b shpae', b_r.shape)

c = np.dot(a_r, b_r)
print('c shpae ', c.shape)
print(c)