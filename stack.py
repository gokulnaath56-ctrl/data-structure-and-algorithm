class Stack:

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Remove the item from the top of the stack and return it."""
        if not self.is_empty():
            return self.stack.pop()

        raise IndexError("pop from empty stack")

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]

        raise IndexError("peek from empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)


# Example usage

stack = Stack()

stack.push(1)
stack.push(2)

print(stack.peek())       # Output: 2
print(stack.pop())        # Output: 2
print(stack.is_empty())   # Output: False
print(stack.size())       # Output: 1
