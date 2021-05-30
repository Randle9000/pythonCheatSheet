# #simple decorator


def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return inner_func


@print_args
def multiply(num_a, num_b):
    return num_a * num_b

print(multiply(3, 5))
"""
1) invoke print_args(multiply):
2) return inner_func
3) invoker inner_func(3,5)
4) invoke func = multiply
"""
