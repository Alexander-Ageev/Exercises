class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        """
        Create ordered list instance.
        If ascending == True, the list is ordered in ascending order.
        """
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, x_value, y_value):
        """Return position for x_value relative y_value."""
        if x_value < y_value:
            res = -1
        elif x_value == y_value:
            res = 0
        else:
            res = 1
        return res

    def add(self, item):
        """
        Add item in ordered list.
        
        Parameters:
        item - value of add item
        """
        
        if self.__ascending:
            mode = 1
        else:
            mode = -1
        new_node = Node(item)
        if self.head is None: # empty list
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail: # list.len = 1
            if self.compare(new_node.value, self.head.value) * mode == 1:
                self.tail = new_node
                self.head.next = new_node
                self.tail.prev = self.head
            else:
                self.head, self.tail = new_node, self.head
                self.head.next = self.tail
                self.tail.prev = self.head
        else: #list.len >= 2
            node = self.head
            while node is not None:
                value_position = self.compare(new_node.value, node.value) * mode
                if value_position in (-1, 0):  # value <= current_node
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
        return 0

    def find(self, val):
        """Return the first value equal val."""
        if self.__ascending:
            mode = 1
        else:
            mode = -1
        if self.head is None:
            res = None
        elif self.head.value * mode > val * mode or self.tail.value * mode < val * mode:
            res = None
        else:
            node = self.head
            while node is not None:
                if node.value == val:
                    res = node
                    return res
                else:
                    node = node.next
            res = None
        return res

    def delete(self, val):
        """Delete the first value equal val."""
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
                break
            node = node.next
        return 0

    def clean(self, asc):
        """Clean ordered list and change it ascending mode."""
        self.__ascending = asc
        self.head = None
        self.tail = None
        return 0

    def len(self):
        """Return size of ordered list."""
        length = 0
        if self.head is not None:
            node_first = self.head
            node_last = self.tail
            while node_last not in (node_first, node_first.next):
                length += 2
                node_first = node_first.next
                node_last = node_last.prev
            if node_first is node_last:
                length += 1
            else:
                length += 2
        return length

    def get_all(self):
        """Return list of all elements of ordered list."""
        node_list = []
        node = self.head
        while node is not None:
            node_list.append(node)
            node = node.next
        return node_list

    def get_list(self):
        """Return list of all values of ordered list."""
        value_list = []
        node = self.head
        while node is not None:
            value_list.append(node.value)
            node = node.next
        return value_list

    def get_head_tail(self):
        """Return list of head and tail of ordered list."""
        res = []
        if self.head is None:
            res.append(None)
        else:
            res.append(self.head.value)
        if self.tail is None:
            res.append(None)
        else:
            res.append(self.tail.value)
        return res

    def get_index(self, index):
        """Return an element at the specified index."""
        if self.head is None:
            res = None
        elif index == -1:
            res = None
        else:
            node = self.head
            for i in range(index):
                node = node.next
            res = node
        return res

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, s1, s2):
        """Return position for s1 relative s2. It's method for string values."""
        s1 = s1.strip()
        s2 = s2.strip()
        if s1 < s2:
            res = -1
        elif s1 == s2:
            res = 0
        else:
            res = 1
        return res
