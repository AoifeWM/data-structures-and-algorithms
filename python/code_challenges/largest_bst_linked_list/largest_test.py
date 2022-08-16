from code_challenges.trees.binary_search_tree import BinarySearchTree
from code_challenges.linked_list.linked_list import LinkedList
from largest import *
import pytest


def linked_list_test_random():
    ll = LinkedList()
    ll.append(3)
    ll.append(14)
    ll.append(7)
    ll.append(89)
    ll.append(11)
    actual = linked_list_largest(ll)
    expected = 89
    assert actual == expected


def linked_list_test_descending():
    ll = LinkedList()
    ll.append(9)
    ll.append(8)
    ll.append(7)
    ll.append(4)
    ll.append(2)
    actual = linked_list_largest(ll)
    expected = 9
    assert actual == expected


def bst_test_1():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(15)
    bst.add(3)
    bst.add(4)
    bst.add(1)
    bst.add(19)
    bst.add(13)
    bst.add(7)
    actual = bst_largest(bst)
    expected = 19
    assert actual == expected
