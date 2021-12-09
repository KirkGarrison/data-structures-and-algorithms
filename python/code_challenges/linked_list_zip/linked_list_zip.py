from linked_list.linked_list import LinkedList

def zip_lists(list_one, list_two):
        list_one_current = list_one.head
        list_two_current = list_two.head

        while list_one_current != None and list_two_current != None:

            list_one_next = list_one_current.next
            list_two_next = list_two_current.next

            list_two_current.next = list_one_next
            list_one_current.next = list_two_current

            list_one_current = list_one_next
            list_two_current = list_two_next
            list_two.head = list_two_current

        return list_one


