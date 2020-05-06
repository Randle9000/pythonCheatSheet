# The thread Module
# It's possible to execute functions in a separate thread with the module Thread. To do this, we can use the function thread.start_new_thread:
#
# thread.start_new_thread(function, args[, kwargs])
#
# This method starts a new thread and return its identifier. The thread executes the function "function" (function is a reference to a function) with the argument list args (which must be a list or a tuple). The optional kwargs argument specifies a dictionary of keyword arguments. When the function returns, the thread silently exits. When the function terminates with an unhandled exception, a stack trace is printed and then the thread exits (but other threads continue to run).
#
# Example for a Thread in Python:

from threading import _start_new_thread

def heron(a):
    """Calculates the square root of a"""
    eps = 0.0000001
    old = 1
    new = 1
    while True:
        old,new = new, (new + a/new) / 2.0
        print(old, new)
        if abs(new - old) < eps:
            break
    return new

_start_new_thread(heron,(99,))
# _start_new_thread(heron,(999,))
# _start_new_thread(heron,(1733,))

c = input("Type something to quit.")