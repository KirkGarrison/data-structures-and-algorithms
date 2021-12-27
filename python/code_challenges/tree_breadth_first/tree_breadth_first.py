from code_challenges.trees.binary_tree import BinaryTree, Node

def breadth_first(tree):
    list = []
    list_values = []

    if tree.root:
        list.insert(0, tree.root)

    while list:
        node = list.pop()
        list_values.append(node.value)
        if node.left:
            list.insert(0, node.left)
        if node.right:
            list.insert(0, node.right)

    return list_values
