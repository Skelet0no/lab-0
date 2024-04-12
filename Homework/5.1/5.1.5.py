class Rectangle:

    def __init__(self, dot1, dot2):
        self.dot1 = dot1
        self.dot2 = dot2
        self.side1 = abs(self.dot1[0] - self.dot2[0])
        self.side2 = abs(self.dot1[1] - self.dot2[1])

    def perimeter(self):
        return round(self.side1 * 2 + self.side2 * 2, 2)

    def area(self):
        return round(self.side1 * self.side2, 2)
