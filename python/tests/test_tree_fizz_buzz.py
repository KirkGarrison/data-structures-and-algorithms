from code_challenges.tree_fizz_buzz.tree_fizz_buzz import Node, KTree, tree_fizz_buzz, fizz_buzz

def test_is_ktree():
    assert KTree

def test_is_fizz_buzz():
    assert tree_fizz_buzz

def test_fizz():
    tree = KTree(Node(3))
    tree_copy = tree_fizz_buzz(tree)
    assert tree_copy.root.value == "Fizz"

def test_buzz():
    tree = KTree(Node(5))
    tree_copy = tree_fizz_buzz(tree)
    assert tree_copy.root.value == "Buzz"

def test_fizz_buzz():
    tree = KTree(Node(15))
    tree_copy = tree_fizz_buzz(tree)
    assert tree_copy.root.value == "FizzBuzz"

def test_fizz_buzz_none_division():
    tree = KTree(Node(2))
    tree_copy = tree_fizz_buzz(tree)
    assert tree_copy.root.value == "2"
