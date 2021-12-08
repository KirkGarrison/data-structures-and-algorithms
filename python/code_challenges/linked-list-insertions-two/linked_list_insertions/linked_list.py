class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):

        current = self.head
        while current:
            if current.next == None:
                current.next = Node(value)
                break
            else:
                current = current.next

    def insert_before(self, value, value_before):
        if self.head.value == value:
            self.head = Node(value_before, self.head)
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    current.next = Node(value_before, current.next)
                    break
                else:
                    current = current.next

    def insert_after(self, value, value_after):
        current = self.head
        while current:
            if current.value == value:
                current.next = Node(value_after, current.next)
                break
            else:
                current = current.next

    def __str__(self):
        current = self.head
        string = ""
        while current:
            string += "{" + str(current.value) + "} -> "
            current = current.next
        string += "NULL"
        return string

    def includes(self, value):

        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False


    def kth_from_end(self, k):
        if self.head is None or k < 0:
            raise Exception
        else:
            current = self.head
            other = self.head

        for _ in range(k):
            if other.next is None:
                raise Exception
            other = other.next

        while other.next is not None:
            other = other.next
            current = current.next

        return current.value
