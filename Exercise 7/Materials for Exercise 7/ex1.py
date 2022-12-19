import math

class Complex:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def print(self):
        sign = "+" if self.imaginary >= 0 else "-"
        print(f"{self.real} {sign} {abs(self.imaginary)}i")

    def abs(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)


c1 = Complex(1.2, -5.4)
c1.print()  # prints 1.2 - 5.4i
c2 = Complex(3.0, 4.0)
c2.print()  # prints 3.0 + 4.0i
print(c2.abs())  # prints 5.0