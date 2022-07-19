from queue1 import Queue
from kary_tree import KaryTree, Node


def fizz_buzz_tree(tree):

    def clone(root):
        if not root:
            return None
        new_root = Node(root.value)
        for kid in root.children:
            new_root.children.append(clone(kid))
        return new_root

    new_tree = KaryTree()
    new_tree.root = clone(tree.root)

    queue = Queue()
    queue.enqueue(new_tree.root)

    while not queue.is_empty():
        node = queue.dequeue()
        if node.value % 15 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(node.value)
        for child in node.children:
            queue.enqueue(child)

    return new_tree
