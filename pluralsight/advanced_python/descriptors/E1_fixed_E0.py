# its better than E0.py but still here is the a lot of code, we can fix it.

class Planet:
    def __init__(self,
                 name,
                 radius_meters,
                 mass_kilograms,
                 orbital_period_seconds,
                 surface_temperature_kelvin):

        """
        The @properties as a setter and getter of sth works here because,
        You have to remember that object is created by __new__ method and all this setter are created,
        before the __init__ is called. So simple but i had to think about it. that's why
        the radius_meter use
        @radius_meters.setter
        def radius_meter():
        ...
        instead of simple assignment.
        """
        self.name = name
        self.radius_meters = radius_meters
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty name")
        self._name = value

    @property
    def radius_meters(self):
        return self._radius_metres

    @radius_meters.setter
    def radius_meters(self, value):
        if value <= 0:
            raise ValueError(f"radius value {value} must be greater than zero")
        self._radius_metres = value

    @property
    def mass_kilograms(self):
        return self._mass_kilograms

    @mass_kilograms.setter
    def mass_kilograms(self, value):
        if value <= 0:
            raise ValueError(f"mass_kilograms value {value} must be greater than zero")
        self._mass_kilograms = value

    @property
    def orbital_period_seconds(self):
        return self._orbital_period_seconds

    @orbital_period_seconds.setter
    def orbital_period_seconds(self, value):
        if value <= 0:
            raise ValueError(f"orbital_period_seconds value {value} must be greater than zero")
        self._orbital_period_seconds = value

    @property
    def surface_temperature_kelvin(self):
        return self._surface_temperature_kelvin

    @surface_temperature_kelvin.setter
    def surface_temperature_kelvin(self, value):
        if value <= 0:
            raise ValueError(f"surface_temperature_kelvin value {value} must be greater than zero")
        self._surface_temperature_kelvin = value

    def __repr__(self):
        return f"Planet {self.name} has radius {self.radius_meters} meters," \
               f"and mass is {self.mass_kilograms} kg"

# but here is a problem we cann assign negative value (or even string 'x') to mass_kg what does no make sense.
# To solve it we can create for each value @property methods and @'func_name.setter methods
# but there is a better solutioon (as almost always)
mercury = Planet("Mercury",
                 radius_meters=2439.7e3,
                 mass_kilograms=1 * 3.3022e23,
                 orbital_period_seconds=7.60052e6,
                 surface_temperature_kelvin=340)

print(mercury)
print(dir(mercury))
print(mercury.__dict__)
