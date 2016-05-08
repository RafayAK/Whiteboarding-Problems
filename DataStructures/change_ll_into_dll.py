def convert_singlyll_into_dll(ll):
    """Provided that LL class is already implemented, turn ll into dll"""

    my_dll = DoublyLinkedList()

    curr = ll.head
    prev = None
    next = curr.next

    while curr:
        if not prev:
            dll_node = DoublyLinkedNode(curr.data, prev, next)
            dll_node = my_dll.head
            prev = curr
            curr = curr.next
        elif not next:
            dll_node = DoublyLinkedNode(curr.data, prev, next)
            dll_node = my_dll.tail
        else:
            dll_node = DoublyLinkedNode(curr.data, prev, next)
            prev = curr
            curr = curr.next


class DoublyLinkedList(object):
    """Doubly Linked List implementation"""

    def __init__(self):
        self.head = None
        self.tail = None

class DoublyLinkedNode(object):
  def __init__(data, prev, next):
    self.data = data
    self.prev = prev
    self.next = next
