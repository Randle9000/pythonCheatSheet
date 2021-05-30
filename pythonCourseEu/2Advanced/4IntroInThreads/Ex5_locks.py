import threading
import time
import concurrent.futures


def print_data(thread_name):
    if thread_name in ['thread_3', 'thread_2']:
        time.sleep(5)
    val = 0
    val += 1
    print(val)



if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4, thread_name_prefix="thread_") as executor:
        executor.map(print_data, ['thread_1', 'thread_2', 'thread_3'])
        # print('in with block') # join are not here they are at the and of with
    print('Out of with block')


    # thread_1 = threading.Thread(target=print_data, args=["thread_1"])
    # thread_2 = threading.Thread(target=print_data, args=["thread_2"])
    # thread_3 = threading.Thread(target=print_data, args=["thread_3"])
    #
    # thread_1.start()
    # thread_2.start()
    # thread_3.start()


