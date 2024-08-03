import avl_tree as avl


tree = None
keys = [1, 2, 6, 3, 3, 5, 4, 0]

for key in keys:
    tree = avl.insert(tree, key)

print("AVL Tree:\n", tree)

print("Maximum value: ", avl.get_max(tree))
print("Minimum value: ", avl.get_min(tree))
print("Sum: ", avl.get_sum(tree))
