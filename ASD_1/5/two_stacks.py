class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size():
            return self.stack.pop(-1)
        else:
            return None

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        stack_len = self.size()
        if stack_len:
            return self.stack[-1]
        else:
            return None

class Queue:
    def __init__(self):
        self.main = Stack()
        self.buf = Stack()

    def enqueue(self, item):
        self.main.push(item)

    def dequeue(self):
        q_size = self.size()
        if q_size > 0:
            for i in range(q_size - 1):
                self.buf.push(self.main.pop())
            head = self.main.pop()
            for i in range(q_size - 1):
                self.main.push(self.buf.pop())
        else:
            head = None
        return head

    def size(self):
        return self.main.size()

    def get_data(self):
        q_size = self.main.size()
        q_list = []
        for i in range(q_size):
            q_list.append(self.dequeue())
        return q_list