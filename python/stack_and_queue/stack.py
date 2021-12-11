from stack_and_queue.node import Node


class Stack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return True

    def peek(self):
        if self._top is None:
            raise UnderflowError()

        return self._top.value

    def push(self, value):
        self._top = Node(value, self._top)

    def pop(self):
        if self._top is None:
            raise UnderflowError()
        temp = self._top
        self._top = self._top.next
        temp.next = None

        return temp.value


class UnderflowError(Exception):
    pass
