expertises = ["Novice", "Beginner", "Intermediate", "Proficient", "Experienced", "2Advanced"]
expertises_iterator = iter(expertises)

print(next(expertises_iterator))
print(next(expertises_iterator))

while expertises_iterator:
    try:
        city = next(expertises_iterator)
        print(city)
    except StopIteration:
        break