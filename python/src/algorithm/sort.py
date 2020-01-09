from random import randint


def quick(arr):
    if len(arr) == 0:
        return

    quickSort(arr, 0, len(arr) - 1)


def quickSort(arr, begin, end):
    if begin >= end:
        return

    pivot = partition(arr, begin, end)

    quickSort(arr, begin, pivot-1)
    quickSort(arr, pivot+1, end)


def partition(arr, begin, end):
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


def merge(arr):
    if len(arr) == 1:
        return arr

    index = round(0 + len(arr) / 2)

    left, right = merge(arr[:index]), merge(arr[index:])
    leftLen, rightLen, leftIndex, rightIndex = len(left), len(right), 0, 0

    ret = []
    while leftIndex < leftLen and rightIndex < rightLen:
        if left[leftIndex] > right[rightIndex]:
            ret.append(right[rightIndex])
            rightIndex += 1
        else:
            ret.append(left[leftIndex])
            leftIndex += 1

    while rightIndex < rightLen:
        ret.append(right[rightIndex])
        rightIndex += 1

    while leftIndex < leftLen:
        ret.append(left[leftIndex])
        leftIndex += 1

    return ret


arr = [randint(0, 20) for x in range(10)]
arr2 = [randint(0, 20) for x in range(10)]


print(arr)
quick(arr)
print(arr)

print(arr2)
arr2 = merge(arr2)
print(arr2)