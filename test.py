import pickle

with open('dataset_1', 'rb') as f:
    lst = pickle.load(f)
    for i in lst:
        i.pre_order_traverse(i.root)
