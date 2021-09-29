def succ(x):
    return x + 1


def_succ = succ ## function is an object!!
del succ

print(def_succ(10))
#succ(10) - cannot be invoke beacuse it is deleted.
###################################
print()

def f():
    def g():
        print("Hi it's me g func")
        print("You call me")

    print("Hi i am f()")
    g()

f()
