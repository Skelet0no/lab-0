class Queue:
    cells = []

    def push(self, item):
        self.cells.append(item)

    def pop(self):
        return self.cells.pop(0)

    def is_empty(self):
        return self.cells == []


queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")