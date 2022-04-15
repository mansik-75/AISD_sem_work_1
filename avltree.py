class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0


class AVLTree(object):
    def __init__(self):
        self.root = None

    def find(self, key):
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

    def left_left_rotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.left), node.height) + 1
        return k1

    def right_right_rotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1
        return k1

    def right_left_rotate(self, node):
        node.right = self.left_left_rotate(node.right)
        return self.right_right_rotate(node)

    def left_right_rotate(self, node):
        node.left = self.right_right_rotate(node.left)
        return self.left_left_rotate(node)

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
                    node = self.left_left_rotate(node)
                else:
                    node = self.left_right_rotate(node)

        elif key > node.data:
            node.right = self._insert(key, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if key > node.right.data:
                    node = self.right_right_rotate(node)
                else:
                    node = self.left_right_rotate(node)

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    def pre_order_traverse(self, node):
        if node:
            print(node.data)
            self.pre_order_traverse(node.left)
            self.pre_order_traverse(node.right)
