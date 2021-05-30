def ex1(n):
    if n == 1:
        return 3
    else:
        return ex1(n-1) + 3

print('start of first example')
print(ex1(3))
############

def ex2(n):
    if n == 1:
        return 1
    else:
        return n + ex2(n-1)
print('\nstart of second example')
print(ex2(6))

############

def ex3(n):
    pass