import numpy as np

dt1 = np.dtype([('id', np.int32), ('price', np.float32)])
t1 = np.array([
    (123, 57.55),
    (156612, 55.20),
    (5123, 123.55),
    (9822, 1664.3)], dtype=dt1)

print(t1['id'][1])
print(t1['price'][3])