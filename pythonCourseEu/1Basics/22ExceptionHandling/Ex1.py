#Exceptions handling in Python is very similar to Java.
# The code, which harbours the risk of an exception,
#  is embedded in a try block. But whereas in Java exceptions
# are caught by catch clauses, we have statements introduced
#  by an "except" keyword in Python. It's possible to create
# "custom-made" exceptions:
#  With the raise statement it's possible to force a specified exception to occur.

import sys

try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno,strerror))
    # e can be printed directly without using .args:
    # print(e)
except ValueError:
    print("No valid integer in line.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
else: # like finally
    print('end of try catch')


try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except (IOError, ValueError):
    print("An I/O error or a ValueError occurred")
except:
    print("An unexpected error occurred")
    raise

# ##Failing Silently
# In the previous example, we informed our users that one of the fles
# was unavailable. But you don’t need to report every exception you catch.
# Sometimes you’ll want the program to fail silently when an exception occurs
# and continue on as if nothing happened. To make a program fail silently, you
# write a try block as usual, but you explicitly tell Python to do nothing in the
# except block. Python has a pass statement that tells it to do nothing in a block: