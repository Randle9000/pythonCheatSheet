import threading


def print_numbers(name):
    l = []
    for i in range(0,20,2):
        print("{0} print {1}".format(name, i))
        l.append("{0} print {1}".format(name, i))

if __name__ == '__main__':
    thread_1 = threading.Thread(target=print_numbers, args=["thread_1"])
    thread_2 = threading.Thread(target=print_numbers, args=["thread_2"])
    thread_3 = threading.Thread(target=print_numbers, args=["thread_3"])

    thread_1.start()
    thread_2.start()
    thread_3.start()



    thread_1.join() # main thread cannot go further till thread_1 won't finisht his work
    thread_2.join() # main thread cannot go further till thread_1 won't finisht his work


    for i in range(1,20,2):
        print("main thread", i)