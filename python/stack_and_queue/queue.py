from stack_and_queue.underflow_error import UnderflowError
from stack_and_queue.node import Node

class Queue:
    def __init__(self):
        self._front = None
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def peek(self):
        if not self._front:
            raise UnderflowError()
        return self._front.value

    def enqueue(self, value):
        self._rear = Node(value, self._rear)

        if not self._front:
            self._front = self._rear
