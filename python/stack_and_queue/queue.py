from stack_and_queue.node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front is None:
            return True
        return False

    def peek(self):
        if not self.front:
            raise ValueError('Queue is empty')
        return self.front.value

    def enqueue(self, value):
        self.rear = Node(value, self.rear)

        if not self.front:
            self.front = self.rear



    def dequeue(self):
        if not self.front:
            raise ValueError("Queue is empty")
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value


