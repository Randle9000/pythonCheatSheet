import numpy as np

A = np.array([[11, 12, 14], [7, 10, 11], [9, 8, 3]])
B = np.array([1, 2, 3])

# turn vector into column vector
B_column = B[:, np.newaxis]
#print(B, '\n', B_column)
#
C = B*B_column
print(C,'\n')

D = A*B_column # First row of A is multiply by 1, second by 2, third by 3
print(D, '\n')

##example above is  treated like
X = np.array([[1, 2, 3], ]*3).transpose()
print(X, '\n')
Y = A*X
print(Y)


