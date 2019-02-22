"""
4.5 BST검증: 주어진 이진 트리가 이진 탐색 트리인지 확인하는 함수를 작성하라.
"""

from binary_tree import BinaryTree
from random import randint
from decorators import time_measurement


@time_measurement
def solution():
    pass


def main_code():
    array = list(set([randint(1, 400) for i in range(randint(10, 40))]))
    bt = BinaryTree()
    for x in array:
        bt.insert(x)
    print("이진 트리(전위 순회):", end=" ")
    bt.pre_order_traversal()
    solution()


if __name__ == "__main__":
    main_code()
