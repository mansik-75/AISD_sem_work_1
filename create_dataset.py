# 100 деревьев в каждом по 1000
# 100 деревьев в каждом по 10000
# 100 деревьев в каждом по 100000
# 100 деревьев в каждом по 1000000
# 100 деревьев в каждом по 10000000
import pickle
from random import shuffle
from avltree import AVLTree, TreeNode


i = 2
result = []
for j in range(100):
    tree = AVLTree()
    lst = [i for i in range(10**(2 + i))]
    shuffle(lst)
    for leaf in lst:
        tree.insert(leaf)
    result.append(tree)

with open(f'dataset_{i}', 'wb') as f:
    pickle.dump(result, f)
