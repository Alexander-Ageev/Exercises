class Queue:
    def __init__(self):
        self.queue = []

# Сложность данного метода О(1)
    def enqueue(self, item):
        self.queue.append(item)

# Сложность данного метода О(n)
    def dequeue(self):
        if self.size() > 0:
            head = self.queue[0]
            self.queue = self.queue[1:]
        else:
            head = None
        return head

# Сложность данного метода О(n)
    def size(self):
        size = 0
        for i in self.queue:
            size += 1
        return size # размер очереди

    def get_data(self):
        return self.queue

def rotate(q, n):
    for i in range(n):
        q.enqueue(q.dequeue())
    return q.get_data()
