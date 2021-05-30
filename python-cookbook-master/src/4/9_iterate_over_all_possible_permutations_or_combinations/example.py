from itertools import permutations,combinations

print('permutations')
a = [1,2,3]
for p in permutations(a):
    print(p)


print('permutations 2')
for p2 in permutations(a,2):
    print(p2)


print('combinations 3')
for c in combinations(a, 3):
    print(c)

print('combinations 2')
for c in combinations(a, 2):
    print(c)

for e, p in enumerate(permutations(a),1):
    print(e, p)