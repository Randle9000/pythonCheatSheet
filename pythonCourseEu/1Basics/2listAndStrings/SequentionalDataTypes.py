# DataTypes: Strings, byte seq, byte array, lists, tuples, range objects.

#Strings:
text = "Lists and Strings can be accessed via indices!"
print("origin of list:",text, "\n examples of text[0], text[10], text[-1]:", text[0], text[10], text[-1])


#lists can be nested or deeply nested (more than one nesting)
#["High up", ["further down", ["and down", ["deep down", "the answer", 42]]]]
#example of list
lst = [1,'2a',3,True]
print("origin list:", lst)
print("first element:", lst[0])
print("second element:", lst[1])
print("last element:", lst[-1])
print("return elements from 0 to 2:", lst[0:2])
print("return elemenets from beginning to 2:", lst[:2])
print("return elements from begin to end by step: ",lst[:4:2]) #begin end step
print ("check if '1' is in lst:",1 in lst)
print ("check if '1' is not in lst::",4 not in lst)
print("len(lst):", len(lst))

#############
print("\nexamples of nested list ")
lst2 = [1,['a',['d','e']]]
print("origin lst:", lst2)
print("lst2[1][1][1]:", lst2[1][1][1])

lst2[1] = 'c'
print("lst2[1] = 'c':", lst2)
############### tuples
tup = ('a','b','c')
print(tup[0])