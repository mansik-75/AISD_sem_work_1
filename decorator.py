from time import time


def insert_decorator(f):
    def wrapper(self, key):
        with open('output_data_5.txt', 'a') as file:
            current = time()
            f(self, key)
            file.write(f'key: {key}, time: {time() - current}, leaf_count: {self.count}\n')
    return wrapper


def delete_decorator(f):
    def wrapper(self, key):
        with open('output_delete_data_5.txt', 'a') as file:
            current = time()
            f(self, key)
            file.write(f'key: {key}, time: {time() - current}, leaf_count: {self.count}\n')
    return wrapper
