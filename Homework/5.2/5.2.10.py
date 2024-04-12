class Fraction:

    def __init__(self, numerator_x=1, denominator_y=1):
        if type(numerator_x) is str:
            if '/' in numerator_x:
                self.numerator_x, self.denominator_y = map(int, list(str(numerator_x).split("/")))
            else:
                self.numerator_x, self.denominator_y = int(numerator_x), 1
        else:
            self.numerator_x, self.denominator_y = numerator_x, denominator_y
        self.__format()
        self.__hcf()

    def __neg__(self):
        return Fraction(-self.numerator_x, self.denominator_y)

    def __str__(self):
        return f"{self.numerator_x}/{self.denominator_y}"

    def __lt__(self, other):
        a, b = self.__processing_numbers(str(other))
        x1, y1 = self.numerator_x, self.denominator_y
        x1, a = x1 * b, a * y1
        if x1 < a:
            return True
        return False

    def __le__(self, other):
        a, b = self.__processing_numbers(str(other))
        x1, y1 = self.numerator_x, self.denominator_y
        x1, a = x1 * b, a * y1
        if x1 <= a:
            return True
        return False

    def __eq__(self, other):
        a, b = self.__processing_numbers(str(other))
        x1, y1 = self.numerator_x, self.denominator_y
        x1, a = x1 * b, a * y1
        if x1 == a:
            return True
        return False

    def __ne__(self, other):
        a, b = self.__processing_numbers(str(other))
        x1, y1 = self.numerator_x, self.denominator_y
        x1, a = x1 * b, a * y1
        if x1 != a:
            return True
        return False

    def __gt__(self, other):
        a, b = self.__processing_numbers(str(other))
        x1, y1 = self.numerator_x, self.denominator_y
        x1, a = x1 * b, a * y1
        if x1 > a:
            return True
        return False

    def __ge__(self, other):
        a, b = self.__processing_numbers(str(other))
        x1, y1 = self.numerator_x, self.denominator_y
        x1, a = x1 * b, a * y1
        if x1 >= a:
            return True
        return False

    def __add__(self, other):
        a, b = self.__processing_numbers(str(other))
        new_fraction = Fraction(self.numerator_x * b + a * self.denominator_y, self.denominator_y * b)
        new_fraction.__format()
        new_fraction.__hcf()
        return new_fraction

    def __sub__(self, other):
        a, b = self.__processing_numbers(str(other))
        new_fraction = Fraction(self.numerator_x * b - a * self.denominator_y, self.denominator_y * b)
        new_fraction.__format()
        new_fraction.__hcf()
        return new_fraction

    def __iadd__(self, other):
        a, b = self.__processing_numbers(str(other))
        self.numerator_x = self.numerator_x * b + a * self.denominator_y
        self.denominator_y = self.denominator_y * b
        self.__format()
        self.__hcf()
        return self

    def __isub__(self, other):
        a, b = self.__processing_numbers(str(other))
        self.numerator_x = self.numerator_x * b - a * self.denominator_y
        self.denominator_y = self.denominator_y * b
        self.__format()
        self.__hcf()
        return self

    def __mul__(self, other):
        a, b = self.__processing_numbers(str(other))
        new_fraction = Fraction(self.numerator_x * a, self.denominator_y * b)
        new_fraction.__format()
        new_fraction.__hcf()
        return new_fraction

    def __truediv__(self, other):
        a, b = self.__processing_numbers(str(other))
        new_fraction = Fraction(self.numerator_x * b, self.denominator_y * a)
        new_fraction.__format()
        new_fraction.__hcf()
        return new_fraction

    def __imul__(self, other):
        a, b = self.__processing_numbers(str(other))
        self.numerator_x = self.numerator_x * a
        self.denominator_y = self.denominator_y * b
        self.__format()
        self.__hcf()
        return self

    def __itruediv__(self, other):
        a, b = self.__processing_numbers(str(other))
        self.numerator_x = self.numerator_x * b
        self.denominator_y = self.denominator_y * a
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

    def __processing_numbers(self, other):
        if type(other) is str:
            if '/' in other:
                a, b = map(int, list(str(other).split("/")))
            else:
                a, b = int(other), 1
        else:
            a, b = other, 1
        return a, b

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

    def reverse(self):
        self.numerator_x, self.denominator_y = self.denominator_y, self.numerator_x
        self.__format()
        self.__hcf()
        return self


a = Fraction(1)
b = Fraction('2')
c, d = map(Fraction.reverse, (2 + a, -1 + b))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)
