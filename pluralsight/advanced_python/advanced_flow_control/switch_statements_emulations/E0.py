animal = ""

# imitate switch case
if animal == "dog":
    print("it's dog")
elif animal == "cat":
    print("it's cat")
elif animal == "elephant":
    print("it's elephant")

# !!!!!!!!!!1
# it can be write as
animals = {
    "dog": lambda: print("it's dog"),
    "cat": lambda: print("it's cat"),
    "elephant": lambda: print("it's elephant")
}

animal_action = animals["dog"]
animal_action()
# each swich case can be write as that: using proper dictionary to assign value to fucntion (like lambada)
# it is key to remember that everything in python is object !
