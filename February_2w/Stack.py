class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            print("pop error: stack is empty!")
            return True
        return False

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return
        # print("pop: {} --> {}".format(self.head, self.head.data))
        self.head = self.head.next

    def peek(self):
        if self.is_empty():
            return
        print("current data: {} --> {}".format(self.head, self.head.data))


class ThreeInOneStack(Stack):
    def __init__(self, arr):
        super().__init__()
        self.max_size = len(arr)
        self.current_size = 0
        for data in arr:
            self.push(data)

    def attach_arr(self, arr):
        self.max_size += len(arr)
        for data in arr:
            self.push(data)

    def push(self, data):
        if self.is_full():
            return
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.current_size += 1
            # print("push: {} --> {}".format(self.head, self.head.data))

    def pop(self):
        if self.is_empty():
            return
        # print("pop: {} --> {}".format(self.head, self.head.data))
        self.head = self.head.next
        self.current_size -= 1

    def is_full(self):
        if self.current_size >= self.max_size:
            print("push error: stack is full!")
            return True
        return False

    def show_all(self):
        result = ""
        start = self.head
        while start is not None:
            result += str(start.data) + " "
            start = start.next
        return result


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
