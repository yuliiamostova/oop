import turtle as t
import math


class Petal:
    def __init__(self, colour, radius):
        self.colour = colour
        self.radius = radius

    def draw(self, x, y, angle):
        t.penup()
        t.goto(x, y)
        t.setheading(angle)
        t.pendown()

        t.color(self.colour)
        t.fillcolor(self.colour)
        t.begin_fill()

        t.circle(self.radius, 60)
        t.left(120)
        t.circle(self.radius, 60)
        t.left(120)

        t.end_fill()


class Leaf:
    def __init__(self, colour, size):
        self.colour = colour
        self.size = size

    def draw(self, x, y, angle):
        t.penup()
        t.goto(x, y)
        t.setheading(angle)
        t.pendown()

        t.color(self.colour)
        t.fillcolor(self.colour)
        t.begin_fill()

        t.circle(self.size, 60)
        t.left(120)
        t.circle(self.size, 60)
        t.left(120)

        t.end_fill()


class Stem:
    def __init__(self, colour, width):
        self.colour = colour
        self.width = width

    def draw(self, x1, y1, x2, y2):
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.pencolor(self.colour)
        t.width(self.width)
        t.goto(x2, y2)


class Flower:
    def __init__(self, x, y, petal_colour, center_colour):
        self.x = x
        self.y = y
        self.petal = Petal(petal_colour, 50)
        self.leaf = Leaf("dark green", 40)
        self.stem = Stem("dark green", 3)
        self.center_colour = center_colour
        self.base_x = 0
        self.base_y = -250

    def draw_center(self, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(self.center_colour)
        t.begin_fill()
        t.circle(8)
        t.end_fill()

    def draw(self):
        self.stem.draw(self.base_x, self.base_y, self.x, self.y)
        dx = self.x - self.base_x
        dy = self.y - self.base_y
        angle = math.degrees(math.atan2(dy, dx))

        leaf1_x = self.base_x + dx * 0.35
        leaf1_y = self.base_y + dy * 0.35
        leaf2_x = self.base_x + dx * 0.6
        leaf2_y = self.base_y + dy * 0.6

        self.leaf.draw(leaf1_x, leaf1_y, angle + 45)
        self.leaf.draw(leaf2_x, leaf2_y, angle - 45)

        for petal_angle in range(0, 360, 45):
            self.petal.draw(self.x, self.y, petal_angle)

        self.draw_center(self.x, self.y)


screen = t.Screen()
screen.setup(900, 700)
t.speed(0)

flowers = [
    Flower(-120, 0, "hot pink", "yellow"),
    Flower(-60, 40, "pink", "orange"),
    Flower(0, 70, "violet", "yellow"),
    Flower(60, 40, "medium violet red", "orange"),
    Flower(120, 0, "magenta", "yellow")
]

for flower in flowers:
    flower.draw()

t.mainloop()
