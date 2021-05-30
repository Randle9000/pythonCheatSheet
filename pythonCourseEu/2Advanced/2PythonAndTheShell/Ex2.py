# Executing Shell scripts with os.system()
# It's not possible in Python to read a character without having to type the return key as well. On the other hand this is very easy on the Bash shell. The Bash command "read -n 1 waits for a key (any key) to be typed. If you import os, it's easy to write a script providing getch() by using os.system() and the Bash shell. getch() waits just for one character to be typed without a return:

import os


def getch():
    os.system("bash -c \"read -n 1\"") # for linux 


getch()