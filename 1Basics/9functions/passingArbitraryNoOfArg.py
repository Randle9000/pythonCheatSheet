def make_pizza(*toppings):
    """Print tuple list of toppings that have been requested."""
    print(toppings)
    print(type(toppings))
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')