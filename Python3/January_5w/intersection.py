"""
2.7 교집합 : 단방향 연결리스트 두 개가 주어졌을 때 이 두 리스트의 교집합 노드를 찾은 뒤 반환하는 코드를 작성하라.
여기서 교집합이란 노드의 값이 아니라 노드의 주소가 완전히 같은 경우를 말한다.
즉, 첫 번째 리스트에 있는 k 번째 노드와 두 번째 리스트에 있는 j 번째 노드가 주소까지 완전히 같다면 이 노드는 교집합의 원소가 된다.
힌트 : #20, #45, #55, #65, #76, #93, #111, #120, #129
"""

from linked_list import LinkedList, setting_list
from random import randint
from decorators import time_measurement


@time_measurement
def solution(LinkedList_01, LinkedList_02):
    start_01 = LinkedList_01.head                   # Constant 1
    start_02 = LinkedList_02.head                   # Constant 1
    long_lnk_list = None                            # Constant 1
    short_lnk_list = None                           # Constant 1
    if start_01 is None or start_02 is None:        # Constant 2
        return
    # 첫번째 루프에서는 어느 리스트가 더 긴지 측정한다.
    while start_01:
        start_01 = start_01.get_next_node()         # Constant n
        start_02 = start_02.get_next_node()         # Constant n
        if start_01 is None:                        # Constant n
            long_lnk_list = LinkedList_02           # Constant 1
            short_lnk_list = LinkedList_01          # Constant 1
            break
        if start_02 is None:                        # Constant n
            long_lnk_list = LinkedList_01           # Constant 1
            short_lnk_list = LinkedList_02          # Constant 1
            break
    start = short_lnk_list.head                     # Constant 1
    node_list = []                                  # Constant 1
    # 두번째 루프에서는 짧은 리스트의 모든 노드 주소를 기록한다.
    while start:
        node_list.append(start)                     # Constant n
        start = start.get_next_node()               # Constant n
    start = long_lnk_list.head                      # Constant 1
    # 세번째 루프에서는 긴 리스트의 노드와 기록한 노드 주소를 비교한다.
    while start:
        if start in node_list:                      # Constant n^2
            print("ok exist! address: {} / data: {} / next_node_address: {}".format(start, start.get_data(), start.get_next_node()))
            return
        start = start.get_next_node()               # Constant 1
    print("not found ;(")

    # T(n) = 13 + 6n + n^2
    # O(n^2)


def main_code():
    my_linked_list_01 = LinkedList()
    my_linked_list_02 = LinkedList()
    data_list_01 = [3, 5, 8, 5]
    data_list_02 = [3, 6]
    setting_list(
        LinkedList=my_linked_list_01,
        data_list=data_list_01
    )
    # 솔루션 함수 동작을 확인하기 위해 임의의 크기만큼 노드를 공유한다.
    start = my_linked_list_01.head
    for i in range(randint(0, len(data_list_01))):
        start = start.get_next_node()
    my_linked_list_02.head = start
    setting_list(
        LinkedList=my_linked_list_02,
        data_list=data_list_02
    )
    print("연결리스트 1: ", end=" ")
    my_linked_list_01.display(show_address=True)
    print("연결리스트 2: ", end=" ")
    my_linked_list_02.display(show_address=True)
    solution(my_linked_list_02, my_linked_list_01)


if __name__ == "__main__":
    for i in range(10):
        main_code()
        print()
