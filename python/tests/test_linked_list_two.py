from linked_list.linked_list import LinkedList, Node


def test_node_function():
    node = Node("protein shakes")
    actual = node.value
    expected = "protein shakes"
    assert actual == expected

def test_import():
    assert LinkedList

def test_init_linked_list():
    linked_list = LinkedList()
    actual = linked_list.head
    expected = None
    assert actual == expected


def test_add_node_front():
    linked_list = LinkedList()
    linked_list.insert("M=D*V")
    linked_list.insert("E=MC2")
    actual = linked_list.head.value
    expected = "E=MC2"
    assert actual == expected

def test_add_node_to_front():
    linked_list = LinkedList()
    linked_list.insert("M=D*V")
    actual = linked_list.head.value
    expected = "M=D*V"
    assert actual == expected

def test_includes():
    linked_list = LinkedList()
    linked_list.insert("M=D*V")
    linked_list.insert("E=MC2")
    actual = linked_list.includes("E=MC2")
    expected = True
    assert actual == expected

def test_includes():
    linked_list = LinkedList()
    linked_list.insert("M=D*V")
    linked_list.insert("nth of fib")
    actual = linked_list.includes("E=MC2")
    expected = False
    assert actual == expected

def test_str():
    linked_list = LinkedList()
    linked_list.insert("M=D*V")
    linked_list.insert("nth of fib")
    linked_list.insert("lucas starts at 2")
    actual = str(linked_list)
    expected = "{ lucas starts at 2 } -> { nth of fib } -> { M=D*V } -> NULL"
    assert actual == expected
