# Like all the other modules, the sys module has to be imported with the import statement, i.e.
#
# import sys
#
# The sys module provides information about constants, functions and methods of the Python interpreter.
# dir(system) gives a summary of the available constants, functions and methods. Another possibility is the help() function.
# Using help(sys) provides valuable detail information.
#
# The module sys informs e.g. about the maximal recursion depth (sys.getrecursionlimit() ) and provides the possibility to change (sys.setrecursionlimit())
# The current version number of Python can be accessed as well:

import sys
print(sys.version)
print(sys.version_info)