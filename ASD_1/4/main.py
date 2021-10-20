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
    return not s.stack

def postfix(sourse_string):
    s1 = Stack() 
    s2 = Stack()
    for char in sourse_string[::-1]:
        s1.push(char)
    for i in range(s1.size()):
        char = s1.pop()
        if char.isdigit():
            s2.push(int(char))
        elif char == '+':                
            d1 = s2.pop()
            d2 = s2.pop()
            s2.push(d1 + d2) 
        elif char == '*':
            d1 = s2.pop()
            d2 = s2.pop()                
            s2.push(d1 * d2)
        elif char == '=':
            return s2.stack
