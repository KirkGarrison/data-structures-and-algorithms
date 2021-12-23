class newNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def add_binary_tree(root):
    if (root / 2) != 0:
        return (root.key + add_binary_tree(root.left) +
                       add_binary_tree(root.right))

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(8)

    sum = add_binary_tree(root)

    print("Sum of all the nodes is:", sum)

