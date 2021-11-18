class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value: str):
        """Return slot number based on hash_function"""
        slot_number = sum(bytes(value, encoding = 'utf-8')) % self.size 
        return slot_number

    def seek_slot(self, value):
        """Return free slot index or None if HashTable is full"""
        index = self.hash_fun(value)
        hash_fun_index = index
        step_count = 0
        while self.slots[index] is not None and step_count < self.size:
            index += self.step
            step_count += 1
            if index >= self.size:
                index = index % self.size
            if index == hash_fun_index:
                return None
        if step_count == self.size:
            return None
        else:
            return index

    def put(self, value):
        """Put value in HashTable[index] and return index or return None if HashTable is full"""
        index = self.seek_slot(value)
        if index is None:
            res = None
        else:
            self.slots[index] = value
            res = index
        return res

    def find(self, value):
        """Retur index of value or None if value not find"""
        index = self.hash_fun(value)
        hash_fun_index = index
        step_count = 0
        while self.slots[index] != value and step_count < self.size:
            index += self.step
            step_count += 1
            if index >= self.size:
                index = index % self.size
            if index == hash_fun_index:
                return None
        if step_count == self.size:
            return None
        else:
            return index