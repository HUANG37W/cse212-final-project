class Stack():
    def __init__(self):
        self.items = []

    def insert(self, item):
        # Insert an item to the list
        self.items.append(item)

    def remove(self):
        # Remove an item from the list

        return self.items.pop()

    def is_empty(self):
        # check if the list is empty
        return self.items == []

    def peek(self):
        # check what is the last item of the list if it is not empty

        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

        
myStack = Stack()
myStack.insert("A")
myStack.insert("B")
myStack.insert("C")
myStack.insert("D")
print(myStack.peek())
# [D]
myStack.remove()
myStack.remove()
print(myStack.get_stack())
# [A,B]
myStack.insert("E")
print(myStack.get_stack())
# [A,B,E]
