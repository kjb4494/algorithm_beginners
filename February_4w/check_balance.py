"""
4.4 균형 확인 : 이진트리가 균형 잡혀있는지 확인하는 함수를 작성하라.
이 문제에서 균형 잡힌 트리란 모든 노드에 대해서 왼쪽 부분 트리의 높이와
오른쪽 부분 트리의 높이의 차이가 최대 하나인 트리를 의미한다.
"""

from binary_tree import Node, BinaryTree
from random import randint
from decorators import time_measurement


class BinaryTreeWithDepthInfo(BinaryTree):
    def __init__(self, random_levels=10):
        super().__init__()
        self.random_level = random_levels
        self.left_or_right = False

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            # 주어진 이진 트리에 무작위로 배치하기 위한 알고리즘
            random_case = randint(0, 10)
            if random_case >= randint(0, self.random_level):
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    # 이진트리의 균형 정보를 반환하는 함수
    def get_balance_info(self):
        # 왼쪽 노드들과 오른쪽 노드들의 최대 깊이 정보를 제어할 수 있는 객체
        # 가변할 수 있는 글로벌 변수의 역할
        class DepthInfo:
            LEFT = False
            RIGHT = True

            def __init__(self):
                self._left_depth = 0
                self._right_depth = 0
                self._current_location = None

            def switching_current_location(self):
                if self._current_location == DepthInfo.LEFT:
                    self._current_location = DepthInfo.RIGHT
                else:
                    self._current_location = DepthInfo.LEFT

            def get_current_location(self):
                return self._current_location

            def set_left_depth(self, left_depth):
                self._left_depth = left_depth

            def set_right_depth(self, right_depth):
                self._right_depth = right_depth

            def get_left_depth(self):
                return self._left_depth

            def get_right_depth(self):
                return self._right_depth

        def _get_balance_info(root, depth, di):
            if root is None:
                pass
            else:
                # 깊이가 1일 경우 최초의 분기점
                if depth == 1:
                    di.switching_current_location()

                # 왼쪽, 오른쪽 방향에 따라서 깊이가 갱신되면 누적
                if di.get_current_location() == di.LEFT and depth > di.get_left_depth():
                    di.set_left_depth(depth)
                elif di.get_current_location() == di.RIGHT and depth > di.get_right_depth():
                    di.set_right_depth(depth)
                depth += 1
                _get_balance_info(root.left, depth, di)
                _get_balance_info(root.right, depth, di)

        di = DepthInfo()
        # 루트 노드의 왼쪽 방향 노드가 없으면 깊이 정보를 오른쪽으로 스위칭
        # 왼쪽 방향 트리의 높이가 0이기 때문
        if self.root.left is None:
            di.switching_current_location()
        # 전위 순회 알고리즘을 이용한 재귀탐색 시작
        _get_balance_info(self.root, 0, di)
        depth_compare = abs(di.get_right_depth() - di.get_left_depth())
        return depth_compare <= 1, di


@time_measurement
def solution(bst):
    return bst.get_balance_info()


def main_code():
    array = list(set([randint(1, 400) for i in range(randint(10, 40))]))
    # 매개변수가 10에 가까울수록 균형 잡힌 트리가 될 확률이 높음
    bst = BinaryTreeWithDepthInfo(random_levels=10)
    for x in array:
        bst.insert(x)
    print("이진 트리(전위 순회):", end=" ")
    bst.pre_order_traversal()
    is_balance, depth_info = solution(bst)
    if is_balance:
        print("균형 잡힌 트리입니다.")
    else:
        print("균형 잡힌 트리가 아닙니다.")
    print("왼쪽 높이: {} / 오른쪽 높이: {}".format(depth_info.get_left_depth(), depth_info.get_right_depth()))


if __name__ == "__main__":
    for i in range(20):
        main_code()
        print()
