import numpy as np

time_type = np.dtype( np.dtype( [('time', [('h', int), ('min', int), ('sec', int)]), ('temperature', float)] )) # time has more complex type
times = np.array( [ ((11, 44, 32), 20.8), ((13, 19, 23), 23.2), ((17, 12, 15), 24.2) ], dtype=time_type)
print(times)
print(times['temperature'])
print(times['time'])
print(times['time']['h'])

