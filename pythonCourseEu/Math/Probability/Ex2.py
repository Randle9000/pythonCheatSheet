import ProbabilisticsFunc as pf
import numpy as np
import matplotlib.pyplot as plt

## Ex2
pay_for_throw = 7
values2=list(range(2-pay_for_throw, 13-pay_for_throw))

weights = []
weights.extend(list(range(1,7)))
weights.extend(list(range(5,0,-1)))

average = np.average(values2, weights=weights)
variance = pf.weigth_variance(values2, average, weights)
standard_deviation = np.sqrt(variance)
print(average)
print('std ', standard_deviation)
print(np.sqrt(35/6))

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)


count, bins, ignored = plt.hist(s, 30, normed=True)

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.show()
#pf.plot_average_variance(values2,weights,average,standard_deviation)
#print(sum([1,2,3,4,5,6,5,4,3,2,1]))

