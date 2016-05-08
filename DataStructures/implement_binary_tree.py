class BTree(object):
    """Binary Tree"""

    def __init__(self, root):
        self.root = root

    def preorder_traversal(self, curr=self.root):

        print curr.data

        if curr.left:
            curr = curr.left
            preorder_traversal()
        elif curr.right:
            curr = curr.right
            preorder_traversal)()


class BNode(object):
    """Node in a binary tree"""

    def __init__(self, data, left=None, right=None):

        assert left is None or isinstance(left, BNode)
        assert right is None or isinstance(right, BNode)

        self.data = data
        self.right = right
        self.left = left

    def find(self, sought):
        """Find node in a binary tree by data"""

        node = self

        while node:

            if node.data == sought:
                return node

            elif sought < node.data:
                node = node.left

            elif sought > node.data:
                node = node.right
