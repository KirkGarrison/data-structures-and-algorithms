from linked_list.linked_list import Node, LinkedList


def test_create_node():
    node = Node('first')
    actual = node.value
    expected = 'first'
    assert actual == expected

def test_node_next_default():
    node = Node('first')
    actual = None
    expected = node.next
    assert actual == expected


def test_node_next_something():
    first = Node('first')
    second = Node('second', first)
    actual = second.next
    expected = first
    assert actual == expected


def test_create_linked_list():
    lst = LinkedList()
    assert lst.head is None


def test_insert_when_empty():
    lst = LinkedList()
    lst.insert('first')
    assert lst.head.value == 'first'

def test_insert_when_not_empty():
    lst = LinkedList()
    lst.insert('first')
    lst.insert('second')
    assert lst.head.value == 'second'
    assert lst.head.next.value == 'first'

def test_includes_true():
    lst = LinkedList()
    lst.insert('first')
    lst.insert('second')
    actual = lst.includes('first')
    expected = True
    assert actual == expected

def test_includes_false():
    lst = LinkedList()
    lst.insert('first')
    lst.insert('second')
    actual = lst.includes('third')
    expected = False
    assert actual == expected

def test_to_string():
    lst = LinkedList()
    lst.insert('first')
    lst.insert('second')
    assert str(lst) == '{ second } -> { first } -> NULL'
