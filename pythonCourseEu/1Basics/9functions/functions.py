def f(**kwargs):
    print(kwargs)

f(de="German",en="English",fr="French")

######
print()
def f(a,b,x,y):
    print(a, b, x, y)

d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
f(**d)

####

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

print(describe_pet(pet_name='harry', animal_type='hamster'))