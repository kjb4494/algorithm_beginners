
class Node:
    def __init__(self, data=None, link=None):
        self._data = data
        self._link = link

    def update_data(self, data):
        self._data = data

    def set_link(self, node):
        self._link = node

    def get_data(self):
        return self._data

    def get_next_node(self):
        return self._link


class LinkedList:
    def __init__(self):
        self.head = None

    def add_data(self, data):
        tmp_node = Node(data)
        tmp_node.set_link(self.head)
        self.head = tmp_node
        del tmp_node

    def display(self, show_address=False):
        start = self.head
        if start is None:
            print("Empty List")
            return

        while start:
            if show_address:
                print("{}({})".format(start.get_data(), hex(id(start))), end=" ")
            else:
                print(start.get_data(), end=" ")
            start = start.get_next_node()
            if start:
                print("-->", end=" ")
        print()


def setting_list(LinkedList, data_list):
    for data in data_list[::-1]:
        LinkedList.add_data(data)

