"""
p.147 [스택과 큐]
3.1 한 개로 세 개 : 배열 한개로 스택 세 개를 어떻게 구현할지 설명하라.
힌트 : #2, #12, #38, #58

--> 하나의 배열로 세 개의 스택 구현하기
"""

from random import randint, choice
from Stack import Stack


class ThreeStackInArr:
    def __init__(self, arr):
        self._arr = arr
        self._max_stack_size = len(arr)
        self._current_stack_size = 0
        self._stack_01, self._stack_02, self._stack_03 = Stack(), Stack(), Stack()

    def _re_sorting_arr(self):
        i = 0
        start = self._stack_01.head
        while start is not None:
            self._arr[i] = start.data
            start = start.next
            i += 1
        start = self._stack_02.head
        while start is not None:
            self._arr[i] = start.data
            start = start.next
            i += 1
        start = self._stack_03.head
        while start is not None:
            self._arr[i] = start.data
            start = start.next
            i += 1
        for x in range(self._max_stack_size - self._current_stack_size):
            self._arr[i] = None
            i += 1
            try:
                if self._arr[i] is None:
                    break
            except IndexError:
                break

    def push_in_stack_01(self, data):
        if self._current_stack_size < self._max_stack_size:
            self._current_stack_size += 1
            self._stack_01.push(data)
            self._re_sorting_arr()
            print("stack_01: push data: {}".format(data))
        else:
            print("stack_01: push error: stack is full!")

    def push_in_stack_02(self, data):
        if self._current_stack_size < self._max_stack_size:
            self._current_stack_size += 1
            self._stack_02.push(data)
            self._re_sorting_arr()
            print("stack_02: push data: {}".format(data))
        else:
            print("stack_02: push error: stack is full!")

    def push_in_stack_03(self, data):
        if self._current_stack_size < self._max_stack_size:
            self._current_stack_size += 1
            self._stack_03.push(data)
            self._re_sorting_arr()
            print("stack_03: push data: {}".format(data))
        else:
            print("stack_03: push error: stack is full!")

    def pop_in_stack_01(self):
        if self._stack_01.is_empty():
            print("stack_01: pop error: stack is empty!")
        else:
            print("stack_01: pop data: {}".format(self._stack_01.head.data))
            self._stack_01.pop()
            self._current_stack_size -= 1
            self._re_sorting_arr()

    def pop_in_stack_02(self):
        if self._stack_02.is_empty():
            print("stack_02: pop error: stack is empty!")
        else:
            print("stack_02: pop data: {}".format(self._stack_02.head.data))
            self._stack_02.pop()
            self._current_stack_size -= 1
            self._re_sorting_arr()

    def pop_in_stack_03(self):
        if self._stack_03.is_empty():
            print("stack_03: pop error: stack is empty!")
        else:
            print("stack_03: pop data: {}".format(self._stack_03.head.data))
            self._stack_03.pop()
            self._current_stack_size -= 1
            self._re_sorting_arr()

    def show_detail(self):
        result = "|스택1: "
        start = self._stack_01.head
        while start is not None:
            result += str(start.data) + " "
            start = start.next
        result += "|스택2: "
        start = self._stack_02.head
        while start is not None:
            result += str(start.data) + " "
            start = start.next
        result += "|스택3: "
        start = self._stack_03.head
        while start is not None:
            result += str(start.data) + " "
            start = start.next
        for i in range(self._max_stack_size - self._current_stack_size):
            result += "| Null "
        result += "|"
        return result


def main_code():
    test_arr = [None for i in range(randint(10, 15))]
    push_function_name = ['push_in_stack_01', 'push_in_stack_02', 'push_in_stack_03']
    pop_function_name = ['pop_in_stack_01', 'pop_in_stack_02', 'pop_in_stack_03']
    print(test_arr)
    tsia = ThreeStackInArr(test_arr)
    for i in range(randint(3, 10)):
        for j in range(randint(3, 10)):
            tsia.__getattribute__(choice(push_function_name))(randint(-50, 50))
        print("arr: {}".format(test_arr))
        print("detail: {}".format(tsia.show_detail()))
        for j in range(randint(3, 10)):
            tsia.__getattribute__(choice(pop_function_name))()
        print("arr: {}".format(test_arr))
        print("detail: {}".format(tsia.show_detail()))


if __name__ == "__main__":
    main_code()
