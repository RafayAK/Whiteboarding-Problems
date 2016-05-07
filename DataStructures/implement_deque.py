class Deque(object):
    """Implementation of Deque DS using list"""

    class Deque:
        def __init__(self):
            self.items = []

        def is_empty(self):
            return self.items == []

        def addRight(self, item):
            self.items.append(item)

        def addLeft(self, item):
            self.items.insert(0, item)

        def removeRight(self):
            self.items.pop()

        def removeLeft(self):
            self.items.pop(0)

        def size(self):
            return len(self.items)
