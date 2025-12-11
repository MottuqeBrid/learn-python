# Method Overloading in Python

import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return math.pi * super().area()


sp = Shape(5, 10)
print("Area of shape:", sp.area())

c = Circle(7)
print("Area of circle:", c.area())
