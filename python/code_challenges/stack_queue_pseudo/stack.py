class InvalidOperationError(Exception):
    pass

class Node:

    """
    Node class for stack and queue
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    Stack Class
    """

    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        if self.top:
            return False
        return True


