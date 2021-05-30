import heapq

numbers = [1,2,3,5,6,7,8,9,0,11,55]
a = heapq.nsmallest(4, numbers)
print(type(a), a)

##
b = heapq.nlargest(4,numbers)
print(type(b), b)
