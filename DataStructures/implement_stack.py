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

# line 25, also _stack
