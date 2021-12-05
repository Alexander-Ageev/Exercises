class PowerSet():
    def __init__(self):
        self.slots = []

    def put(self, value):
        """Добавляет элемент в множество. Всегда"""
        if value not in self.slots:
            self.slots.append(value)
        return 0

    def size(self):
        """Возвращает размер множества"""
        return len(self.list_value())

    def get(self, value):
        """Возвращает True, если элемент присутствует в множестве, иначе возвращает False"""
        return bool(value in self.slots)

    def remove(self, value):
        """Удаляет элемент value, возвращает True. Иначе возвращает False"""
        for i in self.slots:
            if value == i:
                self.slots.remove(i)
                return True
        return False

    def list_value(self):
        """Возвращает список элементов множества"""
        return self.slots

    def intersection(self, set2):
        """Возвращает пересечение исходного множества с параметром set2"""
        res = PowerSet()
        values = self.list_value()
        for i in values:
            if set2.get(i):
                res.slots.append(i)
        return res

    def union(self, set2):
        """Возвращает объединение исходного множества с параметром set2"""
        res = PowerSet()
        values = sorted(self.list_value() + set2.list_value())
        if len(values) > 0:
            prev = values[0]
            res.put(prev)
            for i in range(1, len(values)):
                if prev != values[i]:
                    res.slots.append(values[i])
                prev = values[i]
        return res

    def difference(self, set2):
        """Возвращает отличающиеся элементы исходного множества от set2"""
        res = PowerSet()
        values = self.list_value()
        for i in values:
            if not set2.get(i):
                res.slots.append(i)
        return res

    def issubset(self, set2):
        """Возвращает   True, если set2 полностью входит в исходное множество"""
        subset_size = set2.size()
        if self.size() >= subset_size:
            count = 0
            subset = set2.list_value()
            for i in subset:
                if self.get(i):
                    count += 1
            return bool(count == subset_size)
        return False
