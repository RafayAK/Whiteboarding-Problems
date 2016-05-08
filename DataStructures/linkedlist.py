class LinkedList(object):
    """Linked List"""

    def __init__(self):
        self.head = None

    def print_all_nodes(self):

        curr = self.head

        while curr:
            print curr.data
            curr = curr.next

    def append_node(self, data):

        curr = self.head
        prev = None

        while curr:
            if curr.next:
                prev = curr
                curr = curr.next
            else:
                prev.next = None

    def remove_node_from_end(self):

        curr = self.head
        prev = None

        while curr:
            if curr.next:
                prev = curr
                curr = curr.next
            else:
                prev.next = None

    def insert_node(self, data):

        curr = self.head
        prev = None

        while curr:
            if curr.data < data:
                prev = curr
                curr = curr.next
            else:
                prev.next = node.data
                node.data.next = curr

    def remove_node_by_index(self, index):

        curr = self.head
        prev = None
        count = 0

        # account for negative index
        if index < 0:
            # count items in Linked List:
            while curr:
                curr = curr.next
                count += 1

            index = count + (index)
            count = 0

            while curr:
                if count < index:
                    prev = curr
                    curr = curr.next
                    count += 1
                else:
                    prev.next = curr.next
        else:
            while curr:
                if count < index:
                    prev = curr
                    curr = curr.next
                    count += 1
                else:
                    prev.next = curr.next

    def remove_node_by_data(self, data):

        curr = self.head
        prev = None

        while curr:
            if curr.data != data:
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next

    def insert_node_by_index(self, idex, data):

        curr = self
        prev = None
        count = 0

        while curr:
            if count < idex:
                prev = curr
                curr = curr.next
                count += 1
            else:
                prev.next = node.data
                node.data.next = curr

    def check_if_ll_contains_loops(self):
        """Return True if ll contains loops, else return False"""

        seen = []
        curr = self.head

        while curr:
            if curr.data in seen:
                return True
            else:
                seen.append(curr.data)
                curr = curr.next

        return False


class Node(object):
    """Node in LinkedList"""

    def __init__(self, data):
        self.data = data
        self.next = None
