class Widget:
    """ it is a shorthand for class Widget(object, metaclass=type): # type is base metaclass"""
    pass

w = Widget()
print(w)
print(type(w))
print(type(Widget)) # 'type' is the metaclass for each class. But type of type is type so it is the recursion