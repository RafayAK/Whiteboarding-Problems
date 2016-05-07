class Queue(object):
    """Queue implemented using a linkedlist"""

    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        """Checks if queue is empty"""

        return self.length == 0

    def enqueue(self, data):
        """Add item to the end of the queue"""

        node = Node(data)
        if self.head is None:
            # If queue is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            curr = self.head
            while curr.next:
                curr = curr.next
            # Append the new node
            curr.next = node
        self.length += 1

    def dequeue(self):
        """Remove the 1st item in the queue"""

        data = self.head.data
        self.head = self.head.next
        self.length -= 1
        return data


class ImprovedQueue(object):
    """Queue implemented using a doubly-linkedlist"""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def enqueue(self, data):
        """Add item to the end of the queue"""

        node = Node(data)
        if self.length == 0:
            # If queue is empty the new node is head and tail
            self.head = self.tail = node
        else:
            # Find last node
            tail = self.tail
            # Append the new node
            tail.next = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        data = self.head.data
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return data
