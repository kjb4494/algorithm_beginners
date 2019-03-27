"""
2.3 중간 노드 삭제 : 단반향 연결리스트가 주어졌을 때 중간(정확히 가운데 노드일 필요는 없고
처음과 끝 노드만 아니면 된다)에 있는 노드 하나를 삭제하는 알고리즘을 구현하라.
단, 삭제할 노드에만 접근 할 수 있다.
예제) 입력 : 연결리스트 a -> b -> c -> d -> e에서 노드 c
결과 : 아무것도 반환할 필요는 없지만, 결과로 연결리스트 a -> b -> d -> e가 되어 있어야한다.
힌트 : #72
"""

from linked_list import LinkedList, setting_list
from decorators import time_measurement


@time_measurement
def solution(LinkedList, data):
    pri_node = LinkedList.head                          # Constant 1
    # 노드가 3개 미만이면 함수를 종료한다.
    if pri_node is None:                                # Constant 1
        return
    start = pri_node.get_next_node()                    # Constant 1
    if start is None:
        return
    next_node = start.get_next_node()                   # Constant 1
    while next_node:
        # 삭제할 데이터를 찾으면 링크를 재연결하고 노드를 삭제한다.
        if start.get_data() == data:                    # Constant n
            pri_node.set_link(next_node)                # Constant 1
            del start
            return
        pri_node = pri_node.get_next_node()             # Constant n
        start = start.get_next_node()                   # Constant n
        next_node = next_node.get_next_node()           # Constant n

    # T(n) = 5 + 4n
    # O(n)


def main_code():
    my_linked_list = LinkedList()
    data_list = ['a', 'b', 'c', 'd', 'e']
    setting_list(
        LinkedList=my_linked_list,
        data_list=data_list
    )
    my_linked_list.display()
    solution(my_linked_list, 'd')
    my_linked_list.display()


if __name__ == "__main__":
    for i in range(10):
        main_code()
        print()
