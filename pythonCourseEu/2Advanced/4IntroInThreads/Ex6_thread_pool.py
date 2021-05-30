import threading
import time
import concurrent.futures


class ThreadTest():
    def __init__(self):
        self.val = 0
        self._lock = threading.Lock()

    def update(self, name):
        # self._lock.acquire()
        with self._lock:
            local_copy = self.val
            local_copy += 1
            time.sleep(0.2)
            self.val = local_copy
            print(name, self.val)
        # self._lock.release()

if __name__ == '__main__':
    tt = ThreadTest()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4, thread_name_prefix="thread_") as executor:
        executor.map(tt.update, ['thread_1', 'thread_2', 'thread_3'])

        # print('in with block') # join are not here they are at the and of with
    print('Out of with block')
