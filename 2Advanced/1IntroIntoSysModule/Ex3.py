# Standard data streams
#
# Every serious user of a UNIX or Linux operating system knows standard streams, i.e. input, standard output and standard error. They are known as pipes. They are commonly abbreviated as stdin, stdout, stderr.
# The standard input (stdin) is normally connected to the keyboard, while the standard error and standard output go to the terminal (or window) in which you are working.
#
# These data streams can be accessed from Python via the objects of the sys module with the same names, i.e. sys.stdin, sys.stdout and sys.stderr.

import sys

for i in (sys.stdin, sys.stdout, sys.stderr):
    print(i)

print()
print("Going via stdout")
sys.stdout.write("Another way to do it!\n")
x = input("read value via stdin: ")
print("type in value: ", sys.stdin.readline()[:-1])