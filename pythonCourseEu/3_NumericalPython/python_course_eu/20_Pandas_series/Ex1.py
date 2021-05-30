import pandas as pd

s = pd.Series([11, 28, 82, 12, 85])
print(s, '\n')
print('s.index: ', s.index, '\n')
print('s.values: ', s.values, '\n')
print(type(s))
print('s.values: ', type(s.values), 'Keep in mind that s.values are the numpy arrays', '\n\n####################\n')

###

fruits = ['apples', 'oranges', 'cherries', 'blueberries']
quantities = [20, 10, 15, 300]
quantities2 = [8, 22, 12, 40]
S = pd.Series(quantities, index=fruits)
print('S:\n ', S, '\n')
S2 = pd.Series(quantities2, index=fruits)
print('S + S2:\n ', S + S2, '\n\n####################\n')#datas are added to the corrseponded indexes


fruits2 = ['apples', 'oranges', 'cherries', 'pineapple']
R = pd.Series(quantities2, index=fruits2)
print('R + S:\n ', R + S, '\n\n####################\n') # Blueberries and pineapple are NaN

### Indexing
print("""R['pineapple']: """, R['pineapple'])
print('R[\'pineapple\',\'apples\']: \n', R[['pineapple', 'apples']])
print('(R + 3) * 4: \n', (R + 3) * 4, '\n\n####################\n')


"""
Series.apply it returns the Series or DataFrame depends on which function were applied, func can be numpy func
the func can be lambdas
"""
import numpy as np
print('R.apply(np.log()): \n', R.apply(np.log), '\n')
print('R.apply(np.sin): \n', R.apply(np.sin), '\n')
print('R.apply(lambda x : x if x > 50 else x + 10): \n', R.apply(lambda x : x if x > 50 else x + 10), '\n\n####################\n')

## filtering
print('R[R>30]', R[R > 30], '\n\n####################\n')

####### Creating series objecs from dicts
fruits_amount = dict(zip(fruits, quantities))
print(fruits_amount)
fruits_series = pd.Series(fruits_amount)
print(fruits_series,  '\n\n####################\n')

####

my_fruits = ['apples', 'cherries', 'pears']
my_fruits_series = pd.Series(fruits_amount, index=my_fruits)
print(my_fruits_series, '\n')
print('my_fruits_series.isnull(): \n', my_fruits_series.isnull(), '\n')
print('my_fruits_series.notnull(): \n', my_fruits_series.notnull(), '\n')
print('my_fruits_series.notna(): \n', my_fruits_series.notna(), '\n')
print('my_fruits_series.dropna(): \n', my_fruits_series.dropna(), '\n')
print('my_fruits_series.fillna(0): \n', my_fruits_series.fillna(0), '\n')
missing_fruits = {'pears' : 20}
print('my_fruits_series.fillna(missing_fruits): \n', my_fruits_series.fillna(missing_fruits), '\n')

###


