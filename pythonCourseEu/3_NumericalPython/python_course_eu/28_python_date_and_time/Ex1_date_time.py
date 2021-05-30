import pandas as pd
from datetime import date

def splitter(additional_information=''):
    print('\n\n####### {0} #########\n'.format(additional_information))

# simple date
x = date(1993, 10, 30)
print(x)

print('date.max: ', date.max)
print('date.min: ', date.min)
print('x.toordinal(): ', x.toordinal())
print('date.fromordinal(x.toordinal()): ', date.fromordinal(x.toordinal()))
print('x.weekday(): ', x.weekday())
print('date.today(): ', date.today())
print('x.day, x.month, x.year: ', x.day, x.month, x.year)


# time
splitter('time')
from datetime import time

t = time(15, 2, 44)
print(t)
print('time.max: ', time.max)
print('time.min: ', time.min)
t = t.replace(hour=11, second=59)
print('t = t.replace(hour=11, second=59): ', t)















