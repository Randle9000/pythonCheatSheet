class Planet:

    def __init__(self,
                 name,
                 radius_metres,
                 mass_kilograms,
                 orbital_period_seconds,
                 surface_temperature_kelvin):
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin


# but here is a problem we cann assign negative value (or even string 'x') to mass_kg what does no make sense.
# To solve it we can create for each value @property methods and @'func_name.setter methods
# but there is a better solutioon (as almost always)
mercury = Planet("Mercury",
                 radius_metres=2439.7e3,
                 mass_kilograms=-1 * 3.3022e23,
                 orbital_period_seconds=7.60052e6,
                 surface_temperature_kelvin=340)

print(mercury)


