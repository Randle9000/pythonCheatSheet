#yield from" is available since Python 3.3!
#The yield from <expr> statement can be used
# inside the body of a generator. <expr> has
# to be an expression evaluating to an iterable,
# from which an iterator will be extracted.
#The iterator is run to exhaustion, i.e. until
# it encounters a StopIteration exception. This
# iterator yields and receives values to or from
#  the caller of the generator, i.e. the one which
#  contains the yield from statement.


def gen1():
    for char in "Python":
        yield char
    for i in range(5):
        yield i

def gen2():
    yield from "Python"
    yield from range(5)

g1 = gen1()
g2 = gen2()
print("g1: ", end=", ")
for x in g1:
    print(x, end=", ")
print("\ng2: ", end=", ")
for x in g2:
    print(x, end=", ")
print()


#The benefit of a yield from statement can be seen as a way to
#  split a generator into multiple generators.
# That's what we have done in our previous example and we will dem
def cities():
    for city in ["Berlin", "Hamburg", "Munich", "Freiburg"]:
        yield city


def squares():
    for number in range(10):
        yield number ** 2


def generator_all_in_one():
    for city in cities():
        yield city
    for number in squares():
        yield number


def generator_splitted():
    yield from cities()
    yield from squares()


lst1 = [el for el in generator_all_in_one()]
lst2 = [el for el in generator_splitted()]
print(lst1 == lst2)
