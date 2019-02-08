"""
3.2 스택Min :
기본적인 push와 pop 기능이 구현된 스택에서 최솟값을 반환하는 min함수를 추가하려고 한다.
어떻게 설계할 수 있겠는가?
push, pop, min연산은 모두 O(1) 시간에 동작해야 한다.
힌트 : #27, #59, #78
"""

from Stack import Stack, Node
from random import randint


# StackMin: 기본적인 기능만 가진 Stack 객체를 상속받은 solution용 객체
class StackMin(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = []
        self.current_min = None

    def push(self, data):
        self.min_stack.append(self.current_min)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.current_min is None or self.current_min > data:
            self.current_min = data

    def pop(self):
        if self.is_empty():
            return
        self.current_min = self.min_stack.pop()
        self.head = self.head.next

    def min(self):
        if self.current_min is not None:
            return self.current_min
        else:
            return "min error: stack is empty!"

    def show_all(self):
        result = ""
        start = self.head
        while start is not None:
            result += str(start.data) + " "
            start = start.next
        return result


def test():
    test_list = [1, 2, 3, 4, 5, 6, 7]
    pop_num = test_list.pop()
    print(test_list)
    print(pop_num)


def main_code():
    stack = StackMin()
    for i in range(10):
        for i in range(randint(20, 30)):
            stack.push(randint(0, 1000))
        print(stack.show_all())
        print(stack.min())
        print("=" * 80)
        for i in range(randint(20, 30)):
            stack.pop()
        print(stack.show_all())
        print(stack.min())
        print("=" * 80)


if __name__ == "__main__":
    # test()
    main_code()
