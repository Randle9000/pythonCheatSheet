import numpy as np

A = np.array([[[0, 1],
               [2, 3],
               [4, 5],
               [6, 7]],
              [[8, 9],
               [10, 11],
               [12, 13],
               [14, 15]]])

print(np.shape(A))
print(np.shape(A[0]))
Flattened_x = A.flatten()
print('default', Flattened_x)
print('Order C ', A.flatten(order='C'))
print('Order F ', A.flatten(order='F'))
print('Order A ', A.flatten(order='A'))

### ravel

