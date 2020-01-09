from random import randint


def fn(arr, target, ret=[]):

    for k in arr:
        rest = target - k

        if rest == 0:
            ret.append(k)
            print(ret)
            ret.pop()
        elif rest > 0:
            ret.append(k)
            i = arr.index(k)
            extend = arr[k+1:]
            return fn(extend, rest, ret)


def fn2(arr, target):
    ret = []
    path = []

    def _fn2(arr, target, begin, end):
        nonlocal ret, path

        if begin > end:
            return

        for i in range(begin, end):
            st = arr[i]
            path.append(st)

            rest = target - st
            if rest == 0:
                ret.append([*path])
            elif rest > 0:
                _fn2(arr, rest, i+1, end)

            path.pop()

    _fn2(arr, target, 0, len(arr))

    return ret


l = [randint(1, 10) for _ in range(10)]
print(l)
# fn(l, 7)
print(fn2(l, 7))
