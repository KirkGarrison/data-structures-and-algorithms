from stack_and_queue.node import Node


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def peek(self):
        if self.top is None:
            raise ValueError('Stack is empty')
        return self.top.value

        return self.top.value

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            raise ValueError('Stack is empty')
        temp = self.top
        self.top = self.top.next
        temp.next = None

        return temp.value
