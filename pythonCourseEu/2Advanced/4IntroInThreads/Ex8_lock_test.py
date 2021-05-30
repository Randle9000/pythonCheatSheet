import threading
import time
import concurrent.futures



def func_1(lock_1, lock_2, name):
    lock_1.acquire()
    lock_2.acquire()

    print(name)
    time.sleep(5)
    print('func_1')
    lock_2.release()
    lock_1.release()


def func_2(lock_1, lock_2, name):
    lock_2.acquire()
    print(name)
    print('func_2')
    lock_2.release()

if __name__ == '__main__':
    l_1 = threading.Lock()
    l_2 = threading.Lock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(func_1, l_1, l_2, 'thread_1')
        executor.submit(func_2, l_1, l_2, 'thread_2')
        # executor.map(thread_lock, ['thread_1', 'thread_2'])
