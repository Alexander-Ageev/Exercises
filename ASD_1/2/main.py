class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def get_head_tail(self):
        return [self.head, self.tail]
    
    def list_node (self):
        node_list = []
        node = self.head
        while node is not None:
            node_list.append(node.value)
            node = node.next
        return node_list

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            else:
                node = node.next
        return None

    def find_all(self, val):
        node_list = []
        node = self.head
        while node is not None:
            if node.value == val:
                node_list.append(node)
            node = node.next
        return node_list

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node == self.head and node == self.tail:
                    self.head = None
                    self.tail = None
                elif node == self.head:
                    self.head = node.next
                    node.next.prev = None
                elif node == self.tail:
                    self.tail = node.prev
                    node.prev.next = None                                    
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev                
                if not all:
                    break
            node = node.next
        return None

    def clean(self):
        node = self.head
        while node is not None:
            node.prev = None
            temp = node.next
            node.next = None
            node = temp
        self.head = None
        self.tail = None
        return None

    def len(self):
        node = self.head
        node_len = 0
        while node is not None:
            node_len += 1
            node = node.next
        return node_len

    def insert(self, afterNode, newNode):
        if self.head is None and afterNode is None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        elif self.head is None and afterNode is not None:
            return None
        elif self.head is not None and afterNode is None:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail, newNode.prev = newNode, self.tail
        elif afterNode is not None and afterNode is self.tail:
            self.tail = newNode
            afterNode.next = newNode
            newNode.prev = afterNode
            newNode.next = None
        else:
            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            afterNode.next = newNode
            newNode.prev = afterNode
        return None

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
        try:
            self.head.prev = newNode
        except:
            pass
        newNode.prev = None
        self.head, newNode.next = newNode, self.head
        return None
