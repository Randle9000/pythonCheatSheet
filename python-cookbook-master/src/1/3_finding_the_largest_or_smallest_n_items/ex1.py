import heapq
l = [8, 13, 1, 2, 3 ,4]

a = heapq.nlargest(3, l)
print(a)

# but better solution for list i
print(sorted(l))
min3 = sorted(l)[:3]
max3 = sorted(l)[-3:] # od -3 do konca sprawdz [-3,-2] = n-3,n-2
print(min3)
print(max3)