from functools import singledispatch


class Shape:
    def __init__(self, solid):
        self.solid = solid


class Circle(Shape):
    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.center = center
        self.radius = radius


class Parallelogram(Shape):
    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc


class Triangle(Shape):
    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc


# optimal design
@singledispatch
def draw(shape):
    raise TypeError(f"don't know how to draw {shape}")


@draw.register(Circle)
def _(shape): # name of function is not needed anymore
    print("\u25CF" if shape.solid else "\u25A1")


@draw.register(Parallelogram)
def _(shape):
    print("\u25B0" if shape.solid else "\u25B1")


@draw.register(Triangle)
def _(shape):
    print("\u25B2" if shape.solid else "\u25B3")


def main():
    shapes = [Circle(center=(0, 0), radius=5, solid=False),
              Parallelogram(pa=(0, 0), pb=(1, 1), pc=(0, 3), solid=True),
              Triangle(pa=(0, 0), pb=(2, 3), pc=(0, 1), solid=True)]
    for shape in shapes:
        draw(shape) # instead of shape.draw we know have


if __name__ == '__main__':
    main()
