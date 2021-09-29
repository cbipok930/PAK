import copy


class Item:
    def __init__(self, count=3, max_count=10):
        self._count = count
        self._max_count = max_count

    def update_count(self, val):
        if val <= self._max_count:
            self._count = val
            return True
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self._count < other._count
        elif isinstance(other, int):
            return self._count < other

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self._count > other._count
        elif isinstance(other, int):
            return self._count > other

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self._count >= other._count
        elif isinstance(other, int):
            return self._count >= other

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self._count <= other._count
        elif isinstance(other, int):
            return self._count <= other

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._count == other._count
        elif isinstance(other, int):
            return self._count == other

    def __add__(self, other):
        if isinstance(other, int):
            new_cnt = self._count + other
            if new_cnt > self._max_count or new_cnt < 0:
                print("Prohibited operation:", self, '+=', other)
                return self
            else:
                self._count = new_cnt
                return self

    def __sub__(self, other):
        if isinstance(other, int):
            new_cnt = self._count - other
            if new_cnt > self._max_count or new_cnt < 0:
                print("Prohibited operation:", self, '-=', other)
                return self
            else:
                self._count = new_cnt
                return self

    def __mul__(self, other):
        if isinstance(other, int):
            new_cnt = self._count * other
            if new_cnt > self._max_count or new_cnt < 0:
                print("Prohibited operation:", self, '*=', other)
                return self
            else:
                self._count = new_cnt
                return self

    # Свойство объекта. Не принимает параметров кроме self, вызывается без круглых скобок
    # Определяется с помощью декоратора property
    @property
    def count(self):
        return self._count


class Food(Item):
    def __init__(self, satiety=5, **kwargs):
        super().__init__(**kwargs)
        self._satiety = satiety

    @property
    def eatable(self):
        return self._satiety > 0

    @property
    def satiety(self):
        return self._satiety


class Fruit(Food):
    def __init__(self, juice=5, satiety=8, **kwargs):
        super().__init__(satiety, **kwargs)
        self._juice = juice

    @property
    def juice(self):
        return self._juice

    @property
    def dry(self):
        return self._juice == 0


class Grain(Food):
    def __init__(self, handful=5, satiety=2, **kwargs):
        super().__init__(satiety, **kwargs)
        self._handful = handful

    @property
    def handful(self):
        return self._handful


class Apple(Fruit):
    def __init__(self, color="green", juice=4, **kwargs):
        super().__init__(juice, **kwargs)
        self._color = color

    @property
    def color(self):
        return self._color


class Orange(Fruit):
    def __init__(self, bright=3, juice=6, **kwargs):
        super().__init__(juice, **kwargs)
        self._bright = bright

    @property
    def bright(self):
        return self._bright


class Corn(Grain):
    def __init__(self, pop=True, **kwargs):
        super().__init__(**kwargs)
        self._pop = pop

    @property
    def maypopcorn(self):
        return self._pop


class Rice(Grain):
    def __init__(self, cooked=False, **kwargs):
        super().__init__(**kwargs)
        self._cooked = cooked
        if self._cooked:
            self._satiety = 5

    def cook(self):
        self._cooked = True
        return self
    @property
    def cooked(self):
        return self._cooked


class Inventory:
    def __init__(self, size=5):
        self._list = []
        for i in range(size):
            self._list.append(None)

    def __len__(self):
        return len(self._list)

    # def __getitem__(self, item):
    #     if item > len(self) - 1:
    #         print("Index out of list")
    #     return self._list[item]
    def getitem_copy(self, key):
        if key > len(self) - 1:
            print("Index out of list")
        object_ = copy.copy(self._list[key])
        return object_

    def setitem(self, key, value):
        key = int(key)
        if key > len(self) - 1:
            print("Index out of list")
            return self
        if isinstance(value, Item):
            if value.count == 0:
                self._list[key] = None
                return self
            else:
                object_ = copy.copy(value)
                self._list[key] = object_
                return self
        print("Object should be Item")
        return self

    def remove_from_inventory(self, key):
        if key > len(self) - 1:
            print("Index out of list")
            return self
        self._list[key] = None


class Query:
    def __init__(self, cap=10):
        self._cap = cap
        self.__content = []
        for i in range(cap):
            self.__content.append(None)
        self._begin = 0
        self._end = 0
        self._cnt = 0

    def push(self, value):
        if self._cnt == self._cap:
            print("query is full")
            return self
        self.__content[self._end] = value
        self._end = (self._end + 1) % self._cap
        self._cnt += 1
        return self

    def pop(self):
        if self._cnt == 0:
            print("query is empty")
            return None
        value = self.__content[self._begin]
        self.__content[self._begin] = None
        self._begin = (self._begin + 1) % self._cap
        self._cnt -= 1
        return value

    def get_content(self):
        export_content = []
        for i in range(self._cap):
            export_content.append(self.__content[i])
        return export_content






