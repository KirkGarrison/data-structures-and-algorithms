from stack_and_queue.stack import Stack

class Dog:
    def __init__(self, name):
        self.name = name

class Cat:
    def __init__(self, name):
        self.name = name

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class AnimalShelter:
    def __init__(self):
        self.enqueue_box = Stack()
        self.dequeue_box = Stack()

    def enqueue(self, animal):
        if isinstance(animal, Dog) or isinstance(animal, Cat):
            return self.enqueue_box.push(animal)
        raise ValueError('Only cats or dogs can be pushed into this stack')

    def dequeue(self, pref=None):
        if self.enqueue_box.is_empty():
            raise IndexError("The Queue is empty")

        while not self.enqueue_box.is_empty():
            self.dequeue_box.push(self.enqueue_box.pop())
        string_value = " "
        while not self.dequeue_box.is_empty():
            temp_value = self.dequeue_box.pop()

            if not pref:
                string_value = temp_value
                break
            if pref == 'cat' and isinstance(temp_value, Cat):
                string_value = temp_value
                break
            if pref == 'dog' and isinstance(temp_value, Dog):
                string_value = temp_value
                break
            self.enqueue_box.push(temp_value)

        if string_value:
            return string_value
        return f'No {pref}\'s available at this time'

