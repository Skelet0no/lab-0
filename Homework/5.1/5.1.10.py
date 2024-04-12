class Stack:
    cells = []

    def push(self, item):
        self.cells.append(item)

    def pop(self):
        return self.cells.pop()

    def is_empty(self):
        return self.cells == []


stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")