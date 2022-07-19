from data_structures.invalid_operation_error import InvalidOperationError

class Node:

    """
    Node class for stack and queue
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    The quque class
    """

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear
        pass

    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front:
            value = self.front.value
            self.front = self.front.next
            return value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return not self.front
