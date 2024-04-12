class Rectangle:

    def __init__(self, dot1, dot2):
        dot1_copy = [min(dot1[0], dot2[0]), max(dot1[1], dot2[1])]
        dot2_copy = [max(dot1[0], dot2[0]), min(dot1[1], dot2[1])]
        self.dot1 = dot1_copy
        self.dot2 = dot2_copy
        self.sideX = round(self.dot2[0] - self.dot1[0], 2)
        self.sideY = round(self.dot1[1] - self.dot2[1], 2)

    def perimeter(self):
        return round(self.sideX * 2 + self.sideY * 2, 2)

    def area(self):
        return round(self.sideX * self.sideY, 2)

    def get_pos(self):
        return round(self.dot1[0], 2), round(self.dot1[1], 2)

    def get_size(self):
        return round(self.sideX, 2), round(self.sideY, 2)

    def move(self, dx, dy):
        self.dot1[0] += dx
        self.dot2[0] += dx
        self.dot1[1] += dy
        self.dot2[1] += dy

    def resize(self, width, height):
        self.dot2[0] += (width - self.sideX)
        self.dot2[1] -= (height - self.sideY)
        self.sideX = round(width, 2)
        self.sideY = round(height, 2)

    def turn(self):
        center = [(self.dot1[0] + self.dot2[0]) / 2, (self.dot1[1] + self.dot2[1]) / 2]
        self.dot1 = [center[0] - self.sideY / 2, center[1] + self.sideX / 2]
        self.dot2 = [center[0] + self.sideY / 2, center[1] - self.sideX / 2]
        self.sideX = self.dot2[0] - self.dot1[0]
        self.sideY = self.dot1[1] - self.dot2[1]

    def scale(self, factor):
        center = [(self.dot1[0] + self.dot2[0]) / 2, (self.dot1[1] + self.dot2[1]) / 2]
        self.dot1 = [center[0] - (self.sideX / 2) * factor, center[1] + (self.sideY / 2) * factor]
        self.dot2 = [center[0] + (self.sideX / 2) * factor, center[1] - (self.sideY / 2) * factor]
        self.sideX = round(self.dot2[0] - self.dot1[0], 2)
        self.sideY = round(self.dot1[1] - self.dot2[1], 2)


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')