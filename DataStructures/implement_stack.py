class Stack(object):
    """Stack implemented using a list"""

    def __init__(self):
        self._stack = []

    def push(self, item):
        """Add item to top of the stack"""

        self._stack.append(item)

    def pop(self):
        """Pop item from the top of the stack"""

        self._stack.pop()

    def peek(self):
        """Return , but do not remove top item"""

        return self._stack[-1]

    def is_empty(self):
        """Check if stack is empty"""

        return not self._stack


class Stack2(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
