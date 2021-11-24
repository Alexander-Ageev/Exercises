class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        """Return slot number based on hash_function"""
        slot_number = sum(bytes(key, encoding='utf-8')) % self.size
        return slot_number

    def is_key(self, key):
        """Return True if key exist"""
        index = self.hash_fun(key)
        return False if self.slots[index] is None else True

    def put(self, key, value):
        """Put value in HashTable[index] and return index or return None if HashTable is full"""
        index = self.hash_fun(key)
        self.slots[index] = key
        self.values[index] = value
        return None

    def get(self, key):
        """Return value by key"""
        index = self.hash_fun(key)
        return self.values[index] if self.is_key(key) else None
