class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # or raise an exception

    def is_empty(self):
        return len(self.items) == 0


# You can now use the Stack class in the same script
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Outputs: 2
print(stack.is_empty())  # Outputs: False
