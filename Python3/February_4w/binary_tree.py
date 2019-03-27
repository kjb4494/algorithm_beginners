from random import randint


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            # 주어진 이진 트리에 무작위로 배치하기 위한 알고리즘
            random_case = randint(0, 1)
            if random_case >= randint(0, 1):
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    # ---- 트리값 확인을 위한 순회 알고리즘 ----

    # 전위 순회
    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data, end=" ")
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)

        _pre_order_traversal(self.root)
        print()

    # 중위 순회
    def in_order_traversal(self):
        def _in_order_traversal(root, result):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left, result)
                result.append(root.data)
                _in_order_traversal(root.right, result)

        result = []
        _in_order_traversal(self.root, result)
        return result

    # 후위 순회
    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data, end=" ")

        _post_order_traversal(self.root)
        print()

    # 레벨 순회
    def level_order_traversal(self):
        def _level_order_traversal(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data, end=" ")
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)

        _level_order_traversal(self.root)
        print()
