class Rectangle:

    def __init__(self, dot1, dot2):
        self.dot1 = list(dot1)
        self.dot2 = list(dot2)
        self.side1 = abs(self.dot1[0] - self.dot2[0])
        self.side2 = abs(self.dot1[1] - self.dot2[1])

    def perimeter(self):
        return round(self.side1 * 2 + self.side2 * 2, 2)

    def area(self):
        return round(self.side1 * self.side2, 2)

    def get_pos(self):
        if self.dot1[0] < self.dot2[0] and self.dot1[1] < self.dot2[1]:
            return round(self.dot1[0], 2), round(self.dot2[1], 2)
        elif self.dot1[0] > self.dot2[0] and self.dot1[1] > self.dot2[1]:
            return round(self.dot2[0], 2), round(self.dot1[1], 2)
        elif self.dot1[0] < self.dot2[0] and self.dot1[1] >= self.dot2[1]:
            return round(self.dot1[0], 2), round(self.dot1[1], 2)
        else:
            return round(self.dot2[0], 2), round(self.dot2[1], 2)

    def get_size(self):
        return round(self.side1, 2), round(self.side2, 2)

    def move(self, dx, dy):
        self.dot1[0] += dx
        self.dot2[0] += dx
        self.dot1[1] += dy
        self.dot2[1] += dy

    def resize(self, width, height):
        self.side1 = width
        self.side2 = height


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())
