from code_challenges.hashtable.hashtable import HashTable
from code_challenges.tree_intersection.tree_intersection import tree_intersection
from code_challenges.trees.binary_search_tree import BinarySearchTree, Node

def test_is_tree_intersection():
    assert tree_intersection

# def test_tree_intersection():
    # tree_b = BinarySearchTree()
    # tree_b.add("8")
    # tree_b.add("4")
    # tree_b.add("1")
    # tree_a = BinarySearchTree()
    # tree_a.add("10")
    # tree_a.add("5")
    # tree_a.add("1")
    # actual = tree_intersection(tree_a, tree_b)
    # lst = ['8','4','1']
    # expected = set(lst)
    # assert actual == expected

# def test_tree_intersection_two():
#     tree_b = BinarySearchTree()
#     tree_b = Node("2")
#     tree_b.left = Node("1")
#     tree_b.right = Node("3")
#     tree_a = BinarySearchTree()
#     tree_a = Node("2")
#     tree_a.left = Node("4")
#     tree_a.right = Node("3")
#     actual = tree_intersection(tree_a, tree_b)
#     lst = ['2','3']
#     expected = set(lst)
#     assert actual == expected

# def test_tree_intersection_duplicates():
#     tree_b = BinarySearchTree()
#     tree_b = Node("2")
#     tree_b.left = Node("2")
#     tree_b.right = Node("3")
#     tree_a = BinarySearchTree()
#     tree_a = Node("2")
#     tree_a.left = Node("2")
#     tree_a.right = Node("3")
#     actual = tree_intersection(tree_a, tree_b)
#     lst = ['2','3']
#     expected = set(lst)
#     assert actual == expected
