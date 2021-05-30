# Under Windows you will have to import the module msvcrt. Pricipially we only have to import getch() from this module.
# So this is the Windows solution of the problem:

import os, platform
if platform.system() == "Windows":
    import msvcrt
def getch():
    if platform.system() == "Linux":
        os.system("bash -c \"read -n 1\"")
    else:
        msvcrt.getch()

print("Type a key!")
getch()
print("Okay")