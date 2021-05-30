s = "Regular expressions easily explained!"
print("easily" in s)

#########################
print()

import re
x = re.search("cat","A cat and a rat can't be friends.")
print(x)
x = re.search("cow","A cat and a rat can't be friends.")
print(x)
#############################
print()
if re.search("cat", "A cat and a rat can't be friends."):
    print("Some kind of cat has been found :-)")
else:
    print("No cat has been found :-)")

##########################
print()

if re.search("cow","A cat and a rat can't be friends."):
    print("Cats and Rats and a cow.")
else:
    print("No cow around.")

a = re.search(r'.at','cat, bat, dog')
print(a)

#######################
import re
line = "He is a German called Mayer."
if re.search(r"M[ae][iy]er",line): print("I found one!")

#re.match  # match(re_str, s) checks for a match of re_str merely at the beginning of the string.


