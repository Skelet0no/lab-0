class Fraction:

    def __init__(self, numerator_x=0, denominator_y=0):
        if type(numerator_x) is str:
            self.numerator_x, self.denominator_y = map(int, list(numerator_x.split("/")))
        else:
            self.numerator_x = numerator_x
            self.denominator_y = denominator_y
        self.__hcf()

    def __str__(self):
        return f"{self.numerator_x}/{self.denominator_y}"

    def __repr__(self):
        return f"Fraction({self.numerator_x}, {self.denominator_y})"

    def __hcf(self):
        ans = 0
        for i in range(1, min(self.numerator_x, self.denominator_y) + 1):
            if self.numerator_x % i == 0 and self.denominator_y % i == 0:
                ans = i
        self.numerator_x //= ans
        self.denominator_y //= ans

    def numerator(self, change=None):
        if change is None:
            return self.numerator_x
        self.numerator_x = change
        self.__hcf()

    def denominator(self, change=None):
        if change is None:
            return self.denominator_y
        self.denominator_y = change
        self.__hcf()



