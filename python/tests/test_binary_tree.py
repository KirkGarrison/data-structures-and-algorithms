from code_challenges.trees.binary_tree import BinaryTree, Node

def test_is_binary_tree():
    tree = BinaryTree()
    assert tree

def test_binary_tree_root():
    first = Node("first")
    tree = BinaryTree(first)
    actual = tree.root.value
    expected = "first"
    assert actual == expected

def test_binary_tree_empty():
    tree = BinaryTree()
    assert tree

## pre-order = (root) first, (left) second, (right) third
def test__binary_tree_pre_order():
    first = Node("first")
    first.left = Node("second")
    first.right = Node("third")
    tree = BinaryTree(first)
    actual = tree.pre_order()
    expected = ["first", "second", "third"]

    assert actual == expected

## in-order = (left) second, (root) first, (right) third
def test_binary_tree_in_order():
    first = Node("first")
    first.left = Node("second")
    first.right = Node("third")
    tree = BinaryTree(first)
    actual = tree.in_order()
    expected = ["second", "first", "third"]

    assert actual == expected

## post-order = (left) second, (right) third, (root) first
def test_post_order():
    first = Node("first")
    first.left = Node("second")
    first.right = Node("third")
    tree = BinaryTree(first)
    expected = ["second", "third", "first"]
    actual = tree.post_order()

    assert actual == expected
