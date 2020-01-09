def translate_nums(n: int):
    s = str(n)
    cached = {}

    def _fn(s: str):
        if len(s) == 1:
            return 1

        if len(s) == 0:
            return 0

        if s in cached:
            return cached[s]

        first = s[0]
        second = s[1]

        if (int(first) == 2 and int(second) < 7) or (int(first) == 1):
            value = _fn(s[1:]) + _fn(s[2:])
            cached[s] = value
            return value
        else:
            value = _fn(s[1:])
            cached[s] = value
            return value

    return _fn(s)


print(translate_nums(12258))
