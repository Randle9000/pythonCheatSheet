#initailization of list
lst = [1,2,3,4]
print("origin list ",lst)

#Adding element to list
lst.append(66)
print("append 66 example ", lst)

#change first element, in that case from 1 to 0.
lst[0] = "c"
print("change 0 position to c example ", lst)

#remove third element remeber that it is counted from 1 not from 0 !!! remove(1) - removes elemnt[0] !
lst.remove(3)
print("remove 3 element example ", lst)

#insert element in chosen place. Each elemnt in position higher will have added a +1
lst.insert(0,99)
print("insert 99 into position 0 example ", lst)

# index method to find a element index
print("index(99) example", lst.index(99) )

#difference between extend and append
lst2 = ['a', 'b', 'c']
#extend operation add each eleemnt of list
lst.extend(lst2)
print("extend example ", lst)

#append operation add a object to list.
# REMEMBER TO NEVER EVER DO STH LIKE THAT lst = lst + [42]
#it is not an alternative, the augmented assignment (+=) is an alternative
lst.append(lst2)
print("append position example ",lst)

#pop - pop display element and remove from list at the same time
#pop() is equivalent to pop(-1)
lst.pop(0)
print("pop(0) example ",lst)

#We can see that the "+" operator is about 1268 slower
# than the append method. The explanation is easy:
# If we use the append method,
# we will simply append a further element to the list
# in each loop pass. Now we come to the first loop,
# in which we use l = l + [i * 2]. The list will be copied
# in every loop pass. The new element will be added to the
# copy of the list and result will be reassigned
# to the variable l. After this the old list will have
# to be removed by Python, because it is not referenced anymore.
# We can also see that the version with the augmented assignment
# ("+="), the loop in the middle,
# is only slightly slower than the version using "append".









# key word for list:
# lst.append(66)
# lst.remove(3)
# lst.insert(0,99)
# lst[0] = "c"
# lst.extend(lst2)
# 1 in lst
# lst.index(4)
# len(lst)



