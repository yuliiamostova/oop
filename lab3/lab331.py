import math


class Figure:
    def dimention(self):
        return None

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        if self.dimention() == 2:
            return self.square()
        else:
            return None

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise ValueError("Трикутник не існує")
    def dimention(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimetr() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def dimention(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        difference = abs(self.a - self.b)
        if difference == 0:
            raise ValueError("Трапеція не існує")

        x = (self.c ** 2 - self.d ** 2 + difference ** 2) / (2 * difference)
        h = self.c ** 2 - x ** 2
        if h <= 0:
            raise ValueError("Трапеція не існує")

        h1 = h ** 0.5
        return (self.a + self.b) * h1 / 2

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

class Ball(Circle):
    def __init__(self, r):
        super().__init__(r)

    def dimention(self):
        return 3

    def squareSurface(self):
        return 4 * math.pi * self.r ** 2

    def volume(self):
        return 4 * math.pi * self.r ** 3 / 3

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = float(h)

    def dimention(self):
        return 3

    def squareBase(self):
        return Triangle.square(self)

    def height(self):
        return self.h

    def squareSurface(self):
        l = math.sqrt(self.h ** 2 + (self.a * math.sqrt(3) / 6) ** 2)
        return 3 * self.a * l / 2

    def volume(self):
        return self.squareBase() * self.h / 3

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def squareSurface(self):
        l1 = math.sqrt(self.h ** 2 + (self.b / 2) ** 2)
        l2 = math.sqrt(self.h ** 2 + (self.a / 2) ** 2)
        return self.a * l1 + self.b * l2

    def volume(self):
        return self.squareBase() * self.h / 3

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def height(self):
        return self.c

    def squareSurface(self):
        return 2 * (self.a + self.b) * self.c

    def volume(self):
        return self.a * self.b * self.c


class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def squareSurface(self):
        l = math.sqrt(self.r ** 2 + self.h ** 2)
        return math.pi * self.r * l

    def volume(self):
        return self.squareBase() * self.h / 3

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = float(h)

    def dimention(self):
        return 3

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def squareSurface(self):
        return super().perimetr() * self.h

    def volume(self):
        return self.squareBase() * self.h





def create_figure(name, p):
    if name == "Triangle":
        return Triangle(p[0], p[1], p[2])
    elif name == "Rectangle":
        return Rectangle(p[0], p[1])
    elif name == "Trapeze":
        return Trapeze(p[0], p[1], p[2], p[3])
    elif name == "Parallelogram":
        return Parallelogram(p[0], p[1], p[2])
    elif name == "Circle":
        return Circle(p[0])
    elif name == "Ball":
        return Ball(p[0])
    elif name == "TriangularPyramid":
        return TriangularPyramid(p[0], p[1])
    elif name == "QuadrangularPyramid":
        return QuadrangularPyramid(p[0], p[1], p[2])
    elif name == "RectangularParallelepiped":
        return RectangularParallelepiped(p[0], p[1], p[2])
    elif name == "Cone":
        return Cone(p[0], p[1])
    elif name == "TriangularPrism":
        return TriangularPrism(p[0], p[1], p[2], p[3])

def read_figures(filename):
    figures = []
    counts = {
        "Triangle": 3,
        "Rectangle": 2,
        "Trapeze": 4,
        "Parallelogram": 3,
        "Circle": 1,
        "Ball": 1,
        "TriangularPyramid": 2,
        "QuadrangularPyramid": 3,
        "RectangularParallelepiped": 3,
        "Cone": 2,
        "TriangularPrism": 4
    }
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read().split()
    i = 0
    while i < len(data):
        name = data[i]
        if name not in counts:
            i += 1
            continue
        count = counts[name]
        try:
            params = []
            for j in range(count):
                params.append(float(data[i + 1 + j]))
            figure = create_figure(name, params)
            figure.volume()
            figures.append((name, params, figure))

        except ValueError:
            pass
        except IndexError:
            pass
        i += count + 1
    return figures

def find_max_figure(figures):
    if len(figures) == 0:
        return None
    max_figure = figures[0]
    for figure in figures:
        if figure[2].volume() > max_figure[2].volume():
            max_figure = figure
    return max_figure

figures = read_figures("input01.txt")
max_figure = find_max_figure(figures)


print("Назва фігури:", max_figure[0])
print(max_figure[1])
print("Найбільша міра:", max_figure[2].volume())
