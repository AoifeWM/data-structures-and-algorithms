class LinkedList:
    """
    Creates a singly linked list. First argument is the head node.
    """

    def __init__(self, head=None):
        # initialization here
        self.head = head

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def includes(self, value):
        current = self.head
        does_include = False
        while current:
            if current.value == value:
                does_include = True
            current = current.next
        return does_include

    def to_string(self):
        current = self.head
        s = ""
        while current:
            s += "{ " + str(current.value) + " } -> "
            current = current.next
        s += "NULL"

        return s


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass
