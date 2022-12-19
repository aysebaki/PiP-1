class Shape:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def to_string(self) -> str:
        return "Shape: x={}, y={}".format(self.x, self.y)

    def area(self) -> float:
        raise NotImplementedError

