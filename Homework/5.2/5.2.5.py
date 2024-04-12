class Fraction:

    def __init__(self, numerator_x=0, denominator_y=0):
        if type(numerator_x) is str:
            self.numerator_x, self.denominator_y = map(int, list(numerator_x.split("/")))
        else:
            self.numerator_x = numerator_x
            self.denominator_y = denominator_y
        self.__format()
        self.__hcf()

    def __neg__(self):
        return Fraction(-self.numerator_x, self.denominator_y)

    def __str__(self):
        return f"{self.numerator_x}/{self.denominator_y}"

    def __add__(self, other):
        a, b = map(int, list(str(other).split("/")))
        new_fraction = Fraction(self.numerator_x * b + a * self.denominator_y, self.denominator_y * b)
        new_fraction.__format()
        new_fraction.__hcf()
        return new_fraction

    def __sub__(self, other):
        a, b = map(int, list(str(other).split("/")))
        new_fraction = Fraction(self.numerator_x * b - a * self.denominator_y, self.denominator_y * b)
        new_fraction.__format()
        new_fraction.__hcf()
        return new_fraction

    def __iadd__(self, other):
        a, b = map(int, list(str(other).split("/")))
        self.numerator_x = self.numerator_x * b + a * self.denominator_y
        self.denominator_y = self.denominator_y * b
        self.__format()
        self.__hcf()
        return self

    def __isub__(self, other):
        a, b = map(int, list(str(other).split("/")))
        self.numerator_x = self.numerator_x * b - a * self.denominator_y
        self.denominator_y = self.denominator_y * b
        self.__format()
        self.__hcf()
        return self

    def __repr__(self):
        return f"Fraction('{self.numerator_x}/{self.denominator_y}')"

    def __hcf(self):
        num1 = abs(self.numerator_x)
        num2 = abs(self.denominator_y)
        while num2:
            num1, num2 = num2, num1 % num2
        ans = max(num1, num2)
        self.numerator_x //= ans
        self.denominator_y //= ans

    def __format(self):
        if self.denominator_y < 0:
            self.denominator_y *= (-1)
            self.numerator_x *= (-1)

    def numerator(self, change=None):
        if change is None:
            return abs(self.numerator_x)
        self.numerator_x = change * (self.numerator_x // abs(self.numerator_x))
        self.__format()
        self.__hcf()

    def denominator(self, change=None):
        if change is None:
            return abs(self.denominator_y)
        self.denominator_y = change * (self.denominator_y // abs(self.denominator_y))
        self.__format()
        self.__hcf()

a = Fraction(1, 8)
c = b = Fraction(3, 8)
b -= a
print(a, b, c, b is c)
