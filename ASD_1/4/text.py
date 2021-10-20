#1
#сложность данного метода О(1), поскольку используетсяобращение к списку по индексу
    def pop_from_end(self):
        if self.size():
            return self.stack.pop(-1)
        else:
            return None

#сложность данного метода О(1), поскольку используетсяобращение к списку по индексу
    def push_to_end(self, value):
        self.stack.append(value)


#3
while stack.size() > 0:
    print(stack.pop())
    print(stack.pop())
#Данный код выведет на экран содержимое стека в обратном порядке (если стек не пустой). 
#Если количество элементов в стеке нечетное, то последним сообщением будет выведено None.
#Например стек [1, 2, 3] (верхушка справа) будет выведен как
#3
#2
#1
#None


#4
#сложность данного метода О(n-1), поскольку используется срез
    def pop(self):
        if self.size():
            top = self.stack[0]
            self.stack = self.stack[1::]
            return top
        else:
            return None

# сложность данного метода О(n+1), поскольку n элементов старого списка сдвигаются (копируются в новый список)
    def push(self, value):
        self.stack = [value] + self.stack

#5
def braket_braker(source_string):
    s = Stack()
    for i in source_string:
        if i == '(':
            s.push(1)
        elif i == ')':
            if s.pop() is None:
                return False
    return not s.stack

#5
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

# 85+5*9+= 74