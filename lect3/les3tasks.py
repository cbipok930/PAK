class Item:
    def __init__(self, count=0, max_count=0):
        self._count = count
        self._max_count = 16

    def update_count(self, val):
        if val <= self._max_count:
            self._count = val
            return True
        else:
            return False

    def is_lower_then(self, val):
        if self._count < val:
            return True
        else:
            return False

    def is_greater_then(self, val):
        if self._count > val:
            return True
        else:
            return False

    def is_ge_then(self, val):
        if self._count >= val:
            return True
        else:
            return False

    def is_le_then(self, val):
        if self._count <= val:
            return True
        else:
            return False

    def is_equal(self, val):
        if self._count == val:
            return True
        else:
            return False

    def item_add(self, val):
        new_cnt = self._count + val
        if val > self._max_count or val < 0:
            print("Prohibited operation")
        else:
            self._count = new_cnt

    def item_add(self, val):
        new_cnt = self._count + val
        if val > self._max_count or val < 0:
            print("Prohibited operation")
        else:
            self._count = new_cnt

    # Свойство объекта. Не принимает параметров кроме self, вызывается без круглых скобок
    # Определяется с помощью декоратора property
    @property
    def count(self):
        return self._count


lol = Item(2)
lol.update_count(5)
