memo = {0:0, 1:1}
def memo_fib(n):
    if not n in memo:
        memo[n] = memo_fib(n-1) + memo_fib(n-2)
    return memo[n]

print(memo_fib(8))