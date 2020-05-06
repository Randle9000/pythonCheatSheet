lst = [1,'2a',3,True]
print(lst[0])
print(lst[1])
print(lst[3])
print(lst[-1])
print(lst[0:2])
print(lst[:2])
print(lst[:4:2]) #begin end step

print (1 in lst)
print (4 not in lst)

#############33

lst2 = [1,['a',['d','e']]]
print(lst2[1][1][1])
print(lst2)

lst2[1] = 'c'
print(lst2)
############### tuples
tup = ('a','b','c')
print(tup[0])