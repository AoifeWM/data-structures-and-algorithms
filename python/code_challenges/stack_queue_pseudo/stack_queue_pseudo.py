from data_structures.invalid_operation_error import InvalidOperationError
from stack import Stack


class PseudoQueue:

    def __init__(self):
        self.stack = Stack()
        self.temp = Stack()

    def enqueue(self, value):
        if self.stack.is_empty():
            self.stack.push(value)
            print(self.stack.top.value)
        else:
            while self.stack.is_empty() is False:
                self.temp.push(self.stack.pop())
                print('yh')
            self.stack.push(value)
            while self.temp.is_empty() is False:
                print("gh")
                self.stack.push(self.temp.pop())
        print("ENQUEUED PROPERLY")
        print(self.stack.top.value)
        print(self.stack.is_empty())

    def dequeue(self):
        print("DEQUEUED PROPERLY")
        return self.stack.pop()


if __name__ == "__main__":
    pq = PseudoQueue()
    pq.enqueue("apple")
    print("guh")
    pq.enqueue("frog")
    # print(pq.dequeue())
