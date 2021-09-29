def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(
                    'Argument {} must be non-negative.'.format(index)
                )
            return f(*args)
        return wrap
    return validator


#  !!!! check_on_negative is not decorator the call of check_non_negative is actual decorator!!!!
@check_non_negative(1)
def create_list(value, size):
    return [value] * size

print(create_list('a', 5))
# print(create_list('a', -2))


validator_decorator = check_non_negative(1)  # return validator it stores info about index!

# and it works as usual: multply_value = validator(multiply_value), and then call of multiply_value invoke
# what is in wrap index is from validator decorator
# the args from multiply_value goes to f(*args) of check_non_negative
@validator_decorator
def multiply_value(value, size):
    return value * size

print(multiply_value('a', 3))
print(multiply_value('a', -2))