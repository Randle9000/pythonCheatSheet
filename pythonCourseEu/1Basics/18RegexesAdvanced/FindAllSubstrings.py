import re

t="A fat cat doesn't eat oat but a rat eats bats."
mo = re.findall("[force]at", t)

print(mo)
################
print()
import re
str = "Course location is London or Paris!"
mo = re.search(r"location.*(London|Paris|Zurich|Strasbourg)",str)
if mo: print(mo.group())