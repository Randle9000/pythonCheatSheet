def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print('start first approach to calc fibbonaci for first 8 digits \n', fib(8) , '\n')

#######

def fib2(n):
    old,new = 0 , 1
    if n == 0:
        return 0
    else:
        for i in range(n-1):
            old, new = new, old + new
        return new

print('start second approach to calc fibbonaci for first 8 digits \n', fib(8) , '\n')

################
