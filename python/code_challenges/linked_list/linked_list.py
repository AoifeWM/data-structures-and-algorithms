class LinkedList:
    """
    Creates a singly linked list of Node objects. First argument is the head Node.
    """

    def __init__(self, head=None):
        # initialization here
        self.head = head

    def insert(self, value):
        """
        Inserts a new node with a value of 'value' at the head of the list. Value can be assigned to anything.
        Returns true on success.
        """
        new_node = Node(value, self.head)
        self.head = new_node
        return True

    def append(self, value):
        """
        Inserts a new node with a value of 'value' at the end of the list. Value can be assigned to anything.
        Returns True on success and False on failure.
        """
        new_node = Node(value)
        current = self.head
        while current:
            if current.next:
                current = current.next
            else:
                current.next = new_node
                # Success
                return True
        # Failure
        return False

    def insert_before(self, value, target_value):
        """
        Creates a new node with a value of 'value'. Inserts the new node directly before the first instance of any
        node with a value of 'target value' in the list. Value and target_value can be assigned to anything. Returns
        True on success and False on failure.
        """
        new_node = Node(value)
        current = self.head
        # We need to store the previous node, because we will have to attach the new node to its .next once we find
        # the target. Because each node in a singly linked list doesn't know its previous node, we have to keep
        # track manually in this method, using prev_node.
        prev_node = None
        # Traverse until we find target_value or finish the list
        while current:
            # Check for match
            if current.value == target_value:
                # Check if there is a valid previous node (ie, if this node is not the head of the list) because
                # behavior is slightly different between these two cases
                if prev_node:
                    # This node isn't the head so proceed as normal
                    prev_node.next = new_node
                else:
                    # This node is the head, so we have to attach new_node to the linkedlist.head instead of prev_node
                    self.head = new_node
                # Reattach the rest of the list
                new_node.next = current
                # Success
                return True
            # Keep track of prev_node while traversing
            prev_node = current
            # Do next step of traversal
            current = current.next
        # Failure, probably due to target_value not appearing in the list
        return False

    def insert_after(self, value, target_value):
        """
        Creates a new node with a value of 'value'. Inserts the new node directly after the first instance of any
        node with a value of 'target value' in the list. Value and target_value can be assigned to anything. Returns
        True on success and False on failure.
        """
        new_node = Node(value)
        current = self.head
        # Traverse until we find target_value or finish the list
        while current:
            # Check for match with target value
            if current.value == target_value:
                # Link new_node to the rest of the list
                new_node.next = current.next
                # Link current to new_node
                current.next = new_node
                # Success
                return True
            # Do next step of traversal
            current = current.next
        # Failure, probably due to target_value not appearing in the list
        return False

    def includes(self, target_value):
        """
        Target_value can be anything. Returns True if a node appears anywhere in the list with a matching value.
        Returns false if no such node exists.
        """
        current = self.head
        does_include = False
        while current:
            if current.value == target_value:
                does_include = True
            current = current.next
        return does_include

    def kth_from_end(self, k):
        """
        Returns the Kth value from the end of the list. K must be an integer that is less than or equal to the
        length of the list.
        """
        counter = 0
        current = self.head
        length = None
        while current:
            counter += 1
            current = current.next
        if counter < k + 1:
            raise Exception
        else:
            length = counter - k
        current = self.head
        while length - 1:
            current = current.next
            length -= 1
        return current.value

    def to_string(self):
        """
        Returns a formatted string with the entire contents of the linked list, in this format: "{ 0 } -> { 1 } -> {
        2 } -> NULL"
        """
        current = self.head
        s = ""
        while current:
            s += "{ " + str(current.value) + " } -> "
            current = current.next
        s += "NULL"
        return s

    def __str__(self):
        """
        Returns a formatted string with the entire contents of the linked list, in this format: "{ 0 } -> { 1 } -> {
        2 } -> NULL"
        """
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
