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

    def add(self, other: "Complex"):
        if not isinstance(other, Complex):
            raise TypeError("other must be an instance of Complex")

        self.real += other.real
        self.imaginary += other.imaginary

    @staticmethod
    def add_all(comp: "Complex", *comps: "Complex"):
        if not isinstance(comp, Complex):
            raise TypeError("comp must be an instance of Complex")

        result = Complex(comp.real, comp.imaginary)
        for c in comps:
            if not isinstance(c, Complex):
                raise TypeError("all items in comps must be instances of Complex")
            result.add(c)

        return result

c1 = Complex(1.0, -2.0)
c1.print()
c2 = Complex(9.0, 100.0)
c1.add(c2)
c1.print()
c_sum = Complex.add_all(c1, c1, c2, Complex(33.75, -14.25))
c_sum.print()
c1.print()
will_fail = Complex.add_all(100)
