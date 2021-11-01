class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

    def add(self, item):
        if self.__ascending:
            mode = 1
        else:
            mode = -1
        new_node = Node(item)
        if self.head is None: # empty list
            self.head = new_node
        elif self.tail is None: # list.len = 1
            if self.compare(new_node.value, self.head.value) * mode == 1:
                self.head.next = new_node
                self.tail = new_node
                self.tail.prev = self.head
            else:
                self.head, self.tail = new_node, self.head
                self.head.next = self.tail
                self.tail.prev = self.head
        else: #list.len >= 2
            node = self.head
            while node is not None:
                value_position =  self.compare(new_node.value, node.value) * mode
                if value_position == -1 or value_position == 0:  # value <= current_node  
                    if node == self.head:
                        self.head = new_node
                        self.head.next = node
                        node.prev = new_node
                        break
                    else:
                        node.prev.next = new_node
                        new_node.prev = node.prev
                        new_node.next = node
                        node.prev = new_node
                        break
                elif value_position == 1:
                    if node == self.tail:
                        self.tail = new_node
                        self.tail.prev = node
                        node.next = new_node
                        break
                    else:
                        node = node.next
        return None


    def find(self, val):
        return None # здесь будет ваш код

    def delete(self, val):
        pass # здесь будет ваш код

    def clean(self, asc):
        self.__ascending = asc
        pass # здесь будет ваш код

    def len(self):
        return 0 # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def get_list(self):
        l = []
        node = self.head
        while node is not None:
            l.append(node.value)
            node = node.next
        return l


    def get_head_tail(self):
        l = []
        if self.head is not None:
            l.append(self.head.value)
        if self.tail is not None:
            l.append(self.tail.value)
        return l

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return 0
