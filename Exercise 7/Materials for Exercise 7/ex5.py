import math

class Shape:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def to_string(self) -> str:
        return "Shape: x={}, y={}".format(self.x, self.y)

    def area(self) -> float:
        raise NotImplementedError


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
