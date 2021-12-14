from stack_and_queue.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.in_box = Stack()
        self.out_box = Stack()

    def enqueue(self, value):
        self.in_box.push(value)

    def dequeue(self):
        if self.in_box.is_empty():
            raise IndexError("The Queue is empty")

        while not self.in_box.is_empty():
            self.out_box.push(self.in_box.pop())

        temp_value = self.out_box.pop()

        while not self.out_box.is_empty():
            self.in_box.push(self.out_box.pop())
        return temp_value


