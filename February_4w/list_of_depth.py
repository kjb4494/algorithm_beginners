"""
4.3 깊이의 리스트 : 이진트리가 주어졌을 때,
같은 깊이에 있는 노드를 연결리스트로 연결해 주는 알고리즘을 설계하라.
즉, 트리의 깊이가 D라면 D개의 연결리스트를 만들어야한다.
"""

from binary_tree import BinaryTree
from linked_list import LinkedList, setting_list
from random import randint
from decorators import time_measurement


class Solution(BinaryTree):
    def __init__(self):
        super().__init__()

    # 깊이에 따른 이차배열을 생성해 반환하는 함수
    def get_depth_arrays(self):
        def _get_depth_arrays(result, root, depth):
            if root is None:
                pass
            else:
                try:
                    result[depth]
                except IndexError:
                    result.append([])
                result[depth].append(root.data)
                depth += 1
                _get_depth_arrays(result, root.left, depth)
                _get_depth_arrays(result, root.right, depth)
        result = []
        _get_depth_arrays(result, self.root, 0)
        return result


@time_measurement
def solution(bst):
    depth_arrays = bst.get_depth_arrays()
    linked_lists = []
    depth = 0
    # 생성된 이차배열을 이용해 연결리스트 생성 및 데이터 삽입 후 반환
    for array in depth_arrays:
        linked_lists.append(LinkedList())
        setting_list(linked_lists[depth], array)
        depth += 1
    return linked_lists


def main_code():
    array = list(set([randint(1, 400) for i in range(randint(10, 40))]))
    bst = Solution()
    for x in array:
        bst.insert(x)
    print("이진 트리(전위 순회):", end=" ")
    bst.pre_order_traversal()
    linked_lists = solution(bst)
    for linked_list in linked_lists:
        linked_list.display()


if __name__ == "__main__":
    main_code()
