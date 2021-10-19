class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size():
            top = self.stack[0]
            self.stack = self.stack[1::]
            return top
        else:
            return None
    def push(self, value):
        self.stack = [value] + self.stack

    def peek(self):
        stack_len = self.size()
        if stack_len:
            return self.stack[0]
        else:
            return None

    def pop_from_end(self):
        if self.size():
            return self.stack.pop(-1)
        else:
            return None

    def push_to_end(self, value):
        self.stack.append(value)

    def peek_from_end(self):
        stack_len = self.size()
        if stack_len:
            return self.stack[-1]
        else:
            return None

def braket_braker(source_string):
    s = Stack()
    for i in source_string:
        if i == '(':
            s.push(1)
        elif i == ')':
            if s.pop() is None:
                return False
    if len(s.stack) > 0:
        return False
    else:
        return True

