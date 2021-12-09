from linked_list.linked_list import Node, LinkedList
from code_challenges.linked_list_zip.linked_list_zip import zip_lists

def test_linked_list_zip():
    list_one = LinkedList()
    list_one.insert('first')
    list_one.insert('second')
    list_one.insert('third')
    list_two = LinkedList()
    list_two.insert('A')
    list_two.insert('B')
    list_two.insert('C')
    str_list = str(zip_lists(list_one, list_two))
    actual = str_list
    expected = '{ third } -> { C } -> { second } -> { B } -> { first } -> { A } -> NULL'
    assert actual == expected




