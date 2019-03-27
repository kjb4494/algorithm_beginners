"""
4.5 BST검증: 주어진 이진 트리가 이진 탐색 트리인지 확인하는 함수를 작성하라.
"""

from binary_tree import BinaryTree
from binary_search_tree import BinarySearchTree
from random import randint
from decorators import time_measurement
import sys


@time_measurement
def solution(bt):
    # 아래 두 가지 유형의 객체가 아니면 강제 에러 발생
    if type(bt) not in (BinarySearchTree, BinaryTree):
        raise TypeError

    def _is_bst(node, min, max):
        # 노드가 없으면 이진 트리의 끝부분이므로 True 반환
        if node is None:
            return True

        # 노드의 데이터가 기준값보다 작거나 크면 이진 탐색 트리가 아니므로 False 반환
        if node.data < min or node.data > max:
            return False

        # 재귀를 이용해 각 노드의 왼쪽 트리 체크 및 오른쪽 트리 체크를 순차적으로 수행
        # 모든 재귀적 절차에서 True 값이 반환되면 이진 탐색 트리임
        return _is_bst(node.left, min, node.data - 1) and _is_bst(node.right, node.data + 1, max)

    return _is_bst(bt.root, -sys.maxsize, sys.maxsize)


def main_code():
    array = list(set([randint(1, 400) for i in range(randint(10, 40))]))
    bt = BinaryTree()
    bst = BinarySearchTree()
    for x in array:
        bt.insert(x)
    for x in array:
        bst.insert(x)
    print("이진 트리(전위 순회):", end=" ")
    bt.pre_order_traversal()
    if solution(bt):
        print("이진탐색트리 입니다.")
    else:
        print("이진탐색트리가 아닙니다.")
    print("이진 탐색 트리(전위 순회):", end=" ")
    bst.pre_order_traversal()
    if solution(bst):
        print("이진탐색트리 입니다.")
    else:
        print("이진탐색트리가 아닙니다.")


if __name__ == "__main__":
    for i in range(20):
        main_code()
        print()
