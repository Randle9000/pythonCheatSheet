def BMI_weight(height):
    def h(weight):
        return weight / height**2
    return h

print(BMI_weight(1.7)(50))