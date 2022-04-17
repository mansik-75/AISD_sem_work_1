from time import time


def insert_decorator(f):
    def wrapper(self, key):
        with open('output_data_2.txt', 'a') as file:
            current = time()
            f(self, key)
            file.write(f'key: {key}, time: {time() - current}, leaf_count: {self.count}\n')
    return wrapper
