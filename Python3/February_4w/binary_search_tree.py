from binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
