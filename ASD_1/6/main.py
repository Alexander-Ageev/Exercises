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
        if v1.value < v2.value:
            return -1
        elif v1.value == v2.value:
            return 0
        else:
            return 1
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

    def add(self, value):
        if self.__ascending:
            mode = 1
        else:
            mode = -1
        if self.head is None: # empty list
            self.head = value
        elif self.tail is None: # list.len = 1
            if self.compare(value, self.head) * mode == 1:
                self.head.next = value
                self.tail = value
                self.tail.prev = self.head
            else:
                self.head, self.tail = value, self.head
                self.head.next = self.tail
                self.tail.prev = self.head
        else: #list.len >= 2
            node = self.head
            while node is not None:
                value_position =  self.compare(value, node) * mode
                if value_position == -1 or value_position == 0:  # value <= current_node  
                    if node == self.head:
                        self.head = value
                        self.head.next = node
                        node.prev = value
                        break
                    else:
                        node.prev.next = value
                        value.prev = node.prev
                        value.next = node
                        node.prev = value
                        break
                elif value_position == 1:
                    if node == self.tail:
                        self.tail = value
                        self.tail.prev = node
                        node.next = value
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
        return [self.head, self.tail]

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return 0
