import itertools

option = {
    'x': [1,2],
    'y': ['a', 'b', 'c']
}
keys = option.keys()
values = [option[key] for key in keys]
a = itertools.product(*values)

combination = [dict(zip(keys, combination)) for combination in itertools.product(*values)]
print(combination)