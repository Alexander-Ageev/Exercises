SET_LEN = 65000
STEP = 11
class PowerSet():
    def __init__(self):
        self.length = SET_LEN
        self.step = STEP
        self.slots = [None] * self.length

    def _hash_fun(self, value: str):
        slot_number = (sum(bytes(value, encoding='utf-8')) * 32500) % self.length
        return slot_number

    def _seek_slot(self, value):
        index = self._hash_fun(value)
        hash_fun_index = index
        step_count = 0
        while self.slots[index] is not None and step_count < self.length:
            if self.slots[index] == value:
                return index
            index += self.step
            step_count += 1
            if index >= self.length:
                index = index % self.length
            if index == hash_fun_index:
                return None
        if step_count == self.length:
            return None
        else:
            return index

    def put(self, value):
        index = self._seek_slot(value)
        if index is None:
            res = None
        else:
            self.slots[index] = value
            res = index
        return res

    def size(self):
        s = 0
        for i in range(SET_LEN):
            if self.slots[i] is not None:
                s +=1
        return s

    def get(self, value):
        index = self._hash_fun(value)
        step_count = 0
        hash_fun_index = index
        while self.slots[index] != value:
            index += self.step
            if index >= SET_LEN:
                index = index % SET_LEN
            if index == hash_fun_index or step_count == SET_LEN - 1 or self.slots[index] is None:
                return False
        return True

    def remove(self, value):
        index = self._seek_slot(value)
        if index is not None:
            self.slots[index] = None
            return True
        else:
            return False

    def list_value(self):
        res = []
        for i in range(SET_LEN):
            if self.slots[i] is not None:
                res.append(self.slots[i])
        return res

    def intersection(self, set2):
        # пересечение текущего множества и set2
        res = PowerSet()
        values = self.list_value()
        for i in values:
            if set2.get(i) == True:
                res.put(i)
        return res

    def union(self, set2):
        res = PowerSet()
        values = self.list_value() + set2.list_value()
        for i in values:
            res.put(i)
        return res

    def difference(self, set2):
        # разница текущего множества и set2
        res = PowerSet()
        values = self.list_value()
        for i in values:
            if set2.get(i) != True:
                res.put(i)
        return res

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        a = sorted(self.list_value())
        b = sorted(set2.list_value())
        if a < b:
            return False
        else:
            i = 0
            count = 0
            while b[i] in a:
                i += 1
                count += 1
        return True if count == len(b) else False
