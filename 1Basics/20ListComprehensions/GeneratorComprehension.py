x = (x **2 for x in range(20))
print(x)
x = list(x)
print(x)

##################
print()
noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
primes = [x for x in range(2, 100) if x not in noprimes]
print(primes)
print(noprimes)