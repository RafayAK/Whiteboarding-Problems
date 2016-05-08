class Tree(object):

    def __init__(self, root):
        self.root = root

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.find_dfs(data)
        # return self.root.find_dfs(data)
        # return self.root.find_node_recursively(data)


class Node(object):
    """Node in a tree"""

    def __init__(self, data, children):

        cildren = children or []
        assert isinstance(cildren, list)

        self.data = data
        self.children = children

    def find_dfs(self, data):
        """DFS"""

        to_visit = [self]

        while to_visit:
            node = to_visit.pop()

            if node.data == data:
                return node
            else:
                to_visit.extend(node.children)

    def find_node_recursively(self, data, to_visit=[self]):
        """Find node in a tree recursivelly"""

        node = to_visit.pop()

        if node.data == data:
            return node
        else:
            to_visit.extend(node.children)
            find_node_recursively()

    def find_bfs(self, data):
        """BFS"""

        to_visit = [self]

        while to_visit:
            node = to_visit.pop(0)

        if node.data == data:
            return node
        else:
            to_visit.extend(node.children)

# ADVANCED


class ReverseNode(object):
    """Node that points to it's parent."""

    def __init__(self, parent=None):
        self.parent = parent


class BidirectionalNode(object):
    """Node that is bidirectional."""

    def __init__(self,
                 parent=None,
                 children=None):
        self.parent = parent
        self.children = children or []
