import numpy as np
import matplotlib.pyplot as plt


def get_list_of_values(lst):
    values = []
    for i in range(len(lst)):
        values.append(lst[i][0])
    return values

def get_list_of_weigths(lst):
    weight = []
    for i in range(len(lst)):
        weight.append(lst[i][1])
    return weight

def weigth_variance(values, average, weights):
    return np.average(abs(values - average)**2, weights=weights)


val_and_weights = np.array([[-2.0, 5/8],[ -1.0 , 1/8],[ 1.0, 1/8],[3.0, 1/8]])
val = get_list_of_values(val_and_weights)
weights = get_list_of_weigths(val_and_weights)
print(type(weights))

average = np.average(val, weights=weights)
variance = weigth_variance(val,average,weights) # it calc weights variance
standard_deviation = np.sqrt(variance)

print('average = ', average)
print('variance = ',variance)
print('standard deviation = ',standard_deviation)

plt.plot(val, weights, 'ob')
plt.axvline(x=average,c='b', ls='dashed')
plt.axvline(x=average + variance,  c='g', ls='dashed')
plt.axvline(x=average + standard_deviation, c='r', ls='dashed')
plt.axvline(x=average - variance,  c='g', ls='dashed')
plt.axvline(x=average - standard_deviation, c='r', ls='dashed')
plt.show()