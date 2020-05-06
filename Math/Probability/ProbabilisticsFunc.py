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

def weigth_variance(values, average, weights , ):
    return np.average(abs(values - average)**2, weights=weights)

def plot_average_variance(arguments,values, average, standard_deviation):
    plt.plot(arguments, values, 'ob')
    plt.axvline(x=average, c='b', ls='dashed')
    plt.axvline(x=average + standard_deviation, c='r', ls='dashed')
    plt.axvline(x=average - standard_deviation, c='r', ls='dashed')
    plt.show()