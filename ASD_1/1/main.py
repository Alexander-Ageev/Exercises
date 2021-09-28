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
    
    def print_all_nodes(self):
        node = self.head
        while node != None:
            #print(node.value)
            node = node.next

    def list_all_nodes(self):
        node = self.head
        nodes_list = []
        while node != None:
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
        if self.head != None:
            node = self.head
        else:
            return []
        find_list = []
        while node != None:
            if node.value == val:
                find_list.append(node)
            node = node.next
        return find_list

    def delete(self, val, all=False):
        if self.head != None:
            node = self.head
            before_node = node
        else:
            return None
        while node != None:  
            if node.value == val:
                if self.head == node:
                    self.head = node.next
                elif node == self.tail:
                    before_node.next = None
                    self.tail = before_node
                elif node.value == val:
                    before_node.next = node.next
                if not all:
                    break
            before_node = node
            node = node.next                   

    def clean(self):
        if self.head != None:
            node = self.head
        else:
            return
        while node != None:
            next_node = node.next
            node.next = None
            node = next_node
        self.head = None
        self.tail = None
        
    def len(self):
        len = 0
        if self.head != None:
            node = self.head
        else:
            return len
        while node != None:
            len += 1
            node = node.next
        return len
        
    def insert(self, afterNode, newNode):
        if self.head == None and not afterNode:
            self.head = newNode
            return
        elif self.head != None and not afterNode:
            temp = self.head
            self.head = newNode
            self.head.next = temp
            return
        elif self.head == None and afterNode:
            return
        else:
            node = self.head
        while node != None:
            if node == afterNode:
                try:
                    temp = afterNode.next
                    afterNode.next = newNode
                    newNode.next = temp
                except:
                    afterNode.next = newNode
                    newNode.next = None
                    self.tail = newNode
            node = node.next