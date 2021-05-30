def no_side_effect(cities):
    print(cities)
    cities = cities + ['Warsaw','Krakow'] # don't modify globals
    print(cities)

###################

def side_effect(cities):
    print(cities)
    cities += ['Warsaw','Krakow'] # modify global
    print(cities)

###################

locations = ['London', 'Paris']

no_side_effect(locations)
print(locations) # no sides effects

print()

side_effect(locations[:]) # You are passing a copy of locations
print(locations ) # so no side effects

side_effect(locations)
print(locations) #side effect

print()





