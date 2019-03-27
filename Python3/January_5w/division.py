"""
2.4 분할 : 값 x가 주어졌을 때 x 보다 작은 노드들을 x보다 크거나 같은 노드들보다 앞에 오도록 하는 코드를 작성하라.
만약 x가 리스트에 있다면 x는 그보다 작은 원소들보다 뒤에 나오기만 하면 된다.
즉 원소 x는 ‘오른쪽 그룹’ 어딘가에만 존재하면 된다. 왼쪽과 오른쪽 그룹 사이에 있을 필요는 없다.
예제) 입력 : 3 -> 5 -> 8 -> 5 -> 10 -> 2 ->1 [분할값 x = 5 ]
출력 : 3 -> 1- > 2 -> 10 -> 5 -> 5 -> 8
_힌트_ : _#3,_ _#24_
"""

from linked_list import LinkedList, setting_list
from decorators import time_measurement


@time_measurement
def solution(LinkedList, data):
    # 노드가 2개 미만이면 함수를 종료한다.
    start = LinkedList.head                 # Constant 1
    if start is None:                       # Constant 1
        return
    if start.get_next_node() is None:       # Constant 1
        return
    # 두 그룹으로 나눈 뒤 재결합
    small = []                              # Constant 1
    other = []                              # Constant 1
    while start:
        node_data = start.get_data()        # Constant n
        if node_data < data:                # Constant n
            small.append(node_data)         # Constant n
        else:
            other.append(node_data)
        start = start.get_next_node()
    result = small + other                  # Constant 1
    index = 0                               # Constant 1
    start = LinkedList.head                 # Constant 1
    while start:
        start.update_data(result[index])    # Constant n
        start = start.get_next_node()       # Constant n
        index += 1                          # Constant n

    # T(n) = 8 + 6n
    # O(n)


def main_code():
    my_linked_list = LinkedList()
    data_list = [3, 5, 8, 5, 10, 2, 1]
    setting_list(
        LinkedList=my_linked_list,
        data_list=data_list
    )
    my_linked_list.display()
    solution(my_linked_list, 5)
    my_linked_list.display()


if __name__ == "__main__":
    for i in range(10):
        main_code()
        print()
