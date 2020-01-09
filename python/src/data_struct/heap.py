from random import randint
from math import floor
from abc import ABC, abstractmethod


class heap(ABC):
    def get_parent(self, index):
        if index == 0 or index >= len(self._ls):
            return None

        return (index - 1) >> 1

    def get_left_child(self, index):
        if index >= len(self._ls):
            return None

        left = 2 * index + 1
        return left if left < len(self._ls) else None

    def get_right_child(self, index):
        if index >= len(self._ls):
            return None

        right = 2 * index + 1
        return right if right < len(self._ls) else None

    @abstractmethod
    def up_shift(self):
        pass

    @abstractmethod
    def down_shift(self):
        pass

    @abstractmethod
    def add(self):
        pass


class max_heap(heap):

    list = property(lambda self: self._ls)

    def __init__(self):
        heap.__init__(self)
        self._ls = []

    def up_shift(self, index):
        if index <= 0:
            return

        while index != 0:
            parent = self.get_parent(index)
            if (parent or parent == 0) and self._ls[parent] < self._ls[index]:
                self._ls[index], self._ls[parent] = self._ls[parent], self._ls[index],
                index = parent
            else:
                break

    def down_shift(self, index):
        if index < 0 or index >= len(self._ls):
            return

        l = self._ls

        while True:
            left = self.get_left_child(index)
            right = self.get_right_child(index)

            if left or right:
                if left and right:
                    max_index = left if l[left] > l[right] else right

                    if l[index] >= l[max_index]:
                        break
                    else:
                        l[index], l[max_index] = l[max_index], l[index]
                        index = max_index
                else:
                    if l[left] <= l[index]:
                        break
                    else:
                        l[left], l[index] = l[index], l[left]
                        break

            else:
                break

    def add(self, data):
        self._ls.append(data)
        self.up_shift(len(self._ls) - 1)

    def remove(self):
        if len(self._ls) <= 0:
            return

        ret = self._ls[0]
        self._ls[0] = self._ls[len(self._ls) - 1]
        self._ls.pop()
        self.down_shift(0)

        return ret


mh = max_heap()
l = []
for _ in range(10):
    value = randint(1, 20)
    l.append(value)
    mh.add(value)

print('origin list: %s' % l)
print('max heap is: %s' % mh.list)
print('after remove root : %s' % (mh.remove() and mh.list))
