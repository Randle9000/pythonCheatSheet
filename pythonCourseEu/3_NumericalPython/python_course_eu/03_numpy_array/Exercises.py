import numpy as np

#1) create an arbitrary one dimensional array called v
v = np.array([1, 2, 3, 4, 5, 66, 12, 167, -5])
print(v)

#2) create a new array which consists of the odd indeces of previously created array 'v'
x = v[1::2]
print(x)

#3) create a new array in backwards ordering from v
z = v[::-1]
print(z)

#4) example of how view works
a = np.array([1, 2, 3, 4, 5])
b = a[1:4]
b[0] = 200
print(a, "\n", b, '\n')

#5) Create two dimensional array called m
m = np.array([[1, 5, 7, 8], [5, 7, -2, -3]])
print(m, '\n')

#6) Create a new array from m in which the elements of each row are in reverse order
n = m[::, ::-1]
print(n, '\n')

#7) Where the rows are in reverse order
o = m[::-1, ::]
print(o, '\n')

#8) Where columns and rows are in reverse order
p =m[::-1,::-1]
print(p, '\n')