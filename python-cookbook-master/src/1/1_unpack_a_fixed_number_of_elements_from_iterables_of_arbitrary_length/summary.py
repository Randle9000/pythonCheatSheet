# example.py
#
# Unpacking of tagged tuples of varying sizes
"""
if you want to discard certain values then use _
unpacking works with any object that happens to be iterable
"""

records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records: # first example: tah = foo, args = [1, 2] *args = 1, 2
    print(type(args))
    if tag == 'foo':
        do_foo(*args) # it is unpacked list tahts why it can go x, y,
    elif tag == 'bar':
        do_bar(*args)
