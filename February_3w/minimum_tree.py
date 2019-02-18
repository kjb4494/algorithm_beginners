"""
4.2 최소 트리: 오름차순으로 정렬된 배열이 있다.
이 배열 안에 들어 있는 원소는 정수이며 중복된 값이 없다고 했을 때
높이가 최소가 되는 이진 탐색 트리를 만드는 알고리즘을 작성하라.
힌트 #19, #73, #116
"""

from binary_search_tree import BinarySearchTree
from decorators import time_measurement
from random import randint


# 배열을 반으로 쪼개주는 제네레이터
def chunks(array):
    arr_len = len(array)
    if arr_len % 2 == 0:
        for i in range(0, arr_len, arr_len // 2):
            yield array[i:i + arr_len // 2]
    else:
        arr_len += 1
        for i in range(0, arr_len, arr_len // 2):
            yield array[i:i + arr_len // 2]


# 배열의 중간에 위치한 값을 반환하는 함수
def get_middle_value(array):
    arr_len = len(array) // 2
    return array[arr_len]


@time_measurement
def solution(array):
    # 높이가 최소가 되는 정렬로 이진 탐색 트리에 들어갈 값의 배열
    resorted_array = []
    # 작업을 처리할 큐 배열
    array_que = [array]

    while len(array_que[0]) > 2:                            # 배열의 크기가 2이하인 데이터가 나오면 작업 완료
        middle_value = get_middle_value(array_que[0])
        resorted_array.append(middle_value)                 # 배열의 중간값인 데이터를 결과 배열에 추가
        array_que[0].remove(middle_value)                   # 배열의 중간값인 데이터는 이후 배열에서 제외
        for i in chunks(array_que[0]):
            array_que.append(i)                             # 배열을 반으로 쪼갠 뒤 큐에 저장
        del array_que[0]                                    # 작업이 끝난 배열은 큐에서 삭제
        # print(array_que)
    for arr in array_que:
        for data in arr:
            resorted_array.append(data)                     # 작업이 끝나고 남은 데이터들을 순서대로 결과 배열에 추가

    # 결과 배열을 이용해 이진 탐색 트리 생성 후 반환
    bst = BinarySearchTree()
    for x in resorted_array:
        bst.insert(x)
    return bst


def main_code():
    # array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array = sorted(list(set([randint(1, 400) for i in range(randint(10, 40))])))
    print("최초 배열: {}".format(array))
    bst = solution(array)

    # 전위 순회로 표기
    print("최소 높이를 가진 이진 탐색 트리:", end=" ")
    bst.pre_order_traversal()


if __name__ == "__main__":
    for i in range(10):
        main_code()
        print()
