"""
Currying: instead of f(x,y) => G(x)(y) or h(i(x))
"""
# simple example of composition


def compose(g, f):
    def h(x):
        return g(f(x))
    return h


def celsius2fahrenheit(t):
    return 1.8*t+32


def adjustment_of_termometer(t):
    return 0.9*t+1

real_temp_coverter = compose(adjustment_of_termometer, celsius2fahrenheit)
real_temp = real_temp_coverter(10)
print(real_temp, celsius2fahrenheit(10))

# compose with arbitraty number of arguments:


def compose_for_bmi(g,f):
    def h(*args, **kwargs):
        return g(f(*args, *kwargs))
    return h


def BMI(weight, height):
    print(weight / height**2)
    return weight / height**2



def evaluate_BMI(bmi):
    if bmi < 15:
        print("vere severly underweight")
    elif bmi < 16:
        print('severly underweight')
    elif bmi < 18.5:
        print('underweight')
    elif bmi < 25:
        print('normal')
    elif bmi < 30:
        print('overweight')
    elif bmi < 35:
        print("obese Class I")
    elif bmi < 40:
        print("obese Class II")
    else:
        print("obese Class III")

f = compose_for_bmi(evaluate_BMI, BMI)
print(f(8, 1.88))