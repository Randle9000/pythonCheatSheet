lst = [1,2,3,4]
lst.append(66)
lst[0] = "c"
lst.remove(3)
print(lst)
lst.insert(0,99)

print (lst.index(4))

lst2 = ['a', 'b', 'c']
lst.extend(lst2)
print(lst)
lst.append(lst2)
print(lst)

# key word for list:
# lst.append(66)
# lst.remove(3)
# lst.insert(0,99)
# lst[0] = "c"
# lst.extend(lst2)
# 1 in lst
# lst.index(4)
# len(lst)
#never do lst = lst + [42] (NEVER !


