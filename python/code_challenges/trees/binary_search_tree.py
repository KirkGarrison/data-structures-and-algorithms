from code_challenges.trees.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node

        def walk(root, adding_node):
            if not root:
                return

            if adding_node.value < root.value:
                if root.left:
                    walk(root.left, adding_node)
                else:
                    root.left = adding_node

            else:
                if root.right:
                    walk(root.right, adding_node)
                else:
                    root.right = adding_node

        walk(self.root, node)

    def contains(self, value):
        if self.root is None:
            return "Tree empty at this time"

        def search_tree(root,value):
            if root.value == value:
               return True

            if value < root.value:
                if root.left:
                    return search_tree(root.left, value)
                else:
                    return False

            else:
                if root.right:
                    return search_tree(root.right, value)
                else:
                    return False


        return search_tree(self.root, value)
