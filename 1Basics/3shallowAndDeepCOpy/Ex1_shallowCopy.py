from copy import deepcopy

l1 = [1,2,3,[1,2]]
l2 = l1[:]

print(id(l1))
print(id(l2))

print(l1)
print(l2)
l1[0] = "abc"
print(l1)
print(l2)
l1[3].append('dd') # affect on each lsit !
print(l1)
l1[3][1] = 'AC/DC' # element [3][1] will be changed for each list !

print(l1)
print(l2)

###

print("\n \nDEEEP COPY1")
l1 = [1,2,3,[1,2]]
l3 = deepcopy(l1)
print(id(l1))
print(id(l3))

print(l1)
print(l3)
l1[0] = "abc"
print(l1)

print(l3)
l1[3].append('dd') # affect only l1 lsit !
l1[3][1] = 'AC/DC' # element [3][1] is changed only for l1 list !

print(l1)
print(l3)