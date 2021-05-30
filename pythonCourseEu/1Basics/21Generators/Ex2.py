def city_generator(): # then you don't have to use iter like in that example: expertises_iterator = iter(expertises)
    yield("London")
    yield("Hamburg")
    yield("Konstanz")
    yield("Amsterdam")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")

city = city_generator()
print(next(city))
print(next(city))



