import math

class Rectangle(object):
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2*self.height + 2*self.width

class Triangle(object):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class Circle(object):
    def __init__(self,r):
        self.radius = r

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Regularhexagon(object):
    def __init__(self, s):
        self.side = s

    def area(self):
        return (3 * math.sqrt(3) / 2) * self.side ** 2

    def perimeter(self):
        return 6 * self.side

def main():
    Rectangles = []
    Triangles = []
    Circles = []
    Regularhexagons = []

    Rectangles.append(Rectangle(6,3))
    Triangles.append(Triangle(3, 4, 5))
    Circles.append(Circle(4))
    Regularhexagons.append(Regularhexagon(5))

    for shape in Rectangles:
        print(f"Rectangle area : {shape.area()}")
        print(f"Rectangle perimater : {shape.perimeter()}")

    for shape in Triangles:
        print(f"Triangle area : {shape.area()}")
        print(f"Triangle perimater : {shape.perimeter()}")

    for shape in Circles:
        print(f"Circle area : {shape.area():.2f}")
        print(f"Circle perimater : {shape.perimeter():.2f}")

    for shape in Regularhexagons:
        print(f"Regularhexagon area : {shape.area():.2f}")
        print(f"Regularhexagon perimater : {shape.perimeter()}")



if __name__== "__main__":
        main()