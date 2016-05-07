class PriorityQueue(object):
    """PriorityQueue implemented using a linkedlist"""

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
        """Remove item with highest prority from PriorityQueue.

        In this case priority is given to the largest item.
        In differert PriorityQueue priority could be given to smallest item,
        in alphabetical order etc. """

        maxi = 0
        for i in range(1, len(self.data)):
            if self.data[i] > self.data[maxi]:
                maxi = i
            data = self.data[maxi]
            del self.data[maxi]
            return data
