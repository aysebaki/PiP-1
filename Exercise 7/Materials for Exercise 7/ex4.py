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