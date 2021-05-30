import numpy as np

celsius_values = [20, 30.1, 12.2, 15.2, 17.4]

# turn into one dimensional numpy array
c_numpy = np.array(celsius_values)
print(type(c_numpy), "\n", c_numpy)

# change values of array
print(c_numpy * 9 / 5 + 32)
print(c_numpy)

old_way_list_comprehension = [x*9/5+32 for x in celsius_values]
print(old_way_list_comprehension)


#-----------------------------------
import matplotlib.pyplot as plt

plt.plot(c_numpy)
plt.show()