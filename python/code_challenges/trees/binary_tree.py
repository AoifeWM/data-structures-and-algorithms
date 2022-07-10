class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root
        pass

    def pre_order(self):
        tree = []
        self._pre_order(self.root, tree)
        return tree

    def _pre_order(self, root, tree):
        if not root:
            return
        tree.append(root.value)
        self._pre_order(root.left, tree)
        self._pre_order(root.right, tree)

    def in_order(self):
        tree = []
        self._in_order(self.root, tree)
        return tree

    def _in_order(self, root, tree):
        if not root:
            return
        self._in_order(root.left, tree)
        tree.append(root.value)
        self._in_order(root.right, tree)

    def post_order(self):
        tree = []
        self._post_order(self.root, tree)
        return tree

    def _post_order(self, root, tree):
        if not root:
            return
        self._post_order(root.left, tree)
        self._post_order(root.right, tree)
        tree.append(root.value)


class Node:
    def __init__(self, value, left=None, right=None):
        # initialization here
        self.value = value
        self.left = left
        self.right = right

