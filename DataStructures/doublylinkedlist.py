class Node(object):
	"""DLL Node"""

	def __init__(self, data, prev, next):
		self.data = data
		self.prev = None
		self.next = None

class DoublyLinkedList(object):
	"""Doubly Linked List implementation"""

	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, data):
		
		# create new node w data
		new_node = None(data, None, None)
		# if DLL is empty make new_node head and tail of DLL
		if self.head is None:
			self.head = self.tail = new.node
		else:
			self.tail.next = new.node
			new.node.next = None
			self.tail = new.node

	def remove(self, data):

		curr = self.head

		while curr:
			if curr.data == data:
				if curr.prev is not None:
					curr.prev.next = curr.next
					curr.next.prev = curr.prev
				else:
				    self.head = curr.next
				    curr.next.prev = None
			else:
				curr = curr.next
				
	def show(self):

		curr = self.head

		while curr:
			print "Previous ", curr.prev.data if hasattr(curr.prev) else None
			print "Data ", curr.data
			print "Next", curr.next.data if hasattr(curr.next) else None

			curr = curr.nect
			print "*" * 50

