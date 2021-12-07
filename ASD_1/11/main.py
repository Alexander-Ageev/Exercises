class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.random_h1 = 17
        self.random_h2 = 223
        self.table = 2 ** 64 - 2 ** self.filter_len
        # создаём битовый массив длиной f_len ...


    def hash1(self, str1):
        res = 0
        for c in str1:
            code = ord(c)
            res = ((res * self.random_h1) + code) % self.filter_len
        return res

    def hash2(self, str1):
        res = 0
        for c in str1:
            code = ord(c)
            res = ((res * self.random_h2) + code) % self.filter_len
        return res

    def add(self, str1):
        h1 = 2 ** self.hash1(str1)
        h2 = 2 ** self.hash2(str1)
        self.table = self.table | h1 | h2
        return 0

    def is_value(self, str1):
        h1 = 2 ** self.hash1(str1)
        h2 = 2 ** self.hash2(str1)
        if self.table & (h1 + h2) == h1 + h2:
            return True
        else:
            return False


        # проверка, имеется ли строка str1 в фильтре