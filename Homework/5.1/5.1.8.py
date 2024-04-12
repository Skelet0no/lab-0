class Checkers:
    def __init__(self):
        self.field = [
            "WXWXWXWX",
            "XWXWXWXW",
            "WXWXWXWX",
            "XXXXXXXX",
            "XXXXXXXX",
            "XBXBXBXB",
            "BXBXBXBX",
            "XBXBXBXB",
        ]

    def move(self, f, t):
        letters = {"A": 0, "B": 1, "C": 2, "D": 3,
                   "E": 4, "F": 5, "G": 6, "H": 7}
        x1 = int(f[1]) - 1
        y1 = letters[f[0]]
        x2 = int(t[1]) - 1
        y2 = letters[t[0]]
        if self.field[x1][y1] == "W":
            self.field[x2] = self.field[x2][:y2] + "W" \
                             + self.field[x2][y2 + 1:]
        else:
            self.field[x2] = self.field[x2][:y2] + "B" \
                             + self.field[x2][y2 + 1:]
        self.field[x1] = self.field[x1][:y1] + "X" + self.field[x1][y1 + 1:]

    def get_cell(self, p):
        letters = {"A": 0, "B": 1, "C": 2, "D": 3,
                   "E": 4, "F": 5, "G": 6, "H": 7}
        x = int(p[1]) - 1
        y = letters[p[0]]
        return Cell(self.field[x][y])


class Cell:
    def __init__(self, condition):
        self.condition = condition

    def status(self):
        return self.condition
