class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.random_h1 = 17
        self.random_h2 = 223
        self.table = 2 ** 64 - 2 ** self.filter_len
        # создаём битовый массив длиной f_len ...

    def hash1(self, str1):
        """Возвращаем результат хэш-функции 1"""
        res = 0
        for char in str1:
            code = ord(char)
            res = ((res * self.random_h1) + code) % self.filter_len
        return res

    def hash2(self, str1):
        """Возвращаем результат хэш-функции 2"""
        res = 0
        for char in str1:
            code = ord(char)
            res = ((res * self.random_h2) + code) % self.filter_len
        return res

    def add(self, str1):
        """Добавляем строку в фильтр"""
        hash_1 = 2 ** self.hash1(str1)
        hash_2 = 2 ** self.hash2(str1)
        self.table = self.table | hash_1 | hash_2
        return 0

    def is_value(self, str1):
        """Если строка имеется в вильтре, возвращаем True"""
        hash_1 = 2 ** self.hash1(str1)
        hash_2 = 2 ** self.hash2(str1)
        if self.table & (hash_1 + hash_2) == hash_1 + hash_2:
            return True
        return False
