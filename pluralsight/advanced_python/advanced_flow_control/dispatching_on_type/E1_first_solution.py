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


# better design
def draw_circle(shape):
    print("\u25CF" if shape.solid else "\u25A1")


def draw_parallelogram(shape):
    print("\u25B0" if shape.solid else "\u25B1")


def draw_triangle(shape):
    print("\u25B2" if shape.solid else "\u25B3")


def draw(shape):
    # if isinstance(shape, Circle):
    #     draw_circle(shape)
    # elif isinstance(shape, Parallelogram):
    #     draw_parallelogram(shape)
    # elif isinstance(shape, Triangle):
    #     draw_triangle(shape)
    # else:
    #     raise TypeError(f"Can't draw shape {shape}")

    # emulate case by dict:
    drawers = {
        Circle: draw_circle,
        Parallelogram: draw_parallelogram,
        Triangle: draw_triangle
    }
    try:
        drawer = drawers[type(shape)]
    except KeyError as e:
        raise TypeError("can't draw shape") from e
    else:
        drawer(shape)

def main():
    shapes = [Circle(center=(0, 0), radius=5, solid=False),
              Parallelogram(pa=(0, 0), pb=(1, 1), pc=(0, 3), solid=True),
              Triangle(pa=(0, 0), pb=(2, 3), pc=(0, 1), solid=True)]
    for shape in shapes:
        draw(shape) # instead of shape.draw we know have


if __name__ == '__main__':
    main()