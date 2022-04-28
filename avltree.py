from decorator import insert_decorator, delete_decorator


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0


class AVLTree(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def __getitem__(self, key):
        if not self.root:
            return None

        else:
            return self._find(key, self.root)

    def _find(self, key, node):
        if not node:
            return None

        elif key < node.data:

            return self._find(key, node.left)

        elif key > node.data:
            return self._find(key, node.right)

        else:
            return node

    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root)

    def _find_min(self, node):
        if node.left:
            return self._find_min(node.left)
        return node

    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root)

    def _find_max(self, node):
        if node.right:
            return self._find_max(node.right)
        return node

    @staticmethod
    def height(node):
        if node is None:
            return -1
        else:
            return node.height

    def balance(self, node):
        if node:
            return self.height(node.left) - self.height(node.right)
        return 0

    def low_right_rotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.left), node.height) + 1
        return k1

    def low_left_rotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1
        return k1

    @insert_decorator
    def insert(self, key):
        self.count += 1
        self.root = self._insert(key, self.root)

    def _insert(self, key, node):
        if node is None:
            return TreeNode(key)

        elif key <= node.data:
            node.left = self._insert(key, node.left)

        elif key > node.data:
            node.right = self._insert(key, node.right)

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        balance = self.balance(node)
        if balance > 1 and node.left.data > key:
            return self.low_right_rotate(node)

        if balance < -1 and key > node.right.data:
            return self.low_left_rotate(node)

        if balance > 1 and key > node.left.data:
            node.left = self.low_left_rotate(node.left)
            return self.low_right_rotate(node)

        if balance < -1 and key < node.right.data:
            node.right = self.low_right_rotate(node.right)
            return self.low_left_rotate(node)

        return node

    @delete_decorator
    def delete(self, key):
        self.count -= 1
        self._delete(key, self.root)

    def _delete(self, key, node):
        if node is None:
            return node

        elif key < node.data:
            node.left = self._delete(key, node.left)

        elif key > node.data:
            node.right = self._delete(key, node.right)

        else:
            if not node.left:
                lt = node.right
                return lt

            elif not node.right:
                lt = node.left
                return lt

            rgt = self._find_min(node.right)
            node.data = rgt.data
            node.right = self._delete(rgt.data, node.right)

        if not node:
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)

        if balance > 1 and self.balance(node.left) >= 0:
            return self.low_right_rotate(node)

        if balance < -1 and self.balance(node.right) <= 0:
            return self.low_left_rotate(node)

        if balance > 1 and self.balance(node.left) < 0:
            node.left = self.low_left_rotate(node.left)
            return self.low_right_rotate(node)

        if balance < -1 and self.balance(node.right) > 0:
            node.right = self.low_right_rotate(node.right)
            return self.low_left_rotate(node)

        return node

    def pre_order_traverse(self, node, depth=0):
        if node:
            print(depth, node.data)
            self.pre_order_traverse(node.left, depth + 1)
            self.pre_order_traverse(node.right, depth + 1)
