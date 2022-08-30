import pytest
from code_challenges.tree_intersection import tree_intersection
from code_challenges.trees.binary_tree import BinaryTree, Node
from code_challenges.stacks_and_queues.queue import Queue


def test_exists():
    assert tree_intersection


# @pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def test_tree_intersection_self_duplicates():
    tree_a = BinaryTree()
    values = [1, 1, 2, 2, 2, 3, 4, 5, ]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [5, 6, 7, 8, 8, 8, 8, 9, ]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [5, ]


def test_tree_intersection_string_vs_int():
    tree_a = BinaryTree()
    values = ["1", "2", "3", 4]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [1, 2, 3, 4]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [4]


def test_tree_intersection_no_match():
    tree_a = BinaryTree()
    values = [1, 2, 3, 4]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [5, 6, 7, 8]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = None


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)
