dt = {'First' : 1, 'Second' : 2}
print(dt)
print(dt['First'])

dt['Third'] = 3
print(dt)

dt2 =  {(1,2,3):"abc", 3.1415:"abcd"}
print(dt2)
print(dt2[(1,2,3)])

print(len(dt))
print("Third" in dt, '\n\n')

#################
w = dt.copy() # shallow copy not deep
print('copy of dt', w)

################
dt.update(dt2) # Merging Dictionaries
print('update of dt using dt2 ', dt)
###########3
print('\nprint all keys in dt')
for key in dt:
    print(key)
#################
print('\nprint all keys in dt')
for value in dt.keys():
    print(value)
############
print('\nprint all values in dt')
for value in dt.values():
    print(value)


###############################
print('\n')
dishes = ['pizza', 'hamburger', 'saussage']
countries = ['ITA', 'USA']
cd = zip(countries,dishes) # cd is not implicitly dictionary, it must be casted
print('type of cd (which was zipped) ',cd)
cd1 = dict(cd) # casting can be done onlz once
cd2 = dict(cd)
cd3 = list(cd)


print('\ncd ', cd)
print('cd1 ', cd1)
print('cd2 ', cd2)
print('cd3 ', cd3)