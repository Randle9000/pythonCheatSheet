# syntax:
#initialization
# d = {}
# d = dict()
# d = dcit([('k','v')])
dt = {'First' : 1, 'Second' : 2}
print("dt:", dt)
print("dt['First']:", # trailing coma is ok!
      dt['First'])

# shallow copy of dict
print('\nshallow copy of dict d = {**dt}')
d = {**dt}
print('dict d:', d)

## add value to dict
dt['Third'] = 3
print("\nAfter dt['Third'] = 3")
print("dt:", dt)

#delete element
del dt['Third']
print('dt after del dt[\'Third\']', dt)


## key in dict can have many formats (not only string)
dt2 = {(1,2,3):"abc", 3.1415:"abcd"}
print("\nnew dict\ndt2:",dt2)
print("dt2[(1,2,3)]:",dt2[(1,2,3)])
print("len(dt):",len(dt))
print("\"Third\" in dt","Third:" in dt, '\n\n')


#################
w = dt.copy() # shallow copy not deep
print('shallow copy of dt', w)

################
dt.update(dt2) # Merging Dictionaries
print('dt.update(dt2) ', dt)

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

##########
print('\ndict comprehesnsion')
d8 = {k:v for k,v in [('key', 'value'),('k2','v2')]}
print('dict comprehension: ', d8 )

########
# ordered dict that collection maintain the order according to the put elements first k,v will be first in such dict
from collections import OrderedDict
ordered_dict = OrderedDict([('k1','v1'),('k2','v2')])
print('\nordered dict')
for i in ordered_dict:
    print(i, ordered_dict[i])

## default value of dict:
d = {"s" : 'giraffe'}
d.setdefault("s", "horse")
print('\n\n', d["s"])

## default dict:
from collections import defaultdict
dd = defaultdict(lambda: "empty")
print('\ndefault dict', dd['anyElement\n'])

########
#iterate over dict
for i in ordered_dict:
    print(i, ordered_dict[i])

#or

for k,v in ordered_dict.items():
    print(k,v)

## merging dict:
## to merge use {**d1, **d2} or ChainMap



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