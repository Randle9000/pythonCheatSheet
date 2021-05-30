from _thread import start_new_thread, allocate_lock
num_threads = 0

""" added solution of lock"""
thread_started = False
lock = allocate_lock()

def heron(a):
    """calculate rest root of a"""
    global num_threads, thread_started
    """problem: 
    thread 1 can go to that point and but put to sleep by system, however value readed is 0 and, local variable of thread is also 0
    then the thread 2 can go and als check it and then value is 0 and local is zero
    but when these two thread go further then the num_threads will be 1 for both of then but should be 2!!!
    
    Solution: lock: so the druing execution of particular section a thread will not be interrupted or put to sleep!
    Key words:
    thread_started
    allocate_lock
    lock.acquire
    lock release
    
    """
    lock.acquire()
    num_threads += 1
    thread_started = True
    lock.release()

    eps = 0.00000001
    new = old = 1
    while True:
        old, new = new, (new + a/new) / 2
        print(old, new)
        if abs(new - old) < eps:
            break
    lock.acquire()
    num_threads -= 1
    lock.release()
    return new


start_new_thread(heron,(99,))
start_new_thread(heron,(999,))


while not thread_started:
    pass

while num_threads > 0:
    pass

# c = input("Type sth to qui\n") # it is nacessary because otherwise all threads would be extied
