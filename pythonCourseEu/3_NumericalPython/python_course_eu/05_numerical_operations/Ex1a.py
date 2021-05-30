import numpy as np
a = [[1, 2], [2, 4]]
b = [[3, 5], [5, 2]]
c = [[3, 1], [8, 8]]
d = [[9, 10], [4, 7]]

a_r = np.array(a)
b_r = np.array(b)
c_r = np.array(c)
d_r = np.array(d)

x = np.array([[a, b], [c, d]])
y = np.array([[b, a], [d, c]])

# print('x=', x)
# print('y=', y)

a_b = np.dot(a, b)
b_d = np.dot(b, d)
a_b__b_d = a_b+b_d

print(a_r.shape)
print(a_b.shape)
print(a_b__b_d.shape)
print(a_r)

print('\n matrix multiplication')
print(x.shape)
# print(len(x[0]))
# print(len(x[:][0]))
# print(x[0][0][0][0])
# for i in range(0, len(x[0])):
#     for j in range(0, len(x[:][0])):
#         print('x_{0}_{1} '.format(i, j), x[i][j])

#
r = np.dot(x, y)
print(x.shape)
print(y.shape)
print(r.shape)