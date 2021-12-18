class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        list = []

        def walk_around_and_do_stuff(root):
            if root is None:
                return
            list.append(root.value)
            walk_around_and_do_stuff(root.left)
            walk_around_and_do_stuff(root.right)

        walk_around_and_do_stuff(self.root)

        return list

    def in_order(self):
        """
        left root right
        """
        list_two = []

        def walk_around_and_do_stuff(root):
            if root is None:
                return

            walk_around_and_do_stuff(root.left)
            list_two.append(root.value)
            walk_around_and_do_stuff(root.right)

        walk_around_and_do_stuff(self.root)

        return list_two

    def post_order(self):
        list_three = []

        def walk_around_and_do_stuff(root):
            if root is None:
                return

            walk_around_and_do_stuff(root.left)
            walk_around_and_do_stuff(root.right)
            list_three.append(root.value)

        walk_around_and_do_stuff(self.root)

        return list_three
