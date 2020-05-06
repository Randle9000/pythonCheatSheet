cities = {"Stuttgart", "Konstanz", "Freiburg"}
cities.clear()
print(cities,'\n')

#Creates a shallow copy, which is returned.
print('shallowCopy')
more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
cities_backup = more_cities.copy()
more_cities.clear()
print(cities_backup, '\n')

#This method returns the difference of two or more sets as a new set. ,
print('difference')
x = {"a", "b", "c", "d", "e"}
y = {"b","c"}
z = {"c","d"}
print(x.difference(y))
print(x.difference(y).difference(z), '\n')

#An element el will be removed from the set, if it is contained in the set. If el is not a member of the set, nothing will be done.
print('Discard')
x = {"a", "b", "c", "d", "e"}
print(x)
x.discard("a")
print('discard a \n', x, '\n')