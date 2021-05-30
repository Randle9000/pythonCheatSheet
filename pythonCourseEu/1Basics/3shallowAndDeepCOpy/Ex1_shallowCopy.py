from copy import deepcopy

l1 = [1,2,3,[1,2]]
l2 = l1[:]
print("l1:",l1)
print("l2:",l2,"is a shallow copy of l1:\n")

print("id(l1):",id(l1))
print("id(l2):",id(l2))

l1[0] = "abc"
print("\nAfter: l1[0] = \"abc\":")
print("l1:",l1)
print("l2:",l2)


l1[3].append('dd') # affect on each lsit !
print("\nAfter: l1[3].append('dd')")
print("l1:",l1)

l1[3][1] = 'AC/DC' # element [3][1] will be changed for each list !
print("\nAfter: l1[3][1] = 'AC/DC'")
print(l1)
print(l2)

###

print("\n \nDEEEP COPY")
l1 = [1,2,3,[1,5]]
l3 = deepcopy(l1)
print("l1:",l1)
print("l3:",l3,"is a deep copy of l1")

print("id(l1):",id(l1))
print("id(l3):",id(l3))

l1[0] = "abc"
print("\nAfter l1[0] = \"abc\"")
print("l1:",l1)
print("l3:",l3)


l1[3].append('dd') # affect only l1 lsit !
l1[3][1] = 'AC/DC' # element [3][1] is changed only for l1 list !
print("\nAfter: l1[3].append('dd') & l1[3][1] = 'AC/DC' ")

print("l1:",l1)
print("l3:",l3)