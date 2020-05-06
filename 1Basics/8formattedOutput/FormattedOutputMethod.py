print("First argument: {0}, second one: {1}".format(47,11))
print("Second argument: {1}, first one: {0}".format(47,11))
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42,11))
print("First argument: {}, second one: {}".format(47,11) )
print("Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058))
print("""First value {0} , Second value {1}""".format(22, 33))
print()

#################################

data = dict(province="Ontario",capital="Toronto")
print("The capital of {province} is {capital}".format(**data))

#####################################

