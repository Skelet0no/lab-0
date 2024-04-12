class Programmer:

    def __init__(self, name, level):
        status = {'Junior': 2, 'Middle': 3, 'Senior': 4}
        self.name = name
        self.level = status[level]
        self.time = 0
        self.bank = 0

    def work(self, hours):
        self.time += hours
        if self.level < 5:
            self.bank += hours * (self.level * 5)
        else:
            self.bank += hours * (self.level - 4) + hours * 20

    def rise(self):
        self.level += 1

    def info(self):
        return f'{self.name} {self.time}ч. {self.bank}тгр.'
