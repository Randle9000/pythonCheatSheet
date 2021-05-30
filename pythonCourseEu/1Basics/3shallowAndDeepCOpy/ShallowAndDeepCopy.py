from copy import deepcopy


c1 = ['g','r']
c2 = c1[:] # [:] copies the list in shallow way!

print("c1:",c1)
print("c2:",c2, "is a shallow copy of c1")
print("id(c1):",id(c1)) #     Return the identity of an object. This is guaranteed to be unique among simultaneously existing objects
print("id(c2):",id(c2))
print("id(c1[0]):",id(c1[0]))
print("id(c2[0]):",id(c2[0]))
print("id(c1[1]):",id(c1[1]))
print("id(c2[1]):",id(c2[1]))

c2.append('b')
c2[1] = 'y'

print("\nAfter: c2.append('b') & c2[1] = 'y'")
print("c1:",c1)
print("c2:",c2)
print("id(c1[0]):",id(c1[0]))
print("id(c2[0]):",id(c2[0]))
print("id(c1[1]):",id(c1[1]))
print("id(c2[1]):",id(c2[1]))

################### deepCopy


c3 = deepcopy(c1)
print('\nDeepcopy!')
print("c1:",c1)
print("c3:",c3,",is a deepcopy of c1")
print("id(c1):",id(c1))
print("id(c3):",id(c3))

c3[0] = 1
print("\nAfter c3[0] = 1")
print("c1:",c1)
print("c3:",c3)

print("id(c1[0]):",id(c1[0]))
print("id(c3[0]):",id(c3[0]))
print("id(c1[1]):",id(c1[1]))
print("id(c3[1]):",id(c3[1]))
