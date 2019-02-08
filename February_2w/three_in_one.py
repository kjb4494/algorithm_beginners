"""
p.147 [스택과 큐]
3.1 한 개로 세 개 : 배열 한개로 스택 세 개를 어떻게 구현할지 설명하라.
힌트 : #2, #12, #38, #58

--> 하나의 배열로 세 개의 스택 구현하기
"""

from random import randint
from decorators import time_measurement
from Stack import ThreeInOneStack


def slice_arr(arr, n):
    for i in range(0, len(arr), n):
        yield arr[i:i + n]


# ThreeInOneStack: 기본적인 기능만 가진 Stack 객체를 상속받은 solution용 객체
@time_measurement
def solution(arr):
    if len(arr) < 3:                                    # Constant 1
        print("Array too small...")
        return None
    arr_scissors = slice_arr(arr, len(arr) // 3)        # Constant 1
    stack_01 = ThreeInOneStack(next(arr_scissors))      # Constant n^2
    stack_02 = ThreeInOneStack(next(arr_scissors))
    stack_03 = ThreeInOneStack(next(arr_scissors))
    try:
        stack_03.attach_arr(next(arr_scissors))
    except StopIteration:
        pass
    return stack_01, stack_02, stack_03

    # T(n) = 2 + n^2
    # O(n^2)


def main_code():
    quest_arr = [randint(0, 9) for i in range(randint(0, 50))]
    print("original arr: {}".format(quest_arr))
    stacks = solution(quest_arr)
    if stacks is not None:
        i = 1
        for stack in stacks:
            print("스택 {}: {}".format(i, stack.show_all()))
            i += 1


if __name__ == "__main__":
    for i in range(10):
        main_code()
        print()
