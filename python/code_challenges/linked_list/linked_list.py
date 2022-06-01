class LinkedList:
    """
    Creates a singly linked list of Node objects. First argument is the head Node.
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

    def __str__(self):
        current = self.head
        s = ""
        while current:
            s += "{ " + str(current.value) + " } -> "
            current = current.next
        s += "NULL"
        return s


class Node:
    """
    Creates a node for a singly linked list. Arguments: (value, next). Value = the working value to be stored by the
    list. Next = positional reference to another node object, used to link nodes together for lists.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
