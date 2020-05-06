#set contains an unordered collection of unique and immutable objects. The set data type is, as the name implies, a Python implementation of the sets as they are known from mathematics. This explains, why sets unlike lists or tuples can't have multiple occurrences of the same element.

#Sets are implemented in a way, which doesn't allow mutable objects. The following example demonstrates that we cannot include for example lists as elements:
cities = set((("Python","Perl"), ("Paris", "Berlin", "London")))
#cities = set((["Python","Perl"], ["Paris", "Berlin", "London"])) # it is prohibited

#Though sets can't contain mutable objects, sets are mutable:
cities1 = set(["Frankfurt", "Basel","Freiburg"])
cities1.add("Strasbourg")
print(cities1,'\n')

#Frozensets are like sets except that they cannot be changed, i.e. they are immutable:


# remove duplicates
a = set ('AAAAAAAAAAA ppyytthhoonn')
print(a)


a.add('cccccc eeeeeeee')
print('\n adding doesnt prevent to duplicates\n', a)

