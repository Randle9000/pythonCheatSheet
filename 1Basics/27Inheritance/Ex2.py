#Overloading and overriding

#Instead of using the methods "Name" and "GetEmployee" in our previous example,
# it might have been better to put this functionality into the "__str__" method.
# In doing so, we gain a lot, especially a leaner design.
# We have a string casting for our classes and we can simply print out instances.
# Let's start with a __str__ method in Person:

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self): # String method !
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum

    #Overriding
    def __str__(self):
        return self.firstname + " " + self.lastname + ", " +  self.staffnumber


x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x)
print(y)

#overloading is replace by * operator