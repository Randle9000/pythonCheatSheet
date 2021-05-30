import numpy as np

# Creation
array_arange = np.arange(1, 5)
print('arange: np.arange(1, 5)')
print(array_arange, "\n")


lin_array = np.linspace(1, 5, 7)
print('linspace: np.linspace(1, 5, 7)')
print(lin_array, "\n")


# multidemnsional
multi_array = np.array([[1, 2], [2, 3]]) #etc
print('multi_array: np.array([[1, 2], [2, 3]])')
print(multi_array, "\n")

#reshapeing
print('shape of multi_array ', np.shape(multi_array))
x = np.linspace(5, 10, 20)
print(np.shape(x))
a = x.reshape(2, 10) # reshape does not create new object only the view!
a[0][0] = 100 # it change the value of x , a
print(x, '\n')
print(a, '\n')

# slicing
b = a[1:, 2:4] # also creates a view
print(b)

#
