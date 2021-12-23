class Node:
    def __init__(self, value=None, child=[]):
        self.value = value
        self.child = child


class KTree:
    def __init__(self, node=None):
        self.root = node


def fizz_buzz(value):
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return str(value)

def tree_fizz_buzz(tree):
    queue = []
    duplicate_queue = []

    if tree.root:
        tree_duplicate = KTree(Node(fizz_buzz(tree.root.value)))
        queue.insert(0, tree.root)
        duplicate_queue.insert(0, tree_duplicate.root)
    else:
        return KTree()

    while queue:
        node = queue.pop()
        node_copy = duplicate_queue.pop()
        temp_value = []
        for child in node.child:
            queue.insert(0, child)
            copied_child = Node(fizz_buzz(child.value))
            duplicate_queue.insert(0, copied_child)

            print(len(tree.root.child[0].child), node_copy.child is node.child)
            temp_value.append(copied_child)
            print(len(tree.root.child[0].child))

        node_copy.child = temp_value
    return tree_duplicate
