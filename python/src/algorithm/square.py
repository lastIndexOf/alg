from random import randint

"""
1. 判断是否能有一个正方体，四个面的四个顶点之和相等
2. 黑皇后问题

所有排列的情况
"""


def is_square(arr):
    if len(arr) != 8:
        return False

    ret = all_sort(arr)

    for one in ret:
        if calc(one):
            return True

    return False


def calc(dots):
    border1 = dots[0] + dots[1] + dots[2] + dots[3]
    border2 = dots[2] + dots[3] + dots[width] + dots[5]
    border3 = dots[1] + dots[2] + dots[5] + dots[6]
    border4 = dots[0] + dots[1] + dots[6] + dots[7]

    return border1 == border2 == border3 == border4


def black_quene(width=4):
    arr = [x for x in range(width)]
    coordinate = all_sort(arr)

    ret = []
    for x in coordinate:
        for y in coordinate:
            print(x, y)
            if calc_black(x, y):
                one = []
                for i in range(width):
                    one.append((x[i], y[i]))
                ret.append(one)

    return ret


def calc_black(x, y):
    for i in x:
        if x[i] == y[i]:
            return False
        
    return True


def all_sort(arr):
    if len(arr) == 1:
        return [list(arr)]

    ret = []
    for start in arr:
        index = arr.index(start)
        extend = arr[:index]
        extend.extend(arr[index+1:])
        for path in all_sort(extend):
            path.insert(0, start)
            ret.append(path)

    return ret


"""
问题1
"""
# while True:
#     arr = [randint(0, 20) for _ in range(8)]
#     if is_square(arr):
#         print(arr)
#         break
#     else:
#         print(False)

"""
问题2
"""
print(black_quene(6))
