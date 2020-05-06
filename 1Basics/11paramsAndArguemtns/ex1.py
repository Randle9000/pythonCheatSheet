def arithmetic_mean(*var):
    if len(var) == 0:
        return 0
    else:
        a = 0
        for i in var:
            a = a + i
        return a / len(var)


c = arithmetic_mean(5,3,4,5,4)
print('c = ', c)
print('function arithmetic_mean', arithmetic_mean(), '\n')

x = [1,2,3,4,5,6,7]
print(x)
print(*x)
print(arithmetic_mean(*x))