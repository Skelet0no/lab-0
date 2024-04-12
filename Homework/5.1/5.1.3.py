class RedButton:
    def __init__(self):
        self.clicks = 0

    def click(self):
        self.clicks += 1
        return print("Тревога!")

    def count(self):
        return self.clicks
