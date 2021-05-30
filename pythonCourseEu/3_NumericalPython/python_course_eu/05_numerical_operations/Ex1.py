import numpy as np

matrix = np.array([[1, 2, 3], [4, 3, 1]])
print(matrix)
print(matrix + 2) #
"""
+ 2 does not change the matrix it produce the new object but it affects all values
the same rules is for - / * **  
"""
print(matrix)

""""pythonic way but still much more slowe than numpy """

a = [ val + 2 for val in matrix]
print(a, '\n')

a = np.array([[1, 2, 3], [3, 2, 4]])
b = np.array([[1, 2, 3], [3, 2, 3]])
c = a * b # !! IT IS NOT Matrix multiplication a_i_j * b_i_j = c_i_j it is not matrix multipilicaton!!
print(c, '\n')
d = np.array([[1, 2], [5, 3], [2, 8]])
e = np.dot(a, d) # it is matrix multiplication!! e_i_j = sum_of_all(a_i_k * b_k_j) (k = 1, n)
print (e, '\n')
print(np.ndim(d),np.ndim(e))

Ma = np.mat(a)
Md = np.mat(d)
print(Ma*Md) # same as np.dot(a,d)
print(type(d), type(Md))
print(a == b)



