import pytest
from linked_list import Node, LinkedList


def test_create_node():
    node1 = Node(5)
    assert node1.value == 5


def test_create_node_not_pass():
    node1 = Node(5)
    assert node1.value != 6


def test_create_node_test_next():
    node1 = Node(5)
    assert node1.next is None


def test_new_ll():
    ll = LinkedList()
    assert ll.head is None


def test_new_ll_with_node():
    node1 = Node(100)
    node2 = Node(99, node1)
    ll = LinkedList(node2)
    assert ll.head is node2
    assert ll.head.next is node1


def test_insert_node():
    node1 = Node(1)
    node2 = Node(2, node1)
    ll = LinkedList(node2)
    ll.insert(5)
    assert ll.head.value is 5
    assert ll.head.next is node2


def test_ll_includes():
    node1 = Node(6)
    node2 = Node(5, node1)
    node3 = Node(4, node2)
    ll = LinkedList(node3)
    assert ll.includes(6)
    assert ll.includes(5)
    assert ll.includes(4)
    assert not ll.includes(7)


def test_ll_to_string():
    node1 = Node(12321)
    node2 = Node(121, node1)
    node3 = Node(1, node2)
    ll = LinkedList(node3)
    assert ll.to_string() == "{ 1 } -> { 121 } -> { 12321 } -> NULL"
    assert str(ll) == "{ 1 } -> { 121 } -> { 12321 } -> NULL"


def test_multiple_insert_node():
    node1 = Node(5)
    node2 = Node(6, node1)
    ll = LinkedList(node2)
    ll.insert(7)
    ll.insert(8)
    assert ll.head.value is 8
    assert ll.head.next.value is 7
    assert ll.head.next.next is node2


def test_append():
    node1 = Node(4)
    node2 = Node(2, node1)
    node3 = Node(1, node2)
    ll = LinkedList(node3)
    ll.append(5)
    ll.append(7)
    assert ll.head.next.next.next.value == 5
    assert ll.head.next.next.next.next.value == 7
    assert str(ll) == "{ 1 } -> { 2 } -> { 4 } -> { 5 } -> { 7 } -> NULL"


def test_insert_before():
    node1 = Node(4)
    node2 = Node(2, node1)
    node3 = Node(1, node2)
    ll = LinkedList(node3)
    ll.insert_before(3, 4)
    assert ll.head.next.next.value == 3
    assert str(ll) == "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> NULL"


def test_insert_after():
    node1 = Node(4)
    node2 = Node(2, node1)
    node3 = Node(1, node2)
    node4 = Node(0, node3)
    ll = LinkedList(node4)
    ll.insert_after(3, 2)
    assert ll.head.next.next.next.value == 3
    assert str(ll) == "{ 0 } -> { 1 } -> { 2 } -> { 3 } -> { 4 } -> NULL"


def test_insert_failure():
    node1 = Node(4)
    node2 = Node(2, node1)
    node3 = Node(1, node2)
    node4 = Node(0, node3)
    ll = LinkedList(node4)
    assert not ll.insert_before(1, 7)
    assert not ll.insert_after(1, "a")
    assert str(ll) == "{ 0 } -> { 1 } -> { 2 } -> { 4 } -> NULL"
