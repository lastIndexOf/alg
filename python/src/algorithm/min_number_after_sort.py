
from functools import reduce


def min_number(ls):
    '''暴力解法'''
    ret = []
    path = []

    def _fn(ls, begin, end):
        if begin >= end:
            return

        if begin == end - 1:
            path.append(ls[begin])
            ret.append([*path])
            path.pop()
            return

        for index in range(begin, end):
            path.append(ls[index])
            ls[begin], ls[index] = ls[index], ls[begin]
            _fn(ls, begin + 1, end)
            path.pop()
            ls[begin], ls[index] = ls[index], ls[begin]

    _fn(ls, 0, len(ls))

    return min(map(lambda x: int(reduce(lambda a, b: str(a) + str(b), x)), ret))


def min_number2(ls):
    ret = 0
    count = 0

    sum_ = reduce(lambda a, b: a * b, range(1, len(ls)+1))

    for i in range(1, sum_ + 1):
        value = ls[i]
        while value:
            value = value >> 1

    return sum_


ls = [3, 32, 321]

print(min_number(ls))
