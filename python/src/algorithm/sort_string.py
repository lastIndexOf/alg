def all_sort(words=''):
    if len(words) == 1:
        return list(words)

    words = [*words]

    ret = []

    for start in words:
        i = words.index(start)
        extend = words[:i]
        extend.extend(words[i+1:])
        temp = map(lambda x: start + x, all_sort(extend))
        ret.extend(list(temp))

    return ret


def all_combine(words):
    def _util(words):
        if len(words) == 0:
            return ['']

        ret = ['']
        words = [*words]

        for start in words:
            i = words.index(start)
            extend = words[i+1:]
            temp = map(lambda x: start + x, _util(extend))
            ret.extend(list(temp))

        return ret

    ret = _util(words)
    ret.pop(0)

    return ret


# print(list(all_sort('abc')))
# print(list(all_combine('abc')))
