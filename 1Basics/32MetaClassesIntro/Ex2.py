#We can improve our approach in Ex1.py
# by defining a manager function and avoiding redundant code this way.
# The manager function will be used to augment the classes conditionally.

# the following variable would be set as the result of a runtime calculation:
x = input("Do you need the answer? (y/n): ")
if x == "y":
    required = True
else:
    required = False


def the_answer(self, *args):
    return 42


# manager function
def augment_answer(cls):
    if required:
        cls.the_answer = the_answer


class Philosopher1:
    pass


augment_answer(Philosopher1)


class Philosopher2:
    pass


augment_answer(Philosopher2)


class Philosopher3:
    pass


augment_answer(Philosopher3)

plato = Philosopher1()
kant = Philosopher2()
# let's see what Plato and Kant have to say :-)
if required:
    print(kant.the_answer())
    print(plato.the_answer())
else:
    print("The silence of the philosphers")

#This is again useful to solve our problem, but we, i.e. the class designers, must be careful not to forget to call the manager function "augment_answer". The code should be executed automatically. We need a way to make sure that "some" code might be executed automatically after the end of a class definition Ex3.py
    # .