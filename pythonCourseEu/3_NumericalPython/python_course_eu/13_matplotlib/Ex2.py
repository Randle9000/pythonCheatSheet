import matplotlib.pyplot as plt
import random

def splitter(additional_information=''):
    print('\n\n####### {0} #########\n'.format(additional_information))

days = list(range(1, 9))
days_2 = list(range(7, 12))
#days_2 = [2.5, 3.5, 4.5, 5.5, 6.5] #just for tests

celsius_min = [random.randint(16, 20) for i in range(0, 8)]
celsius_max = [random.randint(28, 33) for i in range(0, 8)]

celsius_min_2 = [random.randint(5, 9) for i in range(0, 5)]

fix, ax = plt.subplots()
ax.set(xlabel='Day',
       ylabel='temperature',
       title='temperature per day')

ax.plot(days, celsius_min,
        days,celsius_min, 'oy',
        days, celsius_max,
        days, celsius_max, 'or',
        days_2, celsius_min_2,
        days_2, celsius_min_2, 'ob'
        )
""""
one comprehensive ax.plot() can replaced by multiples ax.plot() functions e.g.
ax.plot(days, celsius_min)
ax.plot(days,celsius_min, 'oy')
ax.plot(days, celsius_max)
ax.plot(days, celsius_max, 'or')
ax.plot(days_2, celsius_min_2)
ax.plot(days_2, celsius_min_2, 'ob')

"""

plt.show()