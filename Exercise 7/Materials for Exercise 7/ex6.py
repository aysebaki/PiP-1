import math
class Shape:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def to_string(self) -> str:
        return "Shape: x={}, y={}".format(self.x, self.y)

    def area(self) -> float:
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def to_string(self) -> str:
        return "Rectangle: x={}, y={}, width={}, height={}".format(self.x, self.y, self.width, self.height)

    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int):
        # call the superclass constructor to set the x and y attributes
        super().__init__(x, y)
        self.radius = radius

    def to_string(self) -> str:
        # call the superclass to_string method to get the string representation of the x and y attributes
        base_str = super().to_string()
        return "{}, radius={}".format(base_str, self.radius)

    def area(self) -> float:
        return self.radius ** 2 * math.pi

class Square(Rectangle):
    def __init__(self, x: int, y: int, length: int):
        # call the superclass constructor and set the width and height to the length value
        super().__init__(x, y, length, length)

    def to_string(self) -> str:
        # call the superclass to_string method to get the string representation of the attributes
        return "Square: {}".format(super().to_string())

    def area(self) -> float:
        # call the superclass area method to calculate the area
        return super().area()

s = Shape(4, 9)
print(s.to_string())
r = Rectangle(1, 2, 3, 4)
print(r.to_string())
print("Rectangle area:", r.area())
c = Circle(5, 2, 2)
print(c.to_string())
print("Circle area:", c.area())
s = Square(0, 0, 10)
print(s.to_string())
print("Square area:", s.area())