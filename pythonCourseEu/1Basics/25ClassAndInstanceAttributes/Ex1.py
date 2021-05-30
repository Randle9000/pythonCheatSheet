#We can also define attributes at the class level.
# Class attributes are attributes which are owned by the class itself.
# like static fields in java.

class A:
    a = 'i am a class attribute'

x = A()
y = A()
print ('x - ' + x.a, '\n','y - ' + y.a, '\n','A class - ' + A.a, '\n' )

# if you want to change a class attribute,
# you have to do it with the notation ClassName.AttributeName.
# Otherwise, you will create a new instance variable.

x.a = "This creates a new instance attribute for x!"
print ('x - ' + x.a, '\n','y - ' + y.a, '\n','A class - ' + A.a, '\n' )

# print(x.__dict__)
# print(A.__dict__)
# print(A.__class__.__dict__)