from datetime import datetime, timedelta as delta
import random
import pandas as pd
import numpy as np

def splitter(additional_information=''):
    print('\n\n####### {0} #########\n'.format(additional_information))


#Time series in pandas and python
splitter('Time series in pandas and python')
ndays = 6
start = datetime(2012, 12, 12)
dates = [start - delta(x) for x in range(0, ndays)]
print(dates)

values = [random.randint(1, 30) for x in range(0, ndays)]
print(values, '\n')

ts = pd.Series(values, index=dates)
print('pd.Series(values, index=dates): \n', ts, type(ts), '\n')
print('ts.index: \n', ts.index, '\n')

values_2 = [random.randint(4,20) for x in range(0, ndays)]
ts_2 = pd.Series(values_2, index=dates)


# it is possible to add series to each other with same indexes.
ts_3 = ts + ts_2
print('ts + ts_2: \n', ts_3)

##########
start = datetime(2017, 3, 31)
dates = [start - delta(days=x) for x in range(0, ndays)]

start2 = datetime(2017, 3, 26)
dates2 = [start2 - delta(days=x) for x in range(0, ndays)]

values = [25, 50, 15, 67, 70, 9, 28, 30, 32, 12]
values2 = [32, 54, 18, 61, 72, 19, 21, 33, 29, 17]

ts = pd.Series(values, index=dates)
ts2 = pd.Series(values2, index=dates2)
print(ts + ts_2)

