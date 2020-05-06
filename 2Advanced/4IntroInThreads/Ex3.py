# threading Module
# We want to introduce the threading module with an example. The Thread of the example doesn't do a lot, essentially it just sleeps for 5 seconds and then prints out a message:

import time
from threading import Thread

def sleeper(i):
    print("thread %d sleeps for 5 seconds" % i)
    time.sleep(5)
    print("thread %d woke up" % i)

for i in range(10):
    t = Thread(target=sleeper, args=(i,))
    t.start()

#Method of operation of the threading.Thread class: The class threading.Thread has a method start(), which can start a Thread. It triggers off the method run(), which has to be overloaded. The join() method makes sure that the main program waits until all threads have terminated.

