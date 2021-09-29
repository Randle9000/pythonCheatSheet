"""
we will introduce class positive - special descriptor.
"""
from weakref import WeakKeyDictionary


class Positive:
    """
    it is a class which behaves like a descriptor it assures that value will be positive
    """
    def __init__(self):
        """
        needed to configure the new instance of a descriptor
        """
        self._instance_data = WeakKeyDictionary()
        # WeakKeyDict... is needed to keep data related to the proper descriptor
        # but the fill of that dicts is done in __set__

    def __get__(self, instance, owner): #  instance and owner are needed to know which instance we use.
        # remember that Positive is a part of class not the object and then we need which instance of class we use,
        # owner is a simple the class.
        if instance is None: # for Planet.__set__
            return self # return descriptor object itself.
        return self._instance_data[instance]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"Value {value} must be positive")
        self._instance_data[instance] = value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete attribute")


class Planet:
    # the po
    def __init__(self,
                 name,
                 radius_meters,
                 mass_kilograms,
                 orbital_period_seconds,
                 surface_temperature_kelvin):
        self.name = name
        self.radius_meters = radius_meters # set through descriptor
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

    radius_meters = Positive()  # bind descriptor instance to class attribute
    mass_kilograms = Positive()
    orbital_period_seconds = Positive()
    surface_temperature_kelvin = Positive()

    def __repr__(self):
        return f"Planet {self.name} has radius {self.radius_meters} meters," \
               f"and mass is {self.mass_kilograms} kg"

# but here is a problem we cann assign negative value (or even string 'x') to mass_kg what does no make sense.
# To solve it we can create for each value @property methods and @'func_name.setter methods
# but there is a better solution (as almost always)


mercury = Planet("Mercury",
                 radius_meters=2439.7e3,
                 mass_kilograms=1 * 3.3022e23,
                 orbital_period_seconds=7.60052e6,
                 surface_temperature_kelvin=340)


pluto = Planet("pluto",
                 radius_meters=1234.7e3,
                 mass_kilograms=1 * 1.3022e23,
                 orbital_period_seconds=5.60052e6,
                 surface_temperature_kelvin=120)

print(mercury)
print(dir(mercury))
print(mercury.__dict__)
m = mercury.mass_kilograms  # in fact it works like this: m = Positive.__get__(self, mercury, Planet)
mercury.mass_kilograms = m  # works like: Positive.__set__(self, mercury, m)
