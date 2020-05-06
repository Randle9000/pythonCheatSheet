#Attributes are created inside of a class definition,
# as we will soon learn. We can dynamically
# create arbitrary new attributes for existing instances of a class.
# We do this by joining an arbitrary name to the instance name, separated
#  by a dot ".". In the following example,
# we demonstrate this by created an attribute for the name and the build year:

class Robot:
    pass

x = Robot()
y = Robot()

x.name = "Marvin"
x.build_year = "1979"

y.name = "Caliban"
y.build_year = "1993"

print(x.name)
print(y.name)

print(x.__dict__)
print(y.__dict__)

#Attributes can be bound to class names as well.
# In this case, each instance will possess this name as well.
#  Watch out, what happens, if you assign the same name to an instance:
print()
Robot.brand = "Kuka"
print(x.brand)
print(y.brand)
print(Robot.brand)

print()
x.brand = "Thales"
print(x.brand)
print(y.brand)
print(Robot.brand)

print(Robot.__dict__)


#Binding attributes to objects is a general concept in Python.
#Even function names can be attributed.
# You can bind an attribute to a function name in the same way,
#  we have done so far:
def f(x):
    return 42

f.x = 43
print(f.x)