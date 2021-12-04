from linked_list.linked_list import Node, LinkedList


def test_create_node():
    node = Node('apple')
    actual = node.value
    expected = 'apple'
    assert actual == expected

def test_node_next_default():
    node = Node('apple')
    actual = None
    expected = node.next
    assert actual == expected


def test_node_next_something():
    apple = Node('apple')
    banana = Node('banana', apple)
    actual = banana.next
    expected = apple
    assert actual == expected


def test_create_linked_list():
    lst = LinkedList()
    assert lst
