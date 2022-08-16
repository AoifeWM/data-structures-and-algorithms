
def linked_list_largest(linked_list):
    current = linked_list.head
    counter = current.value
    while current:
        if current.value > counter:
            counter = current.value
        current = current.next
    return counter


def bst_largest(bst):
    current = bst.root
    while current.right:
        current = current.right
    return current.value
