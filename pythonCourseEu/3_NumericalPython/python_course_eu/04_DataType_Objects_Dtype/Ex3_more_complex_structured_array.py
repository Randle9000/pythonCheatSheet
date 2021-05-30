import numpy as np

dt = np.dtype([('country', 'S20'), ('density', 'i4'), ('area', 'i4'), ('population', 'i4')])
popuplation_table = np.array([
    ('Hungary', 105, 93030, 9772756),
    ("Poland", 318, 312696, 38383000),
    ('Lithuania', 114, 65300, 2794329),
    ('Slovenia', 102, 20271, 2095861),
    ('Italy', 201, 301340, 60317116),
    ('Romania', 84, 238397, 19405156),
    ('Ukraine', 73, 603628, 41660982)],
    dtype=dt)
print(popuplation_table, '\n')
print(popuplation_table['country'], '\n')
print(popuplation_table['population'], '\n')
print(popuplation_table['country'][1:5], '\n')

"""
Unicode String
array prints: b'Poland'. it means that it is a binary strings, and it is caused because we use S20.
to get unicode Strings we have to exchange the definition of dtype to 'np.unicode, 20' 20 is a length of string

"""

# save data to csv file
np.savetxt("population.csv", popuplation_table, fmt='%s;%d;%d;%d', delimiter=';')