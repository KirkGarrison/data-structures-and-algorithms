from linked_list.linked_list import LinkedList, Node
import pytest


def test_kth_from_negative_integer():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    with pytest.raises(ValueError):
        list.kth_from_end(-1)

def test_kth_same_value_as_length():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    with pytest.raises(ValueError):
        list.kth_from_end(3)


def test_kth_from_end():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    actual = list.kth_from_end(0)
    expected = 1
    assert actual == expected


def test_kth_from_end_one():
    list = LinkedList()
    list.insert(1)
    actual = list.kth_from_end(0)
    expected = 1
    assert actual == expected


def test_kth_from_end_two():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    actual = list.kth_from_end(1)
    expected = 2
    assert actual == expected


def test_kth_from_end_three():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    actual = list.kth_from_end(2)
    expected = 3
    assert actual == expected
