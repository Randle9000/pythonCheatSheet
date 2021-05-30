## list comprehesion
"""
syntax:
[ <expresion> for <element> in <iterable> ]
expression -  can be quite complex so You can use there if else statement, can be fucntion f(x)

[ <expresion> for <element> in <iterable>  if <condition>]
"""


Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print(Fahrenheit)

#############################

print()
print([(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2])


#################################

print()
colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [(x, y) for x in colours for y in things]
print(coloured_things)

####
# else  exampel:
"""
if/else before 'for' is not part of list comprehension, however after for is, and is used to filter elemetes form the source of iterable
"""
print('else example')
l = [1,2,3,4,5]
l1 = [x*x for x in l if x > 2]
print(l1)

##
#lsit comprehension does not work with in place mutations functions like .sort() instead can vbe ysed sorted(x)
##

## if else example
l = [1,2,3,4,5,6,7]
l2 = [x * (x if (x % 2) == 0 else 1) for x in l]
print(l2)