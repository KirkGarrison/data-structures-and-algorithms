from code_challenges.hashtable.hashtable import HashTable

def tree_intersection(tree1, tree2):
   table = tree_to_hashtable(tree1)

   return matched_values(tree2, table)

def matched_values(binary_tree, hashtable):
    root = binary_tree.root
    list = []

    def walk(root, hashtable):
        if root is None:
            return
        nonlocal list

        if hashtable.get(root.value):
            list.append(root.value)
        walk(root.left, hashtable)
        walk(root.right, hashtable)
    walk(binary_tree.root, hashtable)
    return list

def tree_to_hashtable(binary_tree):
    root = binary_tree.root
    hashtable = HashTable()

    def find(root):
        if root is None:
            return
        nonlocal hashtable
        hashtable.add(root.value, True)
        find(root.left)
        find(root.right)
    find(root)
    return hashtable
