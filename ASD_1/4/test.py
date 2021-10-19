import unittest, random
from unittest import result
from main import Stack, braket_braker, postfix

class main_tests(unittest.TestCase):
    def test_push(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        data = my_stack.stack
        res =  [3, 2, 1]
        self.assertEqual( data, res)
    
    def test_pop_one(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        pop_el = my_stack.pop()
        data = my_stack.stack + [pop_el]
        res =  [2, 1, 3]
        self.assertEqual( data, res)
    
    def test_pop_none(self):
        my_stack = Stack()
        pop_el = my_stack.pop()
        data = my_stack.stack + [pop_el]
        res =  [None]
        self.assertEqual( data, res)

    def test_pop_all(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        pop_el1 = my_stack.pop()
        pop_el2 = my_stack.pop()
        pop_el3 = my_stack.pop()
        data = my_stack.stack + [pop_el1] + [pop_el2] + [pop_el3]
        res =  [3, 2, 1]
        self.assertEqual( data, res)

    def test_pop_in_middle(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        pop_el = my_stack.pop()
        my_stack.push(3)
        data = my_stack.stack + [pop_el]
        res =  [3, 1, 2]
        self.assertEqual( data, res)
    
    def test_size(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        data = my_stack.size()
        res = 3
        self.assertEqual( data, res)
    
    def test_peek(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        data = my_stack.stack + [my_stack.peek()]
        res =  [3, 2, 1, 3]
        self.assertEqual( data, res)

    def test_random(self):
        for i in range(10000):
            s = Stack()
            res = []
            comand = random.randint(0, 1) # 0 - pop, 1 - push
            if comand:
                t = random.randint(0,9)
                s.push(t)
                res.append(t)
            else:
                s.pop()
                try:
                    res.pop()
                except:
                    pass
            data = s.stack + [s.size()]
            res =  res[::-1] + [len(res)]
            self.assertEqual( data, res)
 
    def test_braket_breaker (self):
        for i in range(10000):
            balance = 0
            braket_string = ''
            res = True
            for j in range(random.randint(1, 9)):
                braket = random.randint(0, 1) # 0 - '(',   1 - ')'
                if braket:
                    braket_string += ')'
                    balance += -1
                else:
                    braket_string += '('
                    balance += 1
                if balance < 0:
                    res = False
            if balance > 0:
                res = False
            data = braket_braker(braket_string)
            self.assertEqual( data, res)
            
    def test_postfix_1(self):
        sourse_string = '12+3*='
        data = postfix(sourse_string)
        res = [9]
        self.assertEqual( data, res)

    def test_postfix_1(self):
        sourse_string = '85+5*9+='
        data = postfix(sourse_string)
        res = [74]
        self.assertEqual( data, res)

# First realisation tests  
    
    def test_push_e(self):
        my_stack = Stack()
        my_stack.push_to_end(1)
        my_stack.push_to_end(2)
        my_stack.push_to_end(3)
        data = my_stack.stack
        res =  [1, 2, 3]
        self.assertEqual( data, res)
    
    def test_pop_one_e(self):
        my_stack = Stack()
        my_stack.push_to_end(1)
        my_stack.push_to_end(2)
        my_stack.push_to_end(3)
        pop_el = my_stack.pop_from_end()
        data = my_stack.stack + [pop_el]
        res =  [1, 2, 3]
        self.assertEqual( data, res)
    
    def test_pop_none_e(self):
        my_stack = Stack()
        pop_el = my_stack.pop_from_end()
        data = my_stack.stack + [pop_el]
        res =  [None]
        self.assertEqual( data, res)

    def test_pop_all_e(self):
        my_stack = Stack()
        my_stack.push_to_end(1)
        my_stack.push_to_end(2)
        my_stack.push_to_end(3)
        pop_el1 = my_stack.pop_from_end()
        pop_el2 = my_stack.pop_from_end()
        pop_el3 = my_stack.pop_from_end()
        data = my_stack.stack + [pop_el1] + [pop_el2] + [pop_el3]
        res =  [3, 2, 1]
        self.assertEqual( data, res)

    def test_pop_in_middle_e(self):
        my_stack = Stack()
        my_stack.push_to_end(1)
        my_stack.push_to_end(2)
        pop_el = my_stack.pop_from_end()
        my_stack.push_to_end(3)
        data = my_stack.stack + [pop_el]
        res =  [1, 3, 2]
        self.assertEqual( data, res)
    
    def test_peek_e(self):
        my_stack = Stack()
        my_stack.push_to_end(1)
        my_stack.push_to_end(2)
        my_stack.push_to_end(3)
        data = my_stack.stack + [my_stack.peek_from_end()]
        res =  [1, 2, 3, 3]
        self.assertEqual( data, res)

    def test_random_e(self):
        for i in range(10000):
            s = Stack()
            res = []
            comand = random.randint(0, 1) # 0 - pop, 1 - push
            if comand:
                t = random.randint(0,9)
                s.push_to_end(t)
                res.append(t)
            else:
                s.pop_from_end()
                try:
                    res.pop()
                except:
                    pass
            data = s.stack + [s.size()]
            res =  res + [len(res)]
            self.assertEqual( data, res)


if __name__ == '__main__':
    unittest.main()
