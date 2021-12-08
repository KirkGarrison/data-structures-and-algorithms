from linked_list.linked_list import LinkedList

def zip_lists(list_one, list_two):
    placeholder = 0
    one_traverser = list_one.head
    while one_traverser is not None:
        placeholder += 1
        one_traverser = one_traverser.next

    two_traverser = list_two.head
    placeholder_two = 0
    while two_traverser is not None:
        placeholder_two += 1
        two_traverser = two_traverser.next

    return list_one

