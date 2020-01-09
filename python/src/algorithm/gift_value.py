def gift_value(ls):
    if not len(ls):
        return 0

    path = []
    max_value = 0
    ret = []
    max_x = len(ls) - 1
    max_y = len(ls[0]) - 1

    def _fn(ls, x_begin, y_begin):
        nonlocal max_value, ret
        path.append(ls[x_begin][y_begin])

        if x_begin == max_x and y_begin == max_y:
            if sum(path) > max_value:
                max_value = sum(path)
                ret = [*path]

        if x_begin < max_x and y_begin < max_y:
            _fn(ls, x_begin + 1, y_begin)
            _fn(ls, x_begin, y_begin + 1)

        elif x_begin < max_x:
            _fn(ls, x_begin + 1, y_begin)

        elif y_begin < max_y:
            _fn(ls, x_begin, y_begin + 1)

        path.pop()

    _fn(ls, 0, 0)

    return ret


def gift_value2(ls):
    if not len(ls):
        return 0

    max_value = ''
    path = []
    cached = []

    for i in range(len(ls)):
        cached.append([])
        for j in range(len(ls[i])):
            cached[i].append(0)

    def _fn(ls, i, j):
        if i == 0 and j != 0:
            return ls[i][j] + _fn(ls, i, j - 1)
        if i != 0 and j == 0:
            return ls[i][j] + _fn(ls, i - 1, j)
        if i == 0 and j == 0:
            return ls[0][0]

        if i in cached and j in cached[i] and cached[i][j]:
            return cached[i][j]

        value = ls[i][j] + max(_fn(ls, i - 1, j), _fn(ls, i, j - 1))
        cached[i][j] = value

        return value

    return _fn(ls, len(ls) - 1, len(ls[0]) - 1)


ls = [
    [1, 10, 3, 8],
    [12, 2, 9, 6],
    [5, 7, 4, 11],
    [3, 7, 16, 5]
]
print(gift_value(ls))
print(gift_value2(ls))
