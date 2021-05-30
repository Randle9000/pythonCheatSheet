

import queue
import concurrent.futures
import threading
import time


def producer(pipeline, event):
    while not event.is_set():
        for i in range(0, 10, 1):
            message = i
            print("producer thread produced {0}".format(message))
            pipeline.set_msg(message)
            if i == 3:
                time.sleep(0.5) # articial sleep corresponds to the bottleneck in real live! :  problem !!!
            print('producer pipeline size', pipeline.qsize())
        print("producer thread ends producing")


def consumer(pipeline, event):
    print('CONSUMER thread started work')
    while (not pipeline.empty() or not event.is_set()):
        message = pipeline.get_msg()
        print(message, "consumer")
        # print('in while consumer pipeline size', pipeline.qsize())
    print('CONSUMER thread ends work')


class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def set_msg(self, msg):
        self.put(msg)

    def get_msg(self):
        value = self.get()
        return value
#

if __name__ == "__main__":
    pipeline = Pipeline()
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:

        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(10)

        print('just before event.set')
        event.set()


