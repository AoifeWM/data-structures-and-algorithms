if __name__ == "__main__":
    from stacks_and_queues.queue import Queue
else:
    from code_challenges.stacks_and_queues.queue import Queue


def breadth_first(tree):
    searched = []
    q = Queue()
    if tree.root:
        q.enqueue(tree.root)
    while not q.is_empty():
        current = q.dequeue()
        searched.append(current.value)
        if current.left:
            q.enqueue(current.left)
        if current.right:
            q.enqueue(current.right)
    return searched
