# This fixes an import issue when this is loaded as a module in pytest vs. as a script
if __name__ == "__main__":
    from stack import Stack, InvalidOperationError
else:
    from ..stack_queue_pseudo.stack import Stack, InvalidOperationError


class PseudoQueue:

    def __init__(self):
        self.stack = Stack()
        self.temp = Stack()

    def enqueue(self, value):
        if self.stack.is_empty():
            self.stack.push(value)
        else:
            while self.stack.is_empty() is False:
                self.temp.push(self.stack.pop())
            self.stack.push(value)
            while self.temp.is_empty() is False:
                self.stack.push(self.temp.pop())

    def dequeue(self):
        return self.stack.pop()


if __name__ == "__main__":
    pq = PseudoQueue()
    pq.enqueue("apple")
    print("guh")
    pq.enqueue("frog")
    # print(pq.dequeue())
