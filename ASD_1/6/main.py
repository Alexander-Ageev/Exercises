class Deque:
    def __init__(self):
        self.queue = []

    # За голову принят нулевой элемент списка. Сложность O(n), 
    # поскольку для добавления элемента необходимо сдвинуть (скопировать)
    # всю предыдущую очередь. Если принять за голову последний элемент списка
    # сложность addFront и addTail оменяются местами
    def addFront(self, item):
        self.queue = [item] + self.queue

    # За хвост принят последний элемент списка. Сложность O(1)
    def addTail(self, item):
        self.queue.append(item)

    # Сложность O(n)    
    def removeFront(self):
        if len(self.queue):
            res = self.queue.pop(0)
        else:
            res = None
        return res

    # Сложность O(1), послкольку удаление происходит с конца
    def removeTail(self):
        if len(self.queue):
            res = self.queue.pop(-1)
        else:
            res = None
        return res

    def size(self):
        return len(self.queue)

    def get_data(self):
        return self.queue

def palindrom_detector(s):
    deq = Deque()
    for char in s:
        deq.addTail(char)
    char_equal = True
    while deq.size() > 1 and char_equal:
        char_equal = deq.removeFront() == deq.removeTail()
    return char_equal