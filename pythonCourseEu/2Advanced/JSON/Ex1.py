# The json module allows you to dump simple Python data structures into a
# fle and load the data from that fle the next time the program runs. You can
# also use json to share data between different Python programs. Even better,
# the JSON data format is not specifc to Python, so you can share data you
# store in the JSON format with people who work in many other programming
# languages. It’s a useful and portable format, and it’s easy to learn.

import json

numbers = [1,2,3,4,5,6]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    #we use the json.dump() function to store the list numbers in the fle numbers.json
    json.dump(numbers, f_obj)


with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)