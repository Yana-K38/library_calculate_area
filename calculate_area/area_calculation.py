import math


class Shape:
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        
    def calculate_area(self):
        half_meter = (self.side_1 + self.side_2 + self.side_3)/2
        area = math.sqrt(half_meter * (half_meter - self.side_1) * (half_meter - self.side_2) * (half_meter - self.side_3))
        return area
    
    def right_triangle(self):
        sides = sorted([self.side_1, self.side_2, self.side_3])
        if sides[0] ** 2 + sides[1] ** 2 == sides[3] ** 2:
            return "Треугольник прямоугольный"
        else:
            return "Треугольник не прямоугольный"
        