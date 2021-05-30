ex_dict = {'a': 1,
        'b': 2,
        'c': 15,
        'd': -1}

minval = min(ex_dict, key= lambda k : ex_dict[k])
s = sorted(ex_dict, key= lambda k : ex_dict[k])
print(minval)
print(s)
## or
inverse_dict = zip(ex_dict.values(), ex_dict.keys())
min_val = min(inverse_dict)
print(min_val)