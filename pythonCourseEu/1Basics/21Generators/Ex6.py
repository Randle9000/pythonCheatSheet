#enerators can not only send objects but
#  also receive objects. Sending a message, i.e. an object,
# into the generator can be achieved by applying the send
#  method to the generator object. Be aware of the fact that send both sends a value to the generator and returns the value yielded by the generator.
# We will demonstrate this
# behavior in the following simple example of a coroutine:
def infinite_looper(objects):

    count = 0
    while True:
        if count >= len(objects):
            count = 0
        message = yield objects[count]
        if message != None:
            count = 0 if message < 0 else message
        else:
            count += 1

x = infinite_looper("A string with some words")
print(next(x))

print(x.send(9))