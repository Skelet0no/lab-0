class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x_move, y_move):
        self.x += x_move
        self.y += y_move

    def length(self, some_point):
        x1 = abs(self.x - some_point.x)
        y1 = abs(self.y - some_point.y)
        return round((x1 ** 2 + y1 ** 2) ** 0.5, 2)
