import ProbabilisticsFunc as pf
import numpy as np
import matplotlib.pyplot as plt

## Ex2
values=list(range(0,4))
weights = [5/12, 1/3, 1/12, 1/6]

average = np.average(values, weights=weights)
variance = pf.weigth_variance(values, average, weights)
standard_deviation = np.sqrt(variance)
print('std ', standard_deviation)
print(np.sqrt(35/6))

pf.plot_average_variance(values,weights,average,standard_deviation)
#print(sum([1,2,3,4,5,6,5,4,3,2,1]))

