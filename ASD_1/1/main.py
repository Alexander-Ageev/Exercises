class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return 0

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
        return 0

    def list_all_nodes(self):
        node = self.head
        nodes_list = []
        while node is not None:
            nodes_list.append(node.value)
            node = node.next
        return nodes_list

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        if self.head is not None:
            node = self.head
        else:
            return []
        find_list = []
        while node is not None:
            if node.value == val:
                find_list.append(node)
            node = node.next
        return find_list

    def delete(self, val, mass=False):
        if self.head is not None:
            node = self.head
            before_node = node
        else:
            return None
        while node is not None:
            if node.value == val:
                if self.head == node:
                    self.head = node.next
                elif node == self.tail:
                    before_node.next = None
                    self.tail = before_node
                    print('end del')
                elif node.value == val:
                    before_node.next = node.next
                    print('mid del')
                if not mass:
                    break
            else:
                before_node = node
            node = node.next
        return 0


    def clean(self):
        if self.head is not None:
            node = self.head
        else:
            return 0
        while node is not None:
            next_node = node.next
            node.next = None
            node = next_node
        self.head = None
        self.tail = None
        return 0

    def len(self):
        length = 0
        if self.head is not None:
            node = self.head
        else:
            return length
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, after_node, new_node):
        if self.head is None and not after_node:
            self.head = new_node
            return 0
        elif self.head is not None and not after_node:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            return 0
        elif self.head is None and after_node:
            return None
        else:
            node = self.head
        while node is not None:
            if node is after_node:
                try:
                    temp = after_node.next
                    after_node.next = new_node
                    new_node.next = temp
                except IndexError:
                    after_node.next = new_node
                    new_node.next = None
                    self.tail = new_node
                return 0
            node = node.next
        return None
