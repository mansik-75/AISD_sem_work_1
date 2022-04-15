class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0


class AVLTree(object):
    def __init__(self):
        self.root = None

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
        else:
            return self._find_min(self.root)

    def _find_min(self, node):
        if node.left:
            return self._find_min(node.left)
        else:
            return node

    def find_max(self):
        if self.root is None:
            return None
        else:
            return self._find_max(self.root)

    def _find_max(self, node):
        if node.right:
            return self._find_max(node.right)
        else:
            return node

    @staticmethod
    def height(node):
        if node is None:
            return -1

        else:
            return node.height

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

    def high_left_rotate(self, node):
        k1 = node.right.left
        k1.right, node.right.left = node.right, k1.right
        k1.left, node.right = node, k1.left
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1
        return k1

    def high_right_rotate(self, node):
        k1 = node.left.right
        k1.left, node.left.right = node.left, k1.left
        k1.right, node.left = node, k1.right
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1
        return k1

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)

        else:
            self.root = self._insert(key, self.root)

    def _insert(self, key, node):
        if node is None:
            node = TreeNode(key)

        elif key < node.data:
            node.left = self._insert(key, node.left)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if key < node.left.data:
                    node = self.low_right_rotate(node)
                else:
                    node = self.high_right_rotate(node)

        elif key > node.data:
            node.right = self._insert(key, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if key > node.right.data:
                    node = self.low_left_rotate(node)
                else:
                    node = self.high_left_rotate(node)

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    def pre_order_traverse(self, node, depth=0):
        if node:
            print(depth, node.data)
            self.pre_order_traverse(node.left, depth + 1)
            self.pre_order_traverse(node.right, depth + 1)
