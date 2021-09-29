def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(f"arg1:{arg1}")
    print(f"arg2:{arg2}")
    print(f"args:{args}")
    print(f"kwarg1:{kwarg1}")
    print(f"kwarg2:{kwarg2}")
    print(f"kwargs:{kwargs}")
    print('\n')


print_args(1,2, 3, 4, 5, 6, kwarg1="k1", kwarg2="k2", k3=3, k4=4)

test_dict = {"kwarg1": "k1", "kwarg2": "k2", "kwarg3": "k3", "kwarg4": "k4"}

print_args(1, 2, 3, 4, 5, 6, **test_dict)

test_dict = {"arg1": 1, "arg2": 3, 'args': 4,
             "kwarg1": "kwarg1", "kwarg2": "kwarg2", "kwarg3": "kwarg3", "kwarg4": "kwarg4"}
print_args(**test_dict)