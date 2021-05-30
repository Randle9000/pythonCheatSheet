# Command-line arguments
# Lots of scripts need access to the arguments passed to the script, when the script was started. argvargv (or to be precise sys.argv) is a list, which contains the command-line arguments passed to the script. The first item of this list contains the name of the script itself. The arguments follow the script name.
# The following script iterates over the sys.argv list :

#!/usr/bin/python

import sys

# it's easy to print this list of course:
print(sys.argv)

# or it can be iterated via a for loop:

for i in range(len(sys.argv)):
    if i == 0:
        print("Function name: %s" % sys.argv[0])
    else:
        print("%d. argument: %s" % (i,sys.argv[i]))