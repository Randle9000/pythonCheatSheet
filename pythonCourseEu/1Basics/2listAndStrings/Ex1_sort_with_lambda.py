
import datetime

class Person():
    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height

    def __repr__(self):
        return self.name

people_list = [Person('Matthew', datetime.date(1990,12,13), 188),
            Person('John', datetime.date(1960, 7, 4), 166),
            Person('Richard', datetime.date(1950,11,23), 176)]

people_list.sort(key=lambda item: item.name)
print(people_list)

""" how key works:
lambda item: item.name
item is a passed value and operation which is done is item.name
"""
john = Person('John', datetime.date(1960, 7, 4), 166)
a  = lambda item: item.name
print(a(john))

##
from operator import attrgetter
print("\nbeeter sorting !!!")
""" it uses attrgetter() or itemgeter()
attrgetter is for objects
itemgetter is for dicts tuples etc.
 """
people_list.sort(key=attrgetter('height'), reverse=True)
print(people_list)