"""
@property is a decorator and work as:
@property
def name():
....
corresponds to:
name = property(name)
"""


class Planet:
    # the po
    def __init__(self,
                 name,
                 radius_meters,
                 mass_kilograms,
                 orbital_period_seconds,
                 surface_temperature_kelvin):
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

    def _get_radius_meters(self):
        return self._radius_metres

    def _set_radius_meters(self, value):
        if value <= 0:
            raise ValueError(f"radius value {value} must be greater than zero")
        self._radius_metres = value

    radius_meters = property(fget=_get_radius_meters, fset=_set_radius_meters)

    def _get_mass_kilograms(self):
        return self._mass_kilograms

    def _set_mass_kilograms(self, value):
        if value <= 0:
            raise ValueError(f"mass_kilograms value {value} must be greater than zero")
        self._mass_kilograms = value

    mass_kilograms = property(fget=_get_mass_kilograms, fset=_set_mass_kilograms)

    def _get_orbital_period_seconds(self):
        return self._orbital_period_seconds

    def _set_orbital_period_seconds(self, value):
        if value <= 0:
            raise ValueError(f"orbital_period_seconds value {value} must be greater than zero")
        self._orbital_period_seconds = value

    orbital_period_seconds = property(fget=_get_orbital_period_seconds, fset=_set_orbital_period_seconds)

    def _get_surface_temperature_kelvin(self):
        return self._surface_temperature_kelvin

    def _set_surface_temperature_kelvin(self, value):
        if value <= 0:
            raise ValueError(f"surface_temperature_kelvin value {value} must be greater than zero")
        self._surface_temperature_kelvin = value

    surface_temperature_kelvin = property(fget=_get_surface_temperature_kelvin, fset=_set_surface_temperature_kelvin)

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


