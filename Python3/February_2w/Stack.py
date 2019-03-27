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
