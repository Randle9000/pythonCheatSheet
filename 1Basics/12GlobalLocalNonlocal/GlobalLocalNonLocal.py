# Python deals with variables the other way around. They are local, if not otherwise declared.

def f():
    print(s)
s = 'i love WRO'

f()

###############
def g():
    p = 'i love PRG'
    print(p)

p = 'i love PRS'
g()
print(p)

############
print()

def h():
    global a
    print(a)
    a = "hehehehe" ## it is a gloabl !!
    print(a)

a = "haahahahah"
h()
print(a)






