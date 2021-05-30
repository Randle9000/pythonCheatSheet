import pandas as pd


def splitter(additional_information=''):
    print('\n\n####### {0} #########\n'.format(additional_information))


years = range(2014, 2017)
shop1 = pd.Series([2409.13, 2941.44, 3495.10], index = years)
shop2 = pd.Series([1409.41, 2123.92, 3785.30], index = years)
shop3 = pd.Series([2239.58, 2455.57, 4950.13], index = years)

conc = pd.concat([shop1, shop2, shop3])
print(conc, '\n')
print(conc.index, '\n')
print(conc.values, '\n')
print(type(conc), '\n')
conc2 = pd.concat([shop1, shop2, shop3], axis=1)
print(conc2, '\n')
print(conc2[0][2014])

### --------- adding names to columns
splitter('adding names to columns')

cities = ["Warszawa", "Kielce", 'Wrocław']
#first appraoch
conc2.columns = cities
print(conc2, '\n\n')

# second approach
shop1.name = 'Kielce'
shop2.name = 'Wrocław'
shop3.name = 'Warszawa'
shops_cities = [shop1, shop2, shop3]
shops_df = pd.concat(shops_cities, axis=1)
print(shops_df)
### ----------- dict to dataframes

splitter('dict to dataframes')

people_dict = {'name': ['John', 'Mateo', 'Mark'],
        'age' : [ 33, 23, 22],
        'height': [ 185, 188, 179]}

people_data_frame = pd.DataFrame(people_dict)
print('pd.DataFrame(people_dict): \n', people_data_frame)

## retrieving from data
splitter('retrieving columns')

print("people_data_frame.columns.values:\n ", people_data_frame.columns.values)

###custom_index
splitter('custom_index')

ordinals = ['first', 'second', 'third']
people_data_frame_2 = pd.DataFrame(people_dict, index=ordinals)
print('pd.DataFrame(people_dict, index=ordinals): \n', people_data_frame_2)

##
splitter('rearanging the order of columns')
people_data_frame_3 = pd.DataFrame(people_dict, columns=['height', 'age', 'name'])
print("""pd.DataFrame(people_dict, columns=['height', 'age', 'name']):""", '\n', people_data_frame_3)


## reindexed
splitter('reindexed')
reindexed = people_data_frame_3.reindex(index=[1, 2], columns=[ 'name', 'age', 'height', ])
print('people_data_frame_3.reindex(index=[1, 2], columns=[ "name", "age", "height" ]: \n', reindexed)


## columns rename
splitter('columns rename')
columns_renamed = people_data_frame_3.rename(columns = {'name': 'nome', 'age': 'eta', 'height': 'altezza'})
print("""people_data_frame_3.rename(columns = {'name': 'nome', 'age': 'eta', 'height': 'altezza'})""",'\n', columns_renamed)


## Existing columns as ined of DF - DataFrame
splitter('Existing columns as index of DF - DataFrame')
people_data_frame_4 = pd.DataFrame(people_dict, columns=['name', 'age'], index=people_dict['height'])
print("""pd.DataFrame(people_dict, columns=['name', 'age'], index=people_dict['height'])""", '\n', people_data_frame_4,'\n')

# or the existing dataframes can be used
people_data_frame_age = people_data_frame.set_index('age') # it return a new DF
print('people_data_frame.set_index("age") : \n', people_data_frame_age,'\n')

# but it is possible to change the existing DF just set parameter in_place=true
people_data_frame_3.set_index('age', inplace=True)
print("""people_data_frame_3.set_index('age', inplace=True)""", '\n',people_data_frame_3)

##indexing
splitter('label_indexing on the rows')
data_frame_test = pd.DataFrame(people_dict, columns=['name', 'height'], index=people_dict['age'])
print(data_frame_test, '\n')
print('data_frame_test.loc[33]: \n', data_frame_test.loc[33], '\n')
print('data_frame_test.loc[data_frame_test.height > 180]: \n', data_frame_test.loc[data_frame_test.height > 180], '\n')

#sum and cumulative sum
splitter('sum and cumulative sum')
print('data_frame_test.sum(): \n', data_frame_test.sum(), '\n')
print('print(data_frame_test["height"]).sum(): \n', data_frame_test['height'].sum(), '\n')
print('x = print(data_frame_test["hetight]).cumsum(): \n', data_frame_test['height'].cumsum(), '\n')
data_frame_test['cumulative_height'] = data_frame_test['height'].cumsum()
print('data_frame_test["cumulative_height"] = data_frame_test["height"].cumsum(): \n', data_frame_test, '\n')

#access to columns of df
splitter('access tto columns of df')
print('data_frame_test["cumulative_height"]: \n', data_frame_test["cumulative_height"], '\n')
print('data_frame_test.height: \n', data_frame_test.height, '\n')
data_frame_test["random_col"] = 555 # it can be series or list
print('data_frame_test["random_col"] = 555: \n', data_frame_test, '\n')

# inserting new columns into existing dataframes
splitter('inserting new columns into existing dataframes')
data_frame_test.insert(loc=2, column='addres', value="Kielce")
print("""data_frame_test.insert(loc=2, column='addres', value="Kielce")""", '\n', data_frame_test)

# dataframe from nested dict
splitter('dataframe from nested dict')
dict_for_df = {'Kielce': {'2010': "225k", '2011': '220k', '2012': '215k'},
               'Wroclaw': {'2010': "500k", '2011': '550k', '2012': '600k'},
               'Warszawa': {'2010': "1000 k", '2011': '1050 k', '2012': '1215k'},
               }
population_in_cities = pd.DataFrame(dict_for_df)
print(population_in_cities, '\n')
print('population_in_cities.T:\n:', population_in_cities.T ,'\n')# T does not change the original DF
print(population_in_cities) #not change
