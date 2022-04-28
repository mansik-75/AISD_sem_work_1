# 100 деревьев в каждом по 1000
# 100 деревьев в каждом по 10000
# 100 деревьев в каждом по 100000
# 10 деревьев в каждом по 1000000
# 1 деревьев в каждом по 10000000
import pickle
from time import sleep
from random import shuffle
from avltree import AVLTree, TreeNode


# i = 5
# result = []
# # for j in range(10):
# tree = AVLTree()
# lst = [i for i in range(10**(2 + i))]
# shuffle(lst)
# for leaf in lst:
#     tree.insert(leaf)
# result.append(tree)
#
# with open(f'dataset_{i}', 'wb') as f:
#     pickle.dump(result, f)

i = 5
lst = pickle.load(open(f'C://Users/mansu/Downloads/dataset_{i}', 'rb'))

for tree in lst:
    to_delete = [i for i in range(10 ** (2 + i))]
    shuffle(to_delete)
    for elem in to_delete:
        tree.delete(elem)
