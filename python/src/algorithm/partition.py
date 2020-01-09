from random import randint
from math import ceil
from ..data_struct.heap import max_heap as heap

"""
找出数组中第k大的数
"""


def index_big(arr, index):
    if len(arr) <= 0 or index <= 0:
        return

    return do_index(arr, 0, len(arr) - 1, index - 1)


def do_index(arr, begin, end, index):
    pivot = partition(arr, begin, end)

    if pivot < index:
        return do_index(arr, pivot+1, end, index)
    elif pivot > index:
        return do_index(arr, begin, pivot-1, index)
    else:
        return arr[pivot]


def partition(arr, begin, end):
    if begin == end:
        return begin

    pivot = arr[begin]
    while begin < end:
        while begin < end and arr[end] >= pivot:
            end -= 1
        arr[begin] = arr[end]
        while begin < end and arr[begin] <= pivot:
            begin += 1
        arr[end] = arr[begin]

    arr[begin] = pivot
    return begin


# 2
def index_big2(arr, k):
    max_heap = heap()

    for current in arr:
        if len(max_heap) < k:
            max_heap.add(current)

        elif max_heap.root > current:
            max_heap.add(current)
            max_heap._remove_max()
            pass

    return list(max_heap)


arr = [1, 2, 2, 2, 2, 3, 4, 5, 3]
print(sorted(arr))
print(index_big(arr, ceil(len(arr)/2)))
