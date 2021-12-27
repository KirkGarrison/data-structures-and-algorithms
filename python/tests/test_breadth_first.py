from code_challenges.trees.binary_tree import BinaryTree, Node
from code_challenges.tree_breadth_first.tree_breadth_first import breadth_first

def test_is_tree_breadth_tree_():
    assert breadth_first

def test_breadth_first_empty():
    tree = BinaryTree()
    assert breadth_first(tree) == []


def test_breadth_first_single():
    tree = BinaryTree(Node(3))
    assert breadth_first(tree) == [3]


def test_breadth_first_given_tree():
    tree = BinaryTree(Node(2))
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    assert breadth_first(tree) == [2,7,5,2,6,9,5,11,4]
