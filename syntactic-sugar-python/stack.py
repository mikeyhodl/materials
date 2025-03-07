class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __iter__(self):
        yield from self.items

    # def __iter__(self):
    #     return iter(self.items)

    # def __iter__(self):
    #     for item in self.items:
    #         yield item


stack = Stack()
stack.push("one")
stack.push("two")
stack.push("three")

for item in stack:
    print(item)

print(stack.pop())
