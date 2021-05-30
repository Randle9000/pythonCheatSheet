import numpy as np

#structured array with density columns
dt = np.dtype([('density', np.int32)])

x = np.array([(393,), (336,), (223,)], dtype=dt) # it's not possible to use list and tuples interchangeably the tuple are sued to define records, the list is the cointainer for the records the tuples define the atomic elements of the structure
print(x)
print('the internal representation: ')
print(repr(x))
print(x['density'])

#example of dt
dt = np.dtype('<d')
print(dt.name, dt.byteorder, dt.itemsize)

dt = np.dtype('d')
print(dt.name, dt.byteorder, dt.itemsize)

dt = np.dtype('>d')
print(dt.name, dt.byteorder, dt.itemsize)