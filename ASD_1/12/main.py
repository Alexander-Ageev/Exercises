class NativeCache:
    """Данный класс демонстрирует алгоритм работы кэша"""

    def __init__(self, sz):
        self.size = sz
        self.step = 7
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def __select_slot(self, value):
        """Данный метод возвращает индекс слота для нового элемента.
        Если кэш заполнен - возвращает индекс с наименьшим значением в self.hits
        """
        start_index = hash(value) % self.size
        index = start_index
        while self.slots[index] is not None:
            index = (index + self.step) % self.size
            if index == start_index:
                index = self.__min_hits()
                break
        return index

    def put(self, key, value):
        """Метод помещает новый элемент в кэш"""
        index = self.__select_slot(key)
        self.values[index] = value
        self.slots[index] = key
        self.hits[index] = 0
        return 0

    def __min_hits(self):
        """Метод возвращает индекс элемента с наименьшим значением в self.hits"""
        min_value = self.hits[0]
        min_index = 0
        for i in range(1, self.size):
            if self.hits[i] < min_value:
                min_index = i
                min_value = self.hits[i]
        return min_index

    def get(self, key):
        """Возвращает значение по ключу"""
        index = self.slots.index(key)
        if key in self.slots:
            index = self.slots.index(key)
            self.hits[index] += 1
            res = self.values[index]
        else:
            res = None
        return res

    def get_list_values(self):
        """Возвращает список значений"""
        return self.values

    def get_list_hits(self):
        """Возвращает список запросов"""
        return self.hits
