# from code_challenges.trees.binary_tree import BinaryTree, Node
# from code_challenges.trees.binary_search_tree import BinarySearchTree


# def test_is_search_tree():
#     serach_tree = BinarySearchTree()
#     assert isinstance(serach_tree, BinaryTree)


# def test_add_child():
#     first = Node('first')
#     serach_tree = BinarySearchTree(first)
#     serach_tree.add('second')
#     serach_tree.add('third')

#     assert serach_tree.root.value == 'first'
#     assert serach_tree.root.left.value == 'second'
#     assert serach_tree.root.right.value == 'third'


# def test_add_multiple_child():
#     first = Node('first')
#     serach_tree = BinarySearchTree(first)
#     serach_tree.add('second')
#     serach_tree.add('third')
#     serach_tree.add('fourth')
#     serach_tree.add('fifth')

#     assert serach_tree.root.value == 'first'
#     assert serach_tree.root.left.value == 'second'
#     assert serach_tree.root.right.value == 'third'
#     assert serach_tree.root.left.right.value == 'fourth'
#     assert serach_tree.root.right.right.value == 'fifth'


# def test_search_tree_contains():
#     search_tree = BinarySearchTree()
#     search_tree.add(4)
#     search_tree.add(17)
#     search_tree.add(3)
#     actual = search_tree.contains(17)
#     expected = True
#     assert actual == expected
