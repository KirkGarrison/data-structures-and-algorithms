class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += '{ ' + current.value + ' } -> '
            current = current.next
        output += 'NULL'
        return output


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

    def kth_from_end(self, k):
        leader = self.head
        follower = None

        steps_ahead = 0

        while leader:
            leader = leader.next

            if follower:
                follower = follower.next
            elif steps_ahead == k:
                follower = self.head
            else:
                steps_ahead += 1

        if not follower:
            raise ValueError(f'k is out of range: {k}')

        return follower.value
