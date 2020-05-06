# # We expand the previous example with counters for the threads.
# from threading import _start_new_thread
#
# num_threads = 0
#
# new = 0
# def heron(a):
#     global num_threads
#     num_threads += 1
#
#     # code has been left out, see above
#     num_threads -= 1
#     return new
#
#
# _start_new_thread(heron, (99,))
# _start_new_thread(heron, (999,))
# _start_new_thread(heron, (1733,))
# _start_new_thread(heron, (17334,))
#
# while num_threads > 0:
#     pass