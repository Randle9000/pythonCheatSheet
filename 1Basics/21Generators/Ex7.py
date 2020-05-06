#The throw() method raises an exception at the point where the generator
# was paused, and returns the next value yielded by the generator.
def infinite_looper(objects):
    count = 0
    while True:
        if count >= len(objects):
            count = 0
        try:
            message = yield objects[count]
        except Exception:
            print("index: " + str(count))
        if message != None:
            count = 0 if message < 0 else message
        else:
            count += 1

looper = infinite_looper("Python")
print(next(looper))
print(next(looper))
looper.throw(Exception)